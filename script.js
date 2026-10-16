/* Dr. Gustavo Corrado — interacciones */
document.documentElement.classList.add('js');

const WA_MAIN = '5491126591809';
const wa = (text) => `https://wa.me/${WA_MAIN}?text=${encodeURIComponent(text)}`;

/* ---------- menú mobile ---------- */
const bar = document.querySelector('.bar');
const menuBtn = document.querySelector('.bar__menu');
menuBtn.addEventListener('click', () => {
  const open = bar.classList.toggle('open');
  menuBtn.setAttribute('aria-expanded', open);
  menuBtn.textContent = open ? 'Cerrar' : 'Menú';
});
document.querySelectorAll('.bar__nav a').forEach(a => a.addEventListener('click', () => {
  bar.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); menuBtn.textContent = 'Menú';
}));

/* ---------- escenario fijo: cambia la foto según la sección ---------- */
document.querySelectorAll('[data-split]').forEach(split => {
  const imgs = split.querySelectorAll('.stage__frame img');
  const caps = split.querySelectorAll('.stage__cap');
  const show = (id) => {
    imgs.forEach(i => i.classList.toggle('is-on', i.dataset.for === id));
    caps.forEach(c => { c.hidden = c.dataset.capFor !== id; });
  };
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) show(e.target.dataset.stage); });
  }, { rootMargin: '-45% 0px -45% 0px' });
  split.querySelectorAll('[data-stage]').forEach(s => io.observe(s));
});

/* ---------- guía por zonas ---------- */
const ZONES = {
  mirada: {
    title: 'Párpados y mirada',
    say: 'Mi objetivo es una mirada más descansada y armónica, sin modificar la expresión natural del rostro.',
    opts: [
      { n: 'Blefaroplastia', d: 'Saca el exceso de piel de los párpados superiores y, según el caso, las bolsas de los inferiores. A veces ese exceso de piel también tapa parte del campo visual.',
        f: [['Tipo', 'Cirugía'], ['Suele indicarse', 'desde los 35 años'], ['Antes', 'a veces, control oftalmológico']] },
      { n: 'Valle de lágrimas', d: 'Ácido hialurónico para la ojera hundida, cuando no hace falta cirugía.',
        f: [['Tipo', 'Inyectable']] }
    ]
  },
  frente: {
    title: 'Frente y entrecejo',
    say: 'Se busca un resultado natural: que te vean descansada, no "hecha".',
    opts: [
      { n: 'Toxina botulínica', d: 'Para las arrugas que aparecen al gesticular: frente, entrecejo y patas de gallo. También levanta un poco la cola de la ceja.',
        f: [['Dura', '4 a 6 meses'], ['Vuelta a la rutina', 'en el momento']] },
      { n: 'Ultherapy', d: 'Ultrasonido que calienta las capas profundas sin tocar la superficie y estimula colágeno nuevo. Para cejas caídas y flacidez leve.',
        f: [['Reposo', 'no hace falta']] }
    ]
  },
  pomulos: {
    title: 'Pómulos y surcos',
    say: 'Cada paciente tiene un diagnóstico diferente. Por eso el primer paso siempre es la consulta.',
    opts: [
      { n: 'Ácido hialurónico', d: 'Surco nasogeniano, pómulos y la técnica Pointlift para levantar el tercio medio de la cara.',
        f: [['Tipo', 'Inyectable']] },
      { n: 'Radiesse', d: 'Hidroxiapatita de calcio: da volumen en el momento y además estimula tu propio colágeno. Muy usado para la flacidez.',
        f: [['Dura', '12 a 18 meses'], ['Sesiones', 'cada 4 semanas a 3 meses']] },
      { n: 'Plasma rico en plaquetas', d: 'Con tu propia sangre centrifugada. Mejora textura, firmeza y luminosidad de la piel.',
        f: [['Sesiones', '2 a 3 por año'], ['Después', 'protector solar']] }
    ]
  },
  nariz: {
    title: 'Nariz',
    say: 'No se trata de hacer más. Se trata de saber qué hacer, cuándo y por qué.',
    opts: [
      { n: 'Rinomodelación', d: 'Corrige el dorso o la punta con ácido hialurónico o Radiesse, sin cirugía.',
        f: [['Tipo', 'Inyectable'], ['Cirugía', 'no']] }
    ]
  },
  labios: {
    title: 'Labios y mentón',
    say: 'Un buen resultado no cambia quién sos.',
    opts: [
      { n: 'Delineado y volumen de labios', d: 'Ácido hialurónico para definir el contorno o dar volumen, a medida.',
        f: [['Tipo', 'Inyectable']] },
      { n: 'Mentón y líneas de marioneta', d: 'Ácido hialurónico para proyectar el mentón y suavizar las líneas que bajan desde la comisura.',
        f: [['Tipo', 'Inyectable']] }
    ]
  },
  contorno: {
    title: 'Papada y contorno',
    say: 'La clave no es solo reducir: es tratar la zona con criterio. Evalúo qué está generando esa pérdida de definición.',
    opts: [
      { n: 'Endolift con Endoláser VELAS', d: 'Mínimamente invasivo. Trabaja la grasa localizada, la firmeza de los tejidos y la definición del contorno mandibular.',
        f: [['Láser', '1470 / 980 nm'], ['Cirugía tradicional', 'no']] },
      { n: 'Lifting facial y cervical', d: 'Cuando hay más flacidez: reposiciona tejidos, define el ángulo del cuello y la línea de la mandíbula.',
        f: [['Tipo', 'Cirugía']] }
    ]
  },
  cuello: {
    title: 'Cuello y rostro completo',
    say: 'En cirugía facial mi prioridad no es seguir una tendencia: es indicar lo que cada rostro necesita.',
    opts: [
      { n: 'Lifting Deep Plane', d: 'Actúa sobre las estructuras profundas de la cara en lugar de estirar la piel, respetando la expresión.',
        f: [['Tipo', 'Cirugía'], ['Dejar de fumar', '1 a 2 semanas antes']] },
      { n: 'Lifting facial y cervical', d: 'Tensa músculos, saca el exceso de grasa y redistribuye la piel de la cara y el cuello. Se puede combinar con blefaroplastia.',
        f: [['Tipo', 'Cirugía']] }
    ]
  },
  orejas: {
    title: 'Orejas',
    say: 'Lo ideal en chicos es operar antes del ingreso escolar.',
    opts: [
      { n: 'Otoplastia', d: 'Corrige orejas en asa o prominentes y asimetrías. La cicatriz queda escondida detrás de la oreja.',
        f: [['Duración', '90 min aprox.'], ['Alta', 'el mismo día'], ['Vendas', '48 a 72 h']] }
    ]
  },
  cuerpo: {
    title: 'Cuerpo y mamas',
    say: 'Siempre con una evaluación médica previa y expectativas reales.',
    opts: [
      { n: 'Implantes mamarios', d: 'Gel de silicona de alta cohesividad, en general debajo del músculo pectoral.',
        f: [['Cirugía', '1 h aprox.'], ['Manejar', 'a los 7 días'], ['Deporte', 'a los 30 días']] },
      { n: 'Abdominoplastia', d: 'Saca el exceso de piel y grasa y tensa la pared abdominal. No es un método para bajar de peso.',
        f: [['Cirugía', '2 a 6 h'], ['Internación', '1 a 3 días'], ['Trabajo', '2 a 4 semanas']] },
      { n: 'Lipoescultura', d: 'Aspira grasa localizada de varias zonas para un contorno más armónico.',
        f: [['Cirugía', '2 a 4 h'], ['Resultado final', 'a los 3 meses']] },
      { n: 'Reducción mamaria e implantes de glúteos', d: 'Se evalúan en consulta según cada caso.',
        f: [['Reducción', '2 a 4 h'], ['Glúteos', '2 h aprox.']] }
    ]
  }
};

const result = document.getElementById('guia-resultado');
const chips = document.querySelectorAll('.chip');
const spots = document.querySelectorAll('.spot');
const esc = (s) => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function renderZone(key, focus) {
  const z = ZONES[key];
  if (!z) return;
  const opts = z.opts.map(o => `
    <div class="opt"><h4>${esc(o.n)}</h4><p>${esc(o.d)}</p>
      <dl>${o.f.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('')}</dl>
    </div>`).join('');
  const msg = `Hola Dr. Corrado, me gustaría una evaluación por ${z.title.toLowerCase()} (${z.opts.map(o => o.n).join(', ')}).`;
  result.classList.remove('swap');
  result.innerHTML = `<h3 class="result__title">${esc(z.title)}</h3>${opts}
    <p class="say">«${esc(z.say)}»</p>
    <a class="btn" href="${wa(msg)}" target="_blank" rel="noopener">Consultar esto por WhatsApp <span class="btn__arrow" aria-hidden="true">→</span></a>`;
  void result.offsetWidth;
  result.classList.add('swap');
  chips.forEach(c => c.setAttribute('aria-pressed', c.dataset.zone === key));
  spots.forEach(s => s.classList.toggle('is-on', s.dataset.zone === key));
  if (focus && window.matchMedia('(max-width: 1100px)').matches) {
    result.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}
chips.forEach(c => c.addEventListener('click', () => renderZone(c.dataset.zone, false)));
spots.forEach(s => s.addEventListener('click', () => renderZone(s.dataset.zone, true)));
renderZone('mirada', false);

/* ---------- antes / después ---------- */
const frame = document.getElementById('ba-frame');
const range = document.getElementById('ba-range');
const before = document.getElementById('ba-before');
const after = document.getElementById('ba-after');
const cap = document.getElementById('ba-cap');
range.addEventListener('input', () => frame.style.setProperty('--pos', range.value + '%'));
document.querySelectorAll('.case').forEach(b => b.addEventListener('click', () => {
  const k = b.dataset.case, name = b.textContent.trim();
  frame.style.setProperty('--ratio', `${b.dataset.w}/${b.dataset.h}`);
  before.src = `assets/img/antes-despues/${k}-antes.jpg`;
  after.src = `assets/img/antes-despues/${k}-despues.jpg`;
  [before, after].forEach(i => { i.width = b.dataset.w; i.height = b.dataset.h; });
  before.alt = `${name}, antes del tratamiento con ${b.dataset.t.toLowerCase()}`;
  after.alt = `${name}, después del tratamiento con ${b.dataset.t.toLowerCase()}`;
  cap.textContent = `${name} · ${b.dataset.t}`;
  range.value = 50; frame.style.setProperty('--pos', '50%');
  document.querySelectorAll('.case').forEach(x => x.setAttribute('aria-pressed', x === b));
}));

/* ---------- compartir ---------- */
document.querySelectorAll('[data-share]').forEach(btn => btn.addEventListener('click', async () => {
  const data = { title: 'Dr. Gustavo Corrado · Cirujano plástico', url: location.href };
  try {
    if (navigator.share) await navigator.share(data);
    else { await navigator.clipboard.writeText(location.href); btn.textContent = 'Link copiado'; setTimeout(() => btn.textContent = 'Compartir este sitio', 2200); }
  } catch (e) { /* cancelado */ }
}));

/* ---------- botón fijo en mobile: aparece después del hero ---------- */
const dock = document.querySelector('.dock');
const hero = document.getElementById('inicio');
new IntersectionObserver(([e]) => dock.classList.toggle('show', !e.isIntersecting), { threshold: 0.1 }).observe(hero);

/* ---------- entradas escalonadas ---------- */
const groups = document.querySelectorAll('.col > section:not(.hero), .menu, .slip-sec, .places, .faq, .foot__top');
groups.forEach(g => {
  const kids = g.matches('.menu, .slip-sec, .faq') ? g.children : g.querySelectorAll(':scope > *');
  [...kids].slice(0, 14).forEach((k, i) => { k.classList.add('rv'); k.style.setProperty('--d', `${Math.min(i, 8) * 70}ms`); });
});
const rio = new IntersectionObserver(entries => entries.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); }
}), { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.rv').forEach(el => rio.observe(el));
document.querySelectorAll('.sheet .row, .slip .row, .cv > div').forEach((r, i) => {
  r.classList.add('rv'); r.style.setProperty('--d', `${(i % 6) * 60}ms`); rio.observe(r);
});

/* ---------- la barra ocupa todo el ancho fuera de las zonas con foto fija ---------- */
const splitsAtTop = new Set();
const topIO = new IntersectionObserver(entries => {
  entries.forEach(e => e.isIntersecting ? splitsAtTop.add(e.target) : splitsAtTop.delete(e.target));
  bar.classList.toggle('wide', splitsAtTop.size === 0);
}, { rootMargin: '0px 0px -96% 0px' });
document.querySelectorAll('[data-split]').forEach(s => topIO.observe(s));
