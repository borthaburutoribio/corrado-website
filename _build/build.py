# -*- coding: utf-8 -*-
"""Genera el sitio estático del Dr. Gustavo Corrado.

Uso:  python _build/build.py   (desde la raíz del proyecto)
Cada página vive en /<slug>/index.html, igual que las URLs de la web vieja.
"""
import json, os, html, urllib.parse
from content import CATS, T, BY_SLUG, CASES, REVIEWS, CV, WA_MAIN, WA_NORDELTA

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://borthaburutoribio.github.io/corrado-website/"
V = "7"  # versión de css/js (cache)
e = html.escape


def wa(text, num=WA_MAIN):
    return f"https://wa.me/{num}?text={urllib.parse.quote(text)}"


def arrow():
    return '<span class="btn__ic" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M3 8h9M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'


MONO = '''<svg class="mono" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="none" stroke="currentColor" stroke-width="2"/><text x="25" y="35" text-anchor="middle" font-family="Bodoni Moda, Didot, Georgia, serif" font-size="30" fill="currentColor">G</text><text x="38" y="47" text-anchor="middle" font-family="Bodoni Moda, Didot, Georgia, serif" font-size="30" fill="currentColor">C</text></svg>'''


# ------------------------------------------------------------------ layout
def nav(r, current):
    def group(cat):
        items = "".join(f'<li><a href="{r}{x["slug"]}/"{" aria-current=\"page\"" if current == x["slug"] else ""}>{e(x["menu"])}</a></li>' for x in T if x["cat"] == cat)
        cur = ' aria-current="page"' if current == cat else ""
        return f'''<li class="nav__g">
          <a class="nav__top" href="{r}{cat}/"{cur}>{CATS[cat]["name"]}</a>
          <button class="nav__exp" type="button" aria-expanded="false" aria-label="Ver tratamientos de {CATS[cat]["name"]}"><svg viewBox="0 0 12 12"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></button>
          <ul class="nav__sub">{items}</ul></li>'''
    def li(slug, name):
        cur = ' aria-current="page"' if current == slug else ""
        return f'<li><a class="nav__top" href="{r}{slug}/"{cur}>{name}</a></li>'
    return f'''<header class="hd" id="top">
  <a class="hd__brand" href="{r}" aria-label="Dr. Gustavo Corrado, inicio">{MONO}<span><b translate="no">Gustavo Corrado</b><small>Cirujano plástico</small></span></a>
  <nav class="nav" id="nav" aria-label="Principal">
    <ul class="nav__list">
      {group("cirugia-plastica")}
      {group("medicina-estetica")}
      {group("otros-tratamientos")}
      {li("acerca-de-mi", "Acerca de mí")}
      {li("consultorios", "Consultorios")}
      {li("contacto", "Contacto")}
    </ul>
    <a class="btn btn--glow nav__cta" href="{wa("Hola Dr. Corrado, quisiera pedir un turno.")}" target="_blank" rel="noopener">Pedir turno por WhatsApp {arrow()}</a>
  </nav>
  <a class="btn btn--glow btn--sm hd__cta" href="{wa("Hola Dr. Corrado, quisiera pedir un turno.")}" target="_blank" rel="noopener">Pedir turno</a>
  <button class="hd__menu" type="button" aria-expanded="false" aria-controls="nav"><span class="sr">Abrir menú</span><i></i><i></i></button>
</header>'''


def footer(r):
    cols = ""
    for cat in CATS:
        items = "".join(f'<li><a href="{r}{x["slug"]}/">{e(x["menu"])}</a></li>' for x in T if x["cat"] == cat)
        cols += f'<div><h3><a href="{r}{cat}/">{CATS[cat]["name"]}</a></h3><ul>{items}</ul></div>'
    return f'''<footer class="ft">
  <div class="ft__cta wrap">
    <p class="ft__big">¿Qué te gustaría mejorar?<br><span>Contámelo y lo vemos en consulta.</span></p>
    <a class="btn btn--glow btn--lg" href="{wa("Hola Dr. Corrado, quisiera pedir una evaluación.")}" target="_blank" rel="noopener">Pedir evaluación {arrow()}</a>
  </div>
  <div class="ft__grid wrap">
    <div class="ft__id">
      <a class="hd__brand" href="{r}">{MONO}<span><b translate="no">Gustavo Corrado</b><small>Cirujano plástico · MN 113095</small></span></a>
      <p>Belgrano: Arcos 2173, 1.º A, CABA<br>Nordelta: Lorem ipsum, Tigre</p>
      <p><a href="{wa("Hola Dr. Corrado")}" target="_blank" rel="noopener">WhatsApp 11 2659-1809</a><br><a href="https://www.instagram.com/gc.cirujanoplastico/" target="_blank" rel="noopener">Instagram @gc.cirujanoplastico</a></p>
      <button class="ft__share" type="button" data-share>Compartir este sitio</button>
    </div>
    {cols}
    <div><h3>El doctor</h3><ul><li><a href="{r}acerca-de-mi/">Acerca de mí</a></li><li><a href="{r}consultorios/">Consultorios</a></li><li><a href="{r}contacto/">Contacto</a></li><li><a href="{r}#antes-despues">Antes y después</a></li><li><a href="{r}#preguntas">Preguntas frecuentes</a></li></ul></div>
  </div>
  <p class="ft__word" aria-hidden="true">Gustavo Corrado</p>
  <p class="ft__legal wrap">Dr. Gustavo Corrado · Cirujano plástico · MN 113095 · Miembro de la SCPBA. La información de este sitio no reemplaza una consulta médica; los resultados varían en cada paciente. Fotos: archivo del doctor, @gc.cirujanoplastico y Saffiro Tecnologías Médicas. Propuesta de diseño de Tranquera Digital.</p>
</footer>
<div class="dock"><a class="btn btn--glow" href="{wa("Hola Dr. Corrado, quisiera pedir una evaluación.")}" target="_blank" rel="noopener">Pedir evaluación por WhatsApp</a></div>'''


def page(r, current, title, desc, body, schema=None, og_img="assets/img/dr-gustavo-corrado-nordelta-mercedes-pitrau.jpg"):
    sch = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    return f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<!-- Sitio de muestra: sacar noindex al pasar a producción -->
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#061417">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}{og_img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@300;400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Bodoni+Moda:opsz,wght@6..96,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}styles.css?v={V}">
{sch}
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="grain" aria-hidden="true"></div>
{nav(r, current)}
<main id="contenido">
{body}
</main>
{footer(r)}
<script src="{r}script.js?v={V}" defer></script>
</body>
</html>
'''


def faq_html(items, schema_list):
    schema_list.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})
    return "".join(f'<details class="qa"{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(items))


def card(r, x, big=False):
    return f'''<a class="tcard{" tcard--big" if big else ""}" href="{r}{x["slug"]}/" data-spot>
  <span class="tcard__img"><img src="{r}assets/img/t/{x["img"]}.jpg" alt="" loading="lazy" width="640" height="420"></span>
  <span class="tcard__body"><span class="tcard__cat">{CATS[x["cat"]]["name"]}</span><b>{e(x["name"])}</b><span class="tcard__txt">{e(x["short"])}</span><span class="tcard__more">Ver tratamiento {arrow()}</span></span>
</a>'''


def ba_html(r, cases, idp="ba"):
    k0 = cases[0]
    n, tr, w, h = CASES[k0]
    btns = "".join(f'<button type="button" class="pill" aria-pressed="{"true" if k == k0 else "false"}" data-case="{k}" data-w="{CASES[k][2]}" data-h="{CASES[k][3]}" data-t="{CASES[k][1]}">{CASES[k][0]}</button>' for k in cases)
    return f'''<div class="ba" data-ba data-root="{r}">
  <div class="ba__frame" style="--ratio:{w}/{h}">
    <img class="ba__b" src="{r}assets/img/antes-despues/{k0}-antes.jpg" width="{w}" height="{h}" alt="{n}, antes" loading="lazy">
    <div class="ba__a"><img src="{r}assets/img/antes-despues/{k0}-despues.jpg" width="{w}" height="{h}" alt="{n}, después" loading="lazy"></div>
    <span class="ba__tag ba__tag--l">Antes</span><span class="ba__tag ba__tag--r">Después</span>
    <span class="ba__handle" aria-hidden="true"></span>
    <input class="ba__range" type="range" min="0" max="100" value="50" aria-label="Deslizá para comparar antes y después">
  </div>
  <div class="ba__side">
    <p class="ba__cap"><b>{n}</b><span>{tr}</span></p>
    <div class="pills" role="group" aria-label="Casos">{btns}</div>
    <p class="note">Pacientes reales del doctor. Los ojos se pixelan para cuidar su identidad. Los resultados varían en cada paciente.</p>
  </div>
</div>'''
    # A CONFIRMAR: consentimiento para publicar estas fotos


# ------------------------------------------------------------------ HOME
def home():
    r = ""
    schema = [{
        "@context": "https://schema.org", "@type": "Physician", "name": "Dr. Gustavo Corrado",
        "description": "Cirujano plástico: blefaroplastia, lifting Deep Plane, Endoláser VELAS, medicina estética y cirugía mamaria y corporal.",
        "medicalSpecialty": "PlasticSurgery", "identifier": "MN 113095", "telephone": "+54 9 11 2659-1809",
        "image": SITE + "assets/img/dr-gustavo-corrado-retrato.jpg",
        "sameAs": ["https://www.instagram.com/gc.cirujanoplastico/", "https://www.facebook.com/p/Dr-Gustavo-Corrado-Cirujano-Plastico-100069136395153/"],
        "memberOf": {"@type": "Organization", "name": "Sociedad de Cirugía Plástica de Buenos Aires"},
        "location": [
            {"@type": "MedicalClinic", "name": "Consultorio Belgrano", "address": {"@type": "PostalAddress", "streetAddress": "Arcos 2173, 1.º A", "addressLocality": "Ciudad Autónoma de Buenos Aires", "addressCountry": "AR"}},
            {"@type": "MedicalClinic", "name": "Consultorio Nordelta", "telephone": "+54 9 11 3518-4999", "address": {"@type": "PostalAddress", "addressLocality": "Nordelta, Tigre", "addressRegion": "Buenos Aires", "addressCountry": "AR"}}]}]

    featured = ["cirugia-de-parpados", "lifting-facial-y-cervical", "cirugia-laser"]
    tabs = ""
    panels = ""
    for i, cat in enumerate(CATS):
        sel = "true" if i == 0 else "false"
        tabs += f'<button type="button" role="tab" class="tab" id="tab-{cat}" aria-controls="p-{cat}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{CATS[cat]["name"]}<sup>{sum(1 for x in T if x["cat"] == cat)}</sup></button>'
        cards = "".join(card(r, x) for x in T if x["cat"] == cat)
        panels += f'<div class="tpanel" role="tabpanel" id="p-{cat}" aria-labelledby="tab-{cat}"{"" if i == 0 else " hidden"}><div class="tgrid">{cards}</div><a class="link" href="{r}{cat}/">Todo sobre {CATS[cat]["name"].lower()} {arrow()}</a></div>'

    reviews = "".join(f'<figure class="rv-card" data-spot><blockquote>{e(t_)}</blockquote><figcaption><span class="stars" aria-label="Recomienda">★★★★★</span>{e(n)} · Facebook</figcaption></figure>' for n, t_ in REVIEWS)

    faqs_schema = []
    faq = faq_html([
        ("¿Tengo que saber qué tratamiento quiero antes de la consulta?", "No. Podés llegar sabiendo qué te gustaría mejorar y qué querés preservar. Mi trabajo es escucharte, evaluar tu rostro y definir si un lifting, una blefaroplastia u otro abordaje está realmente indicado."),
        ("¿Dónde atiende el doctor?", "En Belgrano (Arcos 2173, 1.º A, CABA) y, desde octubre de 2026, también en Nordelta."),
        ("¿Cómo pido un turno?", "Por WhatsApp al 11 2659-1809 (Nordelta: 11 3518-4999) o con el formulario de turnos de esta página."),
        ("¿Cuánto dura el botox?", "Entre 4 y 6 meses en la mayoría de los casos, y volvés a la rutina en el momento."),
        ("¿El Deep Plane es siempre la mejor técnica de lifting?", "No siempre. Se elige según lo que necesita cada rostro, no según la tendencia."),
        ("¿Atiende por obra social o prepaga?", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
    ], faqs_schema)
    schema += faqs_schema

    body = f'''
<section class="hero" aria-labelledby="hero-t">
  <div class="hero__fx" aria-hidden="true"><span class="glow g1"></span><span class="glow g2"></span><span class="gridfx"></span></div>
  <div class="hero__in wrap">
    <div class="hero__copy">
      <p class="badge"><span class="dot"></span>MN 113095 · Miembro SCPBA · Belgrano y Nordelta</p>
      <h1 id="hero-t" class="hero__h">Cirugía plástica <em>de precisión</em></h1>
      <p class="hero__rot" aria-live="off">para tu <span class="rot" data-rot="mirada|contorno|rostro|cuello|cuerpo">mirada</span></p>
      <p class="hero__lead">Soy el Dr. Gustavo Corrado. No necesitás llegar sabiendo qué procedimiento elegir: alcanza con saber qué te gustaría mejorar y qué querés preservar.</p>
      <div class="hero__cta">
        <a class="btn btn--glow btn--lg" href="{wa("Hola Dr. Corrado, quisiera pedir una evaluación.")}" target="_blank" rel="noopener">Pedir evaluación {arrow()}</a>
        <a class="btn btn--ghost btn--lg" href="#guia">Encontrá tu tratamiento</a>
      </div>
      <dl class="hero__stats">
        <div><dt><span data-count="22">22</span></dt><dd>años de médico</dd></div>
        <div><dt><span data-count="13">13</span></dt><dd>años de cirujano plástico</dd></div>
        <div><dt>1470<small>nm</small></dt><dd>Endoláser VELAS</dd></div>
      </dl>
    </div>
    <div class="scan" aria-hidden="true">
      <div class="scan__frame">
        <img src="assets/img/t/hero-rostro-marcacion.jpg" width="800" height="996" alt="" fetchpriority="high">
        <span class="scan__line"></span>
        <span class="scan__c c1"></span><span class="scan__c c2"></span><span class="scan__c c3"></span><span class="scan__c c4"></span>
        <span class="hot" style="--x:44%;--y:34%"><i></i><b>Blefaroplastia</b></span>
        <span class="hot hot--r" style="--x:48%;--y:76%"><i></i><b>Endolift</b></span>
        <span class="hot" style="--x:31%;--y:51%"><i></i><b>Deep Plane</b></span>
        <span class="scan__hud">VELAS · 1470 / 980 nm</span>
      </div>
      <div class="scan__card">
        <img src="assets/img/dr-gustavo-corrado-retrato.jpg" width="340" height="595" alt="">
        <span><b>Dr. Gustavo Corrado</b><small>Disertante Masterhub 2026</small></span>
      </div>
    </div>
  </div>
</section>

<section class="strip" aria-label="Datos de contacto">
  <div class="strip__in wrap">
    <a class="strip__it" href="{wa("Hola Dr. Corrado")}" target="_blank" rel="noopener"><span class="ico"><svg viewBox="0 0 24 24"><path d="M5 19l1.2-3.6A7.5 7.5 0 1 1 9 18.6z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></span><span><small>Turnos por WhatsApp</small>11 2659-1809</span></a>
    <a class="strip__it" href="consultorios/"><span class="ico"><svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="9.5" r="2.5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></span><span><small>Consultorios</small>Belgrano · Nordelta</span></a>
    <a class="strip__it" href="https://www.instagram.com/gc.cirujanoplastico/" target="_blank" rel="noopener"><span class="ico"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="5" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="12" cy="12" r="3.6" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></span><span><small>Instagram</small>@gc.cirujanoplastico · 12 mil</span></a>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__t">{"".join(f"<span>{e(x['name'])}</span>" for x in T) * 2}</div></div>

<section class="sec resumen wrap" aria-labelledby="res-t">
  <h2 id="res-t" class="h2">En resumen</h2>
  <div class="resumen__grid">
    <p class="big">Cirujano plástico con matrícula nacional 113095, formado en cirugía general y reparadora antes que en estética. Hoy su consulta es sobre todo facial: <a href="cirugia-de-parpados/">blefaroplastia</a>, <a href="lifting-facial-y-cervical/">lifting Deep Plane</a> y <a href="cirugia-laser/">Endolift con Endoláser</a>.</p>
    <ul class="why">
      <li data-spot><b>Tecnología de punta</b><span>Endoláser VELAS 1470/980 nm y Ultherapy. Enseña la técnica a otros médicos en vivo.</span></li>
      <li data-spot><b>Cada caso es único</b><span>Primero evalúa qué genera el problema; después indica. A veces la respuesta es «esto no te hace falta».</span></li>
      <li data-spot><b>Base reparadora</b><span>Quemados en el Hospital Alemán y cirugía infantil en el Garrahan y el Gutiérrez.</span></li>
      <li data-spot><b>Dos sedes</b><span>Arcos 2173 en Belgrano y el nuevo espacio de Nordelta.</span></li>
    </ul>
  </div>
</section>

<section class="sec trat" id="tratamientos" aria-labelledby="trat-t">
  <div class="wrap">
    <div class="sec__head"><h2 id="trat-t" class="h2">Tratamientos</h2><p>Los mismos de siempre, ahora con una página propia cada uno: qué es, tiempos, recuperación y preguntas.</p></div>
    <div class="tabs" role="tablist" aria-label="Categorías">{tabs}</div>
    {panels}
  </div>
</section>

<section class="sec guide" id="guia" aria-labelledby="guia-t">
  <div class="wrap guide__in">
    <div class="guide__head">
      <h2 id="guia-t" class="h2">¿Qué te gustaría mejorar?</h2>
      <p>Tocá una zona del rostro. Te muestro qué se suele indicar y te dejo el WhatsApp con el mensaje armado.</p>
    </div>
    <figure class="guide__face">
      <img src="assets/img/t/hero-rostro-marcacion.jpg" width="800" height="996" alt="Rostro con líneas punteadas de marcación prequirúrgica sobre párpados, pómulos y mandíbula." loading="lazy">
      <span class="scan__line"></span>
      <button class="spot" type="button" style="--x:58%;--y:16%" data-zone="frente"><span class="sr">Frente y entrecejo</span></button>
      <button class="spot" type="button" style="--x:44%;--y:34%" data-zone="mirada"><span class="sr">Párpados y mirada</span></button>
      <button class="spot" type="button" style="--x:63%;--y:46%" data-zone="nariz"><span class="sr">Nariz</span></button>
      <button class="spot" type="button" style="--x:31%;--y:51%" data-zone="pomulos"><span class="sr">Pómulos y surcos</span></button>
      <button class="spot" type="button" style="--x:63%;--y:61%" data-zone="labios"><span class="sr">Labios y mentón</span></button>
      <button class="spot" type="button" style="--x:48%;--y:76%" data-zone="contorno"><span class="sr">Papada y contorno</span></button>
      <button class="spot" type="button" style="--x:70%;--y:92%" data-zone="cuello"><span class="sr">Cuello</span></button>
    </figure>
    <div class="guide__panel">
      <div class="pills" role="group" aria-label="Zonas">
        <button type="button" class="pill" data-zone="mirada" aria-pressed="true">Mirada</button>
        <button type="button" class="pill" data-zone="frente" aria-pressed="false">Frente</button>
        <button type="button" class="pill" data-zone="pomulos" aria-pressed="false">Pómulos</button>
        <button type="button" class="pill" data-zone="nariz" aria-pressed="false">Nariz</button>
        <button type="button" class="pill" data-zone="labios" aria-pressed="false">Labios</button>
        <button type="button" class="pill" data-zone="contorno" aria-pressed="false">Papada</button>
        <button type="button" class="pill" data-zone="cuello" aria-pressed="false">Cuello</button>
        <button type="button" class="pill" data-zone="orejas" aria-pressed="false">Orejas</button>
        <button type="button" class="pill" data-zone="cuerpo" aria-pressed="false">Cuerpo</button>
      </div>
      <div class="result glass" id="guia-resultado" aria-live="polite">
        <h3 class="result__t">Párpados y mirada</h3>
        <p>Blefaroplastia: saca el exceso de piel de los párpados y las bolsas. <a href="cirugia-de-parpados/">Ver blefaroplastia</a></p>
      </div>
      <p class="note">Orienta, no reemplaza la evaluación médica.</p>
    </div>
  </div>
</section>

<section class="counters" aria-label="El doctor en números">
  <div class="wrap counters__in">
    <div><b data-count="22">22</b><span>años de médico (UAI, 2004)</span></div>
    <div><b data-count="5">5</b><span>años de residencia en cirugía general</span></div>
    <div><b data-count="500" data-prefix="+">+500</b><span>pacientes por año</span></div><!-- A CONFIRMAR: dato de la web de 2019 -->
    <div><b data-count="2">2</b><span>consultorios: Belgrano y Nordelta</span></div>
  </div>
</section>

<section class="sec wrap" id="antes-despues" aria-labelledby="ba-t">
  <div class="sec__head"><h2 id="ba-t" class="h2">Antes y después</h2><p>Casos reales con toxina botulínica y ácido hialurónico. Deslizá la línea.</p></div>
  {ba_html(r, list(CASES.keys()))}
</section>

<section class="sec doc" aria-labelledby="doc-t">
  <div class="wrap doc__in">
    <div class="doc__pics">
      <img class="doc__a" src="assets/img/dr-gustavo-corrado-nordelta-mercedes-pitrau.jpg" width="1400" height="1867" alt="El Dr. Gustavo Corrado bajo el cartel GC del consultorio de Nordelta, junto a Mercedes Pitrau." loading="lazy">
      <img class="doc__b" src="assets/img/t/dr-endolaser-en-vivo-tono.jpg" width="1080" height="1020" alt="El doctor haciendo un Endolifting con Endoláser VELAS en una demostración en vivo." loading="lazy">
    </div>
    <div class="doc__txt">
      <h2 id="doc-t" class="h2">El doctor</h2>
      <blockquote class="pull">«En cirugía facial no se trata de hacer más. Se trata de saber qué hacer, cuándo y por qué.»</blockquote>
      <p>Médico desde 2004, cinco años de residencia de cirugía general en el Hospital Vélez Sarsfield y especialista en cirugía plástica por la Universidad del Salvador. Pasó por el equipo de quemados del Hospital Alemán y por cirugía plástica infantil en el Garrahan y el Gutiérrez.</p>
      <p>En octubre de 2026 sumó un consultorio en Nordelta a su sede de Belgrano.</p>
      <a class="btn btn--ghost" href="acerca-de-mi/">Trayectoria completa {arrow()}</a>
    </div>
  </div>
</section>

<section class="sec tech" aria-labelledby="tech-t">
  <div class="wrap">
    <div class="sec__head"><h2 id="tech-t" class="h2">Tecnología y congresos</h2><p>Lo que usa en el consultorio y lo que enseña a otros médicos.</p></div>
    <div class="bento">
      <article class="bx bx--a glass" data-spot>
        <img src="assets/img/t/endolaser-endolift.jpg" alt="Paciente con marcación para Endolift en el rostro." loading="lazy" width="720" height="680">
        <div><h3>Endoláser VELAS</h3><p>Longitudes de onda de 1470 y 980 nm para papada, flacidez y contorno mandibular, sin cirugía tradicional.</p><a class="link" href="cirugia-laser/">Endolift {arrow()}</a></div>
      </article>
      <article class="bx bx--b glass" data-spot>
        <img src="assets/img/t/masterhub-tono.jpg" alt="Stand de Saffiro en Masterhub 2026 con el equipo de Endoláser." loading="lazy" width="900" height="585">
        <div><h3>Masterhub 2026</h3><p>Charla «Rejuvenecimiento de precisión: casos clínicos y ventajas», 15 de octubre, Hotel Hilton.</p></div>
      </article>
      <article class="bx bx--c glass" data-spot><b class="bx__n">30.10</b><h3>VELAS Experience Mendoza</h3><p>Endolifting facial y corporal en vivo para médicos, junto a la Dra. Claudia Mesber.</p></article>
      <article class="bx bx--d glass" data-spot><b class="bx__n">2027</b><h3>BAAS Congress</h3><p>Disertante en Buenos Aires.</p></article>
      <article class="bx bx--e glass" data-spot><b class="bx__n">US</b><h3>Ultherapy</h3><p>Ultrasonido microfocalizado: lifting sin cirugía, sin reposo.</p><a class="link" href="ultherapy/">Ver {arrow()}</a></article>
    </div>
  </div>
</section>

<section class="sec wrap" aria-labelledby="pac-t">
  <div class="sec__head"><h2 id="pac-t" class="h2">Pacientes</h2><p>Opiniones publicadas en su página de Facebook.</p></div>
  <div class="reviews">{reviews}
    <figure class="rv-card rv-card--video" data-spot><blockquote>Mari se hizo un Endolifting con retracción de papada y contó su experiencia en video.</blockquote><figcaption><a class="link" href="https://www.instagram.com/saffiro.tech/reel/DaqLONHxCnB/" target="_blank" rel="noopener">Ver el testimonio {arrow()}</a></figcaption></figure>
  </div>
  <div class="review-cta glass">
    <p>¿Te atendiste con el doctor? Tu reseña ayuda al próximo paciente.</p>
    <a class="btn btn--glow" href="https://www.facebook.com/p/Dr-Gustavo-Corrado-Cirujano-Plastico-100069136395153/reviews" target="_blank" rel="noopener">Dejar una reseña {arrow()}</a>
  </div>
</section>

<section class="sec book" id="turnos" aria-labelledby="book-t">
  <div class="wrap book__in">
    <div>
      <h2 id="book-t" class="h2">Pedí tu turno</h2>
      <p>Elegí sede, día y horario. Se abre WhatsApp con el mensaje listo para enviar.</p>
      <p class="note">Días y horarios de atención: Lorem ipsum dolor sit amet.</p>
    </div>
    <form class="booker glass" data-booker>
      <fieldset><legend>Consultorio</legend>
        <label><input type="radio" name="sede" value="Belgrano" checked><span>Belgrano<small>Arcos 2173</small></span></label>
        <label><input type="radio" name="sede" value="Nordelta"><span>Nordelta<small>Nuevo</small></span></label>
      </fieldset>
      <fieldset><legend>Día</legend>
        <label><input type="radio" name="dia" value="lunes" checked><span>Lun</span></label>
        <label><input type="radio" name="dia" value="martes"><span>Mar</span></label>
        <label><input type="radio" name="dia" value="miércoles"><span>Mié</span></label>
        <label><input type="radio" name="dia" value="jueves"><span>Jue</span></label>
        <label><input type="radio" name="dia" value="viernes"><span>Vie</span></label>
      </fieldset>
      <fieldset><legend>Horario</legend>
        <label><input type="radio" name="hora" value="por la mañana" checked><span>Mañana</span></label>
        <label><input type="radio" name="hora" value="por la tarde"><span>Tarde</span></label>
      </fieldset>
      <label class="field"><span>¿Qué te gustaría consultar? (opcional)</span>
        <select name="trat"><option value="">Elegí un tratamiento…</option>{"".join(f'<option>{e(x["name"])}</option>' for x in T)}<option>Otra consulta</option></select>
      </label>
      <button class="btn btn--glow btn--lg" type="submit">Enviar por WhatsApp {arrow()}</button>
    </form>
  </div>
</section>

<section class="sec wrap faq" id="preguntas" aria-labelledby="faq-t">
  <div class="sec__head"><h2 id="faq-t" class="h2">Preguntas frecuentes</h2></div>
  <div class="faq__list">{faq}</div>
</section>
'''
    return page(r, "home", "Dr. Gustavo Corrado · Cirujano plástico en Belgrano y Nordelta",
                "Cirugía plástica de precisión: blefaroplastia, lifting Deep Plane, Endoláser VELAS, botox y ácido hialurónico. Dr. Gustavo Corrado, MN 113095. Belgrano y Nordelta.",
                body, schema)


# ------------------------------------------------------------------ helpers de páginas internas
def crumbs(r, items):
    li = "".join(f'<li><a href="{r}{h}">{e(n)}</a></li>' if h is not None else f'<li aria-current="page">{e(n)}</li>' for n, h in items)
    return f'<nav class="crumbs" aria-label="Ruta"><ol>{li}</ol></nav>'


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (h or "")} for i, (n, h) in enumerate(items)]}


def phero(r, crumb_items, h1, lead, img, kicker=None, facts=None, cta_text="Consultar por WhatsApp", cta_msg="Hola Dr. Corrado, quisiera hacer una consulta."):
    fx = ""
    if facts:
        fx = '<dl class="facts">' + "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in facts) + "</dl>"
    kk = f'<p class="badge"><span class="dot"></span>{e(kicker)}</p>' if kicker else ""
    return f'''<section class="phero">
  <div class="hero__fx" aria-hidden="true"><span class="glow g1"></span><span class="gridfx"></span></div>
  <div class="phero__in wrap">
    <div class="phero__copy">
      {crumbs(r, crumb_items)}
      {kk}
      <h1 class="phero__h">{e(h1)}</h1>
      <p class="phero__lead">{e(lead)}</p>
      <div class="hero__cta"><a class="btn btn--glow btn--lg" href="{wa(cta_msg)}" target="_blank" rel="noopener">{cta_text} {arrow()}</a></div>
      {fx}
    </div>
    <div class="phero__img"><img src="{r}assets/img/t/{img}.jpg" alt="" fetchpriority="high"><span class="scan__line"></span><span class="scan__c c1"></span><span class="scan__c c2"></span><span class="scan__c c3"></span><span class="scan__c c4"></span></div>
  </div>
</section>'''


def blocks(r, items):
    out = ""
    for b in items:
        if isinstance(b, tuple) and b[0] == "ul":
            out += "<ul class=\"ticks\">" + "".join(f"<li>{e(x)}</li>" for x in b[1]) + "</ul>"
        else:
            out += f"<p>{e(b)}</p>"
    return out


# ------------------------------------------------------------------ TRATAMIENTO
def treatment(x):
    r = "../"
    cat = CATS[x["cat"]]
    ci = [("Inicio", ""), (cat["name"], f'{x["cat"]}/'), (x["menu"], None)]
    schema = [crumbs_schema([(n, h if h is not None else x["slug"] + "/") for n, h in ci]),
              {"@context": "https://schema.org", "@type": "MedicalProcedure", "name": x["name"], "description": x["short"],
               "url": SITE + x["slug"] + "/", "performer": {"@type": "Physician", "name": "Dr. Gustavo Corrado"}}]
    toc = "".join(f'<li><a href="#s{i}">{e(h)}</a></li>' for i, (h, _) in enumerate(x["sections"]))
    secs = "".join(f'<section class="tsec" id="s{i}"><h2 class="h3">{e(h)}</h2>{blocks(r, b)}</section>' for i, (h, b) in enumerate(x["sections"]))
    summary = '<div class="tldr glass"><h2 class="h4">En resumen</h2><p>' + e(x["short"]) + '</p><table><tbody>' + "".join(f"<tr><th scope=\"row\">{e(k)}</th><td>{e(v)}</td></tr>" for k, v in x["facts"]) + "</tbody></table></div>"
    ba = ""
    if x.get("cases"):
        ba = f'<section class="sec"><h2 class="h3">Antes y después</h2>{ba_html(r, x["cases"])}</section>'
    vid = ""
    if x.get("video"):
        vid = f'<div class="review-cta glass"><p>{e(x["video"][0])}</p><a class="btn btn--glow" href="{x["video"][1]}" target="_blank" rel="noopener">Ver testimonio {arrow()}</a></div>'
    img2 = ""
    if x.get("img2"):
        img2 = f'<figure class="tfig"><img src="{r}assets/img/t/{x["img2"]}.jpg" alt="{e(x["name"])}: imagen ilustrativa del consultorio del doctor." loading="lazy"></figure>'
    faqs = []
    fq = faq_html(x["faq"], faqs)
    schema += faqs
    rel = "".join(card(r, BY_SLUG[s]) for s in x.get("related", []) if s in BY_SLUG)
    body = f'''{phero(r, ci, x["h1"], x["lead"], x["img"], kicker=x.get("kicker"), cta_text="Consultar por " + x["name"].split(" ·")[0], cta_msg=f"Hola Dr. Corrado, quisiera consultar por {x['name'].split(' ·')[0].lower()}.")}
<div class="tbody wrap">
  <aside class="tside">
    {summary}
    <nav class="toc" aria-label="En esta página"><p>En esta página</p><ul>{toc}<li><a href="#faq">Preguntas</a></li></ul></nav>
  </aside>
  <article class="tmain">
    {secs}
    {img2}
    {vid}
    {ba}
    <section class="tsec" id="faq"><h2 class="h3">Preguntas sobre {e(x["name"].split(" ·")[0].lower())}</h2><div class="faq__list">{fq}</div></section>
    <div class="say glass"><p>«Porque en cirugía no se trata de hacer más. Se trata de saber qué hacer, cuándo y por qué.»</p><span>Dr. Gustavo Corrado</span></div>
  </article>
</div>
<section class="sec wrap rel"><div class="sec__head"><h2 class="h2">Relacionados</h2></div><div class="tgrid">{rel}</div></section>
'''
    return page(r, x["slug"], x["title"], x["desc"], body, schema, og_img=f'assets/img/t/{x["img"]}.jpg')


# ------------------------------------------------------------------ CATEGORÍA
def category(slug):
    r = "../"
    c = CATS[slug]
    ci = [("Inicio", ""), (c["name"], None)]
    items = [x for x in T if x["cat"] == slug]
    cards = "".join(card(r, x, big=(i == 0)) for i, x in enumerate(items))
    rows = "".join(f'<tr><th scope="row"><a href="{r}{x["slug"]}/">{e(x["name"])}</a></th>' + "".join(f"<td>{e(v)}</td>" for _, v in x["facts"][:2]) + "</tr>" for x in items)
    body = f'''{phero(r, ci, c["h1"], c["lead"], c["img"])}
<section class="sec wrap"><div class="tgrid tgrid--cat">{cards}</div></section>
<section class="sec wrap"><div class="sec__head"><h2 class="h2">Comparalos de un vistazo</h2><p>Datos de la información del consultorio. Cada caso se define en consulta.</p></div>
<div class="tablewrap glass"><table class="cmp"><thead><tr><th scope="col">Tratamiento</th><th scope="col">Dato 1</th><th scope="col">Dato 2</th></tr></thead><tbody>{rows}</tbody></table></div></section>
'''
    return page(r, slug, c["title"], c["desc"], body, [crumbs_schema([("Inicio", ""), (c["name"], slug + "/")])], og_img=f'assets/img/t/{c["img"]}.jpg')


# ------------------------------------------------------------------ ACERCA
def acerca():
    r = "../"
    ci = [("Inicio", ""), ("Acerca de mí", None)]
    tl = "".join(f'<li class="tl__i"><span class="tl__y">{e(y)}</span><div><b>{e(a)}</b><span>{e(b)}</span></div></li>' for y, a, b in CV)
    body = f'''{phero(r, ci, "Acerca de mí", "Me formé primero en cirugía general y reparadora: quemados, chicos, maxilofacial. Hoy mi consulta es sobre todo facial, con la misma cabeza de cirujano.", "dr-retrato-tono", kicker="Dr. Gustavo Corrado · MN 113095")}
<section class="sec wrap about">
  <div class="about__txt">
    <!-- A CONFIRMAR: texto armado con frases de sus posteos; que lo revise -->
    <p class="big">«Mi trabajo es escucharte, evaluar tu rostro y, desde el criterio médico, definir si un lifting facial, una blefaroplastia u otro abordaje realmente está indicado.»</p>
    <p>Me recibí de médico en 2004 en la UAI e hice cinco años de residencia completa de cirugía general en el Hospital Vélez Sarsfield. Después vino la especialidad en cirugía plástica en la Universidad del Salvador.</p>
    <p>Roté por el IREP, por el Centro de Quemados del Hospital Alemán, por cirugía plástica infantil en el Hospital de Niños Ricardo Gutiérrez y en el Garrahan, y por maxilofacial y oncológica. Con el título de cirujano plástico me quedé dos años más en el equipo de quemados del Alemán.</p>
    <p>Hoy atiendo en Belgrano y en Nordelta, hago Endolift con Endoláser VELAS y lo enseño a otros médicos en jornadas en vivo. Un buen resultado no cambia quién sos: simplemente refleja una mejor versión de vos.</p>
  </div>
  <figure class="about__img"><img src="{r}assets/img/dr-gustavo-corrado-nordelta-mercedes-pitrau.jpg" width="1400" height="1867" alt="El Dr. Gustavo Corrado en el consultorio de Nordelta, bajo el cartel con su monograma GC, junto a Mercedes Pitrau." loading="lazy"><figcaption>Nordelta, octubre de 2026, con Mercedes Pitrau.</figcaption></figure>
</section>
<section class="sec wrap"><div class="sec__head"><h2 class="h2">Trayectoria</h2></div><ol class="tl">{tl}</ol></section>
<section class="sec wrap"><div class="sec__head"><h2 class="h2">Congresos</h2></div>
  <div class="bento">
    <article class="bx bx--b glass"><img src="{r}assets/img/t/masterhub-tono.jpg" alt="Stand de Saffiro en Masterhub 2026." loading="lazy" width="900" height="585"><div><h3>Masterhub 2026</h3><p>«Rejuvenecimiento de precisión: casos clínicos y ventajas». 15 de octubre, Salón Atlántico, Hotel Hilton.</p></div></article>
    <article class="bx bx--a glass"><img src="{r}assets/img/t/dr-endolaser-en-vivo-tono.jpg" alt="El doctor haciendo un Endolifting en vivo." loading="lazy" width="1080" height="1020"><div><h3>VELAS Experience Mendoza</h3><p>Endolifting láser facial y corporal en vivo para médicos. 30 de octubre de 2026.</p></div></article>
    <article class="bx bx--d glass"><b class="bx__n">2027</b><h3>BAAS Congress</h3><p>Disertante, Buenos Aires.</p></article>
  </div>
</section>
'''
    return page(r, "acerca-de-mi", "Acerca del Dr. Gustavo Corrado · Formación y trayectoria",
                "Formación del Dr. Gustavo Corrado: médico UAI, residencia en el Hospital Vélez Sarsfield, cirugía plástica en la USAL, quemados en el Hospital Alemán. Disertante Masterhub 2026.",
                body, [crumbs_schema([("Inicio", ""), ("Acerca de mí", "acerca-de-mi/")])], og_img="assets/img/dr-gustavo-corrado-retrato.jpg")


# ------------------------------------------------------------------ CONSULTORIOS
def consultorios():
    r = "../"
    ci = [("Inicio", ""), ("Consultorios", None)]
    body = f'''{phero(r, ci, "Consultorios", "Belgrano, en Arcos 2173, y el nuevo espacio de Nordelta desde octubre de 2026.", "consulta-mirada")}
<section class="sec wrap places">
  <article class="place glass" data-spot>
    <h2 class="h3">Belgrano</h2>
    <p class="place__a">Arcos 2173, 1.º A<br>Ciudad de Buenos Aires</p>
    <dl class="facts"><div><dt>Días</dt><dd>Lorem ipsum</dd></div><div><dt>Horario</dt><dd>Lorem ipsum</dd></div></dl>
    <div class="place__b"><a class="btn btn--glow" href="{wa("Hola Dr. Corrado, quisiera un turno en Belgrano.")}" target="_blank" rel="noopener">WhatsApp 11 2659-1809 {arrow()}</a><a class="link" href="https://www.google.com/maps/search/?api=1&query=Arcos+2173,+Belgrano,+CABA" target="_blank" rel="noopener">Cómo llegar {arrow()}</a></div>
    <iframe title="Mapa del consultorio de Belgrano" src="https://www.google.com/maps?q=Arcos+2173,+Belgrano,+Ciudad+de+Buenos+Aires&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </article>
  <article class="place glass" data-spot>
    <h2 class="h3">Nordelta</h2>
    <p class="place__a">Lorem ipsum 1234<br>Nordelta, Tigre</p>
    <dl class="facts"><div><dt>Días</dt><dd>Lorem ipsum</dd></div><div><dt>Horario</dt><dd>Lorem ipsum</dd></div></dl>
    <div class="place__b"><a class="btn btn--glow" href="{wa("Hola Dr. Corrado, quisiera un turno en Nordelta.", WA_NORDELTA)}" target="_blank" rel="noopener">WhatsApp 11 3518-4999 {arrow()}</a></div>
    <img class="place__img" src="{r}assets/img/dr-gustavo-corrado-nordelta-mercedes-pitrau.jpg" alt="El cartel GC del consultorio de Nordelta." loading="lazy" width="1400" height="1867">
  </article>
</section>
'''
    return page(r, "consultorios", "Consultorios del Dr. Gustavo Corrado en Belgrano y Nordelta",
                "Dónde atiende el Dr. Gustavo Corrado: Arcos 2173 1.º A en Belgrano y el nuevo consultorio de Nordelta. Turnos por WhatsApp.",
                body, [crumbs_schema([("Inicio", ""), ("Consultorios", "consultorios/")])])


# ------------------------------------------------------------------ CONTACTO
def contacto():
    r = "../"
    ci = [("Inicio", ""), ("Contacto", None)]
    body = f'''{phero(r, ci, "Contacto", "Escribí lo que te gustaría consultar. Se abre WhatsApp con tu mensaje listo para enviar.", "blefaroplastia-marcacion")}
<section class="sec wrap book__in">
  <div>
    <h2 class="h2">Escribinos</h2>
    <p>Por WhatsApp al <a class="link" href="{wa("Hola Dr. Corrado")}" target="_blank" rel="noopener">11 2659-1809</a> (Nordelta: <a class="link" href="{wa("Hola Dr. Corrado", WA_NORDELTA)}" target="_blank" rel="noopener">11 3518-4999</a>) o por mensaje privado en <a class="link" href="https://www.instagram.com/gc.cirujanoplastico/" target="_blank" rel="noopener">Instagram</a>.</p>
  </div>
  <form class="booker glass" data-contact novalidate>
    <label class="field"><span>Nombre</span><input name="nombre" autocomplete="name" required placeholder="Tu nombre…"></label>
    <label class="field"><span>Tratamiento</span><select name="trat"><option value="">Elegí uno…</option>{"".join(f'<option>{e(x["name"])}</option>' for x in T)}<option>Otra consulta</option></select></label>
    <label class="field"><span>Mensaje</span><textarea name="msg" rows="4" placeholder="Contame qué te gustaría mejorar…"></textarea></label>
    <p class="err" role="alert" hidden>Escribí tu nombre para que el doctor sepa quién le escribe.</p>
    <button class="btn btn--glow btn--lg" type="submit">Enviar por WhatsApp {arrow()}</button>
  </form>
</section>
'''
    return page(r, "contacto", "Contacto y turnos · Dr. Gustavo Corrado, cirujano plástico",
                "Pedí turno o consultá al Dr. Gustavo Corrado por WhatsApp: 11 2659-1809 (Belgrano) y 11 3518-4999 (Nordelta).",
                body, [crumbs_schema([("Inicio", ""), ("Contacto", "contacto/")])])


def redirect(to):
    return f'<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><title>Redirigiendo…</title><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{to}"><meta http-equiv="refresh" content="0; url=../{to}"></head><body><a href="../{to}">Ir a la página</a></body></html>'


def not_found():
    body = '''<section class="phero"><div class="hero__fx" aria-hidden="true"><span class="glow g1"></span><span class="gridfx"></span></div><div class="phero__in wrap"><div class="phero__copy"><h1 class="phero__h">Esta página no existe</h1><p class="phero__lead">Puede que el link sea de la web anterior. Probá desde el inicio o mirá los tratamientos.</p><div class="hero__cta"><a class="btn btn--glow btn--lg" href="/corrado-website/">Ir al inicio</a><a class="btn btn--ghost btn--lg" href="/corrado-website/#tratamientos">Ver tratamientos</a></div></div></div></section>'''
    return page("/corrado-website/", "404", "Página no encontrada · Dr. Gustavo Corrado", "La página que buscás no existe.", body)


def write(rel, s):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


if __name__ == "__main__":
    write("index.html", home())
    for c in CATS:
        write(f"{c}/index.html", category(c))
    for x in T:
        write(f'{x["slug"]}/index.html', treatment(x))
    write("acerca-de-mi/index.html", acerca())
    write("consultorios/index.html", consultorios())
    write("contacto/index.html", contacto())
    write("lipoescultura-laser-minimamente-invasiva/index.html", redirect("lipoescultura-laser/"))
    write("404.html", not_found())
    urls = [""] + [c + "/" for c in CATS] + [x["slug"] + "/" for x in T] + ["acerca-de-mi/", "consultorios/", "contacto/"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>2026-10-16</lastmod></url>\n" for u in urls) + "</urlset>\n")
    print("ok", len(urls), "páginas")
