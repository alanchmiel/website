/**
 * Markdown-to-static-HTML build. The browser needs no framework or Markdown parser.
 * Content lives in content/*.md. Layout lives here; appearance lives in src/style.css.
 * Front matter is JSON between --- fences: JSON is also valid YAML and avoids
 * a second parser dependency. This deliberately rejects malformed metadata early.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
// Vendored Marked 17.0.5 (MIT): builds offline, with no package installation.
import { marked } from '../vendor/marked.mjs';
const root = path.resolve(import.meta.dirname, '..');
const dist = path.join(root, 'dist');
const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
// Link values are trusted author configuration, but unsafe protocols are rejected.
const url = value => { if (!/^(\/|https?:\/\/|mailto:|#)/.test(value)) throw new Error(`Unsupported link: ${value}`); return escape(value); };
async function read(file) {
  const raw = await fs.readFile(path.join(root, 'content', file), 'utf8');
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) throw new Error(`Missing JSON front matter: ${file}`);
  return { ...JSON.parse(match[1]), body: match[2], file };
}
const site = await read('site.md');
const pages = await Promise.all(['home','ideas','research','teaching','about','speaking','cv'].map(async slug => ({...(await read(`${slug}.md`)),slug,route:slug==='home'?'/':`/${slug}/`})));
const articles = (await Promise.all((await fs.readdir(path.join(root,'content/ideas'))).filter(f=>f.endsWith('.md')).map(async file=>({...await read(`ideas/${file}`),slug:file.slice(0,-3),route:`/ideas/${file.slice(0,-3)}/`}))))
  .sort((a,b)=>(a.order??99)-(b.order??99));
function cards(items) { return `<div class="essay-list">${items.map((a,i)=>`<article class="essay-card"><span class="index">${String(i+1).padStart(2,'0')}</span><div><p class="eyebrow">${escape(a.eyebrow)}</p><h3><a href="${url(a.route)}">${escape(a.title)}</a></h3><p>${escape(a.summary)}</p><a class="text-link" href="${url(a.route)}">${escape(site.readLabel)}</a></div></article>`).join('')}</div>`; }
function contact() {
  // A real email/profile can be set in site.md; no pretend submission form is used.
  return `<aside class="contact"><p class="eyebrow">${escape(site.contactLabel)}</p><p>${escape(site.contactText)}</p><a class="button light" href="${url(site.contactUrl||site.contactFallback)}">${escape(site.contactButton)}</a></aside>`;
}
function body(p) {
  if(p.slug==='home') {
    // H2 sections become distinct homepage bands; H3 blocks become the three lenses.
    const [intro,...sections] = p.body.split(/^## /m);
    const first=sections[0]||''; const [framework,...lenses]=first.split(/^### /m);
    return `<section class="hero"><div><p class="eyebrow">${escape(p.eyebrow)}</p>${marked.parse(intro)}<div class="actions"><a class="button" href="${url(p.ctaUrl)}">${escape(p.ctaLabel)}</a><a class="text-link" href="${url(p.secondaryUrl)}">${escape(p.secondaryLabel)}</a></div></div><div class="hero-mark"><img src="/assets/brand/icon-color.svg" alt="" width="460" height="330"><p>${escape(p.title)}</p></div></section><section class="framework"><div class="section-heading">${marked.parse('## '+framework)}</div><div class="lenses">${lenses.map((l,i)=>`<div class="lens"><span class="index">${String(i+1).padStart(2,'0')}</span>${marked.parse('### '+l)}</div>`).join('')}</div></section><section class="selected"><p class="eyebrow">${escape(site.ideasLabel)}</p>${cards(articles.filter(a=>a.featured))}</section><section class="experience prose">${sections.slice(1).map(s=>marked.parse('## '+s)).join('')}</section>`;
  }
  const article=!!p.date;
  return `<header class="page-intro"><p class="eyebrow">${escape(p.eyebrow)}</p><p class="page-summary">${escape(p.summary)}</p>${article?`<time datetime="${escape(p.date)}">${escape(new Date(p.date+'T12:00:00Z').toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric',timeZone:'UTC'}))}</time>`:''}</header><article class="prose">${marked.parse(p.body)}</article>${p.slug==='ideas'?cards(articles):''}${article?`<a class="text-link back" href="/ideas/">${escape(site.backLabel)}</a>`:''}${['speaking','research','about'].includes(p.slug)?contact():''}`;
}
function shell(p,content) {
  const nav=site.nav.map(n=>`<a href="${url(n.href)}"${p.route===n.href?' aria-current="page"':''}>${escape(n.label)}</a>`).join('');
  return `<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(p.title)} | ${escape(site.name)}</title><meta name="description" content="${escape(p.summary||site.description)}"><meta name="theme-color" content="#92191A"><link rel="icon" type="image/svg+xml" href="/assets/brand/favicon.svg"><link rel="stylesheet" href="/style.css"><script src="/menu.js" defer></script></head><body><a class="skip" href="#main">${escape(site.skipLabel)}</a><header class="site-header"><a class="identity" href="/" aria-label="${escape(site.name+' — '+site.homeLabel)}"><img src="/assets/brand/header-color.svg" alt="${escape(site.name)}" width="1530" height="330"></a><button class="menu-toggle" aria-controls="navigation" aria-expanded="false" data-open="${escape(site.menuLabel)}" data-close="${escape(site.closeMenuLabel)}">${escape(site.menuLabel)}</button><nav id="navigation" aria-label="${escape(site.menuLabel)}">${nav}</nav></header><main id="main" class="${p.slug==='home'?'home':'interior'}">${content}</main><footer><div><p class="footer-title">${escape(site.footerTitle)}</p><p>${escape(site.footerNote)}</p></div><p>${escape(site.copyright)}</p></footer></body></html>`;
}
await fs.rm(dist,{recursive:true,force:true}); await fs.mkdir(dist,{recursive:true});
await fs.cp(path.join(root,'public'),dist,{recursive:true});
await fs.copyFile(path.join(root,'src/style.css'),path.join(dist,'style.css'));
await fs.copyFile(path.join(root,'src/menu.js'),path.join(dist,'menu.js'));
for(const p of [...pages,...articles]) { const dir=path.join(dist,p.route); await fs.mkdir(dir,{recursive:true}); await fs.writeFile(path.join(dir,'index.html'),shell(p,body(p))); }
await fs.writeFile(path.join(dist,'404.html'),shell({title:site.notFoundTitle,slug:'404',route:'/404/'},`<article class="prose"><h1>${escape(site.notFoundTitle)}</h1><p>${escape(site.notFoundText)}</p><a href="/">${escape(site.homeLabel)}</a></article>`));
// A private preview should not be indexed. Change this before a public launch.
await fs.writeFile(path.join(dist,'robots.txt'),'User-agent: *\nDisallow: /\n');
console.log(`Built ${pages.length+articles.length} pages and ${articles.length} Markdown essays.`);
