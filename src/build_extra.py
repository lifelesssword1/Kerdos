# Extra pages: privacy, instant checker, referral, Greek trade guides, sitemap, robots.
# Run after build.py (it imports build.py, which rebuilds the main pages first).
import os, re
import build as B
OUT = B.OUT
BASE = "https://kerdos.sgdventures.com"

XCSS = """
.doc{max-width:760px;margin:0 auto;padding:56px 28px 72px}
.doc h1{font-size:42px;margin-bottom:14px}
.doc h2{font-size:26px;margin:38px 0 10px}
.doc p,.doc li{color:var(--ink);font-size:18px}
.doc p+p{margin-top:12px}
.doc ul{padding-left:22px}.doc li{margin:6px 0}
.lede{font-size:20px!important;color:var(--muted)!important}
.tool{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:28px;margin-top:28px;box-shadow:0 18px 40px rgba(14,58,91,.08)}
.tool form{background:none;border:0;padding:0}
.tool .line{display:flex;gap:12px;flex-wrap:wrap}.tool .line input{flex:1 1 280px}
.res{margin-top:24px;display:none}
.res.on{display:block}
.score{display:flex;justify-content:space-between;align-items:baseline;padding:14px 0;border-bottom:1px dashed var(--line);font-variant-numeric:tabular-nums}
.score b{font-family:Literata,Georgia,serif;font-size:28px}
.good{color:var(--gain)}.ok{color:var(--gold)}.bad{color:var(--loss);font-size:22px!important}
.hint{font-size:15px;color:var(--muted);margin-top:10px}
.consent{display:flex;gap:10px;align-items:flex-start;font-weight:400;font-size:15px}
.consent input{width:auto;margin-top:5px}
.next{margin-top:26px;padding:22px;background:var(--mist);border-radius:12px}
.guides{list-style:none;padding:0!important}.guides li{border-top:1px solid var(--line);padding:16px 0!important;margin:0!important}
.guides a{font-family:Literata,Georgia,serif;font-size:21px;font-weight:600;text-decoration:none}
.note2{font-size:15px!important;color:var(--muted)!important;margin-top:30px!important}
"""

def shell(lang, title, desc, body, root, path, alt=None):
    alts = ""
    if alt:
        alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{u}">' for l,u in alt)
    home = "/el/" if lang=="el" else "/"
    foot = FOOT[lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">{alts}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400;500;600;700&family=Literata:opsz,wght@7..72,500;7..72,600&display=swap" rel="stylesheet">
<style>{B.CSS}{XCSS}</style>
</head>
<body>
<header><div class="wrap">
<a class="brand" href="{home}">{B.MARK}Kerdos</a>
<nav><a class="btn small" href="{home}#free">{NAVCTA[lang]}</a></nav>
</div></header>
<main>{body}</main>
{foot}
<elevenlabs-convai agent-id="agent_4201m7w49pgfetsbjp9xje4xqs11"></elevenlabs-convai><script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
</body>
</html>'''

NAVCTA = {"en":"Free report","el":"Δωρεάν αναφορά"}
FOOT = {
 "en": '<footer><div class="wrap"><span>© 2026 Kerdos, a service of SGD Ventures · <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a></span><span><a href="/check.html">Free Google check</a> · <a href="/refer.html">Recommend a business</a> · <a href="/privacy.html">Privacy</a></span></div></footer>',
 "el": '<footer><div class="wrap"><span>© 2026 Kerdos, υπηρεσία της SGD Ventures · <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a></span><span><a href="/el/check.html">Δωρεάν έλεγχος</a> · <a href="/el/odigoi/">Οδηγοί</a> · <a href="/el/refer.html">Προτείνετε μια επιχείρηση</a> · <a href="/el/privacy.html">Απόρρητο</a></span></div></footer>',
}

# ---------------- PRIVACY ----------------
PRIV_EN = """<div class="doc">
<h1>Privacy notice</h1>
<p class="lede">Who we are, what business data we use, why, and how to make us stop. Last updated 20 November 2026.</p>
<h2>Who we are</h2>
<p>Kerdos is a service of SGD Ventures. Contact for anything about your data: <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a>.</p>
<h2>What we collect and where from</h2>
<ul>
<li><b>Business contact details from public sources</b>: business name, business email address, website, town, and (for UK companies) the company number. We take these from the business's own website, public business directories and the Companies House register.</li>
<li><b>Public facts about your business's Google presence</b>: for example your Google Maps rating and reviews, your website's speed score, and whether your business runs Google ads (from Google's public Ads Transparency Center).</li>
<li><b>What you send us</b>: details you type into a form on this site, talk about with our AI assistant, or email to us.</li>
</ul>
<h2>Why, and on what legal basis</h2>
<ul>
<li>To email businesses a short, relevant note about their Google presence and offer a free report. Legal basis: our legitimate interest in offering a business service to businesses (GDPR / UK GDPR Article 6(1)(f)). We only email business addresses, only in countries whose law allows it, and every email lets you say "no".</li>
<li>To prepare and send a free report or our service when you ask for it. Legal basis: your request, and later our contract with you.</li>
</ul>
<h2>Saying no</h2>
<p>Reply "no" to any email, or write to <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a>. We stop at once and add your address to a do-not-contact list, which we keep only so that we never contact you again.</p>
<h2>How long we keep it</h2>
<p>Prospect details: up to 12 months after our last contact, then deleted. Do-not-contact list: kept for as long as we operate. Customer records: as long as the law requires for invoices and tax.</p>
<h2>Who helps us (processors)</h2>
<p>IONOS (email), Netlify (website and forms), Google (spreadsheets), Stripe (payments), ElevenLabs (the AI assistant on this site). We don't sell or rent your data to anyone.</p>
<h2>The AI assistant</h2>
<p>The assistant on this site is an AI, not a person. What you say to it is stored so we can send you what you asked for.</p>
<h2>Your rights</h2>
<p>You can ask us to show, correct or delete your data, or to stop using it. You can also complain to your data protection authority: the ICO (UK), the Data Protection Commission (Ireland), or the Hellenic Data Protection Authority (Greece).</p>
</div>"""

PRIV_EL = """<div class="doc">
<h1>Πολιτική απορρήτου</h1>
<p class="lede">Ποιοι είμαστε, ποια στοιχεία χρησιμοποιούμε, γιατί, και πώς μας λέτε να σταματήσουμε. Τελευταία ενημέρωση 20 Νοεμβρίου 2026.</p>
<h2>Ποιοι είμαστε</h2>
<p>Το Kerdos είναι υπηρεσία της SGD Ventures. Επικοινωνία για τα στοιχεία σας: <a href="mailto:sam@sgdventures.com">sam@sgdventures.com</a>.</p>
<h2>Τι συλλέγουμε</h2>
<ul>
<li><b>Ό,τι μας στέλνετε εσείς</b>: στοιχεία που γράφετε σε φόρμα της σελίδας, λέτε στον ψηφιακό βοηθό μας ή μας στέλνετε με email.</li>
<li><b>Δημόσια στοιχεία για την παρουσία της επιχείρησής σας στο Google</b>, μόνο όταν μας ζητήσετε αναφορά: π.χ. βαθμολογία και κριτικές στους Χάρτες Google, ταχύτητα ιστοσελίδας, διαφημίσεις στο Google (από το δημόσιο Ads Transparency Center).</li>
</ul>
<p>Στην Ελλάδα δεν στέλνουμε διαφημιστικά email σε επιχειρήσεις που δεν μας το ζήτησαν.</p>
<h2>Γιατί</h2>
<p>Για να ετοιμάσουμε και να σας στείλουμε τη δωρεάν αναφορά ή την υπηρεσία που ζητήσατε. Νομική βάση: το αίτημά σας και, αργότερα, η σύμβασή μας.</p>
<h2>Πόσο τα κρατάμε</h2>
<p>Αιτήματα χωρίς συνεργασία: έως 12 μήνες. Πελάτες: όσο απαιτεί ο νόμος για τιμολόγια και φορολογία. Αν μας πείτε «όχι», κρατάμε μόνο το email σας σε λίστα «μην επικοινωνήσετε».</p>
<h2>Ποιοι μας βοηθούν</h2>
<p>IONOS (email), Netlify (ιστοσελίδα και φόρμες), Google (υπολογιστικά φύλλα), Stripe (πληρωμές), ElevenLabs (ο ψηφιακός βοηθός). Δεν πουλάμε τα στοιχεία σας σε κανέναν.</p>
<h2>Ο ψηφιακός βοηθός</h2>
<p>Ο βοηθός στη σελίδα είναι τεχνητή νοημοσύνη, όχι άνθρωπος. Ό,τι του πείτε αποθηκεύεται για να σας στείλουμε αυτό που ζητήσατε.</p>
<h2>Τα δικαιώματά σας</h2>
<p>Μπορείτε να ζητήσετε να δείτε, να διορθώσετε ή να διαγράψουμε τα στοιχεία σας. Μπορείτε επίσης να απευθυνθείτε στην Αρχή Προστασίας Δεδομένων Προσωπικού Χαρακτήρα (dpa.gr).</p>
</div>"""

# ---------------- CHECKER ----------------
CHECK_T = {
 "en": dict(title="Free Google check for your business website | Kerdos",
   desc="Type your website and see in 30 seconds how fast it loads on a phone and how well Google can read it. Free, no sign-up.",
   h1="How does your website look to Google?",
   lede="Type your website. In about 30 seconds you'll see how fast it loads on a phone and how well Google can read it. Free, no sign-up.",
   ph="yourbusiness.com", go="Check my website", wait="Checking… this takes about 30 seconds.",
   err="Google's checker is busy right now. Try again in a minute, or ask for the full free report below.",
   speed="Speed on a phone (out of 100)", seo="How well Google can read it (out of 100)", lcp="Time until the main content shows",
   s_good="Good", s_ok="Could be better", s_bad="Losing visitors",
   hint="Measured just now by Google PageSpeed Insights, on a mobile phone.",
   nh="Want the full picture?", np="This check looks at your website only. The free report also checks your Google Maps profile, your reviews and, if you run them, your Google ads, and explains one finding in full with the fix.",
   n="Your name", w="Website", agree="Yes, email me the free report about my business. One report per business, no payment, no account access.",
   send="Send me the free report", formname="checker", priv="/privacy.html", privt="How we use your details",
   secs="s"),
 "el": dict(title="Δωρεάν έλεγχος της ιστοσελίδας σας στο Google | Kerdos",
   desc="Γράψτε την ιστοσελίδα σας και δείτε σε 30 δευτερόλεπτα πόσο γρήγορα ανοίγει στο κινητό και πόσο καλά τη διαβάζει το Google. Δωρεάν, χωρίς εγγραφή.",
   h1="Πώς βλέπει το Google την ιστοσελίδα σας;",
   lede="Γράψτε την ιστοσελίδα σας. Σε περίπου 30 δευτερόλεπτα θα δείτε πόσο γρήγορα ανοίγει στο κινητό και πόσο καλά τη διαβάζει το Google. Δωρεάν, χωρίς εγγραφή.",
   ph="epixeirisi.gr", go="Έλεγχος", wait="Γίνεται έλεγχος… διαρκεί περίπου 30 δευτερόλεπτα.",
   err="Ο έλεγχος του Google είναι απασχολημένος. Δοκιμάστε ξανά σε ένα λεπτό ή ζητήστε την πλήρη δωρεάν αναφορά παρακάτω.",
   speed="Ταχύτητα στο κινητό (στα 100)", seo="Πόσο καλά τη διαβάζει το Google (στα 100)", lcp="Χρόνος μέχρι να φανεί το κύριο περιεχόμενο",
   s_good="Καλό", s_ok="Θέλει βελτίωση", s_bad="Χάνετε επισκέπτες",
   hint="Μετρήθηκε μόλις τώρα από το Google PageSpeed Insights, σε κινητό.",
   nh="Θέλετε την πλήρη εικόνα;", np="Αυτός ο έλεγχος κοιτάζει μόνο την ιστοσελίδα. Η δωρεάν αναφορά ελέγχει επίσης το προφίλ σας στους Χάρτες Google, τις κριτικές σας και, αν τρέχετε, τις διαφημίσεις σας, και εξηγεί ένα εύρημα αναλυτικά με τη λύση του.",
   n="Το όνομά σας", w="Ιστοσελίδα", agree="Ναι, στείλτε μου με email τη δωρεάν αναφορά για την επιχείρησή μου. Μία αναφορά ανά επιχείρηση, χωρίς πληρωμή, χωρίς πρόσβαση σε λογαριασμούς.",
   send="Στείλτε μου τη δωρεάν αναφορά", formname="checker-el", priv="/el/privacy.html", privt="Πώς χρησιμοποιούμε τα στοιχεία σας",
   secs=" δευτ."),
}

def checker(lang):
    T = CHECK_T[lang]
    body = f'''<div class="doc">
<h1>{T["h1"]}</h1>
<p class="lede">{T["lede"]}</p>
<div class="tool">
<form id="chk" onsubmit="return run(event)"><div class="line"><label class="sr" for="u" style="position:absolute;left:-9999px">{T["w"]}</label>
<input id="u" required placeholder="{T["ph"]}" autocomplete="url"><button class="btn" type="submit">{T["go"]}</button></div></form>
<p id="st" class="hint" role="status" aria-live="polite"></p>
<div id="res" class="res">
<div class="score"><span>{T["speed"]}</span><b id="r1"></b></div>
<div class="score"><span>{T["seo"]}</span><b id="r2"></b></div>
<div class="score"><span>{T["lcp"]}</span><b id="r3"></b></div>
<p class="hint">{T["hint"]}</p>
</div>
</div>
<div class="next">
<h2 style="margin-top:0">{T["nh"]}</h2><p>{T["np"]}</p>
<form name="{T["formname"]}" method="POST" data-netlify="true" netlify-honeypot="company_url" action="/thanks.html" style="margin-top:18px;background:#fff">
<input type="hidden" name="form-name" value="{T["formname"]}">
<input type="hidden" name="speed" id="fs"><input type="hidden" name="seo" id="fo">
<p style="display:none"><label>Leave empty <input name="company_url"></label></p>
<div><label for="cn">{T["n"]}</label><input id="cn" name="name" required autocomplete="name"></div>
<div><label for="ce">Email</label><input id="ce" type="email" name="email" required autocomplete="email"></div>
<div><label for="cw">{T["w"]}</label><input id="cw" name="website" required autocomplete="url"></div>
<label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>{T["agree"]}</span></label>
<button class="btn" type="submit">{T["send"]}</button>
<p class="hint"><a href="{T["priv"]}">{T["privt"]}</a></p>
</form>
</div>
</div>
<script>
const L={{good:"{T["s_good"]}",ok:"{T["s_ok"]}",bad:"{T["s_bad"]}",wait:"{T["wait"]}",err:"{T["err"]}",secs:"{T["secs"]}"}};
function cls(v){{return v>=90?"good":v>=50?"ok":"bad"}}
async function run(e){{e.preventDefault();
 let u=document.getElementById("u").value.trim(); if(!/^https?:/i.test(u)) u="https://"+u;
 const st=document.getElementById("st"), res=document.getElementById("res");
 st.textContent=L.wait; res.classList.remove("on");
 document.getElementById("cw").value=u;
 try{{
  const r=await fetch("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?strategy=mobile&category=performance&category=seo&url="+encodeURIComponent(u));
  if(!r.ok) throw 0; const j=await r.json(); const c=j.lighthouseResult.categories;
  const p=Math.round(c.performance.score*100), s=Math.round(c.seo.score*100);
  const lcp=j.lighthouseResult.audits["largest-contentful-paint"].numericValue/1000;
  const set=(id,v,k,t)=>{{const el=document.getElementById(id);el.className=k;el.textContent=t}};
  set("r1",p,cls(p),p+" · "+L[cls(p)]); set("r2",s,cls(s),s+" · "+L[cls(s)]);
  const lk=lcp<=2.5?"good":lcp<=4?"ok":"bad"; set("r3",lcp,lk,lcp.toFixed(1)+L.secs+" · "+L[lk]);
  document.getElementById("fs").value=p; document.getElementById("fo").value=s;
  st.textContent=""; res.classList.add("on");
 }}catch(_){{st.textContent=L.err}}
 return false}}
</script>'''
    path = "/check.html" if lang=="en" else "/el/check.html"
    return shell(lang, T["title"], T["desc"], body, "/", path, alt=[("en","/check.html"),("el","/el/check.html")])

# ---------------- REFERRAL ----------------
REF_T = {
 "en": dict(title="Recommend a business to Kerdos", desc="Know a business that wastes money on Google ads or gets few calls from Google? Send them our free report link.",
  h1="Know a business that should hear about this?",
  lede="Maybe a friend's shop runs Google ads that don't bring calls, or a supplier with three reviews on Google Maps. Here's how to help them.",
  h2a="The simple way: share the link", p2a="Send them this link yourself, by message or email. They can ask for their free report in one minute:",
  link="https://kerdos.sgdventures.com/#free",
  h2b="Or pass on their details, if they asked you to", p2b="Only fill this in if the business owner told you they want us to contact them. We'll mention your name.",
  reward="If you're a Kerdos customer, you get one month free for every business you recommend that signs up for the Growth Plan.",
  fn="Your name", fe="Your email", fb="Their business name", fw="Their website", fc="Their email",
  agree="The business owner asked me to pass on their details so Kerdos can contact them.",
  send="Send", formname="referral", priv="/privacy.html"),
 "el": dict(title="Προτείνετε μια επιχείρηση στο Kerdos", desc="Ξέρετε μια επιχείρηση που χάνει χρήματα στις διαφημίσεις Google ή παίρνει λίγα τηλέφωνα από το Google; Στείλτε της τη δωρεάν αναφορά μας.",
  h1="Ξέρετε μια επιχείρηση που θα την ενδιέφερε;",
  lede="Ίσως ένας φίλος τρέχει διαφημίσεις στο Google που δεν φέρνουν τηλέφωνα, ή ένας συνεργάτης έχει τρεις κριτικές στους Χάρτες Google. Δείτε πώς να τους βοηθήσετε.",
  h2a="Ο απλός τρόπος: στείλτε τον σύνδεσμο", p2a="Στείλτε τους εσείς αυτόν τον σύνδεσμο, με μήνυμα ή email. Ζητούν τη δωρεάν αναφορά τους σε ένα λεπτό:",
  link="https://kerdos.sgdventures.com/el/#free",
  h2b="Ή δώστε μας τα στοιχεία τους, αν σας το ζήτησαν", p2b="Συμπληρώστε τη φόρμα μόνο αν ο ιδιοκτήτης σάς είπε ότι θέλει να επικοινωνήσουμε μαζί του. Θα αναφέρουμε το όνομά σας.",
  reward="Αν είστε πελάτης του Kerdos, παίρνετε έναν μήνα δωρεάν για κάθε επιχείρηση που προτείνετε και εγγράφεται στο πακέτο.",
  fn="Το όνομά σας", fe="Το email σας", fb="Όνομα επιχείρησης", fw="Ιστοσελίδα της", fc="Email της επιχείρησης",
  agree="Ο ιδιοκτήτης μού ζήτησε να δώσω τα στοιχεία του για να επικοινωνήσει μαζί του το Kerdos.",
  send="Αποστολή", formname="referral-el", priv="/el/privacy.html"),
}
def referral(lang):
    T = REF_T[lang]
    body = f'''<div class="doc">
<h1>{T["h1"]}</h1><p class="lede">{T["lede"]}</p>
<h2>{T["h2a"]}</h2><p>{T["p2a"]}</p>
<p style="margin-top:14px"><input readonly value="{T["link"]}" onclick="this.select()" aria-label="link"></p>
<p class="next">{T["reward"]}</p>
<h2>{T["h2b"]}</h2><p>{T["p2b"]}</p>
<form name="{T["formname"]}" method="POST" data-netlify="true" netlify-honeypot="company_url" action="/thanks.html" style="margin-top:18px">
<input type="hidden" name="form-name" value="{T["formname"]}">
<p style="display:none"><label>Leave empty <input name="company_url"></label></p>
<div><label for="a1">{T["fn"]}</label><input id="a1" name="referrer_name" required></div>
<div><label for="a2">{T["fe"]}</label><input id="a2" type="email" name="referrer_email" required></div>
<div><label for="a3">{T["fb"]}</label><input id="a3" name="business" required></div>
<div><label for="a4">{T["fw"]}</label><input id="a4" name="website"></div>
<div><label for="a5">{T["fc"]}</label><input id="a5" type="email" name="business_email" required></div>
<label class="consent"><input type="checkbox" name="they_asked" value="yes" required> <span>{T["agree"]}</span></label>
<button class="btn" type="submit">{T["send"]}</button>
</form>
</div>'''
    path = "/refer.html" if lang=="en" else "/el/refer.html"
    return shell(lang, T["title"], T["desc"], body, "/", path, alt=[("en","/refer.html"),("el","/el/refer.html")])

# ---------------- GREEK TRADE GUIDES ----------------
GUIDES = [
 dict(slug="kleidarades", trade="κλειδαράδες", gen="κλειδαρά", who="έναν κλειδαρά",
  searches="«κλειδαράς τώρα», «ξεκλείδωμα πόρτας», «κλειδαράς 24 ώρες» και το όνομα της περιοχής",
  neg="«πώς να ανοίξω κλειδαριά μόνος μου», «κλειδαριά τιμή», «μαθήματα κλειδαρά», «εργασία κλειδαράς»",
  maps="Οι περισσότεροι πελάτες ψάχνουν κλειδαρά όταν είναι κλειδωμένοι έξω, από το κινητό, και καλούν τον πρώτο που φαίνεται αξιόπιστος στον χάρτη. Βάλτε ωράριο 24ωρο μόνο αν όντως απαντάτε, γιατί μια αναπάντητη κλήση στις 2 τα ξημερώματα γίνεται κακή κριτική.",
  review="Ζητήστε κριτική αμέσως μετά το ξεκλείδωμα, όσο ο πελάτης είναι ανακουφισμένος. Ένα σύντομο μήνυμα με τον σύνδεσμο κριτικής αρκεί.",
  page="Μία σελίδα για κάθε υπηρεσία (ξεκλείδωμα, αλλαγή κυλίνδρου, θωρακισμένες πόρτες) και για κάθε περιοχή που εξυπηρετείτε, με τηλέφωνο που καλείται με ένα πάτημα."),
 dict(slug="ydraylikoi", trade="υδραυλικοί", gen="υδραυλικό", who="έναν υδραυλικό",
  searches="«υδραυλικός», «διαρροή νερού», «βουλωμένη αποχέτευση», «επισκευή θερμοσίφωνα» με την περιοχή",
  neg="«πώς να ξεβουλώσω μόνος μου», «υδραυλικά υλικά», «σωλήνες τιμή», «υδραυλικός μισθός»",
  maps="Οι επείγουσες βλάβες (διαρροή, πλημμύρα) κρίνονται στον χάρτη: ο πελάτης βλέπει απόσταση, αστέρια και αν είστε ανοιχτοί. Φωτογραφίες από πραγματικές δουλειές βοηθούν περισσότερο από φωτογραφίες αρχείου.",
  review="Μετά από κάθε δουλειά, στείλτε τον σύνδεσμο κριτικής μαζί με την απόδειξη. Απαντήστε σε κάθε κριτική, ακόμα και στις καλές, με μία φράση.",
  page="Χωριστή σελίδα για επείγουσες βλάβες και για προγραμματισμένες εργασίες (μπάνια, θερμοσίφωνες), γιατί είναι διαφορετικός πελάτης με διαφορετική βιασύνη."),
 dict(slug="metakomiseis", trade="εταιρείες μετακομίσεων", gen="εταιρεία μετακομίσεων", who="μια εταιρεία μετακομίσεων",
  searches="«μετακομίσεις», «μεταφορική», «μετακόμιση Αθήνα Θεσσαλονίκη», «ανυψωτικό μετακομίσεων»",
  neg="«κούτες μετακόμισης δωρεάν», «μετακόμιση μόνος μου», «ενοικίαση φορτηγού», «εργασία μεταφορική»",
  maps="Η μετακόμιση είναι ακριβή απόφαση, οπότε ο πελάτης διαβάζει κριτικές πριν καλέσει. Ένα προφίλ με πολλές πρόσφατες κριτικές και απαντήσεις χτίζει εμπιστοσύνη που η διαφήμιση μόνη της δεν μπορεί.",
  review="Ζητήστε κριτική την ημέρα που τελειώνει η μετακόμιση, όταν όλα έφτασαν ακέραια. Αναφέρετε στην απάντησή σας τη διαδρομή (π.χ. «Γλυφάδα – Πάτρα»): βοηθά άλλους που ψάχνουν το ίδιο.",
  page="Σελίδες για τις συχνές διαδρομές σας και για υπηρεσίες όπως συσκευασία και αποθήκευση, με φόρμα για δωρεάν εκτίμηση."),
 dict(slug="apentomoseis", trade="εταιρείες απεντομώσεων", gen="εταιρεία απεντομώσεων", who="μια εταιρεία απεντομώσεων",
  searches="«απεντόμωση», «μυρμήγκια σπίτι», «κατσαρίδες», «μυοκτονία», «απολύμανση» με την περιοχή",
  neg="«σπρέι για κατσαρίδες», «φυσικά εντομοαπωθητικά», «απεντόμωση μόνος μου», «σκόνη για μυρμήγκια»",
  maps="Πολλές αναζητήσεις γίνονται τη στιγμή που ο πελάτης βλέπει το πρόβλημα. Ένα προφίλ με σωστές κατηγορίες (απεντόμωση, μυοκτονία, απολύμανση) εμφανίζεται σε περισσότερες αναζητήσεις.",
  review="Οι πελάτες ντρέπονται συχνά να γράψουν για κατσαρίδες. Ζητήστε κριτική για την εξυπηρέτηση και την ταχύτητα, όχι για το πρόβλημα.",
  page="Μία σελίδα ανά πρόβλημα (κατσαρίδες, ποντίκια, κουνούπια, τερμίτες) και μία για επαγγελματικούς χώρους, που χρειάζονται βεβαίωση."),
 dict(slug="odontiatroi", trade="οδοντίατροι", gen="οδοντίατρο", who="ένα οδοντιατρείο",
  searches="«οδοντίατρος», «εμφυτεύματα», «λεύκανση δοντιών», «επείγον οδοντίατρος» με την περιοχή",
  neg="«οδοντιατρική σχολή», «οδοντίατρος μισθός», «λεύκανση στο σπίτι», «πόνος δοντιού τι να κάνω»",
  maps="Οι ασθενείς επιλέγουν οδοντίατρο κοντά στο σπίτι ή τη δουλειά, και διαβάζουν κριτικές για τον πόνο και την ευγένεια. Καταχωρίστε κάθε θεραπεία στο προφίλ σας ως υπηρεσία.",
  review="Ζητήστε κριτική στο τέλος μιας επιτυχημένης θεραπείας. Στις απαντήσεις σας μην αναφέρετε ποτέ στοιχεία υγείας του ασθενούς.",
  page="Χωριστές σελίδες για εμφυτεύματα, ορθοδοντική, λεύκανση και επείγοντα, γιατί κάθε θεραπεία έχει δικούς της ασθενείς και ερωτήσεις."),
 dict(slug="fysikotherapeftes", trade="φυσικοθεραπευτές", gen="φυσικοθεραπευτή", who="ένα φυσικοθεραπευτήριο",
  searches="«φυσικοθεραπευτής», «φυσικοθεραπεία κατ' οίκον», «πόνος στη μέση», «αποκατάσταση χιαστού»",
  neg="«ασκήσεις για τη μέση στο σπίτι», «σχολή φυσικοθεραπείας», «φυσικοθεραπευτής μισθός», «μαξιλάρι μέσης»",
  maps="Πολλοί ασθενείς ψάχνουν μετά από σύσταση γιατρού και θέλουν κάποιον κοντά τους. Αν κάνετε επισκέψεις κατ' οίκον, δηλώστε τις περιοχές εξυπηρέτησης στο προφίλ.",
  review="Ζητήστε κριτική όταν ο ασθενής ολοκληρώνει τις συνεδρίες και νιώθει καλύτερα. Μην αναφέρετε τη διάγνωση στην απάντησή σας.",
  page="Σελίδες για τα συχνά προβλήματα (μέση, αυχένας, αθλητικοί τραυματισμοί) και για την κατ' οίκον φυσικοθεραπεία, με το κόστος συνεδρίας αν το δημοσιεύετε."),
]

def guide(g):
    t = g["trade"]
    title = f"Google για {t}: πώς να πάρετε περισσότερα τηλέφωνα | Kerdos"
    desc = f"Πρακτικός οδηγός για {t}: διαφημίσεις Google χωρίς χαμένα χρήματα, προφίλ στους Χάρτες Google, κριτικές και ιστοσελίδα που φέρνει τηλέφωνα."
    body = f'''<div class="doc">
<h1>Google για {t}: περισσότερα τηλέφωνα, λιγότερα χαμένα χρήματα</h1>
<p class="lede">Τέσσερα πράγματα που κάνουν τη διαφορά για {g["who"]} στην Ελλάδα, και τι μπορείτε να ελέγξετε σήμερα.</p>
<h2>1. Διαφημίσεις: πληρώνετε για λάθος αναζητήσεις;</h2>
<p>Οι πελάτες σας γράφουν πράγματα όπως {g["searches"]}. Όμως οι διαφημίσεις εμφανίζονται συχνά και σε αναζητήσεις ανθρώπων που δεν θα καλέσουν ποτέ, όπως {g["neg"]}. Κάθε κλικ από αυτούς πληρώνεται.</p>
<p><b>Τι να κάνετε σήμερα:</b> στο Google Ads ανοίξτε Insights &amp; reports &gt; Search terms (Όροι αναζήτησης), δείτε τις τελευταίες 30 ημέρες και προσθέστε ως αρνητικές λέξεις όσες δεν φέρνουν πελάτες.</p>
<h2>2. Το προφίλ σας στους Χάρτες Google</h2>
<p>{g["maps"]}</p>
<p><b>Τι να κάνετε σήμερα:</b> ελέγξτε ότι το τηλέφωνο, το ωράριο και οι κατηγορίες στο προφίλ σας είναι σωστά, και προσθέστε τρεις πρόσφατες φωτογραφίες από δουλειές σας.</p>
<h2>3. Κριτικές</h2>
<p>{g["review"]}</p>
<p><b>Τι να κάνετε σήμερα:</b> απαντήστε σε κάθε κριτική που δεν έχει απάντηση. Οι υποψήφιοι πελάτες διαβάζουν και τις απαντήσεις.</p>
<h2>4. Η ιστοσελίδα</h2>
<p>Αν η σελίδα αργεί να ανοίξει στο κινητό, ο επισκέπτης γυρίζει πίσω και καλεί τον επόμενο. {g["page"]}</p>
<p><b>Τι να κάνετε σήμερα:</b> δείτε πόσο γρήγορα ανοίγει η σελίδα σας με τον <a href="/el/check.html">δωρεάν έλεγχό μας</a> (30 δευτερόλεπτα).</p>
<div class="next"><h2 style="margin-top:0">Θέλετε να το ελέγξουμε εμείς;</h2>
<p>Σας στέλνουμε δωρεάν μια σύντομη αναφορά για την επιχείρησή σας: ένα πραγματικό εύρημα αναλυτικά με τη λύση του, και τι άλλο βρήκαμε. Χωρίς πληρωμή, χωρίς πρόσβαση στους λογαριασμούς σας.</p>
<p style="margin-top:16px"><a class="btn" href="/el/#free">Ζητήστε τη δωρεάν αναφορά</a></p></div>
<p class="note2">Τα παραδείγματα αναζητήσεων είναι ενδεικτικά. Οι πραγματικοί όροι διαφέρουν ανά περιοχή και επιχείρηση: γι' αυτό ελέγχουμε τα δικά σας δεδομένα.</p>
</div>'''
    return shell("el", title, desc, body, "/el/", f"/el/odigoi/{g['slug']}.html")

def guide_index():
    li = "".join(f'<li><a href="/el/odigoi/{g["slug"]}.html">Google για {g["trade"]}</a></li>' for g in GUIDES)
    body = f'''<div class="doc"><h1>Οδηγοί Google για τοπικές επιχειρήσεις</h1>
<p class="lede">Πρακτικές συμβουλές ανά επάγγελμα: διαφημίσεις χωρίς χαμένα χρήματα, Χάρτες Google, κριτικές και ιστοσελίδα.</p>
<ul class="guides">{li}</ul></div>'''
    return shell("el", "Οδηγοί Google για τοπικές επιχειρήσεις | Kerdos", "Πρακτικοί οδηγοί για κλειδαράδες, υδραυλικούς, μετακομίσεις, απεντομώσεις, οδοντιάτρους και φυσικοθεραπευτές.", body, "/el/", "/el/odigoi/")

def w(rel, html):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p,"w").write(html)

w("privacy.html", shell("en","Privacy notice | Kerdos","How Kerdos uses business contact details and how to opt out.",PRIV_EN,"/","/privacy.html",alt=[("en","/privacy.html"),("el","/el/privacy.html")]))
w("el/privacy.html", shell("el","Πολιτική απορρήτου | Kerdos","Πώς χρησιμοποιεί το Kerdos τα στοιχεία σας.",PRIV_EL,"/el/","/el/privacy.html",alt=[("en","/privacy.html"),("el","/el/privacy.html")]))
w("check.html", checker("en")); w("el/check.html", checker("el"))
w("refer.html", referral("en")); w("el/refer.html", referral("el"))
for g in GUIDES: w(f"el/odigoi/{g['slug']}.html", guide(g))
w("el/odigoi/index.html", guide_index())

# footer links + nav link to checker on the main pages
for rel, lang in (("index.html","en"),("el/index.html","el")):
    p = os.path.join(OUT, rel); s = open(p).read()
    s = re.sub(r"<footer>.*?</footer>", FOOT[lang], s, flags=re.S)
    chk = ('<a class="hide" href="/check.html">Free check</a>' if lang=="en" else '<a class="hide" href="/el/check.html">Δωρεάν έλεγχος</a>')
    s = s.replace('<a class="hide" href="#faq">', chk + '<a class="hide" href="#faq">', 1)
    s = s.replace("</head>", f'<link rel="canonical" href="{BASE}/{"el/" if lang=="el" else ""}"><link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="el" href="{BASE}/el/"></head>', 1)
    open(p,"w").write(s)

urls = ["/","/el/","/check.html","/el/check.html","/refer.html","/el/refer.html","/privacy.html","/el/privacy.html","/el/odigoi/"] + [f"/el/odigoi/{g['slug']}.html" for g in GUIDES]
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{BASE}{u}</loc><lastmod>2026-11-20</lastmod></url>\n" for u in urls) + "</urlset>\n")
w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("extra built:", len(urls), "urls")
