import { marked } from 'marked'; import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const HERE=path.dirname(fileURLToPath(import.meta.url));
const KB=path.resolve(HERE,'../../../references/odoo20-ce'), OUT=path.resolve(HERE,'../build/files/reports'); fs.mkdirSync(OUT,{recursive:true});
const map={framework:'areas/01-framework-core.md',webui:'areas/02-web-ui-technical.md',communication:'areas/03-communication-collab.md',accounting:'areas/04-accounting-finance.md',sales:'areas/05-sales-crm-product.md',supply:'areas/06-supply-chain-mrp.md',pos:'areas/07-point-of-sale.md',website:'areas/08-website-ecommerce-marketing.md',hr:'areas/09-hr-project-services.md',l10n:'areas/10-localizations.md',paper:'STUDY-PAPER.md'};
for (const [id,f] of Object.entries(map)) {
  let md=fs.readFileSync(`${KB}/${f}`,'utf8');
  md=md.replace(/^# .*\n/,'');            // drop H1
  const parts=md.split(/^(?=## )/m).filter(s=>s.trim());
  const secs=parts.map(p=>{const m=p.match(/^## (.*)\n/); const h=m?m[1].trim():''; const body=m?p.slice(m[0].length):p;
    let html=marked.parse(body);
    html=html.replace(/<a href="(?!https?:)[^"]*"/g,'<a'); // strip relative links
    return {h, html};});
  fs.writeFileSync(`${OUT}/${id}.json`, JSON.stringify(secs));
  console.log(id, secs.length, Math.round(JSON.stringify(secs).length/1024)+'KB');
}
