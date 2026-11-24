import os, shutil
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
PLAN = "https://buy.stripe.com/aFa14pe7g6O2h0jaZY1sQ01"

CSS = """
:root{--sea:#0E3A5B;--sea2:#17507D;--mist:#E4EDF2;--mist2:#F1F6F8;--paper:#FBFCFD;--ink:#12283B;--muted:#4C6274;
--gain:#17744A;--gainbg:#E2F2E9;--loss:#9E4A3C;--line:#C6D5DE;--gold:#B38A33}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;font-family:Commissioner,system-ui,sans-serif;font-size:18px;line-height:1.6;color:var(--ink);background:var(--mist2)}
h1,h2,h3{font-family:Literata,Georgia,serif;font-weight:600;line-height:1.15;margin:0;color:var(--sea)}
p{margin:0}
a{color:var(--sea2)}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:4px}
.wrap{max-width:1120px;margin:0 auto;padding:0 28px}
/* header */
header{background:var(--paper);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--sea);font-family:Literata,Georgia,serif;font-weight:600;font-size:24px}
.brand svg{width:34px;height:34px}
nav{display:flex;align-items:center;gap:22px;font-size:16px}
nav a{color:var(--muted);text-decoration:none}
nav a:hover{color:var(--sea)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;padding:0 26px;border-radius:10px;
background:var(--sea);color:#fff;text-decoration:none;font-weight:600;font-size:17px;border:0;cursor:pointer;font-family:inherit}
.btn:hover{background:var(--sea2)}
.btn.small{min-height:42px;padding:0 18px;font-size:15px}
.btn.quiet{background:transparent;color:var(--sea);border:1.5px solid var(--sea)}
.btn.quiet:hover{background:var(--mist)}
/* hero */
.hero{background:var(--mist);padding:72px 0 80px}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}
.hero h1{font-size:50px;letter-spacing:-.01em;max-width:18ch}
.price{display:flex;align-items:baseline;gap:10px;margin:26px 0 6px}
.price b{font-family:Literata,Georgia,serif;font-size:76px;line-height:1;color:var(--sea);font-weight:600}
.price span{font-size:22px;color:var(--muted)}
.hero .sub{font-size:19px;color:var(--muted);max-width:46ch;margin-top:14px}
.actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:30px}
.promise{display:flex;gap:16px;align-items:center;margin-top:28px;max-width:540px;padding:18px 20px;background:#FBF3DE;border:1.5px solid #E2CC92;border-radius:12px;font-size:17px;font-weight:700;color:var(--sea);line-height:1.45}
.promise svg{flex:none;width:56px;height:56px;color:var(--gold)}
/* statement */
.statement{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:30px 30px 24px;box-shadow:0 18px 40px rgba(14,58,91,.10)}
.statement .head{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:6px}
.statement .head h2{font-size:20px}
.statement .head small{color:var(--muted);font-size:14px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:12px 0;border-bottom:1px dashed var(--line);font-variant-numeric:tabular-nums}
.row .k{color:var(--ink);font-size:16px}
.row .v{font-weight:700;color:var(--gain)}
.row.big .v{font-size:25px;font-family:Literata,Georgia,serif}
.row.mid .v{font-size:22px}
.row.fee{border-bottom:0}
.row.fee .k{color:var(--muted);font-size:14px}
.row.fee .v{color:var(--loss);font-weight:500;font-size:15px}
.net{display:flex;justify-content:space-between;align-items:center;background:var(--gainbg);border-radius:10px;padding:14px 16px;margin-top:6px}
.net span{font-size:15px;color:var(--ink)}
.net b{font-size:26px;color:var(--gain);font-family:Literata,Georgia,serif}
.statement .note{font-size:13px;color:var(--muted);margin-top:12px}
/* sections */
section{padding:84px 0}
.intro{max-width:60ch;margin-bottom:40px}
.intro h2{font-size:38px;margin-bottom:12px}
.intro p{color:var(--muted);font-size:19px}
.list{display:grid;grid-template-columns:1fr 1fr;gap:0 56px}
.item{display:grid;grid-template-columns:44px 1fr;gap:16px;padding:24px 0;border-top:1px solid var(--line)}
.item .ic{width:44px;height:44px;border-radius:50%;display:grid;place-items:center}
.item .ic svg{width:22px;height:22px}
.ic.save{background:var(--gainbg);color:var(--gain)}
.ic.earn{background:#DDEAF4;color:var(--sea2)}
.item h3{font-size:21px;margin-bottom:6px}
.item p{color:var(--muted);font-size:17px}
.item .tag{display:block;font-size:14px;font-weight:600;margin-bottom:4px}
.tag.save{color:var(--gain)}.tag.earn{color:var(--sea2)}
.bonus{margin-top:28px;padding:20px 24px;background:var(--mist);border-radius:12px;color:var(--ink);font-size:17px}
.plans .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:28px}
.card{background:#fff;border:1px solid #D5DEE6;border-radius:14px;padding:28px}
.card.feat{border:2px solid var(--sea2)}
.card h3{font-size:24px;margin-bottom:6px}
.card .pp b{font-size:40px}.card .pp span{margin-left:8px;color:var(--muted)}
.card p{color:var(--muted);margin:10px 0}
.card ul{margin:14px 0 22px 20px}.card li{margin-bottom:8px}
.plans .small{margin-top:18px;color:var(--muted);font-size:15px}
/* guarantee band */
.band{background:var(--sea);color:#E8F0F5}
.band .wrap{display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center}
.seal{width:150px;height:150px;color:var(--gold)}
.band h2{color:#fff;font-size:36px;margin-bottom:14px}
.band p{font-size:19px;max-width:62ch;color:#D3E1EA}
.band p+p{margin-top:12px;font-size:16px;color:#B5C9D6}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;counter-reset:s}
.step{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px}
.step .n{font-family:Literata,Georgia,serif;font-size:40px;color:var(--gold);line-height:1;margin-bottom:12px}
.step h3{font-size:20px;margin-bottom:8px}
.step p{color:var(--muted);font-size:17px}
/* check offer */
.check{background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.check .wrap{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.check h2{font-size:32px;margin-bottom:12px}
.check p{color:var(--muted)}
.ticks{list-style:none;padding:0;margin:20px 0}.ticks li{position:relative;padding-left:32px;margin:10px 0;color:var(--ink)}.ticks li::before{content:"";position:absolute;left:0;top:5px;width:20px;height:20px;border-radius:50%;background:var(--gainbg) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2317744A' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6,12.5 10,16.5 18,8'/%3E%3C/svg%3E") center/14px no-repeat}.check .small{font-size:15px}
form{display:grid;gap:14px;background:var(--mist2);border:1px solid var(--line);border-radius:14px;padding:26px}
label{font-size:15px;font-weight:600;display:block;margin-bottom:4px}
input{width:100%;font:inherit;font-size:17px;padding:12px 14px;border:1px solid #A9BDCB;border-radius:8px;background:#fff;color:var(--ink)}
/* faq */
.faq{max-width:800px}
details{border-top:1px solid var(--line);padding:20px 0}
details:last-of-type{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:600;font-size:19px;color:var(--sea);list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:24px;line-height:1;color:var(--sea2)}
details[open] summary::after{content:"−"}
details p{margin-top:10px;color:var(--muted)}
.final{background:var(--mist);text-align:center}
.final h2{font-size:38px;margin-bottom:12px}
.final p{color:var(--muted);margin-bottom:28px}
footer{background:var(--sea);color:#B5C9D6;font-size:15px;padding:30px 0}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer a{color:#fff}
@media (max-width:900px){
 .hero .wrap,.check .wrap{grid-template-columns:1fr;gap:40px}
 .hero h1{font-size:38px}.price b{font-size:62px}
 .list{grid-template-columns:1fr}
 .steps{grid-template-columns:1fr}
 .band .wrap{grid-template-columns:1fr;gap:20px}.seal{width:110px;height:110px}
 nav a.hide{display:none}
 section{padding:64px 0}
}
"""

MARK = '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="32" fill="#0E3A5B"/><circle cx="28" cy="28" r="15" fill="none" stroke="#fff" stroke-width="5"/><line x1="39" y1="39" x2="49" y2="49" stroke="#fff" stroke-width="6" stroke-linecap="round"/><polyline points="21,28.5 26.5,34 35,23" fill="none" stroke="#3DD68C" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"/><polyline points="8.5,12 11,14.5 15.5,9.5"/></svg>'
SEAL = '<svg class="seal" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="56" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="60" cy="60" r="47" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="2 4"/><path d="M60 30l20 7.5v15c0 11-8.5 20.8-20 22.5-11.5-1.7-20-11.5-20-22.5v-15L60 30z" fill="none" stroke="currentColor" stroke-width="3"/><polyline points="50,60 57,67 71,52" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON = {
 'ads':'<path d="M3 17l6-6 4 4 8-8"/><polyline points="14,7 21,7 21,14"/>',
 'map':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'reply':'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 'star':'<polygon points="12,3 14.8,8.9 21,9.6 16.4,13.8 17.7,20 12,16.9 6.3,20 7.6,13.8 3,9.6 9.2,8.9"/>',
 'site':'<rect x="3" y="4" width="18" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><polyline points="8,11 11,14 16,9"/>',
 'page':'<path d="M6 3h8l4 4v14H6z"/><line x1="12" y1="11" x2="12" y2="17"/><line x1="9" y1="14" x2="15" y2="14"/>',
 'eye':'<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'ai':'<path d="M12 3l1.8 4.6L18.5 9l-4.7 1.6L12 15l-1.8-4.4L5.5 9l4.7-1.4z"/><path d="M18 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>'}
def ic(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'

def page(T, lang, root):
    plans_html = "".join(f'<div class="card{" feat" if d["feat"] else ""}"><h3>{d["n"]}</h3><div class="pp"><b>{d["pr"]}</b><span>{T["permonth"]}</span></div><p>{d["d"]}</p><ul>{"".join("<li>"+x+"</li>" for x in d["pts"])}</ul><a class="btn" href="#free">{T["plans_cta"]}</a></div>' for d in T['plans'])
    items = "".join(f'<div class="item"><div class="ic {c}">{ic(i)}</div><div><span class="tag {c}">{tg}</span><h3>{h}</h3><p>{p}</p></div></div>' for c,i,tg,h,p in T['items'])
    rows = T['rows']
    steps = "".join(f'<div class="step"><div class="n">{n}</div><h3>{h}</h3><p>{p}</p></div>' for n,(h,p) in enumerate(T['steps'],1))
    import json as _j
    _base="https://kerdos.sgdventures.com"
    _url=_base+root
    _org={"@type":"Organization","@id":_base+"/#org","name":"Kerdos","url":_base+"/","email":"sam@sgdventures.com","sameAs":["https://www.linkedin.com/company/kerdos-sgd"],"parentOrganization":{"@type":"Organization","name":"SGD Ventures"}}
    _offers=[{"@type":"Offer","name":d["n"],"price":d["pr"].replace("€",""),"priceCurrency":"EUR","priceSpecification":{"@type":"UnitPriceSpecification","price":d["pr"].replace("€",""),"priceCurrency":"EUR","billingDuration":1,"unitCode":"MON"}} for d in T["plans"]]
    _graph=[_org,{"@type":"WebSite","@id":_base+"/#site","url":_base+"/","name":"Kerdos","inLanguage":lang,"publisher":{"@id":_base+"/#org"}},
      {"@type":"Service","name":"Kerdos Growth Plan","provider":{"@id":_base+"/#org"},"serviceType":"Google Ads, Google Business Profile and website care","areaServed":["GB","IE","GR"],"offers":_offers},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in T["faq"]]}]
    ldjson=_j.dumps({"@context":"https://schema.org","@graph":_graph},ensure_ascii=False)
    ogtags=f'<meta property="og:type" content="website"><meta property="og:site_name" content="Kerdos"><meta property="og:title" content="{T["title"]}"><meta property="og:description" content="{T["desc"]}"><meta property="og:url" content="{_url}"><meta name="twitter:card" content="summary">'
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in T['faq'])
    F = T['form']
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T['title']}</title>
<meta name="description" content="{T['desc']}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400;500;600;700&family=Literata:opsz,wght@7..72,500;7..72,600&display=swap" rel="stylesheet">
{ogtags}
<script type="application/ld+json">{ldjson}</script>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
<a class="brand" href="{root}">{MARK}Kerdos</a>
<nav aria-label="{T['navl']}"><a class="hide" href="#included">{T['n1']}</a><a class="hide" href="#guarantee">{T['n2']}</a><a class="hide" href="#faq">{T['n3']}</a><a href="{T['otherurl']}" lang="{T['otherlang']}">{T['other']}</a><a class="btn small" href="#free">{T['start']}</a></nav>
</div></header>

<main>
<div class="hero"><div class="wrap">
<div>
<h1>{T['h1']}</h1>
<div class="price"><b>€150</b><span>{T['permonth']}</span></div>
<p class="sub">{T['sub']}</p>
<div class="actions"><a class="btn" href="#free">{T['cta']}</a><a class="btn quiet" href="#included">{T['cta2']}</a></div>
<p class="promise">{SHIELD}<span>{T['promise']}</span></p>
</div>
<div class="statement" role="figure" aria-label="{T['stlabel']}">
<div class="head"><h2>{T['sthead']}</h2><small>{T['stsmall']}</small></div>
<div class="row big"><span class="k">{rows[0][0]}</span><span class="v">{rows[0][1]}</span></div>
<div class="row mid"><span class="k">{rows[1][0]}</span><span class="v">{rows[1][1]}</span></div>
<div class="row mid"><span class="k">{rows[2][0]}</span><span class="v">{rows[2][1]}</span></div>
<div class="row mid"><span class="k">{rows[3][0]}</span><span class="v">{rows[3][1]}</span></div>
<div class="row fee"><span class="k">{T['fee']}</span><span class="v">{T['feev']}</span></div>
<div class="net"><span>{T['net']}</span><b>{T['netv']}</b></div>
<p class="note">{T['stnote']}</p>
</div>
</div></div>

<section id="included"><div class="wrap">
<div class="intro"><h2>{T['h2a']}</h2><p>{T['pa']}</p></div>
<div class="list">{items}</div>
<p class="bonus">{T['bonus']}</p>
</div></section>

<section id="plans" class="plans"><div class="wrap">
<div class="intro"><h2>{T['plans_h']}</h2><p>{T['plans_p']}</p></div>
<div class="cards">{plans_html}</div>
<p class="small">{T['plans_note']}</p>
</div></section>

<section id="guarantee" class="band"><div class="wrap">
{SEAL}
<div><h2>{T['gh']}</h2><p>{T['gp']}</p><p>{T['gp2']}</p></div>
</div></section>

<section id="start"><div class="wrap">
<div class="intro"><h2>{T['sh']}</h2><p>{T['sp']}</p></div>
<div class="steps">{steps}</div>
</div></section>

<section id="free" class="check"><div class="wrap">
<div><h2>{T['ch']}</h2><p>{T['cp']}</p><ul class="ticks">{"".join(f"<li>{x}</li>" for x in T['ticks'])}</ul><p class="small">{T['cp2']}</p></div>
<form name="{F['name']}" method="POST" data-netlify="true" netlify-honeypot="company_url" action="/thanks.html">
<input type="hidden" name="form-name" value="{F['name']}">
<p style="display:none"><label>Leave empty <input name="company_url"></label></p>
<div><label for="n">{F['n']}</label><input id="n" name="name" required autocomplete="name"></div>
<div><label for="e">Email</label><input id="e" type="email" name="email" required autocomplete="email"></div>
<div><label for="w">{F['w']}</label><input id="w" name="website" autocomplete="url"></div>
<div><label for="b">{F['b']}</label><input id="b" name="budget" placeholder="{F['bp']}"></div>
<button class="btn" type="submit">{F['send']}</button>
</form>
</div></section>

<section id="faq"><div class="wrap faq">
<div class="intro"><h2>{T['n3']}</h2></div>
{faq}
</div></section>

<section class="final"><div class="wrap">
<h2>{T['fh']}</h2><p>{T['fp']}</p><a class="btn" href="#free">{T['cta']}</a>
</div></section>
</main>

<footer><div class="wrap"><span>© 2026 Kerdos, {T['by']} SGD Ventures · <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a></span><span>{T['notg']}</span></div></footer>
<elevenlabs-convai style="bottom:72px" agent-id="agent_4201m7w49pgfetsbjp9xje4xqs11"></elevenlabs-convai><script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
</body>
</html>'''

EL = dict(title="Kerdos – Φροντίδα της παρουσίας σας στο Google, €150/μήνα",
 desc="Λιγότερα χαμένα χρήματα στις διαφημίσεις Google, περισσότερα τηλέφωνα από τους Χάρτες. €150 τον μήνα, χωρίς δέσμευση, με εγγύηση αποτελέσματος τον πρώτο μήνα.",
 navl="Μενού", n1="Τι περιλαμβάνει", n2="Εγγύηση", n3="Ερωτήσεις", other="English", otherurl="/", otherlang="en", start="Δωρεάν αναφορά",
 h1="Φροντίζουμε την παρουσία σας στο Google, κάθε μήνα.", permonth="τον μήνα",
 sub="Λιγότερα χαμένα χρήματα στις διαφημίσεις, περισσότερα τηλέφωνα από τους Χάρτες Google και μια ιστοσελίδα που δουλεύει σωστά. Εσείς ασχολείστε με τους πελάτες σας.",
 cta="Πάρτε τη δωρεάν αναφορά σας", cta2="Δείτε τι περιλαμβάνει",
 promise="Εγγύηση πρώτου μήνα: αν η πρώτη αναφορά δεν δείχνει εξοικονόμηση και βελτίωση, σας επιστρέφουμε τα χρήματα. Ακύρωση όποτε θέλετε.",
 stlabel="Παράδειγμα μηνιαίας αναφοράς", sthead="Ο μήνας σας σε αριθμούς", stsmall="Παράδειγμα", feev="−€150", netv="+€600",
 rows=[("Εξοικονόμηση στις διαφημίσεις Google","+€750"),("Νέες κριτικές Google","+9"),("Κλήσεις από τους Χάρτες Google","+23%"),("Νέες σελίδες στο Google","+1")],
 fee="Συνδρομή Kerdos", net="Σας μένουν μετά τη συνδρομή", stnote="Ενδεικτικά νούμερα. Η δική σας αναφορά δείχνει τα πραγματικά σας αποτελέσματα, κάθε μήνα.",
 h2a="Οκτώ πράγματα που κάνουμε για εσάς κάθε μήνα", pa="Τα αναλαμβάνουμε όλα. Εσείς βλέπετε τα αποτελέσματα στη μηνιαία αναφορά.",
 items=[("save","ads","Εξοικονόμηση","Έλεγχος κόστους Google Ads","Μπλοκάρουμε τις αναζητήσεις που σας κοστίζουν χωρίς να φέρνουν πελάτες και σας λέμε πόσα ευρώ γλιτώσατε."),
  ("earn","map","Περισσότεροι πελάτες","Προφίλ στους Χάρτες Google","Εβδομαδιαίες αναρτήσεις, σωστό ωράριο και αργίες, φωτογραφίες και απαντήσεις σε ερωτήσεις πελατών."),
  ("earn","reply","Περισσότεροι πελάτες","Απάντηση σε κάθε κριτική","Προσωπική, ευγενική απάντηση μέσα σε 24 ώρες. Για τις αρνητικές σας ενημερώνουμε πρώτα."),
  ("earn","star","Περισσότεροι πελάτες","Περισσότερες κριτικές 5 αστέρων","Σύνδεσμος και QR code για τις κριτικές σας, με έτοιμο μήνυμα για τους πελάτες μετά από κάθε δουλειά."),
  ("save","site","Προστασία","Φροντίδα ιστοσελίδας","Ελέγχουμε ταχύτητα, προβλήματα σε κινητά και σπασμένους συνδέσμους, τα διορθώνουμε και σας ειδοποιούμε αν η σελίδα πέσει."),
  ("earn","page","Περισσότεροι πελάτες","Μία νέα σελίδα στο Google κάθε μήνα","Για μια υπηρεσία και περιοχή που σας ενδιαφέρει, ώστε να σας βρίσκουν δωρεάν από τις αναζητήσεις."),
  ("save","eye","Ένα βήμα μπροστά","Παρακολούθηση ανταγωνισμού","Τι διαφημίζουν οι κοντινοί σας ανταγωνιστές και πώς συγκρίνονται οι κριτικές τους."),
  ("earn","ai","Νέο","Να σας προτείνει η τεχνητή νοημοσύνη","Όλο και περισσότεροι ρωτούν το ChatGPT, το Claude, το Gemini ή τις απαντήσεις AI της Google ποιον να καλέσουν. Κάνουμε την επιχείρησή σας εύκολη να βρεθεί και να προταθεί: σαφείς σελίδες υπηρεσιών και περιοχών, ίδια σωστά στοιχεία σε χάρτες και καταλόγους, και τίποτα στην ιστοσελίδα σας που να εμποδίζει τα εργαλεία αναζήτησής τους.")],
 plans_h="Δύο τρόποι να συνεργαστούμε", plans_p="Ξεκινήστε με τη δωρεάν αναφορά. Μετά διαλέγετε το πακέτο που σας ταιριάζει. Χωρίς συμβόλαιο, ακύρωση όποτε θέλετε.",
 plans=[dict(n="Growth Plan", pr="€150", d="Τα οκτώ παραπάνω, γίνονται για εσάς κάθε μήνα, με μηνιαία αναφορά αποτελεσμάτων.", pts=["Έλεγχος κόστους Google Ads και αναφορά χρημάτων που γλιτώσατε","Προφίλ Χαρτών Google, κριτικές και φροντίδα ιστοσελίδας","Μία νέα σελίδα στο Google τον μήνα","Να σας βρίσκουν οι βοηθοί τεχνητής νοημοσύνης","Εγγύηση πρώτου μήνα"], feat=False),
  dict(n="Growth + Content", pr="€250", d="Όλα του Growth Plan, και η επιχείρησή σας ορατή και ενεργή στα social media.", pts=["Όλα του Growth Plan","12 έτοιμες αναρτήσεις τον μήνα για Facebook και Instagram, με εικόνες","Μηνιαίο πλάνο περιεχομένου: τι θα αναρτήσετε, πότε, και εποχικές προσφορές","Ένα σύντομο άρθρο τον μήνα για την ιστοσελίδα σας","Αναρτώνται για εσάς αν μας προσθέσετε στη σελίδα σας, αλλιώς τις παίρνετε έτοιμες"], feat=True)],
 plans_cta="Ξεκινήστε με τη δωρεάν αναφορά", plans_note="Η ίδια εγγύηση πρώτου μήνα ισχύει και για τα δύο πακέτα.",
 bonus="Επιπλέον: μια σύντομη αναφορά στο τέλος κάθε μήνα με τα χρήματα που γλιτώσατε και τι βελτιώθηκε.",
 gh="Δεν είδατε αποτελέσματα τον πρώτο μήνα; Σας επιστρέφουμε τα χρήματα.",
 gp="Στο τέλος του πρώτου μήνα λαμβάνετε την αναφορά σας. Αν δεν δείχνει και εξοικονόμηση χρημάτων και μετρήσιμη βελτίωση για την επιχείρησή σας, σας επιστρέφουμε ολόκληρο το ποσό του πρώτου μήνα.",
 gp2="Βελτίωση σημαίνει περισσότερες κριτικές, περισσότερες κλήσεις ή αιτήματα οδηγιών από τους Χάρτες, ή περισσότερες επισκέψεις στην ιστοσελίδα σε σχέση με τον μήνα πριν ξεκινήσουμε.",
 sh="Πώς λειτουργεί", sp="Πρώτα βλέπετε τι μπορούμε να κάνουμε για εσάς. Μετά αποφασίζετε.",
 steps=[("Ζητάτε τη δωρεάν αναφορά","Συμπληρώνετε 4 στοιχεία. Χωρίς πληρωμή, χωρίς κάρτα, χωρίς πρόσβαση στους λογαριασμούς σας."),
  ("Βλέπετε τι βρήκαμε","Μέσα σε 48 ώρες λαμβάνετε μια αναφορά για την επιχείρησή σας, με ένα εύρημα αναλυτικά και τι άλλο εντοπίσαμε."),
  ("Αποφασίζετε εσείς","Αν σας αξίζει, ξεκινάτε με €150 τον μήνα και αναλαμβάνουμε τα υπόλοιπα. Αν όχι, δεν σας οφείλετε τίποτα.")],
 ch="Δοκιμάστε μας δωρεάν", cp="Συμπληρώστε τα στοιχεία σας και μέσα σε 48 ώρες σας στέλνουμε μια αναφορά για τη δική σας επιχείρηση.",
 ticks=["Ένα πραγματικό εύρημα, αναλυτικά, που μπορείτε να διορθώσετε αμέσως","Τι άλλο εντοπίσαμε που σας κοστίζει χρήματα ή πελάτες","Χωρίς πληρωμή, χωρίς κάρτα, χωρίς πρόσβαση στους λογαριασμούς σας"],
 cp2="Μία δωρεάν αναφορά ανά επιχείρηση.",
 form=dict(name="request-el", n="Όνομα", w="Ιστοσελίδα", b="Περίπου πόσα ξοδεύετε τον μήνα στο Google Ads;", bp="π.χ. 500€", send="Θέλω τη δωρεάν αναφορά"),
 faq=[("Είναι πραγματικά δωρεάν η αναφορά;","Ναι. Δεν ζητάμε κάρτα ούτε πρόσβαση. Τη στέλνουμε μία φορά ανά επιχείρηση και αποφασίζετε εσείς αν θέλετε να συνεχίσουμε."),("Χρειάζεται να δώσω κωδικούς;","Όχι. Μας προσθέτετε ως χρήστη στο Google Ads και ως διαχειριστή στο Προφίλ Επιχείρησης Google με πρόσκληση. Μπορείτε να μας αφαιρέσετε όποτε θέλετε."),
  ("Πότε πληρώνω;","Μόνο αν αποφασίσετε να ξεκινήσουμε, αφού έχετε δει τη δωρεάν αναφορά. Το Growth Plan κοστίζει €150 τον μήνα, ή €250 με το πακέτο Content. Χωρίς συμβόλαιο, και την ακυρώνετε με ένα κλικ."),
  ("Τι ακριβώς εγγυάστε;","Ότι η πρώτη μηνιαία αναφορά θα δείχνει και εξοικονόμηση στις διαφημίσεις σε ευρώ και μετρήσιμη βελτίωση (κριτικές, κλήσεις από Χάρτες ή επισκέψεις). Αν λείπει κάτι από τα δύο, επιστρέφουμε όλο το ποσό του πρώτου μήνα."),
  ("Κι αν δεν τρέχω διαφημίσεις Google;","Όλα τα υπόλοιπα ισχύουν κανονικά. Η εγγύηση βασίζεται τότε στις βελτιώσεις στο προφίλ και στην ιστοσελίδα σας."),
  ("Εγγυάστε πρώτη θέση στο Google;","Κανείς δεν μπορεί να το υποσχεθεί με ειλικρίνεια. Εγγυόμαστε ότι η δουλειά γίνεται κάθε μήνα και σας δείχνουμε τα αποτελέσματα."),
  ("Μπορείτε να κάνετε το ChatGPT να προτείνει την επιχείρησή μου;","Κανείς δεν μπορεί να εγγυηθεί τι θα πει ένας βοηθός AI. Αυτό που κάνουμε είναι να διορθώνουμε όσα χρησιμοποιεί: μια ιστοσελίδα που εξηγεί καθαρά τι κάνετε και πού, ίδια σωστά στοιχεία σε Google, Bing, χάρτες και καταλόγους, πρόσφατες κριτικές, και πρόσβαση των εργαλείων αναζήτησής τους στη σελίδα σας. Κάθε μήνα ελέγχουμε αν εμφανίζεστε και σας λέμε τι άλλαξε."),
  ("Ποιος κάνει τη δουλειά;","Η Kerdos είναι υπηρεσία της SGD Ventures. Δουλεύουμε με δικά μας εργαλεία ανάλυσης που βασίζονται σε AI, υπό ανθρώπινη επίβλεψη, και κάθε αλλαγή καταγράφεται στη μηνιαία σας αναφορά.")],
 fh="Δείτε πρώτα τι θα βρίσκαμε για εσάς.", fp="Η αναφορά είναι δωρεάν. Αν μετά θελήσετε να συνεχίσουμε, κοστίζει €150 τον μήνα, με επιστροφή χρημάτων αν δεν δείτε αποτελέσματα τον πρώτο μήνα.",
 by="υπηρεσία της", notg="Δεν συνδέεται με την Google")

EN = dict(title="Kerdos – Your Google presence, looked after every month. €150/month",
 desc="Less wasted Google Ads money, more calls from Google Maps. €150 a month, cancel any time, with a first-month results guarantee.",
 navl="Main", n1="What's included", n2="Guarantee", n3="Questions", other="Ελληνικά", otherurl="/el/", otherlang="el", start="Free report",
 h1="We look after your Google presence, every month.", permonth="per month",
 sub="Less money wasted on ads, more calls from Google Maps, and a website that keeps working. You focus on your customers.",
 cta="Get your free report", cta2="See what's included",
 promise="First-month guarantee: if your first report doesn't show money saved and better results, you get your money back. Cancel any time.",
 stlabel="Example monthly report", sthead="Your month in numbers", stsmall="Example, in your currency", feev="−150", netv="+600",
 rows=[("Money saved on Google Ads","+750"),("New Google reviews","+9"),("Calls from Google Maps","+23%"),("New pages on Google","+1")],
 fee="Kerdos subscription", net="What you keep after our fee", stnote="Illustrative figures. Your own report shows your real results, every month.",
 h2a="Eight things we do for you every month", pa="We take care of all of it. You see the results in your monthly report.",
 items=[("save","ads","Saves money","Google Ads cost control","We block the searches that cost you money without bringing customers, and tell you how much money you saved."),
  ("earn","map","More customers","Google Maps profile","Weekly posts, correct hours and holidays, photos, and answers to customer questions."),
  ("earn","reply","More customers","Every review answered","A personal, polite reply within 24 hours. We warn you first about negative ones."),
  ("earn","star","More customers","More 5-star reviews","A review link and QR code, plus a ready message to send customers after each job."),
  ("save","site","Protection","Website care","We check speed, mobile problems and broken links, fix them, and alert you if your site goes down."),
  ("earn","page","More customers","One new Google page a month","For a service and area you want customers from, so people find you through free search."),
  ("save","eye","Stay ahead","Competitor watch","What your nearest competitors advertise and how their reviews compare."),
  ("earn","ai","New","Found by AI assistants","More customers now ask ChatGPT, Claude, Gemini or Google's AI answers who to call. We make your business easy for them to find and recommend: clear service and area pages, consistent details on the directories and maps they read, and nothing on your site blocking their search tools.")],
 plans_h="Two ways to work with us", plans_p="Start with the free report. Then pick the plan that fits. No contract, cancel any time.",
 plans=[dict(n="Growth Plan", pr="€150", d="The eight things above, done for you every month, with a monthly results report.", pts=["Google Ads cost control and money-saved report","Google Maps profile, reviews and website care","One new Google page a month","Found by AI assistants","First-month guarantee"], feat=False),
  dict(n="Growth + Content", pr="€250", d="Everything in the Growth Plan, plus your business kept visible and active on social media.", pts=["Everything in the Growth Plan","12 ready-to-post Facebook and Instagram posts a month, with matching images","A monthly content plan: what to post, when, and seasonal offers","One short article a month for your website, written for the questions customers ask","Posted for you if you add us to your page, otherwise sent to you ready to paste"], feat=True)],
 plans_cta="Start with your free report", plans_note="The same first-month guarantee applies to both plans.",
 bonus="Also included: a short end-of-month report showing the money you saved and what improved.",
 gh="No results in your first month? You get your money back.",
 gp="At the end of your first month you get your report. If it doesn't show both money saved and a measurable improvement for your business, we refund your first month in full.",
 gp2="Improvement means more reviews, more calls or direction requests from Google Maps, or more website visits than the month before we started.",
 sh="How it works", sp="First you see what we can do for you. Then you decide.",
 steps=[("Ask for your free report","Fill in 4 details. No payment, no card, no access to your accounts."),
  ("See what we found","Within 48 hours you get a report on your business: one finding in full, and what else we spotted."),
  ("You decide","If it's worth it, start for €150 a month and we take care of the rest. If not, you owe nothing.")],
 ch="Try us for free", cp="Fill in your details and within 48 hours we send you a report about your own business.",
 ticks=["One real finding, in full, that you can fix right away","What else we spotted that is costing you money or customers","No payment, no card, no access to your accounts"],
 cp2="One free report per business.",
 form=dict(name="request", n="Name", w="Website", b="Roughly how much do you spend on Google Ads per month?", bp="e.g. 500 a month", send="Send me my free report"),
 faq=[("Is the report really free?","Yes. No card and no access needed. We send one per business, and you decide whether you want us to continue."),("Do I need to share passwords?","No. You add us as a user on Google Ads and as a manager on your Google Business Profile, by invitation. You can remove us any time."),
  ("When do I pay?","Only if you decide to go ahead, after you've seen your free report. The Growth Plan is €150 a month, or €250 with the Content package. No contract, cancel with one click."),
  ("What exactly is guaranteed?","That your first monthly report shows both money saved on ads and a measurable improvement (reviews, Maps calls or website visits). If either is missing, we refund your first month in full."),
  ("What if I don't run Google Ads?","Everything else still applies. The guarantee is then based on improvements to your profile and website."),
  ("Do you guarantee first place on Google?","No one can honestly promise that. We guarantee the work gets done every month, and we show you the results."),
  ("Can you make ChatGPT recommend my business?","No one can guarantee what an AI assistant says. What we can do is fix what these assistants rely on: your website explaining clearly what you do and where, the same correct details across Google, Bing, maps and directories, recent reviews, and letting their search tools read your site. Each month we check whether you show up and report what changed."),
  ("Who does the work?","Kerdos is a service of SGD Ventures. We use our own AI-assisted analysis tools under human oversight, and every change is listed in your monthly report.")],
 fh="See what we would find for you first.", fp="The report is free. If you then want us to continue, it's €150 a month, with your money back if you see no results in the first month.",
 by="a service of", notg="Not affiliated with Google")

THANKS = '''<!doctype html><html lang="el"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Kerdos – Ευχαριστούμε</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400;600&family=Literata:opsz,wght@7..72,600&display=swap" rel="stylesheet">
<style>body{margin:0;background:#E4EDF2;font-family:Commissioner,system-ui,sans-serif;color:#12283B;font-size:18px;line-height:1.6}main{max-width:620px;margin:12vh auto;background:#FBFCFD;border:1px solid #C6D5DE;border-radius:16px;padding:40px}h1{font-family:Literata,Georgia,serif;color:#0E3A5B;margin:0 0 12px}p{color:#4C6274}a{color:#17507D}</style></head>
<body><main><h1>Ευχαριστούμε, το λάβαμε.</h1><p>Θα σας στείλουμε με email τις οδηγίες για την αναφορά αναζητήσεων, συνήθως μέσα σε λίγες ώρες.</p><p lang="en">Thanks, we've got it. We'll email you the instructions shortly.</p><p><a href="/el/">Επιστροφή στην Kerdos</a></p></main></body></html>'''
REDIR = lambda u: f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={u}"><link rel="canonical" href="{u}"><a href="{u}">Kerdos</a>'

if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT+'/el')
open(OUT+'/index.html','w').write(page(EN,'en','/'))
open(OUT+'/el/index.html','w').write(page(EL,'el','/el/'))
open(OUT+'/thanks.html','w').write(THANKS)
open(OUT+'/plan.html','w').write(REDIR('/'))
open(OUT+'/el/plan.html','w').write(REDIR('/el/'))
open(OUT+'/favicon.svg','w').write(MARK.replace('aria-hidden="true"','xmlns="http://www.w3.org/2000/svg"'))
print('built')
