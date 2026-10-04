import json, os, subprocess, csv
SRC=os.environ.get('ODOO_SRC','.')
os.chdir(SRC)
m19=json.load(open(SRC+'/data/manifests_19.json')); m20=json.load(open(SRC+'/data/manifests_20.json'))
def path(v,k): return f'odoo{v}/' + (k if k.startswith('odoo/') else 'addons/'+k)
def churn(k):
    r=subprocess.run(['diff','-rq',path(19,k),path(20,k)],capture_output=True,text=True).stdout.splitlines()
    return len(r)
def nfiles(v,k): return sum(len(f) for _,_,f in os.walk(path(v,k)))
rows=[]
for k in sorted(set(m19)|set(m20)):
    a=m20.get(k) or m19.get(k)
    if k in m20 and k not in m19: st='NEW'; ch=''
    elif k in m19 and k not in m20: st='REMOVED'; ch=''
    else:
        c=churn(k); n=nfiles(20,k); ch=f'{c}/{n}'
        st='CHANGED-MAJOR' if c>=max(10,0.3*n) else ('CHANGED' if c>0 else 'UNCHANGED')
    grp='Localization' if k.startswith('l10n') else ('Test' if 'test' in k else (a.get('category') or '').split('/')[0])
    rows.append(dict(module=k,status=st,files_changed=ch,group=grp,category=a.get('category',''),application=bool(a.get('application')),auto_install=bool(a.get('auto_install')),summary=(a.get('summary') or a.get('name') or '').replace('|','/').replace('\n',' ').strip(),name=a.get('name',''),depends=','.join(a.get('depends',[]) or [])))
with open(SRC+'/data/module_catalog_19_vs_20.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(rows,open(SRC+'/data/catalog.json','w'),indent=1)
from collections import Counter
print(Counter(r['status'] for r in rows))
