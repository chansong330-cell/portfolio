import json,subprocess,hashlib,os
from pathlib import Path
repo=os.environ['GH_REPO'];tag='videos-v1'
folder=Path(os.environ['RUNNER_TEMP'])/'video-assembly';folder.mkdir(exist_ok=True)
plan=json.loads(Path('.github/scripts/video-parts.json').read_text())
def gh(args):return subprocess.run(['gh']+args,capture_output=True,text=True,check=True).stdout
def assets():
    rid=json.loads(gh(['api',f'repos/{repo}/releases/tags/{tag}']))['id']
    return {a['name']:a for page in json.loads(gh(['api',f'repos/{repo}/releases/{rid}/assets?per_page=100','--paginate','--slurp'])) for a in page}
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(1024*1024):h.update(chunk)
    return h.hexdigest()
remote=assets()
for video in plan:
    old=remote.get(video['name'])
    if old and old.get('digest')=='sha256:'+video['sha256'] and old['size']==video['bytes']:
        print('Already verified '+video['name'],flush=True);continue
    out=folder/video['name']
    with out.open('wb') as dest:
        for part in video['parts']:
            a=remote.get(part['name']);assert a and a['size']==part['bytes'] and a.get('digest')=='sha256:'+part['sha256'],part['name']
            gh(['release','download',tag,'--repo',repo,'--pattern',part['name'],'--dir',str(folder),'--clobber'])
            src=folder/part['name'];assert digest(src)==part['sha256']
            dest.write(src.read_bytes());src.unlink()
    assert out.stat().st_size==video['bytes'] and digest(out)==video['sha256']
    gh(['release','upload',tag,str(out),'--repo',repo,'--clobber'])
    remote=assets();a=remote[video['name']]
    assert a['size']==video['bytes'] and a.get('digest')=='sha256:'+video['sha256']
    out.unlink();print('Uploaded and verified '+video['name'],flush=True)
remote=assets()
assert all(remote.get(v['name'],{}).get('digest')=='sha256:'+v['sha256'] for v in plan)
# Remove only temporary part assets listed in this exact, verified plan.
for video in plan:
    for part in video['parts']:
        a=remote.get(part['name'])
        if a:gh(['api',f'repos/{repo}/releases/assets/{a["id"]}','--method','DELETE'])
print('All 17 MP4 files verified; temporary parts cleaned.',flush=True)
