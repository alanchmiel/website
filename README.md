# Dr. Alan Chmiel — Engineering the Decision

A complete, responsive personal website with Markdown content and outlined SVG brand assets.

## Start here

You need **Node.js 22 or later**. There are no packages to install and no accounts required to build locally.

```sh
npm run build
npm run check
npm run preview
```

Open http://localhost:8080. Press Ctrl+C to stop the local preview.
After every Markdown edit, rebuild and refresh the page. Upload the **contents of `dist/`** to a static web host. This is compatible with GitHub Pages, Netlify, Cloudflare Pages, and conventional web hosting when served from a domain root.

The generated site works without JavaScript; JavaScript only collapses the phone menu. No tracking, cookies, hosted font dependencies, submission forms, or database are included.

## Edit content in Markdown

All visitor-facing copy is in `content/`. You do not need to edit HTML or JavaScript to maintain it.

| File | What it controls |
| --- | --- |
| `site.md` | Name, page description, navigation, menu and link labels, contact destination, footer |
| `home.md` | Homepage introduction, framework, experience band, button labels |
| `ideas.md` | Essays index introduction |
| `ideas/*.md` | Individual essays, summaries, categories, dates, display order |
| `research.md` | Research interests and discussion invitation |
| `teaching.md` | Teaching approach |
| `about.md` | Biography and credentials |
| `speaking.md` | Talk descriptions and inquiry guidance |
| `cv.md` | Printable selected professional profile |

Each file starts with JSON front matter between `---` lines. JSON is valid YAML, but this project intentionally requires JSON syntax: quoted keys/strings, no trailing commas. Body content uses ordinary Markdown.

```markdown
---
{"title":"An essay title","eyebrow":"Markets & strategy","summary":"A short description.","date":"2026-10-06","featured":true,"order":4}
---

# An essay title

An opening paragraph with **emphasis** and a [link](https://example.com).

## A useful question

- One consideration
- Another consideration
```

To add an essay, create `content/ideas/your-essay-slug.md`. Its filename becomes its URL, `/ideas/your-essay-slug/`. The build automatically adds it to the Ideas page. `featured: true` includes it on Home. `order` controls ordering. Dates use `YYYY-MM-DD`.

Home uses a deliberate heading structure: one `#` introduction, then the framework `##` containing three `###` lenses, then an experience `##`. Keep that structure when changing copy. Interior pages allow normal Markdown headings, lists, links, images, blockquotes, code, and tables. Use one `#` per page.

To add a new top-level page: add its Markdown file, add its slug to the `pages` list in `scripts/build.mjs`, and add a navigation entry to `site.md`.

Logo lettering is artwork and remains in SVG paths; textual identity copy is maintained separately in `site.md`.

## Set your contact destination

No email address or verified personal profile URL was supplied. The current button is clearly labeled **Find Alan on LinkedIn** and opens a LinkedIn people search, not a guessed personal profile.

In `content/site.md`, set `contactUrl` to your actual profile URL or `mailto:your-address@example.com`; update `contactButton` and `contactText` to match. Contact blocks then update across the site. There is no form pretending to send a message.

## Change the design or implementation

- `src/style.css`: brand colors, type stacks, spacing, layout, responsive rules, print styling. The first token block changes shared values.
- `src/menu.js`: small, commented phone-menu enhancement with keyboard support.
- `scripts/build.mjs`: commented Markdown rendering, page templates, essay discovery, metadata, asset copying.
- `scripts/check.mjs`: checks local pages/links/assets and makes sure distribution SVGs contain paths rather than bitmap or font references.
- `scripts/serve.mjs`: a minimal local preview server.
- `vendor/marked.mjs`: Marked 17.0.5, included under its MIT license. Do not edit vendor code; replace it deliberately to upgrade the parser.
- `public/assets/brand/`: editable SVG artwork, copied to the built site.

Markdown is trusted author content. Raw HTML is supported by the parser. Do not accept untrusted visitor Markdown without adding a sanitizer. Builds overwrite `dist/`; edit source content rather than generated HTML.

## SVG asset inventory

Every SVG is a real vector with outlined lettering: no embedded raster and no font installation required.

Six compositions are supplied in color, monochrome, and reverse: `primary`, `header`, `wordmark`, `stacked`, `icon`, and `intellectual`. `favicon.svg` is a simplified small-size derivative. The header variant deliberately omits the descriptor and theme so the name stays readable in a compact navigation bar.

Colors: charcoal `#1F2226`, deep red `#92191A`, neutral gray `#B8B8B8`, white `#FFFFFF`.

These are traced production reconstructions from your supplied raster. They preserve the source letterforms without claiming to identify its original fonts. Tracing removes shading and approximates contours; it does not recover the original designer’s Bézier geometry. SVG paths can be refined in Inkscape or Illustrator. The stacked version is a new arrangement of traced components. The simplified favicon is also a derivative.

Add clear space of at least one quarter of the visible icon height in your layout. Use the full primary composition at approximately 950px visible width or larger when its descriptor and theme must be read. The icon begins at 64px visible width. Use `header` without supporting small text for compact headers. Reverse files are intended for dark surfaces; the node outline remains transparent negative space.

Optional `scripts/trace-logo.py` documents how paths were generated and requires Python with Pillow, NumPy, and SciPy plus the original raster as an argument. It is not needed to build or maintain the website.

## Content and launch review

The three starter essays are newly drafted editorial copy for your review, not previously published articles or empirical research reports. The research page states interests; no unpublished paper is represented as accepted, peer-reviewed, or downloadable. The selected professional profile is intentionally concise and is not a complete dated CV.

Before a public launch, review the essays and biography, verify current roles/credentials, supply a real contact destination, and add approved research/manuscript links and a complete CV if desired. No professional portrait was supplied, so the site uses the brand mark rather than an invented portrait.

`robots.txt` currently discourages indexing for the private first version. Change its content to `User-agent: *` followed by `Allow: /` for a public launch. The deployed first version is private. This package does not change your existing drchmiel.com website or DNS.

## Hosting on your existing domain

The built site uses root-relative paths and is intended for a domain root such as `https://drchmiel.com/`. For GitHub Pages at a custom domain, publish `dist/` through a workflow or copy its contents to the publishing branch and preserve the domain’s `CNAME` file. Add an empty `.nojekyll` file if publishing directly through GitHub Pages. An example workflow is included in `docs/github-pages.yml`; copy it into `.github/workflows/` when you choose to use it. It is provided as a template and does not deploy anything by itself.

For a repository subpath such as `username.github.io/website/`, adjust link/asset prefixes in the build before publishing. Avoid deploying the unbuilt project directory.
