"""Build the Roots Odoo 20 Field Guide into docs/odoo20-site/build/files/ (git-ignored).

Usage (from repo root):
    npm --prefix docs/odoo20-site/tools install     # once: installs marked (+ optional playwright for the PDF)
    python3 docs/odoo20-site/build.py [--pdf]

Then publish build/files/index.html as a claude.ai artifact with every other file under build/files/
as supporting files, and capabilities {"downloads": true, "sample": {}}.
"""
import glob, json, os, shutil, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__))
KB = os.path.normpath(os.path.join(H, '../../references/odoo20-ce'))
SKILL = os.path.normpath(os.path.join(H, '../../skills/odoo20-ce-expert/SKILL.md'))
OUT = os.path.join(H, 'build', 'files')

shutil.rmtree(os.path.join(H, 'build'), ignore_errors=True)
os.makedirs(os.path.join(OUT, 'docs'))

# 1. downloadable docs
for f in ['STUDY-PAPER.md', '01-module-catalog.md', 'llms.txt']:
    shutil.copy(os.path.join(KB, f), os.path.join(OUT, 'docs', f))
for f in glob.glob(os.path.join(KB, 'areas', '*.md')):
    shutil.copy(f, os.path.join(OUT, 'docs'))
shutil.copy(os.path.join(KB, 'data', 'module_catalog_19_vs_20.csv'), os.path.join(OUT, 'docs'))
shutil.copy(os.path.join(H, 'tools', 'README-AI.md'), os.path.join(OUT, 'docs'))
shutil.copy(SKILL, os.path.join(OUT, 'docs', 'odoo20-ce-expert-SKILL.md'))
with open(os.path.join(OUT, 'docs', 'odoo20-ce-knowledge-combined.md'), 'w') as out:
    out.write('# Odoo 20 Community Edition — Combined Knowledge File (Trinity Roots)\n\n'
              'Source: odoo/odoo branch 20.0 @ b100a87 vs 19.0, studied 2026-10-03. Evidence tags: [code] verified in source, '
              '[web] unverified. This single file concatenates the study paper and all 10 area reports, for upload into an '
              "AI assistant's knowledge (Claude Project, custom GPT, NotebookLM, RAG).\n")
    for f in [os.path.join(KB, 'STUDY-PAPER.md')] + sorted(glob.glob(os.path.join(KB, 'areas', '*.md'))):
        out.write(f'\n---\n<!-- FILE: {os.path.basename(f)} -->\n\n' + open(f).read())

# 2. module dataset, 3. pre-rendered report sections
subprocess.run([sys.executable, os.path.join(H, 'tools', 'area.py'), os.path.join(OUT, 'modules.json')], check=True)
subprocess.run(['node', os.path.join(H, 'tools', 'reports.mjs')], check=True)

# 4. optional PDF of the study paper
if '--pdf' in sys.argv:
    subprocess.run(['node', os.path.join(H, 'tools', 'pdf.mjs'), os.path.join(KB, 'STUDY-PAPER.md'),
                    os.path.join(OUT, 'Odoo20-CE-Study-Paper.pdf'), 'Odoo 20 CE Study Paper'], check=True)

# 5. page
content = {}
for f in glob.glob(os.path.join(H, 'content', '*.json')):
    d = json.load(open(f)); content['overview' if 'top10' in d else d['id']] = d
mods = json.load(open(os.path.join(OUT, 'modules.json')))
sizes = {}
for root, _, fs in os.walk(OUT):
    for n in fs:
        p = os.path.join(root, n); sizes[os.path.relpath(p, OUT)] = os.path.getsize(p)
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
src = open(os.path.join(H, 'index.src.html')).read()
html = src.replace('/*__CONTENT__*/', dump(content)).replace('/*__MODULES__*/', dump(mods)).replace('/*__SIZES__*/{}', dump(sizes))
open(os.path.join(OUT, 'index.html'), 'w').write(html)
os.remove(os.path.join(OUT, 'modules.json'))  # inlined into the page
print('built', OUT, f'({round(len(html.encode())/1024)} KB page)')
