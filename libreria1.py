import os
import random

# MENU PRINCIPAL INICIO

menuPrincipal = """
            ============================================
            ║            MENU PRINCIPAL                ║
            ║   -----------⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆-----------   ║
            ║       1 - HORÓSCOPO OCCIDENTAL 𑁍         ║
            ║       2 - HORÓSCOPO ORIENTAL ❀           ║
            ║                                          ║
            ║       0 - SALIR DEL PROGRAMA             ║
            ║   ---------ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ------------   ║
            ============================================
"""

# MENU PRINCIPAL FIN

# FRASES INICIO

# FRASES HORÓSCOPO OCCIDENTAL
frases_Aries= [ "Eres un pionero nato, impulsado por tu energía y valentía. Tu pasión por la vida te lleva a buscar nuevos desafíos, y tu capacidad para tomar la iniciativa inspira a quienes te rodean a seguir tu ejemplo.",
"Con un espíritu competitivo y una mentalidad audaz, no temes enfrentarte a lo desconocido. Tu capacidad para actuar rápidamente y confiar en tu instinto te permite superar obstáculos con facilidad.",
"A veces, tu impaciencia puede jugar en tu contra, pero esa misma determinación es lo que te impulsa a lograr tus objetivos. Recuerda que la paciencia también es una virtud que puede llevarte lejos."]

frases_Tauro= ["Con una profunda conexión a la estabilidad y la seguridad, valoras las cosas simples de la vida. Tu naturaleza persistente te lleva a trabajar arduamente para alcanzar tus metas, y tu lealtad a amigos y seres queridos es inquebrantable.",
"Eres una persona sensata, con un fuerte sentido estético que se refleja en tu entorno. Tu aprecio por la belleza y la comodidad hace que tu hogar sea un refugio, donde todos se sienten bienvenidos y en paz.",
"Tu determinación y paciencia son admirables, pero recuerda que a veces es bueno salir de tu zona de confort. Abrirte a nuevas experiencias puede traerte gratificaciones inesperadas."]

frases_Geminis= ["Eres una persona curiosa y versátil, siempre buscando aprender y experimentar cosas nuevas. Tu ingenio y habilidad para comunicarte te permiten conectar fácilmente con los demás, lo que te convierte en un gran conversador y amigo.",
"La dualidad de tu personalidad te permite ver las cosas desde diferentes ángulos, lo que te da una ventaja en situaciones sociales y profesionales. Sin embargo, a veces puedes sentirte indeciso; aprender a confiar en tus decisiones puede ser clave.",
"Tu adaptabilidad te ayuda a enfrentar cambios con facilidad, y tu deseo de libertad te impulsa a explorar diferentes caminos en la vida. No olvides tomarte un tiempo para reflexionar y encontrar un equilibrio en tu vida."]

frases_Cancer=["Con un profundo sentido de empatía, eres alguien que cuida y nutre a los que te rodean. Tu sensibilidad emocional te permite conectar con los demás a un nivel profundo, y tus amigos saben que siempre pueden contar contigo.",
"Eres protector de tu hogar y tus seres queridos, creando un ambiente cálido y acogedor. Tu intuición te guía en las relaciones, y a menudo eres capaz de percibir lo que otros sienten incluso sin que lo digan.",
"A veces, tu tendencia a ser demasiado sensible puede llevarte a cerrar la puerta ante nuevas experiencias. Aprende a confiar en tu fuerza interior y no temas abrirte a nuevas oportunidades."]

frases_Leo= ["Eres un líder natural, lleno de carisma y confianza en ti mismo. Tu entusiasmo y pasión por la vida son contagiosos, y a menudo inspiras a otros a perseguir sus sueños con la misma fervor que tú.",
"Tu creatividad brilla en todo lo que haces, desde tus proyectos personales hasta tus relaciones. Buscas ser el centro de atención, y tu habilidad para entretener y cautivar a los demás es incomparable.",
"Sin embargo, recuerda que la humildad también es importante. Aceptar y celebrar los logros de los demás fortalecerá tus relaciones y te permitirá crecer aún más como persona."]

frases_Virgo= ["Tu naturaleza analítica y perfeccionista te convierte en una persona muy eficiente y organizada. Eres un solucionador de problemas nato, siempre buscando mejorar y optimizar todo a tu alrededor.",
"La atención al detalle que posees es admirable; sin embargo, asegúrate de no ser demasiado crítico contigo mismo y con los demás. A veces, un poco de flexibilidad puede llevarte a nuevas oportunidades.",
"Tu deseo de ayudar a los demás es genuino, y a menudo te conviertes en el apoyo que tus amigos necesitan. Recuerda cuidar de ti mismo en el proceso; tu bienestar es igualmente importante."]

frases_Libra= ["Eres un buscador de la armonía y el equilibrio, y tu naturaleza diplomática te ayuda a mediar en conflictos y fomentar relaciones saludables. Valoras la justicia y la belleza en todas sus formas.",
"Con un gran sentido estético, tu entorno suele ser un reflejo de tu apreciación por lo bello. Tu capacidad para rodearte de personas afines te proporciona un círculo social vibrante y enriquecedor.",
"Sin embargo, tu deseo de complacer a los demás puede llevarte a la indecisión. Aprender a poner tus propias necesidades en primer lugar te permitirá encontrar un equilibrio más saludable en tus relaciones."]

frases_Escorpio= ["Eres una persona intensa y apasionada, capaz de profundizar en lo emocional. Tu naturaleza misteriosa atrae a los demás, y tus amistades suelen ser profundas y significativas.",
"Tu determinación y capacidad para transformar situaciones difíciles en oportunidades son admirables. No temes enfrentar tus miedos, lo que te convierte en una persona fuerte y resiliente.",
"Sin embargo, tu tendencia a guardar rencor puede ser un obstáculo. Aprender a soltar y perdonar te liberará y permitirá que tus relaciones florezcan aún más."]

frases_Sagitario= ["Eres un aventurero por naturaleza, siempre buscando nuevos horizontes y experiencias. Tu entusiasmo por la vida es contagioso, y a menudo inspiras a otros a seguir sus sueños.",
"Con un espíritu libre y optimista, disfrutas de la exploración, ya sea física, intelectual o espiritual. La filosofía y el aprendizaje continuo son esenciales para tu bienestar.",
"Sin embargo, tu deseo de libertad a veces puede hacerte sentir inquieto. Encuentra un equilibrio entre tu deseo de aventura y tus responsabilidades para lograr una vida plena."]

frases_Capricornio= ["Eres una persona trabajadora y ambiciosa, siempre enfocada en tus metas. Tu disciplina y sentido de responsabilidad te permiten lograr resultados, lo que te convierte en un pilar de apoyo para quienes te rodean.",
"Con un enfoque práctico y realista, planificas cuidadosamente cada paso que das. Tu capacidad para enfrentar desafíos con determinación es admirable y te lleva lejos en la vida.",
"Sin embargo, recuerda que el éxito no solo se mide en logros materiales. Tómate el tiempo para disfrutar de la vida y conectar con tus seres queridos; el equilibrio es clave para tu felicidad."]

frases_Acuario= ["Eres un innovador y un pensador independiente, siempre buscando romper moldes y desafiar las normas. Tu creatividad y originalidad te hacen destacar en cualquier grupo.",
"Con un fuerte sentido de justicia social, te importa el bienestar de los demás. Tus ideales y deseos de cambio positivo inspiran a quienes te rodean a actuar.",
"Sin embargo, a veces puedes ser un poco distante emocionalmente. Aprender a conectar más profundamente con los demás enriquecerá tus relaciones y te brindará una mayor satisfacción personal."]

frases_Piscis= ["Eres un soñador empedernido, con una profunda sensibilidad hacia el mundo que te rodea. Tu empatía y compasión te permiten conectar con los demás a un nivel emocional muy profundo.",
"Tu creatividad fluye a través de ti en diversas formas, desde el arte hasta la música y la escritura. Buscas expresar tus sentimientos y visiones de maneras únicas y auténticas.",
"Sin embargo, tu naturaleza sensible puede hacerte vulnerable a las influencias externas. Aprende a establecer límites y cuida de ti mismo; tu bienestar emocional es fundamental para tu felicidad."]

# FRASES HORÓSCOPO CHINO
frases_Rata = ["Eres ingenioso y adaptable, siempre encuentras soluciones rápidas a los problemas. Tu inteligencia te ayuda a ver oportunidades donde otros no ven nada.",    "Tienes una gran habilidad para hacer amigos, y tu naturaleza encantadora hace que los demás disfruten de tu compañía.",
"Tu ambición te lleva a trabajar duro, pero recuerda que también es importante relajarse y disfrutar el momento."]

frases_Buey = ["Eres persistente y confiable, una persona en la que todos pueden confiar para mantener la estabilidad.",
"Tu ética de trabajo es admirable, y sabes que los buenos resultados se logran con esfuerzo y paciencia.",
"A veces, puedes ser un poco terco, pero tu dedicación es lo que te permite alcanzar grandes logros."]

frases_Tigre = ["Tu valentía y espíritu independiente te convierten en un líder nato. No temes tomar riesgos para lograr lo que deseas.",
"La pasión que pones en todo lo que haces inspira a los demás a seguirte y te hace destacar.",
"A veces, tu impulsividad puede llevarte a actuar sin pensar, pero esa misma energía es la que te impulsa a grandes aventuras."]

frases_Conejo = ["Eres amable y empático, una persona que siempre busca ayudar a los demás y crear un ambiente de paz.",
"Tu sensibilidad te permite conectar profundamente con quienes te rodean, y eres un gran apoyo para tus amigos y seres queridos.",
"A veces, puedes ser un poco reservado, pero esa tranquilidad te ayuda a mantener la calma en situaciones difíciles."]

frases_Dragon = ["Tienes una presencia magnética y poderosa, y tu confianza en ti mismo inspira a quienes te rodean.",
"Eres ambicioso y no te detienes hasta alcanzar tus metas, siempre buscando llevar la vida al máximo.",
"A veces, puedes ser un poco dominante, pero tu energía y determinación son contagiosas y motivan a los demás."]

frases_Serpiente = ["Eres sabio y observador, una persona que siempre ve más allá de la superficie y analiza cada situación.",
"Tu calma y serenidad te dan una ventaja en situaciones complejas, ya que sabes cómo mantenerte tranquilo.",
"A veces, puedes ser reservado, pero tu intuición es una guía poderosa en tu vida."]

frases_Caballo = ["Eres libre y aventurero, siempre buscando nuevas experiencias y disfrutando de la vida al máximo.",
"Tu energía y optimismo contagian a los demás, y tienes una habilidad única para mantener la moral alta.",
"A veces, puedes ser un poco impaciente, pero tu espíritu alegre siempre te impulsa hacia adelante."]

frases_Cabra = ["Eres amable y considerado, siempre buscando armonía en tus relaciones y queriendo ayudar a quienes te rodean.",
"Tu creatividad es una gran fortaleza, y disfrutas de la belleza y la tranquilidad en la vida.",
"A veces, puedes ser un poco indeciso, pero tu naturaleza comprensiva siempre aporta paz a los demás."]

frases_Mono = ["Eres ingenioso y divertido, siempre encuentras una manera de alegrar el ambiente con tu sentido del humor.",
"Tu creatividad y adaptabilidad te ayudan a superar cualquier obstáculo, siempre encuentras soluciones innovadoras.",
"A veces, puedes ser un poco travieso, pero tu encanto natural hace que los demás te perdonen fácilmente."]

frases_Gallo = ["Eres organizado y detallista, siempre tienes un plan para todo y te aseguras de que todo esté en orden.",
"Tu honestidad y lealtad hacen que otros confíen en ti y busquen tu consejo.",
"A veces, puedes ser un poco perfeccionista, pero tu dedicación es lo que te lleva al éxito."]

frases_Perro = ["Eres leal y honesto, una persona en la que todos confían y acuden en busca de apoyo.",
"Tu sentido de justicia y tu empatía te llevan a defender a quienes amas y a cuidar de ellos.",
"A veces, puedes ser un poco desconfiado, pero tu compromiso con tus seres queridos es inquebrantable."]

frases_Cerdo = ["Eres generoso y bondadoso, siempre dispuesto a ayudar y a dar lo mejor de ti.",
"Tu amor por la vida y la buena compañía te hacen disfrutar de los momentos simples y agradables.",
"A veces, puedes ser un poco indulgente, pero tu naturaleza generosa es lo que te hace tan querido por los demás."]

# FRASES FIN

# FUNCIONES INICIO

def aries():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Aries.")
    print(random.choice(frases_Aries))
    os.system('pause')
    os.system('cls')
    return

def tauro():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Tauro.")
    print(random.choice(frases_Tauro))
    os.system('pause')
    os.system('cls')
    return

def geminis():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Géminis.")
    print(random.choice(frases_Geminis))
    os.system('pause')
    os.system('cls')
    return

def cancer():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Cáncer.")
    print(random.choice(frases_Cancer))
    os.system('pause')
    os.system('cls')
    return

def leo():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Leo.")
    print(random.choice(frases_Leo))
    os.system('pause')
    os.system('cls')
    return

def virgo():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Virgo.")
    print(random.choice(frases_Virgo))
    os.system('pause')
    os.system('cls')
    return

def libra():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Libra.")
    print(random.choice(frases_Libra))
    os.system("pause")
    os.system('cls')
    return

def escorpio():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Escorpio.")
    print(random.choice(frases_Escorpio))
    os.system('pause')
    os.system('cls')
    return

def sagitario():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Sagitario.")
    print(random.choice(frases_Sagitario))
    os.system('pause')
    os.system('cls')
    return

def capricornio():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Capricornio.")
    print(random.choice(frases_Capricornio))
    os.system('pause')
    os.system('cls')
    return

def acuario():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Acuario.")
    print(random.choice(frases_Acuario))
    os.system('pause')
    os.system('cls')
    return

def piscis():
    os.system('pause')
    os.system('cls')
    print("Su signo es de Piscis.")
    print(random.choice(frases_Piscis))
    os.system('pause')
    os.system('cls')
    return

# FUNCIONES FIN

# OPCIONES INICIO

def opc1():
    os.system('cls')
    # signo=""
    cont = 0
    for i in range(3):
        dia=input("Ingrese el dia de su nacimiento (1 a 31): ")
        if(dia.isnumeric()):
            dia =int(dia)
            if dia>0 and dia<32:
                mes = input("Ingrese el mes de Nacimiento (1 a 12): ")
                if mes.isnumeric():
                    mes=int(mes)
                    if mes>0 and mes<13:
                        anio = input("Ingrese el año de nacimiento (formato -> 1999): ")
                        if anio.isnumeric():
                            anio=int(anio)
                            if anio<2025:                                
                                if dia==31 and (mes==4 or mes==6 or mes==9 or mes==11):
                                    print("Ingrese fecha valida.")
                                    cont += 1
                                    os.system('pause')
                                    os.system('cls')
                                    
                                elif dia>29 and mes==2:
                                    print("Ingrese fecha valida")
                                    cont += 1
                                    os.system('pause')
                                    os.system('cls')
                                    
                                elif dia==29 and mes==2 and anio%4!=0:
                                    print("Ingrese fecha valida")
                                    cont += 1
                                    os.system('pause')
                                    os.system('cls')
                                else:
                                    if (mes==3 and dia>20) or (mes==4 and dia<20):
                                        aries()
                                        break
                                    if (mes==4 and dia>19) or (mes==5 and dia<21):
                                        tauro()
                                        break
                                    if (mes==5 and dia>20) or (mes==6 and dia<21):
                                        geminis()
                                        break
                                    if (mes==6 and dia>20) or (mes==7 and dia<23):
                                        cancer()
                                        break
                                    if (mes==7 and dia>22) or (mes==8 and dia<23):
                                        leo()
                                        break
                                    if (mes==8 and dia>22) or (mes==9 and dia<23):
                                        virgo()
                                        break
                                    if (mes==9 and dia>22) or (mes==10 and dia<23):
                                        libra()
                                        break
                                    if (mes==10 and dia>22) or (mes==11 and dia<22):
                                        escorpio()
                                        break
                                    if (mes==11 and dia>21) or (mes==12 and dia<22):
                                        sagitario()
                                        break
                                    if (mes==12 and dia>21) or (mes==1 and dia<20):
                                        capricornio()
                                        break
                                    if (mes==1 and dia>19) or (mes==2 and dia<19):
                                        acuario()
                                        break
                                    if (mes==2 and dia>18) or (mes==3 and dia<21):
                                        piscis()
                                        break
                            else:
                                print("Error. Ingreso un dato incorrecto")
                                cont += 1
                                os.system('pause')
                                os.system('cls')
                        else:
                            print("Error. Ingreso un dato incorrecto")
                            cont += 1
                            os.system('pause')
                            os.system('cls')
                    else:
                        print("Error. Ingreso un dato incorrecto")
                        cont += 1
                        os.system('pause')
                        os.system('cls')
                elif mes.isalpha():
                    mes=mes.capitalize()
                    anio = input("Ingrese el año de nacimiento (formato -> 1999): ")
                    if anio.isnumeric():
                        anio=int(anio)
                    if anio<2025:
                        meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"] 
                        if dia==31 and (mes==meses[3] or mes==meses[5] or mes==meses[8] or mes==meses[10]):
                            print("Ingrese fecha valida")
                            cont += 1
                            os.system('pause')
                            os.system('cls')
                        elif dia>29 and meses[1]:
                            print("Ingrese fecha valida")
                            cont += 1
                            os.system('pause')
                            os.system('cls')
                        elif dia==29 and meses[1] and anio%4!=0:
                            print("Ingrese fecha valida")
                            cont += 1
                            os.system('pause')
                            os.system('cls')
                        else:
                            if (mes==meses[2] and dia>20) or (mes==meses[3] and dia<20):
                                aries()
                                break
                            if (mes==meses[3] and dia>19) or (mes==meses[4] and dia<21):
                                tauro()
                                break
                            if (mes==meses[4] and dia>20) or (mes==meses[5] and dia<21):
                                geminis()
                                break
                            if (mes==meses[5] and dia>20) or (mes==meses[6] and dia<23):
                                cancer()
                                break
                            if (mes==meses[6] and dia>22) or (mes==meses[7] and dia<23):
                                leo()
                                break
                            if (mes==meses[7] and dia>22) or (mes==meses[8] and dia<23):
                                virgo()
                                break
                            if (mes==meses[8] and dia>22) or (mes==meses[9] and dia<23):
                                libra()
                                break
                            if (mes==meses[9] and dia>22) or (mes==meses[10] and dia<22):
                                escorpio()
                                break
                            if (mes==meses[10] and dia>21) or (mes==meses[11] and dia<22):
                                sagitario()
                                break
                            if (mes==meses[11] and dia>21) or (mes==meses[0] and dia<20):
                                capricornio()
                                break
                            if (mes==meses[0] and dia>19) or (mes==meses[1] and dia<19):
                                acuario()
                                break
                            if (mes==meses[1] and dia>18) or (mes==meses[2] and dia<21):
                                piscis()
                                break
                else:
                    print("Error. Ingreso un dato incorrecto")
                    cont += 1
                    os.system('pause')
                    os.system('cls')
            else:
                print("Error. Ingreso un dato incorrecto")
                cont += 1
                os.system('pause')
                os.system('cls')
        else:
            print("Error. Ingreso un dato incorrecto")
            cont += 1
            os.system('pause')
            os.system('cls')
        if cont == 3:
            print("Lo siento ha agotado sus posibilidades")
            os.system('pause')
            os.system('cls')
    return

def opc2():
    os.system('cls')
    animal=""
    cont = 0
    for i in range(3):            
        anio = input("Ingrese el año de nacimiento (formato -> 1999): ")
        if anio.isnumeric():
            anio=int(anio)
            if anio<2025:
                animales=["Rata","Buey","Tigre","Conejo","Dragón","Serpiente","Caballo","Cabra","Mono","Gallo","Perro","Cerdo"]
                ind=(anio-1924)%12
                animal=animales[ind]
                                    
                print(f"Tu animal del horoscopo chino es {animal}.")
                    
                if ind==0:
                    print(random.choice(frases_Rata))                    
                elif ind==1:
                    print(random.choice(frases_Buey))                    
                elif ind==2:
                    print(random.choice(frases_Tigre))                    
                elif ind==3:
                    print(random.choice(frases_Conejo))
                elif ind==4:
                    print(random.choice(frases_Dragon))
                elif ind==5:
                    print(random.choice(frases_Serpiente))                    
                elif ind==6:
                    print(random.choice(frases_Caballo))
                elif ind==7:
                    print(random.choice(frases_Cabra))
                elif ind==8:
                    print(random.choice(frases_Mono))
                elif ind==9:
                    print(random.choice(frases_Gallo))
                elif ind==10:
                    print(random.choice(frases_Perro))
                elif ind==11:
                    print(random.choice(frases_Cerdo))                                                
                os.system('pause')
                os.system('cls')
                break
            else:
                print("Error. Ingreso un dato incorrecto")
                cont += 1
                os.system('pause')
                os.system('cls')
        else:
            print("Error. Ingreso un dato incorrecto")
            cont += 1
            os.system('pause')
            os.system('cls')
        if cont == 3:
            print("Lo siento ha agotado sus posibilidades")
            os.system('pause')
            os.system('cls')
    return

# OPCIONES FIN