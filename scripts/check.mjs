/** Build verification: catches missing local links/assets and malformed SVGs.
 * Run after npm run build. External destinations are intentionally not fetched.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'../dist');
async function walk(dir){return(await Promise.all((await fs.readdir(dir,{withFileTypes:true})).map(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]))).flat();}
const files=await walk(root);let checked=0;
for(const file of files.filter(f=>f.endsWith('.html'))){
 const html=await fs.readFile(file,'utf8');
 if(!html.includes('<h1>')||!html.includes('<title>'))throw new Error(`Missing heading/title: ${file}`);
 for(const [,href] of html.matchAll(/(?:href|src)="(\/[^"]*)"/g)){
  const target=path.join(root,href.split(/[?#]/)[0]);
  await fs.access(href.endsWith('/')?path.join(target,'index.html'):target).catch(()=>{throw new Error(`Missing local target ${href} in ${file}`)});checked++;
 }
}
for(const file of files.filter(f=>f.endsWith('.svg'))){const svg=await fs.readFile(file,'utf8');if(/<image\b|<text\b/.test(svg))throw new Error(`Distribution artwork must be outlined: ${file}`);}
console.log(`Verified ${files.filter(f=>f.endsWith('.html')).length} HTML files, ${checked} local references, and outlined SVG assets.`);
