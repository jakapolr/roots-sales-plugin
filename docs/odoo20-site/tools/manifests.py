import ast, os, sys, json, csv
SRC=os.environ.get('ODOO_SRC','.')  # folder holding odoo19/ and odoo20/ shallow clones
def load(root):
    out = {}
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d, '__manifest__.py')
        if not os.path.isfile(p): continue
        try: m = ast.literal_eval(open(p).read())
        except Exception as e: m = {'_err': str(e)}
        out[d] = m
    return out
for v in ('19','20'):
    m = load(fSRC+'/odoo{v}/addons')
    m.update({f'odoo/addons/{k}':x for k,x in load(fSRC+'/odoo{v}/odoo/addons').items()})
    json.dump(m, open(fSRC+'/data/manifests_{v}.json','w'), indent=1, default=str)
    print(v, len(m))
