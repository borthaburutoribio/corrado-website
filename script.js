/* Dr. Gustavo Corrado — interacciones compartidas */
document.documentElement.classList.add('js');
const WA = '5491126591809';
const wa = (t) => `https://wa.me/${WA}?text=${encodeURIComponent(t)}`;
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const ROOT = (document.querySelector('.hd__brand')?.getAttribute('href')) || '';

/* ---------- header + menú ---------- */
const hd = document.querySelector('.hd');
const menuBtn = document.querySelector('.hd__menu');
addEventListener('scroll', () => hd.classList.toggle('scrolled', scrollY > 30), { passive: true });
menuBtn?.addEventListener('click', () => {
  const open = hd.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
  menuBtn.querySelector('.sr').textContent = open ? 'Cerrar menú' : 'Abrir menú';
});
$$('.nav__exp').forEach(b => b.addEventListener('click', () => {
  const g = b.closest('.nav__g'); const on = g.classList.toggle('exp'); b.setAttribute('aria-expanded', on);
}));
$$('.nav a').forEach(a => a.addEventListener('click', () => { hd.classList.remove('open'); menuBtn?.setAttribute('aria-expanded', 'false'); }));
addEventListener('keydown', e => { if (e.key === 'Escape' && hd.classList.contains('open')) { hd.classList.remove('open'); menuBtn.focus(); } });

/* ---------- palabra que rota en el hero ---------- */
$$('[data-rot]').forEach(el => {
  const words = el.dataset.rot.split('|'); let i = 0;
  if (reduce) return;
  setInterval(() => {
    el.classList.add('out');
    setTimeout(() => { i = (i + 1) % words.length; el.textContent = words[i]; el.classList.remove('out'); }, 350);
  }, 2400);
});

/* ---------- altura del escaneo láser ---------- */
const setScan = () => $$('.scan__line').forEach(l => l.style.setProperty('--scan-h', (l.parentElement.clientHeight - 2) + 'px'));
setScan(); addEventListener('resize', setScan);

/* ---------- spotlight en tarjetas ---------- */
$$('[data-spot]').forEach(c => c.addEventListener('pointermove', e => {
  const r = c.getBoundingClientRect();
  c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
}));

/* ---------- pestañas de tratamientos ---------- */
const tabs = $$('.tab');
function selectTab(t) {
  tabs.forEach(x => { const on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).hidden = !on; });
}
tabs.forEach((t, i) => {
  t.addEventListener('click', () => selectTab(t));
  t.addEventListener('keydown', e => {
    const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
    if (d) { const n = tabs[(i + d + tabs.length) % tabs.length]; selectTab(n); n.focus(); }
  });
});

/* ---------- contadores ---------- */
const cio = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return; cio.unobserve(e.target);
  const el = e.target, end = +el.dataset.count, pre = el.dataset.prefix || '';
  if (reduce) { el.textContent = pre + end; return; }
  const t0 = performance.now(), dur = 1600;
  const step = (now) => { const p = Math.min(1, (now - t0) / dur); el.textContent = pre + Math.round(end * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}), { threshold: .6 });
$$('[data-count]').forEach(el => cio.observe(el));

/* ---------- guía por zonas (inicio) ---------- */
const L = (slug, name) => `<a href="${ROOT}${slug}/">${name}</a>`;
const ZONES = {
  mirada: { t: 'Párpados y mirada', q: 'Mi objetivo es una mirada más descansada y armónica, sin modificar la expresión natural del rostro.', o: [
    [L('cirugia-de-parpados', 'Blefaroplastia'), 'Saca el exceso de piel de los párpados superiores y, según el caso, las bolsas de los inferiores.', [['Tipo', 'Cirugía'], ['Suele indicarse', 'desde los 35']]],
    [L('rellenos-con-acido-hialuronico', 'Valle de lágrimas'), 'Ácido hialurónico para la ojera hundida, cuando no hace falta cirugía.', [['Tipo', 'Inyectable']]]] },
  frente: { t: 'Frente y entrecejo', q: 'Que te vean descansada, no distinta.', o: [
    [L('botox', 'Toxina botulínica'), 'Arrugas de expresión en frente, entrecejo y patas de gallo. También levanta la cola de la ceja.', [['Dura', '4 a 6 meses'], ['Reposo', 'no']]],
    [L('ultherapy', 'Ultherapy'), 'Ultrasonido que estimula colágeno nuevo. Para cejas caídas y flacidez leve.', [['Reposo', 'no']]]] },
  pomulos: { t: 'Pómulos y surcos', q: 'Cada paciente tiene un diagnóstico diferente. Por eso el primer paso siempre es la consulta.', o: [
    [L('rellenos-con-acido-hialuronico', 'Ácido hialurónico'), 'Surco nasogeniano, pómulos y técnica Pointlift para levantar el tercio medio.', [['Tipo', 'Inyectable']]],
    [L('relleno-con-radiesse', 'Radiesse'), 'Volumen inmediato y estímulo de tu propio colágeno.', [['Dura', '12 a 18 meses']]],
    [L('plasma-rico-en-plaquetas', 'Plasma rico en plaquetas'), 'Con tu propia sangre: firmeza, luminosidad y textura.', [['Sesiones', '2 a 3 al año']]]] },
  nariz: { t: 'Nariz', q: 'No se trata de hacer más. Se trata de saber qué hacer, cuándo y por qué.', o: [
    [L('rellenos-con-acido-hialuronico', 'Rinomodelación'), 'Corrige dorso o punta con ácido hialurónico o Radiesse, sin cirugía.', [['Cirugía', 'no']]]] },
  labios: { t: 'Labios y mentón', q: 'Un buen resultado no cambia quién sos.', o: [
    [L('rellenos-con-acido-hialuronico', 'Labios'), 'Delineado y volumen con ácido hialurónico, a medida.', [['Tipo', 'Inyectable']]],
    [L('rellenos-con-acido-hialuronico', 'Mentón y líneas de marioneta'), 'Proyecta el mentón y suaviza las líneas que bajan de la comisura.', [['Tipo', 'Inyectable']]]] },
  contorno: { t: 'Papada y contorno', q: 'La clave no es solo reducir: es tratar la zona con criterio.', o: [
    [L('cirugia-laser', 'Endolift con Endoláser VELAS'), 'Grasa localizada, firmeza y definición mandibular, de forma mínimamente invasiva.', [['Láser', '1470 / 980 nm'], ['Cirugía tradicional', 'no']]],
    [L('lifting-facial-y-cervical', 'Lifting cervical'), 'Cuando hay más flacidez: recupera el ángulo del cuello y la línea de la mandíbula.', [['Tipo', 'Cirugía']]]] },
  cuello: { t: 'Cuello y rostro completo', q: 'Mi prioridad no es seguir una tendencia: es indicar lo que cada rostro necesita.', o: [
    [L('lifting-facial-y-cervical', 'Lifting Deep Plane'), 'Trabaja las estructuras profundas en lugar de estirar la piel.', [['Tipo', 'Cirugía'], ['Dejar de fumar', '1–2 semanas antes']]]] },
  orejas: { t: 'Orejas', q: 'En chicos, lo ideal es operar antes de empezar el colegio.', o: [
    [L('auriculoplastia', 'Otoplastia'), 'Orejas en asa o prominentes. Cicatriz escondida detrás de la oreja.', [['Duración', '90 min'], ['Alta', 'el mismo día']]]] },
  cuerpo: { t: 'Cuerpo y mamas', q: 'Siempre con una evaluación previa y expectativas reales.', o: [
    [L('implantes-mamarios', 'Implantes mamarios'), 'Gel de silicona de alta cohesividad, debajo del músculo.', [['Cirugía', '1 h'], ['Deporte', 'a los 30 días']]],
    [L('abdominoplastia', 'Abdominoplastia'), 'Saca piel y grasa sobrante y tensa los músculos.', [['Cirugía', '2 a 6 h']]],
    [L('lipoescultura', 'Lipoescultura'), 'Grasa localizada de varias zonas a la vez.', [['Resultado final', '3 meses']]]] },
};
const result = document.getElementById('guia-resultado');
function zone(k, scroll) {
  const z = ZONES[k]; if (!z || !result) return;
  const names = z.o.map(o => o[0].replace(/<[^>]+>/g, '')).join(', ');
  result.classList.remove('swap');
  result.innerHTML = `<h3 class="result__t">${z.t}</h3>` + z.o.map(([n, d, f]) => `<div class="opt"><h4>${n}</h4><p>${d}</p><dl>${f.map(([a, b]) => `<div><dt>${a}</dt><dd>${b}</dd></div>`).join('')}</dl></div>`).join('') +
    `<p class="say-q">«${z.q}»</p><a class="btn btn--glow" href="${wa(`Hola Dr. Corrado, me gustaría una evaluación por ${z.t.toLowerCase()} (${names}).`)}" target="_blank" rel="noopener">Consultar esto por WhatsApp <span class="btn__ic" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M3 8h9M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>`;
  void result.offsetWidth; result.classList.add('swap');
  $$('.guide .pill').forEach(p => p.setAttribute('aria-pressed', p.dataset.zone === k));
  $$('.guide .spot').forEach(s => s.classList.toggle('is-on', s.dataset.zone === k));
  if (scroll && innerWidth < 1100) result.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'nearest' });
}
$$('.guide .pill').forEach(p => p.addEventListener('click', () => zone(p.dataset.zone)));
$$('.guide .spot').forEach(s => s.addEventListener('click', () => zone(s.dataset.zone, true)));
if (result) zone('mirada');

/* ---------- antes / después ---------- */
$$('[data-ba]').forEach(ba => {
  const root = ba.dataset.root || '';
  const frame = ba.querySelector('.ba__frame'), range = ba.querySelector('.ba__range');
  const b = ba.querySelector('.ba__b'), a = ba.querySelector('.ba__a img'), cap = ba.querySelector('.ba__cap');
  range.addEventListener('input', () => frame.style.setProperty('--pos', range.value + '%'));
  ba.querySelectorAll('[data-case]').forEach(btn => btn.addEventListener('click', () => {
    const k = btn.dataset.case, n = btn.textContent.trim();
    frame.style.setProperty('--ratio', `${btn.dataset.w}/${btn.dataset.h}`);
    b.src = `${root}assets/img/antes-despues/${k}-antes.jpg`; a.src = `${root}assets/img/antes-despues/${k}-despues.jpg`;
    b.alt = `${n}, antes`; a.alt = `${n}, después`;
    cap.innerHTML = `<b>${n}</b><span>${btn.dataset.t}</span>`;
    range.value = 50; frame.style.setProperty('--pos', '50%');
    ba.querySelectorAll('[data-case]').forEach(x => x.setAttribute('aria-pressed', x === btn));
  }));
});

/* ---------- turnero → WhatsApp ---------- */
$$('[data-booker]').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(f);
  const sede = d.get('sede'), tr = d.get('trat');
  const num = sede === 'Nordelta' ? '5491135184999' : WA;
  const txt = `Hola Dr. Corrado, quisiera un turno en ${sede}, un ${d.get('dia')} ${d.get('hora')}${tr ? `, para consultar por ${tr.toLowerCase()}` : ''}.`;
  open(`https://wa.me/${num}?text=${encodeURIComponent(txt)}`, '_blank', 'noopener');
}));
$$('[data-contact]').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(f), err = f.querySelector('.err');
  const nombre = (d.get('nombre') || '').trim();
  if (!nombre) { err.hidden = false; f.querySelector('[name=nombre]').focus(); return; }
  err.hidden = true;
  const tr = d.get('trat'), msg = (d.get('msg') || '').trim();
  open(wa(`Hola Dr. Corrado, soy ${nombre}.${tr ? ` Quisiera consultar por ${tr.toLowerCase()}.` : ''}${msg ? ` ${msg}` : ''}`), '_blank', 'noopener');
}));

/* ---------- índice de la página (tratamientos) ---------- */
const tocLinks = $$('.toc a');
if (tocLinks.length) {
  const tio = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) tocLinks.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id));
  }), { rootMargin: '-30% 0px -60% 0px' });
  $$('.tsec[id]').forEach(s => tio.observe(s));
}

/* ---------- compartir ---------- */
$$('[data-share]').forEach(btn => btn.addEventListener('click', async () => {
  try {
    if (navigator.share) await navigator.share({ title: document.title, url: location.href });
    else { await navigator.clipboard.writeText(location.href); const t = btn.textContent; btn.textContent = 'Link copiado'; setTimeout(() => btn.textContent = t, 2200); }
  } catch (e) { /* cancelado */ }
}));

/* ---------- botón fijo en celular ---------- */
const dock = document.querySelector('.dock');
const first = document.querySelector('.hero, .phero');
if (dock && first) new IntersectionObserver(([e]) => dock.classList.toggle('show', !e.isIntersecting), { threshold: .05 }).observe(first);

/* ---------- entradas escalonadas ---------- */
const rio = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
$$('.sec__head, .tgrid > *, .why > li, .bento > *, .reviews > *, .qa, .counters__in > *, .tsec, .tl__i, .place, .doc__txt > *, .resumen .big, .tldr, .review-cta, .booker, .ft__cta > *').forEach((el, i, all) => {
  const sib = [...el.parentElement.children].indexOf(el);
  el.classList.add('rv'); el.style.setProperty('--d', `${Math.min(sib, 6) * 70}ms`); rio.observe(el);
});

/* ---------- "Pedir turno" abre el formulario ---------- */
const modal = document.getElementById('modal-turno');
if (modal && typeof modal.showModal === 'function') {
  let opener = null;
  $$('[data-turno]').forEach(btn => btn.addEventListener('click', e => {
    e.preventDefault(); opener = btn;
    hd.classList.remove('open'); menuBtn?.setAttribute('aria-expanded', 'false');
    const sel = modal.querySelector('select[name=trat]');
    if (sel) sel.value = btn.dataset.trat || '';
    modal.showModal();
    modal.querySelector('input:checked')?.focus();
  }));
  const close = () => { modal.close(); };
  modal.querySelector('[data-close]').addEventListener('click', close);
  modal.addEventListener('click', e => { if (e.target === modal) close(); });
  modal.addEventListener('close', () => opener?.focus());
  modal.querySelector('form').addEventListener('submit', () => setTimeout(close, 300));
}

/* ---------- atajos "¿Qué me preocupa realmente?" ---------- */
$$('.worry__b').forEach(b => b.addEventListener('click', () => {
  $$('.worry__b').forEach(x => x.setAttribute('aria-pressed', x === b));
  zone(b.dataset.zone, true);
  if (innerWidth >= 1100) document.querySelector('.guide__panel')?.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
}));

/* ---------- "¿Qué te gustaría mejorar?" plegado dentro de Tratamientos ---------- */
const guideSec = document.getElementById('guia');
const guideBtn = document.querySelector('[data-guide-toggle]');
function setGuide(open, scroll) {
  if (!guideSec || !guideBtn) return;
  guideSec.hidden = !open;
  guideBtn.setAttribute('aria-expanded', open);
  if (open && scroll) guideSec.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
}
guideBtn?.addEventListener('click', () => setGuide(guideSec.hidden, true));
$$('[data-guide-open], a[href="#guia"]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); setGuide(true, true); }));
if (location.hash === '#guia') setGuide(true, true);

/* ---------- compartir en redes (como el AddToAny de la web vieja) ---------- */
const shareText = () => `${document.title}`;
const NETS = {
  whatsapp: (u, t) => `https://wa.me/?text=${encodeURIComponent(t + ' ' + u)}`,
  facebook: (u) => `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(u)}`,
  x: (u, t) => `https://twitter.com/intent/tweet?url=${encodeURIComponent(u)}&text=${encodeURIComponent(t)}`,
  telegram: (u, t) => `https://t.me/share/url?url=${encodeURIComponent(u)}&text=${encodeURIComponent(t)}`,
  linkedin: (u) => `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(u)}`,
  pinterest: (u, t) => `https://pinterest.com/pin/create/button/?url=${encodeURIComponent(u)}&description=${encodeURIComponent(t)}`,
  email: (u, t) => `mailto:?subject=${encodeURIComponent(t)}&body=${encodeURIComponent(u)}`,
  recommend: (u) => `https://twitter.com/intent/tweet?text=${encodeURIComponent('Recomiendo al Dr. Gustavo Corrado, cirujano plástico en Belgrano y Nordelta (@gc.cirujanoplastico en Instagram).')}&url=${encodeURIComponent(u)}`,
  'recommend-wa': (u) => `https://wa.me/?text=${encodeURIComponent('Te paso el contacto del Dr. Gustavo Corrado, el cirujano plástico que te conté: ' + u)}`,
};
async function copyLink(btn) {
  try { await navigator.clipboard.writeText(location.href); } catch (e) { /* sin permiso */ }
  const ok = btn.closest('.sh')?.querySelector('.sh__ok');
  if (ok) { ok.hidden = false; setTimeout(() => ok.hidden = true, 2200); }
}
$$('[data-net]').forEach(b => b.addEventListener('click', async () => {
  const net = b.dataset.net, u = location.href.split('#')[0].split('?')[0], t = shareText();
  if (net === 'copy') return copyLink(b);
  if (net === 'more') {
    if (navigator.share) { try { await navigator.share({ title: t, url: u }); } catch (e) { /* cancelado */ } }
    else copyLink(b);
    return;
  }
  const url = NETS[net](u, t);
  if (net === 'email') location.href = url; else window.open(url, '_blank', 'noopener,width=640,height=560');
}));
