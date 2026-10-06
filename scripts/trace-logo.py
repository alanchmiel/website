"""Trace the supplied raster into real paths; never embed a bitmap in an SVG.
Uses pixel boundary polygons rather than guessed fonts. Run with Pillow/NumPy/SciPy.
The original reference is intentionally not distributed with the public site.
"""
from PIL import Image
import numpy as np
from scipy.ndimage import label
from pathlib import Path
import sys
source=Path(sys.argv[1]); out=Path(__file__).resolve().parents[1]/'public/assets/brand'
a=np.asarray(Image.open(source).convert('RGB')).astype(float)
red=(a[:,:,0]>a[:,:,1]*1.35)&(a[:,:,0]>a[:,:,2]*1.3)&(a[:,:,1]<145)
dark=(a.mean(2)<155)&~red

def simplify(points,tolerance=.65):
    # Ramer–Douglas–Peucker removes pixel stairs while preserving letter shapes.
    if len(points)<3: return points
    start=np.array(points[0]); end=np.array(points[-1]); v=end-start
    a=np.array(points[1:-1]); length=np.linalg.norm(v)
    d=np.abs(v[0]*(start[1]-a[:,1])-v[1]*(start[0]-a[:,0]))/length if length else np.linalg.norm(a-start,axis=1)
    i=int(np.argmax(d))+1
    if d[i-1]>tolerance: return simplify(points[:i+1])+simplify(points[i:])[1:]
    return [points[0],points[-1]]

def paths(mask):
    # Ignore isolated antialiasing specks; retain all letter counters using evenodd.
    labels,n=label(mask); counts=np.bincount(labels.ravel()); mask=mask&(counts[labels]>=3)
    edges={}
    for y,x in zip(*np.nonzero(mask)):
        for absent,start,end in [(y==0 or not mask[y-1,x],(x,y),(x+1,y)),(x==mask.shape[1]-1 or not mask[y,x+1],(x+1,y),(x+1,y+1)),(y==mask.shape[0]-1 or not mask[y+1,x],(x+1,y+1),(x,y+1)),(x==0 or not mask[y,x-1],(x,y+1),(x,y))]:
            if absent: edges.setdefault(start,[]).append(end)
    result=[]
    while edges:
        start=next(iter(edges)); cur=start; pts=[]
        while True:
            pts.append(cur); ends=edges[cur]; nxt=ends.pop()
            if not ends: del edges[cur]
            cur=nxt
            if cur==start: break
        # Remove collinear points without changing the traced shape.
        p=[q for i,q in enumerate(pts) if (q[0]-pts[i-1][0])*(pts[(i+1)%len(pts)][1]-q[1])!=(q[1]-pts[i-1][1])*(pts[(i+1)%len(pts)][0]-q[0])]
        if len(p)>4:
            mid=len(p)//2
            p=simplify(p[:mid+1])[:-1]+simplify(p[mid:]+[p[0]])[:-1]
        if len(p)>2: result.append('M'+' L'.join(f'{x},{y}' for x,y in p)+'Z')
    return ''.join(result)

def part(box,mask,color):
    x,y,w,h=box
    return f'<path fill="{color}" fill-rule="evenodd" d="{paths(mask[y:y+h,x:x+w])}"/>'

def svg(name,w,h,body):
    (out/name).write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<!-- Outlined vector traced from Alan’s supplied reference; color standardized. -->\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">Dr. Alan Chmiel</title>{body}</svg>\n')
iconbox=(125,105,460,330); namebox=(660,165,995,133); wordbox=(660,165,995,270)
for mode,c,r in [('color','#1F2226','#92191A'),('mono','#1F2226','#1F2226'),('reverse','#FFFFFF','#FFFFFF')]:
    icon=part(iconbox,dark,c)+part(iconbox,red,r)
    name=part(namebox,dark,c)+part(namebox,red,r)
    word=part(wordbox,dark,c)+part(wordbox,red,r)
    svg(f'icon-{mode}.svg',460,330,icon)
    svg(f'wordmark-{mode}.svg',995,270,word)
    svg(f'primary-{mode}.svg',1530,330,icon+f'<path d="M490 50V315" stroke="{c if mode!="color" else "#B8B8B8"}" stroke-width="1.5"/>'+f'<g transform="translate(535 60)">{word}</g>')
    svg(f'header-{mode}.svg',1530,330,icon+f'<path d="M490 50V315" stroke="{c if mode!="color" else "#B8B8B8"}" stroke-width="1.5"/>'+f'<g transform="translate(535 85)">{name}</g>')
    svg(f'stacked-{mode}.svg',1100,730,f'<g transform="translate(320 0)">{icon}</g><g transform="translate(52 420)">{word}</g>')
    svg(f'intellectual-{mode}.svg',130,150,f'<path fill="{r}" d="M10 47H120V58H10Z M10 80H120V91H10Z M100 5L105 8L30 142L25 139Z"/>')
# Small-size favicon is an explicitly simplified derivative, not the full artwork.
svg('favicon.svg',64,64,'<path fill="#92191A" d="M55 17C44 2 20 6 16 28C12 49 36 61 55 46L54 42C37 55 20 44 22 28C24 13 43 8 55 20Z"/><path fill="#1F2226" d="M9 55L30 6H34L51 55H41L28 20L15 55Z"/><path d="M6 35H56" stroke="#1F2226" stroke-width="2"/><circle cx="40" cy="35" r="4" fill="#92191A" stroke="white" stroke-width="2"/>')
print('Created',len(list(out.glob('*.svg'))),'outlined SVG assets')
