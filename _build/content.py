# -*- coding: utf-8 -*-
"""Contenido del sitio del Dr. Gustavo Corrado.

Fuente: textos de su web actual (gustavo-corrado-cirujano-plastico.com, 2019)
y de sus posteos de Instagram (@gc.cirujanoplastico, 2026).
Lo marcado con A CONFIRMAR se lista al entregar.
"""

WA_MAIN = "5491126591809"       # link del bio de IG (wa.link/quqevv)
WA_NORDELTA = "5491135184999"   # "Nordelta: 11 3518-4999" en el bio

CATS = {
    "cirugia-plastica": {
        "name": "Cirugía plástica",
        "img": "cirugia-plastica",
        "title": "Cirugía plástica en Belgrano y Nordelta · Dr. Gustavo Corrado",
        "desc": "Blefaroplastia, lifting facial Deep Plane, otoplastia, implantes y reducción mamaria, abdominoplastia y lipoescultura con el Dr. Gustavo Corrado, MN 113095.",
        "h1": "Cirugía plástica",
        "lead": "Cirugías de rostro y de cuerpo. Cada indicación sale de una evaluación en consultorio, no de una tendencia.",
    },
    "medicina-estetica": {
        "name": "Medicina estética",
        "img": "medicina-estetica",
        "title": "Medicina estética: botox, ácido hialurónico y Radiesse · Dr. Corrado",
        "desc": "Toxina botulínica, rellenos con ácido hialurónico, Radiesse, plasma rico en plaquetas y Ultherapy en Belgrano y Nordelta.",
        "h1": "Medicina estética",
        "lead": "Tratamientos sin cirugía, con vuelta a la rutina en el día. Resultados naturales: que te vean descansada, no distinta.",
    },
    "otros-tratamientos": {
        "name": "Otros tratamientos",
        "img": "otros-tratamientos",
        "title": "Endoláser, cirugía láser y chip hormonal · Dr. Gustavo Corrado",
        "desc": "Endolift con Endoláser VELAS 1470/980 nm para papada y contorno, lipoláser y chip de testosterona. Dr. Gustavo Corrado, cirujano plástico.",
        "h1": "Otros tratamientos",
        "lead": "Láser y procedimientos mínimamente invasivos. Acá está lo más nuevo que hace el doctor.",
    },
}

T = []

def t(**kw):
    T.append(kw)

# ------------------------------------------------------------------ CIRUGÍA PLÁSTICA
t(slug="cirugia-de-parpados", cat="cirugia-plastica", name="Blefaroplastia", menu="Cirugía de párpados",
  img="blefaroplastia", img2="blefaroplastia-marcacion",
  short="Exceso de piel en los párpados superiores y bolsas en los inferiores. Una mirada descansada sin cambiar tu expresión.",
  title="Blefaroplastia en Belgrano y Nordelta · Cirugía de párpados · Dr. Corrado",
  desc="Blefaroplastia (cirugía de párpados) con el Dr. Gustavo Corrado: cuándo está indicada, cómo es y qué esperar. Turnos en Belgrano y Nordelta.",
  h1="Blefaroplastia", kicker="Cirugía de párpados",
  lead="Saca el exceso de piel y las bolsas de los párpados. Mi objetivo es una mirada más descansada y armónica, sin modificar la expresión natural del rostro.",
  facts=[("Tipo", "Cirugía"), ("Párpados", "Superiores, inferiores o ambos"), ("Suele indicarse", "Desde los 35 años"), ("Se combina con", "Lifting facial")],
  sections=[
    ("¿Cuándo está indicada?", [
      "Cuando hay exceso de piel en los párpados superiores o bolsas palpebrales que modifican el aspecto de la mirada. En algunos casos, además de lo estético, ese exceso de piel interfiere con el campo visual.",
      "La blefaroplastia no borra las patas de gallo ni levanta las cejas caídas. Para eso hay otros abordajes, y muchas veces se combinan.",
    ]),
    ("¿Quién es buen candidato?", [
      ("ul", ["Personas con buena salud general y expectativas realistas: se busca mejorar, no la perfección.",
              "Generalmente desde los 35 años, aunque con tendencia familiar a las bolsas se puede antes.",
              "Si tenés problemas de tiroides, ojo seco, presión alta, diabetes, glaucoma o desprendimiento de retina, se evalúa con más cuidado y a veces se pide un control oftalmológico previo."]),
    ]),
    ("Cómo la planifico", [
      "La indicación y la técnica se definen de manera personalizada después de una evaluación. Se puede hacer sola o junto con un lifting facial o frontal.",
      "Duración de la cirugía, tipo de anestesia y días de recuperación: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",  # A CONFIRMAR
    ]),
  ],
  faq=[("¿Me va a cambiar la cara?", "No. La idea es que la mirada se vea descansada manteniendo tu expresión."),
       ("¿Sirve para las patas de gallo?", "No. Para las arrugas del costado del ojo se usa toxina botulínica."),
       ("¿Se puede hacer junto con un lifting?", "Sí, es una combinación frecuente.")],
  related=["lifting-facial-y-cervical", "botox", "rellenos-con-acido-hialuronico"],
  confirm=["Duración, anestesia y recuperación de la blefaroplastia"])

t(slug="lifting-facial-y-cervical", cat="cirugia-plastica", name="Lifting facial y Deep Plane", menu="Lifting facial y cervical",
  img="lifting-deep-plane", img2="lifting-facial-cervical",
  short="Deep Plane y lifting cervicofacial: trabaja las estructuras profundas de la cara en lugar de estirar la piel.",
  title="Lifting facial Deep Plane y cervical en Buenos Aires · Dr. Gustavo Corrado",
  desc="Lifting Deep Plane y lifting facial y cervical con el Dr. Gustavo Corrado. Qué corrige, cómo se planifica y cuándo está indicado.",
  h1="Lifting facial y Deep Plane", kicker="Lifting facial y cervical",
  lead="No se trata de estirar la piel. El Deep Plane actúa sobre las estructuras profundas de la cara para lograr un rejuvenecimiento natural, respetando tu expresión y tu identidad.",
  facts=[("Tipo", "Cirugía"), ("Zonas", "Mejillas, surcos, mandíbula y cuello"), ("Dejar de fumar", "1 a 2 semanas antes"), ("Se combina con", "Blefaroplastia")],
  sections=[
    ("Qué corrige", [
      "Con los años, la gravedad, el sol y el estrés se notan en la cara: surcos profundos entre la nariz y la boca, mejillas que caen, grasa y arrugas en el cuello.",
      "El lifting no detiene ese proceso, pero sí lo atrasa: tensa los músculos, saca el exceso de grasa y redistribuye la piel de la cara y el cuello. El lifting cervical, además, recupera el ángulo del cuello, define el borde de la mandíbula y trata la papada.",
    ]),
    ("¿Deep Plane siempre?", [
      "El Deep Plane Facelift es la técnica de la que todos hablan. Pero mi prioridad no es seguir una tendencia: es indicar lo que cada rostro realmente necesita. Cada paciente es diferente, y la técnica también se elige de manera personalizada.",
    ]),
    ("Antes de la cirugía", [
      ("ul", ["Contame si fumás o tomás medicación, especialmente aspirina.",
              "Dejá de fumar al menos una o dos semanas antes.",
              "Si tenés el pelo corto, dejarlo crecer un poco ayuda a disimular las cicatrices mientras curan.",
              "Organizá que alguien te lleve a tu casa al alta y te acompañe los primeros días."]),
    ]),
  ],
  faq=[("¿El Deep Plane es siempre la mejor técnica?", "No siempre. Es una de las técnicas que más interés genera, pero se elige según lo que necesita cada rostro."),
       ("¿Voy a quedar con cara de estirada?", "La idea es la contraria: un buen resultado no cambia quién sos."),
       ("¿Se puede combinar con párpados?", "Sí, el lifting puede hacerse junto con una blefaroplastia.")],
  related=["cirugia-de-parpados", "cirugia-laser", "ultherapy"])

t(slug="auriculoplastia", cat="cirugia-plastica", name="Otoplastia", menu="Aurículoplastia",
  img="otoplastia",
  short="Orejas en asa o prominentes y asimetrías. Cicatriz escondida detrás de la oreja, alta el mismo día.",
  title="Otoplastia (cirugía de orejas) en niños y adultos · Dr. Gustavo Corrado",
  desc="Otoplastia o auriculoplastia para orejas en asa: duración, anestesia, postoperatorio y edad ideal en chicos. Dr. Gustavo Corrado.",
  h1="Otoplastia", kicker="Aurículoplastia · cirugía de orejas",
  lead="Corrige orejas en asa o prominentes, asimetrías y malformaciones. Te vas a tu casa el mismo día.",
  facts=[("Duración", "90 min aprox."), ("Alta", "El mismo día"), ("Vendas", "48 a 72 h"), ("Puntos", "Desde el día 7")],
  sections=[
    ("Qué se corrige", [
      ("ul", ["Ángulo aumentado entre la oreja y la cabeza (lo normal es 30–35°): las orejas «en asa».",
              "Exceso de cartílago en la concha de la oreja.",
              "Falta de pliegue en el tercio superior.",
              "Lóbulo hendido por el peso de los aros, queloides por piercings y lóbulos grandes."]),
    ]),
    ("¿Se puede operar a los chicos?", [
      "Sí. La oreja se desarrolla temprano, y las cargadas en el colegio pueden afectar la autoestima. Lo ideal es operar antes del ingreso escolar. En chicos se usa anestesia general; en adolescentes y adultos, anestesia local sola o con sedación.",
    ]),
    ("Cómo es la recuperación", [
      "El dolor suele ser leve y se maneja con analgésicos comunes. No hace falta reposo en cama. A las 48–72 h se sacan las vendas y ya te podés lavar el pelo. Conviene usar vincha elástica las primeras semanas, sobre todo para dormir, y evitar deportes de contacto durante el primer mes.",
    ]),
  ],
  faq=[("¿Cuánto dura la cirugía?", "En los casos estándar, unos 90 minutos."),
       ("¿Queda cicatriz visible?", "No: la incisión se hace por detrás, en el surco donde la oreja se une a la cabeza."),
       ("¿A qué edad conviene en chicos?", "Antes de empezar el colegio.")],
  related=["cirugia-de-parpados", "lifting-facial-y-cervical"])

t(slug="implantes-mamarios", cat="cirugia-plastica", name="Implantes mamarios", menu="Implantes mamarios",
  img="implantes-mamarios",
  short="Gel de silicona de alta cohesividad, en general debajo del músculo. Cirugía de una hora, internación de 6.",
  title="Implantes mamarios en Buenos Aires: cirugía y recuperación · Dr. Corrado",
  desc="Aumento mamario con implantes de gel de silicona de alta cohesividad: cirugía, incisión, recuperación y mitos. Dr. Gustavo Corrado, MN 113095.",
  h1="Implantes mamarios", kicker="Aumento mamario",
  lead="Para aumentar el volumen o recuperarlo después de la lactancia. De todas las cirugías plásticas, es la que da el cambio más rápido en la forma del cuerpo.",
  facts=[("Cirugía", "1 h aprox."), ("Internación", "Unas 6 h"), ("Manejar", "A los 7 días"), ("Deporte", "A los 30 días")],
  sections=[
    ("Los implantes", [
      "Tienen una cubierta de silicona flexible y hoy se rellenan con gel de silicona de alta cohesividad, lo que los hace muy confiables. Se colocan en un bolsillo debajo del músculo pectoral. La incisión puede ser en la areola, el surco submamario o la axila; la de elección es la areola.",
    ]),
    ("La recuperación, semana a semana", [
      ("ul", ["Vendaje elástico durante 48 h, hasta la primera curación.",
              "Corpiño las 24 horas durante dos semanas.",
              "Puntos: se sacan entre la 2.ª y la 3.ª semana.",
              "Manejar: a los 7 días. Deporte: a los 30.",
              "Nada de levantar peso durante 3 o 4 semanas.",
              "La forma final se ve alrededor de los 6 meses."]),
    ]),
    ("Mitos y verdades", [
      ("ul", ["Los estudios actuales muestran que los implantes de gel de silicona no producen cáncer ni enfermedades autoinmunes.",
              "No afectan la fertilidad, el embarazo ni la lactancia.",
              "La contractura capsular ronda el 2 %.",
              "Sí necesitan controles regulares y, cuando corresponde, estudios de imagen de las mamas."]),
    ]),
  ],
  faq=[("¿Afectan la lactancia?", "No hay evidencia de alteraciones en la fertilidad ni en la lactancia."),
       ("¿Dónde queda la cicatriz?", "Puede ser en la areola, el surco debajo de la mama o la axila. La de elección es la areola."),
       ("¿Se pierde sensibilidad?", "Puede haber cambios de sensibilidad en el pezón los primeros meses, que en general se van solos.")],
  related=["reduccion-mamaria", "lipoescultura", "abdominoplastia"])

t(slug="reduccion-mamaria", cat="cirugia-plastica", name="Reducción mamaria", menu="Reducción mamaria",
  img="reduccion-mamaria",
  short="Mamas más chicas, livianas y firmes. Alivia dolor de espalda y cuello. Vuelta al trabajo en 2 a 3 semanas.",
  title="Reducción mamaria (mamoplastia) en Buenos Aires · Dr. Gustavo Corrado",
  desc="Reducción mamaria: para quién es, cómo es la cirugía de 2 a 4 horas y la recuperación. Dr. Gustavo Corrado, cirujano plástico.",
  h1="Reducción mamaria", kicker="Mamoplastia de reducción",
  lead="Muchas veces se hace más por un problema físico que estético: dolor de espalda y de cuello, irritación debajo de la mama, actividades que se vuelven incómodas.",
  facts=[("Cirugía", "2 a 4 h"), ("Anestesia", "General"), ("Vida casi normal", "24 a 48 h"), ("Trabajo", "2 a 3 semanas")],
  sections=[
    ("Cómo se hace", [
      "Se saca el exceso de grasa, tejido mamario y piel, y se reubican la areola y el pezón. Las incisiones suelen tener forma de ancla: alrededor de la areola, vertical hacia abajo y en el surco submamario. A veces se suma una liposucción.",
    ]),
    ("Para planificarla, contame", [
      ("ul", ["Si fumás o tomás medicación o vitaminas.",
              "Cuántos embarazos tuviste y si pensás volver a quedar embarazada o dar de mamar.",
              "Qué tamaño y forma esperás: tus expectativas, con franqueza."]),
    ]),
    ("Después", [
      "Los puntos se sacan entre los 7 y 14 días y la hinchazón cede del todo entre las 3 y 6 semanas. Conviene evitar actividad física fuerte durante unas semanas.",
    ]),
  ],
  faq=[("¿Puedo dar de mamar después?", "No se recomienda si planeás amamantar; se conversa en la consulta."),
       ("¿Se pierde sensibilidad en el pezón?", "En general es temporal. En reducciones muy grandes puede ser definitiva.")],
  related=["implantes-mamarios", "abdominoplastia"])

t(slug="abdominoplastia", cat="cirugia-plastica", name="Abdominoplastia", menu="Abdominoplastia",
  img="abdominoplastia",
  short="Saca piel y grasa sobrante y tensa los músculos del abdomen. Muy pedida después de embarazos o grandes bajas de peso.",
  title="Abdominoplastia en Buenos Aires: tipos y recuperación · Dr. Gustavo Corrado",
  desc="Abdominoplastia tradicional, mini abdominoplastia y endoscópica: para quién es, cuánto dura y cómo es la recuperación. Dr. Corrado.",
  h1="Abdominoplastia", kicker="Cirugía de la pared abdominal",
  lead="Remodela abdomen, cintura y tronco: saca el exceso de piel y de grasa y tensa los músculos. No es un método para bajar de peso.",
  facts=[("Cirugía", "2 a 6 h"), ("Internación", "1 a 3 días"), ("Faja", "2 a 3 semanas"), ("Trabajo", "2 a 4 semanas")],
  sections=[
    ("¿Para quién es?", [
      "Para piel del abdomen más flácida y estirada de lo normal, algo muy frecuente después de uno o varios embarazos o de una gran baja de peso, cuando la piel ya no vuelve sola a su lugar.",
    ]),
    ("Tres formas de hacerla", [
      ("ul", ["Tradicional: anestesia general, incisión por encima del pubis, se trabaja el centro y los costados del abdomen.",
              "Mini abdominoplastia: cuando solo hay que tratar debajo del ombligo. Más corta y sencilla.",
              "Endoscópica: incisiones muy chicas guiadas por cámara."]),
      "Muchas veces se combina con una lipoescultura.",
    ]),
    ("Recuperación", [
      "Faja o prenda elástica las primeras dos o tres semanas. Sin ejercicio durante 4 a 6 semanas. Vuelta al trabajo entre la 2.ª y la 4.ª semana.",
    ]),
  ],
  faq=[("¿Es lo mismo que una lipo?", "No. La lipo saca grasa; la abdominoplastia saca piel sobrante y tensa los músculos. Se pueden combinar."),
       ("¿Sirve para adelgazar?", "No. Es una cirugía de contorno, no de pérdida de peso.")],
  related=["lipoescultura", "lipoescultura-laser", "implantes-mamarios"])

t(slug="lipoescultura", cat="cirugia-plastica", name="Lipoescultura", menu="Lipoescultura",
  img="lipoescultura",
  short="Aspira la grasa localizada de varias zonas a la vez para un contorno más armónico. Resultado final a los 3 meses.",
  title="Lipoescultura en Buenos Aires: zonas y recuperación · Dr. Gustavo Corrado",
  desc="Lipoescultura para grasa localizada que no baja con dieta ni ejercicio: cómo se hace, cuánto dura y cuándo se ve el resultado. Dr. Corrado.",
  h1="Lipoescultura", kicker="Contorno corporal",
  lead="Para los depósitos de grasa que no se van con dieta ni ejercicio. Se trabajan varias zonas en la misma cirugía para que el resultado sea proporcionado.",
  facts=[("Cirugía", "2 a 4 h"), ("Vida normal", "Desde el 2.º día"), ("Recuperado", "Al mes"), ("Resultado final", "A los 3 meses")],
  sections=[
    ("Cómo se hace", [
      "Se marcan las zonas, se infiltra una solución tumescente y se aspira la grasa con cánulas finas. Se toman fotos antes y después para comparar.",
    ]),
    ("Qué esperar", [
      ("ul", ["Las primeras 48 h sale líquido rosado por los poros: es normal.",
              "A la semana te sentís mucho mejor; a las 3 semanas los tejidos terminaron de cicatrizar.",
              "A las 48 h se ve el 70 % del resultado; el final, a los 3 meses."]),
    ]),
  ],
  faq=[("¿Reemplaza la dieta?", "No. Mejora el contorno, pero no sustituye una alimentación equilibrada y el ejercicio."),
       ("¿Qué zonas se tratan?", "Abdomen, cintura, flancos, piernas, brazos, espalda y papada, entre otras.")],
  related=["lipoescultura-laser", "abdominoplastia", "implantes-de-gluteos"])

t(slug="lipoescultura-laser", cat="cirugia-plastica", name="Lipoescultura láser", menu="Lipoescultura láser",
  img="lipoescultura-laser",
  short="El láser ablanda y licúa la grasa y ayuda a retraer la piel. Sin suturas, cicatrices mínimas.",
  title="Lipoláser (lipoescultura láser) en Buenos Aires · Dr. Gustavo Corrado",
  desc="Lipoescultura láser o lipolaser: menos traumática, más precisa y con retracción de piel. Zonas, duración y recuperación. Dr. Corrado.",
  h1="Lipoescultura láser", kicker="Lipoláser",
  lead="El láser ablanda y licúa la grasa antes de retirarla y ayuda a que la piel se retraiga. Es menos traumático para los tejidos que la liposucción tradicional.",
  facts=[("Procedimiento", "1 a 3 h"), ("Reposo", "5 días aprox."), ("Suturas", "No"), ("Zonas", "Abdomen, piernas, brazos, espalda, papada")],
  sections=[
    ("Por qué con láser", [
      "Permite moldear la grasa con más precisión y ayuda al estiramiento de la piel a medida que avanza el procedimiento. Los puntos de entrada cicatrizan en pocos días y no necesitan sutura.",
      "También sirve para la papada.",
    ]),
    ("Recuperación", [
      "Se recomienda reposo de unos 5 días, según la zona. Esos días puede hacer falta analgesia.",
    ]),
  ],
  faq=[("¿En qué se diferencia de la lipo común?", "El láser licúa la grasa y estimula la retracción de la piel; es menos traumático para los tejidos."),
       ("¿Se puede hacer en la papada?", "Sí. Para la papada también existe el Endolift con Endoláser.")],
  related=["cirugia-laser", "lipoescultura", "abdominoplastia"])

t(slug="implantes-de-gluteos", cat="cirugia-plastica", name="Implantes de glúteos", menu="Implantes de glúteos",
  img="implantes-de-gluteos",
  short="Implantes intramusculares aprobados por FDA y ANMAT, o tu propia grasa transferida. Dos horas de cirugía.",
  title="Implantes de glúteos y lipotransferencia · Dr. Gustavo Corrado",
  desc="Aumento de glúteos con implantes intramusculares o con tu propia grasa (lipotransferencia): cirugía y postoperatorio. Dr. Corrado.",
  h1="Implantes de glúteos", kicker="Aumento de glúteos",
  lead="Dos caminos: implantes de silicona en el músculo, o tu propia grasa sacada de cintura, caderas y abdomen e inyectada en los glúteos.",
  facts=[("Cirugía", "2 h aprox."), ("Anestesia", "Peridural + sedación"), ("Internación", "1 día"), ("Faja", "3 semanas")],
  sections=[
    ("Implantes o lipotransferencia", [
      ("ul", ["Implantes: técnica intramuscular, que asegura un resultado natural. Silicona de alta cohesividad, de marcas aprobadas por FDA y ANMAT.",
              "Lipotransferencia: lipoaspiración de cintura, caderas y abdomen e injerto de esa grasa en los glúteos, sin implantes."]),
    ]),
    ("Postoperatorio", [
      "Faja compresiva las tres primeras semanas. Después de la primera semana se retoma la rutina sin esfuerzos ni deporte, y entre la 5.ª y la 6.ª semana casi todas las actividades.",
    ]),
  ],
  faq=[("¿Qué anestesia se usa?", "Habitualmente peridural con una sedación suave; se define en la entrevista previa.")],
  related=["lipoescultura", "abdominoplastia"])

# ------------------------------------------------------------------ MEDICINA ESTÉTICA
t(slug="botox", cat="medicina-estetica", name="Toxina botulínica", menu="Botox",
  img="toxina-botulinica",
  short="Frente, entrecejo y patas de gallo. Dura de 4 a 6 meses y volvés a tu rutina en el momento.",
  title="Botox en Belgrano y Nordelta: frente, entrecejo y patas de gallo · Dr. Corrado",
  desc="Toxina botulínica (botox) para arrugas de expresión: frente, entrecejo, patas de gallo y levantamiento de cejas. Antes y después reales.",
  h1="Botox", kicker="Toxina botulínica",
  lead="Para las arrugas que aparecen al gesticular. Resultados naturales y sin reposo: volvés a tu vida en el momento.",
  facts=[("Dura", "4 a 6 meses"), ("Reposo", "No"), ("Zonas", "Frente, entrecejo, patas de gallo, cejas")],
  sections=[
    ("Cómo funciona", [
      "Se aplica toxina botulínica en el músculo que genera la arruga dinámica. El músculo se relaja y la piel de arriba deja de plegarse.",
      "Profesional muy serio y detallista, te hace lucir más joven con cambios que solo podés notar vos: así lo describió una paciente.",
    ]),
  ],
  cases=["entrecejo", "frente", "cejas", "patas-de-gallo"],
  faq=[("¿Cuánto dura?", "Entre 4 y 6 meses en la mayoría de los casos."),
       ("¿Se nota que me hice algo?", "La idea es que no: que te vean fresca y descansada."),
       ("¿Necesito reposo?", "No. Volvés a la rutina inmediatamente.")],
  related=["rellenos-con-acido-hialuronico", "relleno-con-radiesse", "cirugia-de-parpados"])

t(slug="rellenos-con-acido-hialuronico", cat="medicina-estetica", name="Ácido hialurónico", menu="Rellenos con ácido hialurónico",
  img="acido-hialuronico",
  short="Labios, surcos, valle de lágrimas, mentón, rinomodelación y Pointlift. Volumen natural, sin cirugía.",
  title="Rellenos con ácido hialurónico: labios, surcos y rinomodelación · Dr. Corrado",
  desc="Ácido hialurónico para labios, surco nasogeniano, valle de lágrimas, mentón, líneas de marioneta, rinomodelación y Pointlift. Antes y después reales.",
  h1="Ácido hialurónico", kicker="Rellenos faciales",
  lead="Un relleno inyectable que suaviza arrugas y líneas de expresión y devuelve volumen con un resultado natural.",
  facts=[("Tipo", "Inyectable"), ("Reposo", "No"), ("Dura", "Lorem ipsum")],  # A CONFIRMAR
  sections=[
    ("Dónde se aplica", [
      ("ul", ["Delineado y volumen de labios.",
              "Lifting Pointlift: puntos que levantan el tercio medio de la cara.",
              "Mentón y líneas de marioneta.",
              "Rinomodelación: dorso y punta de la nariz sin cirugía.",
              "Surco nasogeniano.",
              "Valle de lágrimas (la ojera hundida)."]),
    ]),
  ],
  cases=["labios", "lifting-pointlift", "lifting-pointlift-2", "menton-lineas-marioneta", "rinomodelacion", "surco-nasogeniano", "valle-de-lagrimas"],
  faq=[("¿Se puede combinar con Radiesse?", "Sí, se combinan de manera segura según la zona."),
       ("¿Cuánto dura?", "Lorem ipsum dolor sit amet.")],
  related=["botox", "relleno-con-radiesse", "plasma-rico-en-plaquetas"],
  confirm=["Duración habitual del ácido hialurónico"])

t(slug="relleno-con-radiesse", cat="medicina-estetica", name="Radiesse", menu="Relleno con Radiesse®",
  img="radiesse",
  short="Hidroxiapatita de calcio: volumen inmediato y estímulo de tu propio colágeno. Dura de 12 a 18 meses.",
  title="Radiesse: bioestimulador para flacidez, pómulos y mentón · Dr. Corrado",
  desc="Radiesse (hidroxiapatita de calcio) para flacidez, pómulos, mentón y rinomodelación. Dura de 12 a 18 meses. Dr. Gustavo Corrado.",
  h1="Radiesse", kicker="Relleno y bioestimulador",
  lead="Da volumen en el momento y, además, estimula la producción de tu propio colágeno durante los meses siguientes.",
  facts=[("Dura", "12 a 18 meses"), ("Sesiones", "Cada 4 semanas a 3 meses"), ("Prueba de alergia", "No hace falta")],
  sections=[
    ("Qué es", [
      "Microesferas de hidroxiapatita de calcio en un gel suave. Con el tiempo el cuerpo absorbe el gel y metaboliza las microesferas, y queda el colágeno nuevo. Más de 5 millones de unidades se usaron en el mundo.",
    ]),
    ("Para qué lo uso", [
      ("ul", ["Flacidez de la piel (bioplastia).", "Pómulos y mentón.", "Rinomodelación."]),
    ]),
    ("Después", [
      "Lo más común es algo de hinchazón o un hematoma. No hace falta ningún cuidado especial: hielo si se inflama. No se masajea la zona.",
    ]),
  ],
  faq=[("¿Se combina con ácido hialurónico?", "Sí, de manera segura.")],
  related=["rellenos-con-acido-hialuronico", "ultherapy", "plasma-rico-en-plaquetas"])

t(slug="plasma-rico-en-plaquetas", cat="medicina-estetica", name="Plasma rico en plaquetas", menu="Plasma rico en plaquetas",
  img="plasma-rico-en-plaquetas",
  short="Con tu propia sangre centrifugada: más firmeza, luminosidad y mejor textura. 2 a 3 sesiones por año.",
  title="Plasma rico en plaquetas (PRP) facial y capilar · Dr. Gustavo Corrado",
  desc="Plasma rico en plaquetas para rostro, cuello, manos y cuero cabelludo: cómo es la sesión, cuántas hacen falta y cuidados. Dr. Corrado.",
  h1="Plasma rico en plaquetas", kicker="PRP",
  lead="El ingrediente principal es tu propia sangre: por eso no hay riesgo de alergia ni de incompatibilidad.",
  facts=[("Sesiones", "2 a 3 por año"), ("Zonas", "Rostro, cuello, manos, cuero cabelludo"), ("Después", "Protector solar")],
  sections=[
    ("Cómo es la sesión", [
      ("ul", ["Antes: historia clínica y análisis de sangre completo.",
              "Crema anestésica en la zona mientras se extrae sangre del brazo, como en un análisis.",
              "La sangre se centrifuga unos 20 minutos y se separa el plasma rico en plaquetas.",
              "Se aplica con pinchazos rápidos en 5 a 10 minutos."]),
      "Pueden quedar marcas de los pinchazos ese día: un poco de maquillaje las disimula.",
    ]),
    ("Para qué sirve", [
      "Mejora firmeza, luminosidad y textura, y suaviza arrugas finas. También se usa para manchas, secuelas de acné, estrías, cicatrices y para potenciar el crecimiento del pelo.",
    ]),
  ],
  faq=[("¿Cuántas sesiones necesito?", "En general, 2 a 3 por año; se puede combinar con otros tratamientos."),
       ("¿Se puede hacer en verano?", "Sí, en cualquier época, con protector solar después.")],
  related=["relleno-con-radiesse", "rellenos-con-acido-hialuronico", "ultherapy"])

t(slug="ultherapy", cat="medicina-estetica", name="Ultherapy", menu="Ultherapy®",
  img="ultherapy",
  short="Ultrasonido microfocalizado que levanta y tensa sin tocar la superficie de la piel. Sin reposo.",
  title="Ultherapy: lifting sin cirugía con ultrasonido · Dr. Gustavo Corrado",
  desc="Ultherapy usa ultrasonido para generar colágeno nuevo y levantar cejas, mandíbula y cuello sin cirugía. Para quién es y qué se siente.",
  h1="Ultherapy", kicker="Lifting con ultrasonido",
  lead="Ultrasonido que llega a las capas profundas de la piel sin alterar la superficie y dispara la producción de colágeno nuevo: un efecto lifting natural.",
  facts=[("Profundidad", "1 a 4,5 mm"), ("Temperatura", "65–70 °C focalizado"), ("Reposo", "No"), ("Ideal", "35 a 55 años")],
  sections=[
    ("¿Quién es candidato?", [
      ("ul", ["Flacidez leve a moderada, entre los 35 y 55 años.",
              "Más flacidez, pero sin querer o poder operarse.",
              "Cejas caídas, mejillas, mandíbula y cuello."]),
    ]),
    ("Qué se siente", [
      "Varía según cada persona. Puede haber una incomodidad momentánea mientras se libera la energía, más sobre zonas óseas como la frente y la mandíbula. Después podés volver a tus actividades en el momento.",
    ]),
    ("Ultherapy o láser", [
      "Los láseres suelen trabajar en la superficie (líneas finas, manchas). Ultherapy actúa en la capa profunda, hasta el músculo superficial de la cara y el cuello, y permite ver en la pantalla dónde se libera la energía.",
    ]),
  ],
  faq=[("¿Duele?", "Puede haber incomodidad momentánea; el umbral de dolor varía de persona a persona."),
       ("¿Necesito reposo?", "No. La inflamación o el enrojecimiento se van en horas.")],
  related=["cirugia-laser", "relleno-con-radiesse", "lifting-facial-y-cervical"])

# ------------------------------------------------------------------ OTROS
t(slug="cirugia-laser", cat="otros-tratamientos", name="Endolift · Endoláser VELAS", menu="Cirugía láser · Endolift",
  img="endolaser-endolift", img2="dr-endolaser-en-vivo-tono",
  short="Endoláser VELAS 1470/980 nm para papada, contorno mandibular y flacidez. Mínimamente invasivo.",
  title="Endolift con Endoláser VELAS: papada y contorno mandibular · Dr. Corrado",
  desc="Endolift con Endoláser VELAS 1470/980 nm para papada, flacidez y definición mandibular, sin cirugía tradicional. Dr. Gustavo Corrado, Belgrano y Nordelta.",
  h1="Endolift con Endoláser", kicker="Cirugía láser",
  lead="¿Es posible redefinir el rostro sin una cirugía tradicional? El Endoláser trata la flacidez, define el contorno mandibular y mejora la papada de forma mínimamente invasiva.",
  facts=[("Equipo", "Endoláser VELAS"), ("Longitudes de onda", "1470 / 980 nm"), ("Zonas", "Papada, mandíbula, flacidez"), ("Cirugía tradicional", "No")],
  sections=[
    ("La clave no es solo reducir", [
      "Es tratar la zona con criterio. En la consulta evalúo qué está generando esa pérdida de definición para saber si el Endolift es realmente la indicación adecuada o si hace falta otro abordaje.",
    ]),
    ("Para quién", [
      ("ul", ["Grasa localizada en la papada.", "Pérdida de firmeza de los tejidos.", "Falta de definición del contorno mandibular.", "También en pacientes jóvenes."]),
    ]),
    ("Lo enseño a otros médicos", [
      "Hago procedimientos en vivo con Endoláser VELAS en jornadas para médicos, como la VELAS Experience de Mendoza (30 de octubre de 2026), y di la charla «Rejuvenecimiento de precisión» en Masterhub 2026.",
    ]),
  ],
  video=("Mari se hizo un Endolifting con retracción de papada y lo contó en video.", "https://www.instagram.com/saffiro.tech/reel/DaqLONHxCnB/"),
  faq=[("¿Me va a doler?", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
       ("¿Me voy a poder ir sola a mi casa?", "Lorem ipsum dolor sit amet."),
       ("¿Voy a quedar muy hinchada?", "Lorem ipsum dolor sit amet, consectetur.")],
  related=["lipoescultura-laser", "ultherapy", "lifting-facial-y-cervical"],
  confirm=["Respuestas del reel de preguntas sobre Endolift (dolor, irse sola, hinchazón)"])

t(slug="chip-sexual", cat="otros-tratamientos", name="Chip hormonal", menu="Chip sexual",
  img="chip-sexual",
  short="Pellets de testosterona bioidéntica: 10 minutos, anestesia local, beneficios desde el día 10 y por 5 a 6 meses.",
  title="Chip hormonal de testosterona (pellets) · Dr. Gustavo Corrado",
  desc="Chip hormonal o pellets de testosterona bioidéntica para hombres y mujeres: cómo se coloca, cuánto dura y qué beneficios tiene.",
  h1="Chip hormonal", kicker="Pellets de testosterona",
  lead="Pellets de testosterona bioidéntica, de origen vegetal, que se liberan lenta y constantemente, imitando la fisiología del cuerpo.",
  facts=[("Colocación", "10 minutos"), ("Anestesia", "Local"), ("Incisión", "3 mm en la cadera"), ("Dura", "5 a 6 meses")],
  sections=[
    ("Beneficios descriptos", [
      ("ul", ["Más energía física y mental y mejor rendimiento sexual.",
              "En mujeres, alivio de síntomas de la menopausia, mejor sueño y densidad ósea.",
              "Los pellets no se sacan: se disuelven solos."]),
      "Requiere una evaluación adecuada antes de indicarlo. Dieta saludable, actividad física y suplementos son parte del tratamiento.",
    ]),
  ],
  faq=[("¿Cuándo se notan los efectos?", "Desde los diez días."), ("¿Hay que sacarlo?", "No, se disuelve solo.")],
  related=["plasma-rico-en-plaquetas"],
  confirm=["Si sigue ofreciendo el chip hormonal"])

BY_SLUG = {x["slug"]: x for x in T}

CASES = {
  "entrecejo": ("Entrecejo", "Toxina botulínica", 800, 859),
  "frente": ("Frente", "Toxina botulínica", 770, 889),
  "cejas": ("Levantamiento de cejas", "Toxina botulínica", 800, 584),
  "patas-de-gallo": ("Patas de gallo", "Toxina botulínica", 800, 889),
  "labios": ("Labios", "Ácido hialurónico", 800, 496),
  "lifting-pointlift": ("Pointlift", "Ácido hialurónico", 540, 602),
  "lifting-pointlift-2": ("Pointlift, otro caso", "Ácido hialurónico", 540, 555),
  "menton-lineas-marioneta": ("Mentón y marioneta", "Ácido hialurónico", 540, 378),
  "rinomodelacion": ("Rinomodelación", "Ácido hialurónico", 800, 496),
  "surco-nasogeniano": ("Surco nasogeniano", "Ácido hialurónico", 646, 710),
  "valle-de-lagrimas": ("Valle de lágrimas", "Ácido hialurónico", 800, 496),
}

REVIEWS = [
  ("María Victoria Núñez", "Profesional muy serio y detallista, te hace lucir más joven con cambios que solo podés notar vos porque sabés lo que te hizo. El resto de la gente te ve espléndida, con un rostro fresco e iluminado. ¡Gracias Gustavo!"),
  ("Andrea Fabiana Mazza", "El doctor es una excelente persona, excelente profesional, respetuoso y ama su profesión. Súper recomendable."),
  ("Mónica Soler", "El Dr. Gustavo Corrado es muy buen profesional y totalmente recomendable. Aparte es una excelente persona y su trato es muy cordial."),
  ("Lola Bredes", "El mejor de todos es poco, no solo como excelente profesional sino que también humanamente."),
  ("Flavia Spago", "Excelentes sus trabajos. Las pacientes que atiende en mi gabinete, felices de cómo lucen con sus tratamientos."),
]
FB_RATING = ("100 %", "10 opiniones en Facebook")

CV = [
  ("2004", "Médico", "Universidad Abierta Interamericana (UAI)"),
  ("2005–2009", "Residencia completa de Cirugía General", "Hospital Vélez Sarsfield"),
  ("2010–2013", "Especialidad en Cirugía Plástica", "Universidad del Salvador"),
  ("2010", "Rotación en IREP", "Cirugía reparadora en miembros"),
  ("2011", "Centro de Excelencia para la Asistencia de Quemaduras (CEPAQ)", "Hospital Alemán"),
  ("2012", "Cirugía Plástica Infantil", "Hospital de Niños Dr. Ricardo Gutiérrez"),
  ("2013", "Cirugía Plástica Infantil", "Hospital Garrahan"),
  ("Rotaciones", "Cirugía Maxilofacial y Cirugía Oncológica", "Instituto de Diagnóstico, Hospital Pirovano y Hospital María Curie"),
  ("2014–2015", "Equipo de Cirugía del Quemado y sus secuelas", "Hospital Alemán"),
  ("2019", "Miembro de la Sociedad de Cirugía Plástica de Buenos Aires", "SCPBA"),
  ("2026", "Disertante en Masterhub y VELAS Experience Mendoza", "Nuevo consultorio en Nordelta"),
  ("2027", "Disertante en BAAS Congress", "Buenos Aires"),
]

IG_USER = "gc.cirujanoplastico"
IG_URL = "https://www.instagram.com/gc.cirujanoplastico/"
IG_STATS = ("12,2 mil", "364")  # seguidores, publicaciones (16/10/2026)
# (imagen en assets/img/ig/, link del posteo, tipo, texto corto)
IG_POSTS = [
  ("nordelta", "p/DeaaXnPDhpS", "post", "Bienvenida al nuevo espacio de Nordelta"),
  ("masterhub", "p/Dd-BKwxh-mZ", "post", "Charla en Masterhub 2026, Hotel Hilton"),
  ("blefaroplastia-antes-despues", "reel/DccLk-_AEwH", "reel", "Blefaroplastia: antes y después"),
  ("deep-plane", "p/DcPLF7RGM2N", "post", "¿La técnica más conocida es siempre la mejor?"),
  ("endolaser-paciente-joven", "reel/DbWn9VKA4CN", "reel", "Endoláser en paciente joven"),
  ("testimonio-mari", "reel/DaqLONHxCnB", "reel", "Testimonio de Mari: Endolifting de papada"),
  ("que-me-preocupa", "p/DdW3csdmMeV", "post", "No necesitás llegar sabiendo qué elegir"),
  ("velas-mendoza", "p/DeNQc59BdeC", "post", "VELAS Experience Mendoza, 30 de octubre"),
]

# Historias destacadas del perfil (id, título, ícono)
IG_HIGHLIGHTS = [
  ("18206603998047509", "Celebrities", "star"),
  ("17972728336361330", "Testimonios", "chat"),
  ("18163009918129868", "Botox", "syringe"),
  ("18191071585032836", "Rinomodelación", "nose"),
  ("17868832699629389", "Contacto", "phone"),
]
