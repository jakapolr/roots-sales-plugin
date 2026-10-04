import json, csv, os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
rows=list(csv.DictReader(open(os.path.join(HERE,'../../../references/odoo20-ce/data/module_catalog_19_vs_20.csv'))))
def area(m):
    n=m.replace('odoo/addons/','')
    p=lambda *a: any(n==x or n.startswith(x+'_') for x in a)
    if n.startswith('l10n'): return 'l10n'
    if 'test' in n.split('_') or n.startswith('test'): return 'framework'
    if p('pos','point_of_sale'): return 'pos'
    if p('website','theme','event','survey','mass_mailing','marketing_card','social_media','link_tracker','utm','gamification'): return 'website'
    if p('crm_sale_project'): return 'sales'
    if p('hr','project','timesheet','resource','lunch','sale_timesheet','sale_project','calendar_hr'): return 'hr'
    if p('account','payment','analytic','certificate','snailmail_account','currency_rate_live'): return 'accounting'
    if p('stock','purchase','mrp','repair','maintenance','fleet','quality','product_expiry'): return 'supply'
    if p('sale','crm','product','loyalty','delivery','uom','sales_team','partnership','mysubscription'): return 'sales'
    if p('mail','im_livechat','sms','calendar','portal','phone_validation','contacts','partner_autocomplete','google_calendar','microsoft_calendar','google_gmail','microsoft_outlook','rating','snailmail','digest','privacy_lookup','bus'): return 'communication'
    if n in ('base','populate','rpc') or m.startswith('odoo/addons/'): return 'framework'
    return 'webui'
out=[]
for r in rows:
    out.append({'m':r['module'],'s':r['status'],'fc':r['files_changed'],'a':area(r['module']),'app':r['application']=='True','auto':r['auto_install']=='True','sum':r['summary'],'name':r['name'],'dep':r['depends'],'cat':r['category']})
dst=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'../build/files/modules.json')
os.makedirs(os.path.dirname(dst),exist_ok=True)
json.dump(out,open(dst,'w'),ensure_ascii=False,separators=(',',':'))
