# build: mode "embed" (data URIs) or "files" (img/<k>.webp next to page)
import sys, json, base64, os
D=os.path.join(os.path.dirname(__file__),'..','src'); mode=sys.argv[1]; out=sys.argv[2]
r=lambda f: open(os.path.join(D,f),encoding='utf8').read()
keys=sorted(f[:-5] for f in os.listdir(os.path.join(D,'img')) if f.endswith('.webp'))
if mode=='embed': A={k:'data:image/webp;base64,'+base64.b64encode(open(os.path.join(D,'img',k+'.webp'),'rb').read()).decode() for k in keys}
else:
    A={k:'img/'+k+'.webp' for k in keys}
    # máscaras CSS exigem mesma origem/CORS: vão embutidas
    for k in ('logo-mask',):
        if k in A: A[k]='data:image/webp;base64,'+base64.b64encode(open(os.path.join(D,'img',k+'.webp'),'rb').read()).decode()
js=r('app.js').replace('__ASSETS__',json.dumps(A),1)
html=r('shell-head.html')+'<style>'+r('style.css')+'</style>'+r('mid.html')+'<script>'+js+'</script>'+r('tail.html')
open(out,'w',encoding='utf8').write(html); print(out,len(html.encode()))
