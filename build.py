# -*- coding: utf-8 -*-
"""Build the portfolio:  python build.py
Reads content.py + the original photos, writes optimized images and all HTML pages."""
import os, re, sys, html, json
from PIL import Image
import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("PHOTOS", "/home/claude/work/Photos")  # folder with the original 'unnamed (N).png/jpg' files
SITE_URL = os.environ.get("SITE_URL", "")  # e.g. https://USERNAME.github.io/REPO  (optional, used for og:url + sitemap)
e = lambda s: html.escape(str(s), quote=True)
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:46]

# ------------------------------------------------------------------ images
def src_path(i):
    n = int(i[1:]); ext = "png" if i[0] == "p" else "jpg"
    return os.path.join(SRC, "unnamed.%s" % ext if n == 0 else "unnamed (%d).%s" % (n, ext))

REG = {}      # id -> info
MANIFEST = []
def img(i, owner, folder, hq=False):
    if i in REG: return REG[i]
    name = "%s-%s" % (slug(owner), i)
    d = os.path.join(ROOT, "assets", "img", folder); os.makedirs(d, exist_ok=True)
    full, thumb = os.path.join(d, name + ".webp"), os.path.join(d, name + "-sm.webp")
    im = Image.open(src_path(i)); im.load()
    if im.mode not in ("RGB", "RGBA"): im = im.convert("RGBA" if "transparency" in im.info else "RGB")
    if i in C.ROTATE: im = im.rotate(C.ROTATE[i], expand=True)
    f = im.copy(); f.thumbnail((1600, 2000), Image.LANCZOS)
    t = im.copy(); t.thumbnail((640, 800), Image.LANCZOS)
    if not os.path.exists(full): f.save(full, "WEBP", quality=88 if hq else 82, method=5)
    if not os.path.exists(thumb): t.save(thumb, "WEBP", quality=78, method=5)
    info = dict(id=i, full="assets/img/%s/%s.webp" % (folder, name), thumb="assets/img/%s/%s-sm.webp" % (folder, name), w=t.width, h=t.height, owner=owner)
    REG[i] = info
    MANIFEST.append((os.path.basename(src_path(i)), info["full"], owner))
    return info

def shot(i, owner, folder, group, cap=None, alt=None, hq=False):
    m = img(i, owner, folder, hq)
    a = alt or "%s (photo %s)" % (owner, i)
    c = cap or ""
    return ('<figure class="shot"><a href="%s" data-lb="%s" data-cap="%s"><img src="%s" width="%d" height="%d" loading="lazy" decoding="async" alt="%s"></a>%s</figure>'
            % (m["full"], e(group), e(c or owner), m["thumb"], m["w"], m["h"], e(a), ("<figcaption>%s</figcaption>" % e(c)) if c else ""))

def gal(ids, owner, folder, group, caps=None, sm=False, hq=False):
    if not ids: return ""
    caps = caps or {}
    return '<div class="gal%s" style="columns:%d 220px">%s</div>' % (" sm" if sm else "", min(len(ids), 3), "".join(shot(i, owner, folder, group, caps.get(i), hq=hq) for i in ids))

CERT_TITLE = {i: t for t, _, ids in C.CERTS for i in ids}
# ------------------------------------------------------------------ helpers
def ext(u): return "target=\"_blank\" rel=\"noopener\"" if u.startswith("http") else ""
def paras(ps): return "".join("<p>%s</p>" % e(p) for p in ps)
def ul(items, cls=""): return "<ul%s>%s</ul>" % (' class="%s"' % cls if cls else "", "".join("<li>%s</li>" % e(x) for x in items)) if items else ""
def tags(ts): return '<div class="tags">%s</div>' % "".join('<span class="tag">%s</span>' % e(t) for t in ts) if ts else ""
def links(ls): return '<div class="links-row">%s</div>' % "".join('<a href="%s" %s>%s ↗</a>' % (e(u), ext(u), e(l)) for l, u in ls) if ls else ""
def filecard(name, local, group="presentations"):
    t = name.rsplit(".", 1)[-1].upper()
    return ('<a class="file" href="%s%s" data-file="%s" target="_blank" rel="noopener"><i>%s</i><span>%s</span></a>'
            % (C.OLD_SITE, group, e(local), t, e(name)))
def video(id_, title):
    return '<div class="vid" data-yt="%s" data-title="%s"><button type="button" aria-label="Play video: %s"></button></div>' % (id_, e(title), e(title))
def sec(inner, alt=False, id_=""):
    return '<section class="sec%s"%s><div class="wrap">%s</div></section>' % (" alt" if alt else "", ' id="%s"' % id_ if id_ else "", inner)

# ------------------------------------------------------------------ layout
def contact_block():
    soc = "".join('<a class="pill" href="%s" %s>%s</a>' % (e(u), ext(u), e(n)) for n, u in C.SOCIAL)
    mails = "<br>".join('<a href="mailto:%s">%s</a>' % (m, m) for m in C.EMAILS)
    return ('<div class="contact"><div><b>Address</b>%s</div><div><b>Mobile</b><a href="tel:%s">%s</a></div><div><b>Email</b>%s</div></div><div class="pills" style="margin-top:18px">%s</div>'
            % (e(C.ADDRESS), C.PHONE, C.PHONE, mails, soc))

def layout(pslug, title, body, desc, head_extra=""):
    nav = "".join('<a href="%s.html"%s>%s</a>' % (s if s != "index" else "index", ' class="on" aria-current="page"' if s == pslug else "", e(l)) for s, l, _, _ in C.PAGES)
    full_title = C.NAME + " | " + title if pslug != "index" else "%s | Mechatronics & Robotics Engineer" % C.NAME
    og = REG[C.HERO]["full"] if C.HERO in REG else ""
    url = (SITE_URL.rstrip("/") + "/" + ("" if pslug == "index" else pslug + ".html")) if SITE_URL else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(desc)}">
{('<meta property="og:image" content="%s/%s">' % (SITE_URL.rstrip("/"), og)) if SITE_URL and og else ""}{('<meta property="og:url" content="%s">' % url) if url else ""}
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#070b14"><meta name="color-scheme" content="dark light">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;700&display=swap">
<link rel="stylesheet" href="assets/css/style.css">{head_extra}
</head>
<body>
<div class="orbs" aria-hidden="true"><i></i><i></i><i></i></div>
<a class="skip" href="#main">Skip to content</a><div id="progress"></div>
<header class="nav"><div class="wrap">
<a class="brand" href="index.html"><span class="logo">GR</span>{e(C.NAME)}</a>
<nav class="links" id="links" aria-label="Main">{nav}</nav>
<button class="icon-btn theme" id="theme" aria-label="Toggle light/dark theme"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 3v18" /><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg></button>
<button class="icon-btn burger" id="burger" aria-label="Menu" aria-expanded="false"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><h3>Let’s connect</h3>{contact_block()}<p style="margin-top:26px"><small>© {C.NAME}. Mechatronics and Robotics Engineering, Assiut University.</small></p></div></footer>
<script src="assets/js/app.js" defer></script>
</body></html>'''

def page_head(pslug):
    _, _, t, intro = next(p for p in C.PAGES if p[0] == pslug)
    return '<div class="ph"><div class="wrap"><span class="eyebrow">George Read</span><h1>%s</h1>%s</div></div>' % (e(t), ("<p>%s</p>" % e(intro)) if intro else "")

# ------------------------------------------------------------------ pages
def p_index():
    hero = img(C.HERO, "George Read hero banner", "bio", hq=True)
    h = f'''<section class="hero"><div class="wrap grid"><div class="rv">
<span class="eyebrow">{e(C.TAGLINE)}</span>
<h1>Hi, I’m <span class="grad">George</span> 👋</h1>
<p class="lead">{e(C.BIO_STORY[0])}</p>
<div class="btns"><a class="btn pri" href="#resume">View my resume</a><a class="btn" href="research.html">Research</a><a class="btn" href="projects.html">Projects</a><a class="btn" href="#contact">Contact</a></div>
<div class="pills">{"".join('<a class="pill" href="%s" %s>%s</a>' % (e(u), ext(u), e(n)) for n, u in C.SOCIAL)}</div>
<div class="pills"><span class="pill fun">⚽ soccer</span><span class="pill fun">♟ chess</span><span class="pill fun">🏓 ping-pong</span><span class="pill fun">🎓 mentoring</span></div>
</div><div class="hero-img rv"><a href="{hero["full"]}" data-lb="hero" data-cap="George Read"><img src="{hero["full"]}" width="{hero["w"]}" height="{hero["h"]}" alt="George Read: robotics and engineering highlights"></a></div></div></section>'''
    stats = '<div class="wrap"><div class="stats">%s</div></div>' % "".join(
        '<div class="stat rv"><b data-count="%s" data-suffix="%s">%s</b><span>%s</span></div>' % (re.sub(r"[^0-9.]", "", n), re.sub(r"[0-9.]", "", n), n, e(l)) for n, l in C.STATS)
    story = sec(f'''<div class="two"><div class="card rv"><h2>My story</h2>{paras(C.BIO_STORY[1:])}<p>{e(C.BIO_STORY[0])}</p>
<h3 style="margin-top:1.2em">Along the way, I’ve:</h3>{ul(C.BIO_ALONG, "check")}</div>
<div><div class="quote rv"><span class="eyebrow">My vision</span><p style="margin:0">{e(C.BIO_VISION)}</p></div>
<div class="card rv" style="margin-top:22px">{paras(C.BIO_OUTRO)}<h3>I enjoy:</h3>{ul(C.BIO_ENJOY, "check")}</div></div></div>''')
    vid = sec('<h2>Watch</h2>' + video(C.VIDEO_BIO, "George Read: introduction video"), alt=True)
    res = sec(f'''<h2>Resume</h2><p class="lead">Click to see my full resume.</p>
<div class="btns"><a class="btn pri" href="{C.RESUME}" target="_blank" rel="noopener">Open full resume ↗</a></div>
<iframe class="frame" src="{C.RESUME_PREVIEW}" title="George Read resume" loading="lazy"></iframe>''', id_="resume")
    fb = sec(f'''<div class="card fb"><img src="assets/img/feedback-qr.png" width="170" height="170" alt="QR code linking to the feedback form"><div><h2>Feedback</h2><p>{e(C.FEEDBACK)}</p><a class="btn pri" href="{C.FORM}" target="_blank" rel="noopener">Open the feedback form ↗</a></div></div>''', alt=True)
    con = sec('<h2>Contact</h2>' + contact_block(), id_="contact")
    ld = {"@context": "https://schema.org", "@type": "Person", "name": C.FULL, "alternateName": C.NAME, "jobTitle": "Mechatronics and Robotics Engineer",
          "affiliation": {"@type": "CollegeOrUniversity", "name": "Assiut University"}, "address": {"@type": "PostalAddress", "addressLocality": "Assiut", "addressCountry": "EG"},
          "email": C.EMAILS[0], "telephone": C.PHONE, "sameAs": [u for _, u in C.SOCIAL]}
    return h + stats + story + vid + res + fb + con, '<script type="application/ld+json">%s</script>' % json.dumps(ld)

def p_research():
    out = page_head("research")
    out += sec('<h2>Research interests</h2>' + ul(C.RESEARCH_INTERESTS, "check") + '<h2 style="margin-top:1.6em">Research papers</h2>')
    for k, r in enumerate(C.RESEARCH):
        inner = '<article class="card rv"><span class="badge">%s</span><div class="meta">%s</div><h2>%s</h2>%s' % (e(r["badge"]), e(r["date"]), e(r["title"]), paras(r["paras"]))
        if r.get("link"): inner += links([r["link"]])
        if r.get("file"): inner += '<div class="files" style="margin-top:14px">%s</div>' % filecard(r["file"][0], r["file"][1])
        if r.get("video"): inner += '<div style="margin-top:20px">%s</div>' % video(r["video"], "Conference presentation")
        inner += gal(r["imgs"], r["title"], "research", r["slug"])
        if r["slug"] == "pear-sorting":
            inner += '<div class="sub"><h3>Currently</h3>%s' % ul(C.RESEARCH_CURRENT) + '<h3>Abstract</h3><p>%s</p>' % e(C.PEAR_ABSTRACT)
            inner += '<h3>Technical methodology</h3><ol class="steps">%s</ol>' % "".join('<li><b>%s</b><br>%s</li>' % (e(a), e(b)) for a, b in C.PEAR_METHOD)
            inner += '<h3>System performance and preliminary results</h3><p>The current prototype demonstrates high operational reliability and accuracy:</p><div class="res3">%s</div>' % "".join(
                '<div class="stat"><b>%s</b><strong>%s</strong><br><span>%s</span></div>' % (e(a), e(b), e(c)) for a, b, c in C.PEAR_RESULTS)
            inner += gal(C.PEAR_IMGS, "Pear sorting system", "research", "pear-sorting") + "</div>"
        inner += "</article>"
        out += sec(inner, alt=(k % 2 == 1))
    return out, ""

def p_projects():
    g = C.GRAD
    inner = '<article class="card feature rv"><span class="badge">Selected robotics project</span><h2>%s</h2>%s' % (e(g["title"]), gal(g["imgs"], "Graduation project", "projects", "grad"))
    for b in g["blocks"]:
        inner += '<div class="sub"><h3>%s</h3>' % e(b["h"])
        if b.get("text"): inner += "<p>%s</p>" % e(b["text"])
        inner += ul(b.get("bullets", []))
        if b.get("file"): inner += '<div class="files" style="margin:12px 0">%s</div>' % filecard(b["file"][0], b["file"][1])
        inner += gal(b.get("imgs", []), "Graduation project: " + b["h"], "projects", "grad", b.get("caps")) + "</div>"
    inner += "</article>"
    cnt = {k: sum(1 for p in C.PROJECTS if p["cat"] == k) for k in C.CATS}
    chips = '<button class="chip" data-cat="all" aria-pressed="true">All (%d)</button>' % len(C.PROJECTS) + "".join(
        '<button class="chip" data-cat="%s" aria-pressed="false">%s (%d)</button>' % (k, e(v), cnt[k]) for k, v in C.CATS.items())
    cards = ""
    for n, p in enumerate(C.PROJECTS):
        body = "<p>%s</p>" % e(p["text"]) + ul(p.get("bullets", [])) + (("<p><strong>%s</strong></p>" % e(p["result"])) if p.get("result") else "")
        cards += ('<article class="card proj rv" data-cat="%s"><span class="badge">%s</span>%s<h3>%s</h3>%s%s%s</article>'
                  % (p["cat"], e(C.CATS[p["cat"]]), gal(p["imgs"], p["title"], "projects", "p%d" % n, sm=len(p["imgs"]) > 3 and False), e(p["title"]), tags(p.get("tags")), body, links(p.get("links"))))
    out = page_head("projects") + sec(inner)
    out += sec('<h2>Selected projects</h2><div class="filters">%s<input class="search" id="q" type="search" placeholder="Search projects…" aria-label="Search projects"></div><div class="proj-grid">%s</div><p id="none" hidden>No projects match your search.</p><p class="meta" style="margin-top:30px">%s</p><p>%s</p>'
               % (chips, cards, e(C.MODELLING_NOTE), e(C.PROJECTS_OUTRO)), alt=True)
    return out, ""

def p_experience():
    arts = ""
    for x in C.EXPERIENCE:
        body = paras(x["paras"]) + ul(x.get("bullets", [])) + (paras([x["after"]]) if x.get("after") else "")
        certs = ""
        if x["certs"]:
            certs = '<h4>Related certificates</h4><div class="certs-mini">%s</div>' % "".join(shot(c, CERT_TITLE.get(c, "certificate"), "certificates", "exp-" + slug(x["org"]), hq=True, alt="Certificate: " + CERT_TITLE.get(c, "")) for c in x["certs"])
        arts += ('<article class="card rv"><span class="badge">%s</span><div class="meta">%s</div><h2>%s</h2>%s%s%s%s</article>'
                 % (e(x["role"]), e(x["date"]), e(x["org"]), body, links([x["link"]]), gal(x["imgs"], x["org"], "experience", "exp-" + slug(x["org"])), certs))
    return page_head("experience") + sec('<div class="tl">%s</div>' % arts), ""

def p_skills():
    cards = "".join('<div class="card rv"><span class="sk-n">%02d</span><h3>%s</h3>%s</div>' % (n + 1, e(t), ul(items)) for n, (t, _, items) in enumerate(C.SKILLS))
    non = '<div class="card rv"><span class="sk-n">%02d</span><h3>Non-Tech Skills</h3>%s</div>' % (len(C.SKILLS) + 1, ul(C.NONTECH, "check"))
    return page_head("skills") + sec('<div class="sk-grid">%s%s</div>' % (cards, non)), ""

def p_community():
    out = page_head("community")
    for k, x in enumerate(C.COMMUNITY):
        out += sec('<article class="card rv"><span class="badge">%s</span><h2>%s</h2>%s%s</article>' % (e(x["role"]), e(x["org"]), paras(x["paras"]), gal(x["imgs"], x["org"], "community", "com-" + slug(x["org"]))), alt=(k % 2 == 1))
    return out, ""

def p_presentations():
    cards = "".join(filecard(n, "files/presentations/" + n) for n in C.PRES_FILES)
    return page_head("presentations") + sec('<h2>Engineering presentations</h2><div class="files">%s</div>' % cards), ""

def p_courses():
    t = C.TRANSCRIPT
    out = page_head("courses") + sec('<h2>Courses inside class</h2><div class="files">%s</div>' % filecard(t[0], t[1], "cources"))
    out += sec('<h2>Extra courses outside class</h2>' + gal(C.COURSES_IMGS, "Extra course", "courses", "courses", {"p86": "Embedded systems course: project grading criteria", "p85": "AMIT Embedded Systems Diploma"}, hq=True), alt=True)
    return out, ""

def p_certificates():
    shots = ""
    for title, date, ids in C.CERTS:
        for n, i in enumerate(ids):
            cap = title + ((" · " + date) if date else "") + ((" (%d/%d)" % (n + 1, len(ids))) if len(ids) > 1 else "")
            shots += shot(i, title, "certificates", "certs", cap, alt="Certificate: " + title, hq=True)
    return page_head("certificates") + sec('<div class="gal" style="columns:4 250px">%s</div>' % shots), ""

# ------------------------------------------------------------------ run
def main():
    os.makedirs(os.path.join(ROOT, "assets", "img"), exist_ok=True)
    import qrcode
    qrcode.make(C.FORM, box_size=8, border=2).save(os.path.join(ROOT, "assets", "img", "feedback-qr.png"))
    open(os.path.join(ROOT, "assets", "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbbf24"/><stop offset="1" stop-color="#fb7185"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="42" font-family="Arial" font-weight="700" font-size="28" text-anchor="middle" fill="#1a1205">GR</text></svg>')
    img(C.HERO, "George Read hero banner", "bio", hq=True)
    descs = {"index": "George Read: Mechatronics and Robotics Engineering student at Assiut University. Robotics, ROS2, embedded systems, automation and energy-efficient control research.",
             "research": "Research by George Read: energy optimization in robotics with machine learning, freezing desalination, and vision-based robotic fruit sorting.",
             "projects": "Robotics, embedded systems, automation, modelling & control, and mechanical design projects by George Read.",
             "experience": "Internships and work: Siemens, ExxonMobil, Halliburton, Fab Lab Egypt, HA Consultation Group, DCS, SemiColon, and founder of Tech Spot academy.",
             "skills": "Technical and non-technical skills: robotics, ROS2, embedded systems, PLC and automation, mechanical design and simulation, AI and ML.",
             "community": "Student activities and community service: Matrix Mu, Green Assiut University Initiative, Enactus AU, ASME AU, Assiut Robotics, USAID Scholars Camps.",
             "presentations": "Over 50 engineering presentations, from academic talks to pitch decks and project demonstrations.",
             "courses": "Courses inside class and extra courses outside class.", "certificates": "Certificates, awards and letters of recognition."}
    fns = dict(index=p_index, research=p_research, projects=p_projects, experience=p_experience, skills=p_skills, community=p_community,
               presentations=p_presentations, courses=p_courses, certificates=p_certificates)
    for s, _, t, _ in C.PAGES:
        body, extra = fns[s]()
        open(os.path.join(ROOT, s + ".html"), "w", encoding="utf-8").write(layout(s, t, body, descs[s], extra))
    # coverage check: every original photo must be placed on the site
    allsrc = sorted(f for f in os.listdir(SRC) if f.startswith("unnamed"))
    used = {os.path.basename(src_path(i)) for i in REG}
    missing = [f for f in allsrc if f not in used]
    print("photos in archive: %d | placed on site: %d | missing: %s" % (len(allsrc), len(used), missing or "none"))
    if missing: sys.exit("MISSING PHOTOS: %s" % missing)
    with open(os.path.join(ROOT, "assets", "img", "MANIFEST.md"), "w") as f:
        f.write("# Photo manifest\n\nEvery original photo from `Photos.rar` and where it is used.\n\n| Original file | Optimized file | Used for |\n|---|---|---|\n")
        for o, n, w in sorted(MANIFEST): f.write("| `%s` | `%s` | %s |\n" % (o, n, w))
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n" + (("Sitemap: %s/sitemap.xml\n" % SITE_URL.rstrip("/")) if SITE_URL else ""))
    if SITE_URL:
        u = SITE_URL.rstrip("/")
        open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % "".join("<url><loc>%s/%s</loc></url>" % (u, "" if s == "index" else s + ".html") for s, *_ in C.PAGES))

if __name__ == "__main__":
    main()
