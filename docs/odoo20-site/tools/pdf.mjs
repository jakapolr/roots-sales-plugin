import { marked } from 'marked';
import { chromium } from 'playwright';
import fs from 'fs';
const [src, out, title] = process.argv.slice(2);
const md = fs.readFileSync(src, 'utf8');
const body = marked.parse(md);
const html = `<!doctype html><html><head><meta charset="utf-8"><title>${title}</title><style>
@page{size:A4;margin:18mm 16mm 20mm}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:10.2pt;line-height:1.5;color:#1d2a26}
h1{font-size:22pt;color:#0f4d3c;margin:0 0 6pt;line-height:1.15}
h2{font-size:15pt;color:#0f4d3c;border-bottom:1.5pt solid #0f4d3c;padding-bottom:3pt;margin-top:22pt;break-after:avoid}
h3{font-size:12pt;color:#13352c;margin-top:14pt;break-after:avoid}
code{font-family:"DejaVu Sans Mono",monospace;font-size:8.6pt;background:#eef3f1;padding:0 2pt;border-radius:2pt}
pre{background:#eef3f1;padding:7pt;border-radius:3pt;white-space:pre-wrap;font-size:8.4pt}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;font-family:"DejaVu Sans",sans-serif;font-size:8.2pt;margin:6pt 0;break-inside:auto}
th,td{border:0.6pt solid #b9c9c3;padding:3pt 4pt;vertical-align:top;text-align:left}
th{background:#dfeae6}
tr{break-inside:avoid}
blockquote{border-left:3pt solid #c58b2a;margin:8pt 0;padding:2pt 10pt;background:#faf5ea}
a{color:#0f4d3c}
hr{border:none;border-top:0.6pt solid #b9c9c3}
</style></head><body>${body}</body></html>`;
const b = await chromium.launch();
const p = await b.newPage(); await p.setContent(html, { waitUntil: 'load' });
await p.pdf({ path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: `<div style="font-size:7pt;width:100%;text-align:center;color:#6b7c76;font-family:sans-serif">${title} · Trinity Roots internal · page <span class="pageNumber"></span>/<span class="totalPages"></span></div>`,
  margin: { top: '18mm', bottom: '20mm', left: '16mm', right: '16mm' } });
await b.close(); console.log('ok', out);
