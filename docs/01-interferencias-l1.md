# Catálogo de interferencias L1: español latinoamericano → inglés

Este catálogo es la **fuente única de verdad** de los códigos `PRON-`, `GRAM-`, `VOC-` y `PRAG-` que usan las lecciones (campo `l1_focus`) y el currículo (`curriculum/syllabus.yml`). El validador (`tools/lessons.py`) lee las tablas de este archivo: si un código no aparece aquí, la lección no pasa la validación.

## Cómo usar este catálogo

- **Planear:** cada unidad del currículo declara sus focos L1; cada lección elige entre 3 y 7, y **al menos uno de pronunciación** (`PRON-`).
- **Corregir:** al dar retroalimentación, anota el código junto al error en la bitácora del aprendiz ([plantilla](../templates/speaking-log.md)). Así los errores recurrentes se vuelven visibles y medibles.
- **Priorizar:** la columna *Prioridad* refleja el impacto en la **inteligibilidad** y en la imagen comunicativa, no la distancia frente a un "acento nativo" (ver [03-pronunciacion.md](03-pronunciacion.md)).

### Reglas de mantenimiento

1. Los códigos **nunca se renumeran ni se reutilizan**. Si un código queda obsoleto, se marca como `(obsoleto)` en la columna *Fenómeno*.
2. Un código nuevo toma el siguiente número libre de su categoría.
3. Toda adición incluye un ejemplo real de error (✗), la forma meta (✓), la prioridad y una técnica sugerida.

### Leyenda de prioridad

- **Alta:** afecta la inteligibilidad o el significado, o tiene un riesgo social o profesional alto. Se trabaja desde A1–A2 y se recicla siempre.
- **Media:** se nota y puede causar malentendidos ocasionales. Se trabaja cuando aparece en la tarea.
- **Baja:** rara vez impide entender. Se trabaja en B2+ o si el aprendiz lo pide.

## Pronunciación (PRON)

El español tiene 5 vocales y un ritmo de base silábica; el inglés general americano (GA) tiene alrededor de 11 vocales simples más diptongos y un ritmo de base acentual con vocales reducidas. De ese contraste nace la mayoría de estas interferencias. Transcripciones según la convención de la [guía de estilo](05-guia-de-estilo.md).

| Código | Fenómeno | Error típico (✗) | Forma meta (✓) | Prioridad | Técnica sugerida |
|---|---|---|---|---|---|
| PRON-01 | Vocales /ɪ/ vs /iː/ | *ship* y *sheep*, *live* y *leave* suenan igual | ship /ʃɪp/ · sheep /ʃiːp/ | Alta | Pares mínimos; /ɪ/ corta y relajada, /iː/ larga y tensa (sonrisa) |
| PRON-02 | Vocales /æ/, /ʌ/, /ɑː/ (todas suenan como la *a* española) | *cat*, *cut* y *cot* suenan igual | cat /kæt/ · cut /kʌt/ · cot /kɑːt/ | Media | Pares mínimos; /æ/ con boca muy abierta y lengua adelante; /ʌ/ corta y central |
| PRON-03 | Schwa /ə/ y reducción de vocales átonas | *banana* con tres *a* plenas; *chocolate* con cuatro sílabas | banana /bəˈnænə/ · chocolate /ˈtʃɑːklət/ | Media | Marcar la sílaba tónica y "aplastar" las demás; banda elástica |
| PRON-04 | Vocales /ʊ/ vs /uː/ | *full* = *fool*, *pull* = *pool* | full /fʊl/ · fool /fuːl/ | Media | Pares mínimos; /ʊ/ corta y con labios poco redondeados |
| PRON-05 | Vocal epentética antes de *s* + consonante | *I espeak Espanish*, *estudent*, *escope* | speak /spiːk/ · Spanish /ˈspænɪʃ/ · scope /skoʊp/ | Media | "Serpiente": alargar la /sss/ y añadir la palabra (*ssss-peak*); enlazar con la palabra anterior |
| PRON-06 | /b/ vs /v/ | *very* = *berry*, *vote* = *boat* | very /ˈveri/ · berry /ˈberi/ | Media | Dientes superiores sobre el labio inferior para /v/; vibración audible |
| PRON-07 | /θ/ y /ð/ | *think* → *tink* o *sink*; *this* → *dis* | think /θɪŋk/ · this /ðɪs/ | Baja | Punta de la lengua entre los dientes; aceptar sustituciones inteligibles en A1–B1 |
| PRON-08 | /z/ sonora | *zoo*, *easy*, *is* con /s/ sorda | zoo /zuː/ · easy /ˈiːzi/ · is /ɪz/ | Media | Zumbido de abeja (*zzz*) con la mano en la garganta para sentir la vibración |
| PRON-09 | /ʃ/ vs /tʃ/ | *shoe* = *chew*, *wash* = *watch* | shoe /ʃuː/ · chew /tʃuː/ | Media | /ʃ/ continua como al pedir silencio (*shhh*); /tʃ/ con golpe inicial |
| PRON-10 | /dʒ/ vs /j/ | *yes* → *Jess*; *jet* = *yet*; *use* = *juice* | yes /jes/ · Jess /dʒes/ · juice /dʒuːs/ | Media | Pares mínimos; /j/ suave como la *i* de *hielo*; /dʒ/ con contacto de la lengua |
| PRON-11 | /h/ inglesa: suave (no jota fuerte) y no muda | *hello* con jota fuerte; *house* → *ouse*; *eat* por *heat* | hello /heˈloʊ/ · house /haʊs/ | Media | "Empañar un espejo" con el aliento; pares *hold/old*, *heat/eat* |
| PRON-12 | Consonantes finales y grupos consonánticos | *last* → *las*; *world* → *wor*; *asked* → *as* | last /læst/ · world /wɝːld/ · asked /æskt/ | Alta | Construir desde el final (*backchaining*); enlazar con la vocal siguiente |
| PRON-13 | Terminación -ed (/t/, /d/, /ɪd/) | *worked* → *work-ed*; o se omite y suena a presente | worked /wɝːkt/ · played /pleɪd/ · wanted /ˈwɑːntɪd/ | Alta | Clasificar en 3 grupos; /ɪd/ solo después de /t/ o /d/; enlazar (*worked‿a lot*) |
| PRON-14 | Terminación -s/-es (/s/, /z/, /ɪz/) | *works* → *work*; *dogs* con /s/; *watches* sin sílaba extra | works /wɝːks/ · dogs /dɑːgz/ · watches /ˈwɑːtʃɪz/ | Alta | Tres grupos como en -ed; no omitirla porque cambia el significado gramatical |
| PRON-15 | Nasales finales /m/, /n/, /ŋ/ | *some*, *sun* y *sung* suenan igual; *thing* → *thin* o *think* | some /sʌm/ · sun /sʌn/ · sung /sʌŋ/ | Media | Pares mínimos; cerrar los labios en /m/; /ŋ/ sin soltar una /g/ |
| PRON-16 | /r/ aproximante y vocales con r (/ɝː/, /ɚ/) | *work* = *walk*; *r* vibrante; *bird* con vocal española | work /wɝːk/ · walk /wɑːk/ · bird /bɝːd/ | Media | Lengua hacia atrás sin tocar el paladar; pares *work/walk*, *first/fast* |
| PRON-17 | Aspiración de /p/, /t/, /k/ iniciales | *pin* suena como *bin*; *time* como *dime* | pin [pʰɪn] · time [tʰaɪm] · coffee [ˈkʰɑːfi] | Alta | Prueba del papel o de la vela: debe moverse con /p t k/ iniciales |
| PRON-18 | Acento de palabra (sobre todo en cognados) | *comfortable* con acento en *-TA-*; *develop* con acento en *DE-*; *thirteen* = *thirty* | comfortable /ˈkʌmftɚbəl/ · develop /dɪˈveləp/ · thirteen /θɝːˈtiːn/ | Alta | Marcar la sílaba tónica en MAYÚSCULAS; golpear el ritmo; familias de palabras |
| PRON-19 | Acento de frase y acento nuclear o contrastivo | Todas las palabras con el mismo peso; no se resalta la información nueva | I said TUESDAY, not Thursday. | Alta | Subrayar la palabra con información nueva; diálogos de corrección contrastiva |
| PRON-20 | Ritmo acentual y formas débiles | *can* y *can't* indistinguibles; *to*, *for*, *of* pronunciados plenos | I can /kən/ swim · I can't /kænt/ swim | Media | Golpear el ritmo (palabras de contenido = golpe); *shadowing*; reconocer formas débiles primero |
| PRON-21 | Entonación (preguntas, cortesía, rango tonal) | Rango tonal plano que suena aburrido o cortante; preguntas *yes/no* sin subida | Could you help me? ↗ · Where do you work? ↘ | Media | Exagerar los contornos (tararear la frase); grabarse y comparar con el modelo |
| PRON-22 | Pronunciación guiada por la ortografía | *Wednesday* con tres sílabas; *island* con *s*; *-tion* como "-sión" | Wednesday /ˈwenzdeɪ/ · island /ˈaɪlənd/ · nation /ˈneɪʃən/ | Media | Lista personal de "palabras trampa"; consultar siempre el audio del diccionario |
| PRON-23 | Habla conectada: enlace, elisión y asimilación | No reconoce *gonna*, *wanna*, *didja*; separa cada palabra al hablar | going to → /ˈgʌnə/ · did you → /ˈdɪdʒə/ | Media | Primero receptivo (dictados), luego productivo; aprovechar la sinalefa del español |
| PRON-24 | Nombres de las letras del alfabeto | Deletrear *E, I, G, J, H, Y* "a la española" | E /iː/ · I /aɪ/ · G /dʒiː/ · J /dʒeɪ/ · H /eɪtʃ/ · Y /waɪ/ | Alta | Agrupar letras por sonido vocálico; deletrear nombres, correos y códigos |

## Gramática (GRAM)

| Código | Fenómeno | Error típico (✗) | Forma meta (✓) | Prioridad | Técnica sugerida |
|---|---|---|---|---|---|
| GRAM-01 | Omisión del sujeto (el español lo permite) | *Is raining.* *Is very good.* *Is tested by HPLC.* | It's raining. It's very good. It's tested by HPLC. | Alta | "Toda oración necesita sujeto": *it* y *there* como sujetos "vacíos" |
| GRAM-02 | *Have* para edad y estados físicos | *I have 30 years.* *I have hunger.* *You have reason.* | I'm 30. I'm hungry. You're right. | Alta | Tabla contrastiva *tener* → *be*; repetición en tareas de presentación |
| GRAM-03 | Preguntas sin auxiliar o sin inversión | *You like coffee?* *Where you live?* *What means "scope"?* | Do you like coffee? Where do you live? What does "scope" mean? | Alta | Fórmula QUASI (*Question word, Auxiliary, Subject, Infinitive*); transformación rápida |
| GRAM-04 | Negación con *no* y doble negación | *I no like it.* *I don't know nothing.* | I don't like it. I don't know anything. | Alta | Auxiliar + *not*; *any-* después de un negativo |
| GRAM-05 | Posición y concordancia del adjetivo | *a car red*; *differents options* | a red car; different options | Media | El adjetivo va antes del sustantivo y no lleva plural |
| GRAM-06 | Artículos: *the* genérico y omisión de *a/an* | *The life is hard.* *The people are friendly.* *I'm engineer.* | Life is hard. People are friendly. I'm an engineer. | Media | Generalizaciones sin *the*; profesiones con *a/an* |
| GRAM-07 | Sustantivos incontables y concordancia | *informations*, *advices*, *the people is* | information, advice, people are | Media | Lista de incontables frecuentes; *a piece of advice* |
| GRAM-08 | Duración: presente perfecto con *since/for* | *I live here since 2015.* *How much time do you work here?* | I've lived here since 2015. How long have you worked here? | Alta | Línea de tiempo pasado → presente; *How long have you...?* como bloque |
| GRAM-09 | Verbo + preposición calcados del español | *depend of*, *married with*, *arrive to*, *think in* | depend on, married to, arrive at/in, think about | Media | Aprender verbo + preposición como un solo bloque (*chunk*) |
| GRAM-10 | Infinitivo, gerundio y *for* + verbo | *I came for learn.* *I enjoy to dance.* | I came to learn. I enjoy dancing. | Media | Propósito = *to* + verbo; lista de verbos seguidos de *-ing* |
| GRAM-11 | Objeto indirecto con *explain*, *say*, *suggest* | *Can you explain me?* *She said me.* | Can you explain it to me? She told me. | Media | *explain/say something to someone*; *tell someone something* |
| GRAM-12 | *His/her* y pronombres para objetos | *My sister and his husband.* *The table... she is old.* | My sister and her husband. It's old. | Alta | El posesivo concuerda con el poseedor; las cosas son *it* |
| GRAM-13 | Posesión con *of* en lugar de *'s* | *the car of my brother* | my brother's car | Baja | *'s* para personas; *of* para cosas (*the name of the product*) |
| GRAM-14 | Futuro: *will*, *going to* y presente continuo | *I go to call you.* *Tomorrow I go to the doctor.* | I'm going to call you. I'm going to the doctor tomorrow. | Media | Planes = *going to* o presente continuo; *will* para decisiones del momento y promesas |
| GRAM-15 | Tercera persona *-s* | *She work in a lab.* *He don't know.* | She works in a lab. He doesn't know. | Media | Hacer audible la *-s* (ver PRON-14); autocorrección en grabaciones |
| GRAM-16 | Futuro o condicional en cláusulas de tiempo y de *if* | *When I will arrive, I call you.* *If I would know...* | When I arrive, I'll call you. If I knew... | Media | Contraste con el subjuntivo español: *cuando llegue* → *when I arrive* |
| GRAM-17 | Comparativos | *more big*, *more better*, *more easy* | bigger, better, easier | Media | Reglas por número de sílabas; irregulares como bloque |
| GRAM-18 | Posición de adverbios | *I go always to the gym.* *I like very much coffee.* | I always go to the gym. I like coffee very much. | Media | Frecuencia antes del verbo principal; nada entre verbo y objeto |
| GRAM-19 | *There is/are* y concordancia | *Is many people.* *There is many problems.* | There are many people. There are many problems. | Media | *There* + *be* que concuerda con lo que sigue |
| GRAM-20 | *Be born* | *I born in Cali.* | I was born in Cali. | Alta | Bloque fijo: *I was born in/on...* |

## Vocabulario y falsos amigos (VOC)

| Código | Fenómeno | Error típico (✗) | Forma meta (✓) | Prioridad | Técnica sugerida |
|---|---|---|---|---|---|
| VOC-01 | *actually* ≠ actualmente | *Actually I work in Bogotá* (queriendo decir "actualmente") | Currently / These days I work in Bogotá. (*actually* = en realidad) | Alta | Tarjeta de contraste; usar *currently* en presentaciones |
| VOC-02 | *embarrassed* ≠ embarazada | *She's embarrassed* (queriendo decir "embarazada") | She's pregnant. (*embarrassed* = avergonzado/a) | Alta | Historia breve con ambas palabras |
| VOC-03 | *library* ≠ librería | *I bought it at the library.* | I bought it at the bookstore. (*library* = biblioteca) | Media | Pares de imágenes |
| VOC-04 | *realize* ≠ realizar | *We realize the analysis every day.* | We carry out / perform / run the analysis every day. (*realize* = darse cuenta) | Alta | Banco de verbos: *carry out, perform, run, conduct* |
| VOC-05 | *assist* ≠ asistir | *I assisted a conference.* | I attended a conference. (*assist* = ayudar) | Media | *attend* + evento sin preposición |
| VOC-06 | *career* ≠ carrera universitaria | *I studied the career of chemistry.* | I studied chemistry. / My degree is in chemistry. (*career* = trayectoria profesional) | Media | Frases modelo para hablar de estudios |
| VOC-07 | *exit* ≠ éxito | *The project was an exit.* | The project was a success. (*exit* = salida) | Media | Tarjeta de contraste |
| VOC-08 | *sensible* ≠ sensible | *She's very sensible* (queriendo decir "sensible") | She's very sensitive. (*sensible* = sensato/a) | Media | Tarjeta de contraste |
| VOC-09 | *carpet* ≠ carpeta | *Put the documents in the carpet.* | Put the documents in the folder. (*carpet* = alfombra) | Media | Objetos reales de oficina |
| VOC-10 | *constipated* ≠ constipado | *I'm constipated* (queriendo decir "resfriado") | I have a cold. / I have a stuffy nose. (*constipated* = estreñido) | Alta | Diálogo en la farmacia o el médico |
| VOC-11 | *introduce* ≠ introducir | *Introduce the data in the system.* | Enter the data into the system. (*introduce* = presentar a alguien) | Media | *enter, insert, put in* según el objeto |
| VOC-12 | *lecture* ≠ lectura | *I love the lecture* (queriendo decir "leer") | I love reading. (*lecture* = conferencia o clase magistral) | Baja | Tarjeta de contraste |
| VOC-13 | *eventually* ≠ eventualmente | *Eventually we have problems* (queriendo decir "a veces") | Occasionally / Sometimes we have problems. (*eventually* = finalmente, con el tiempo) | Media | Línea de tiempo |
| VOC-14 | *attend* ≠ atender | *She attends the clients.* | She serves / helps / deals with the customers. | Media | Situaciones de servicio al cliente |
| VOC-15 | *make* vs *do* (hacer) | *make homework*, *do a mistake*, *do a party* | do homework, make a mistake, have a party | Media | Colocaciones en dos columnas |
| VOC-16 | *say*, *tell*, *speak*, *talk* (decir y hablar) | *She said me the truth.* *He talked me about it.* | She told me the truth. He told me about it. | Media | *tell* + persona; *say* + mensaje |
| VOC-17 | *borrow* vs *lend* (prestar) | *Can you borrow me your pen?* | Can you lend me your pen? / Can I borrow your pen? | Media | Dirección del objeto con flechas |
| VOC-18 | *large* ≠ largo | *a large road* (queriendo decir "larga") | a long road (*large* = grande) | Media | Tarjeta de contraste |
| VOC-19 | *discuss* ≠ discutir (pelear) | *We discussed and now we don't talk.* | We argued / had an argument. (*discuss* = hablar sobre un tema) | Media | Dos escenas: reunión vs pelea |
| VOC-20 | *molest* ≠ molestar | *Sorry to molest you.* | Sorry to bother you. (*molest* = abusar sexualmente: evitar siempre) | Alta | Alerta explícita desde A1 |
| VOC-21 | *compromise* ≠ compromiso | *We have a compromise with quality.* | We are committed to quality. / our commitment to quality (*compromise* = concesión, término medio) | Alta | Frases corporativas correctas |
| VOC-22 | *fabric* ≠ fábrica | *I work in a fabric.* | I work in a factory / plant. (*fabric* = tela) | Media | Tarjeta de contraste |
| VOC-23 | *parents* ≠ parientes | *All my parents came* (queriendo decir "parientes") | All my relatives came. (*parents* = papá y mamá) | Media | Árbol genealógico |
| VOC-24 | *success* ≠ suceso | *There was a success in the lab* (queriendo decir "incidente") | There was an incident in the lab. | Media | Tarjeta de contraste |
| VOC-25 | *advertise/advise* ≠ advertir | *I advertised him about the risk.* | I warned him about the risk. | Media | *warn someone about something* |
| VOC-26 | *pretend* ≠ pretender | *I pretend to finish this year.* | I intend / plan / hope to finish this year. (*pretend* = fingir) | Media | Tarjeta de contraste |
| VOC-27 | *billion* ≠ billón | *un billón* traducido como *one billion* | un billón (10¹²) = one trillion; one billion = mil millones (10⁹) | Alta | Tabla de magnitudes; dictado de cifras |
| VOC-28 | *college* ≠ colegio | *My son is in college* (queriendo decir "colegio") | My son is in high school. (*college* = educación superior) | Media | Línea del sistema educativo |
| VOC-29 | *remove* ≠ remover (revolver) | *Remove the coffee.* | Stir the coffee. (*remove* = quitar) | Baja | Instrucciones de receta |
| VOC-30 | *notice* ≠ noticia | *I have a good notice.* | I have some good news. (*notice* = aviso) | Media | *news* es incontable (ver GRAM-07) |
| VOC-31 | *control* ≠ controlar (verificar) | *I control the temperature every hour* (queriendo decir "revisar") | I check / monitor the temperature every hour. (*control* = regular, dominar) | Media | *check, monitor, verify, test* según el contexto |
| VOC-32 | *theme* ≠ tema | *What's the theme of the meeting?* | What's the topic of the meeting? / What's the issue? | Media | *topic, subject, issue, matter* |
| VOC-33 | *formation* ≠ formación | *I have formation in chemistry.* *formation records* | I have a background in chemistry. training records | Media | *training, education, background, degree* |

## Pragmática y discurso (PRAG)

| Código | Fenómeno | Error típico (✗) | Forma meta (✓) | Prioridad | Técnica sugerida |
|---|---|---|---|---|---|
| PRAG-01 | Peticiones demasiado directas | *Give me a coffee.* *I want the bill.* | Could I have a coffee, please? Could we have the check, please? | Alta | Escalera de cortesía: *Can I...? → Could I...? → Would it be possible to...?* |
| PRAG-02 | Muletillas del español | *eh...*, *este...*, *o sea*, *pues*, *bueno* | um..., well..., I mean..., let me think..., you know... | Media | Banco de frases para ganar tiempo; grabarse y contar muletillas |
| PRAG-03 | Toma de turnos y señales de escucha | Silencio total mientras el otro habla, o interrupción sin señal | Uh-huh. Right. Really? Sorry to interrupt, but... | Media | Escucha activa con 5 reacciones; frases para tomar y ceder el turno |
| PRAG-04 | Registro y tratamiento (no existe tú/usted) | Sonar brusco por falta de modales, o rígido por traducción literal | Cortesía con *could*, *would*, *please*; nombre de pila en contextos laborales informales | Media | Comparar versiones neutra, cortés e informal |
| PRAG-05 | Preguntas rituales (*How are you?*, *What's up?*) | Responder con un reporte completo o no devolver la pregunta | Good, thanks. And you? / Not much. You? | Media | Diálogos rituales cortos hasta automatizarlos |
| PRAG-06 | Atenuación en desacuerdos y negativas | *No. That is wrong.* *You are wrong.* | I see your point, but... I'm not sure that's the case. I'm afraid we can't... | Alta | Fórmulas de atenuación (*hedging*); "suavizar" frases directas |
| PRAG-07 | Títulos profesionales como tratamiento | *Good morning, Engineer Pérez.* *Doctor* para quien no es médico | Good morning, Mr. Pérez. / This is Ana Pérez, our QC Manager. | Media | Presentar a colegas con nombre + cargo |
| PRAG-08 | Fórmulas telefónicas y de reuniones virtuales | *Aló?* *With whom do I speak?* *Who speaks?* | Hello, this is Ana. May I ask who's calling? I think you're on mute. | Media | Guiones de llamada; práctica de deletreo (ver PRON-24) |
| PRAG-09 | Agradecer, disculparse y responder | *With pleasure* para todo; *Excuse me* tras un error; silencio ante *Thank you* | You're welcome. / No problem. / Sorry! / Excuse me (para llamar la atención o pasar) | Media | Minisituaciones de respuesta rápida |

## Variación regional

Latinoamérica no es un bloque homogéneo. Estas tendencias ayudan a **anticipar**, pero cada aprendiz se diagnostica con su propia grabación inicial ([04-evaluacion-speaking.md](04-evaluacion-speaking.md)).

| Región | Rasgo del español | Efecto típico en inglés | Códigos |
|---|---|---|---|
| México | Jota velar [x]; *s* final bien conservada | *hello* con fricción velar; ventaja en finales con -s | PRON-11 |
| Caribe, costas y parte de Centroamérica | Aspiración o pérdida de *s* final; *n* final velar; neutralización *r*/*l* en algunas zonas; jota como [h] | Omisión de -s y de consonantes finales; *sun* = *sung*; confusión *r*/*l* (ventaja: la /h/ ya existe) | PRON-12, PRON-14, PRON-15, PRON-16 |
| Colombia andina, Ecuador, Perú y Bolivia | *s* final conservada; *r* asibilada en algunas zonas; jota como [h] en Colombia | /r/ con fricción; ventaja en finales con -s | PRON-16 |
| Río de la Plata | *ll* y *y* como [ʃ] o [ʒ] | *yes* → *shes*, *yellow* → *shellow* (ventaja: /ʃ/ y /ʒ/ ya existen) | PRON-10, PRON-09 |
| Chile | /tʃ/ a veces como [ʃ]; aspiración de *s* | *chair* → *share*; omisión de -s | PRON-09, PRON-14 |

## Transferencias positivas (puentes desde el español)

No todo es interferencia. Estos sonidos ya existen en el español como variantes y sirven de **puente**:

- **[ð]** aparece entre vocales en *na**d**a* o *de**d**o*: es el sonido de *this* y *the*.
- **[ŋ]** aparece antes de /k/ y /g/ en *te**ng**o* o *ba**n**co*: es el final de *sing* y *thing*.
- **[z]** aparece antes de consonante sonora en *mi**s**mo* o *de**s**de*: es la /z/ de *is* y *easy*.
- **[ɾ]** (la *r* simple de *pero*) es la "t" de *water* o *better* en inglés americano.
- **La sinalefa** (*la‿amiga*) es la misma habilidad que el enlace en inglés (*an‿apple*).
- **/tʃ/** existe en casi todas las variedades (*mucho*): base para contrastar con /ʃ/.

## Referencias

- Coe, N. (2001). Speakers of Spanish and Catalan. En M. Swan y B. Smith (Eds.), *Learner English* (2.ª ed.). Cambridge University Press.
- Jenkins, J. (2000). *The Phonology of English as an International Language*. Oxford University Press.
- Levis, J. (2018). *Intelligibility, Oral Communication, and the Teaching of Pronunciation*. Cambridge University Press.
- Derwing, T. M. y Munro, M. J. (2015). *Pronunciation Fundamentals*. John Benjamins.
