import os

x="""MENU PRINCIPAL
1- HOROSCOPO OCCIDENTAL
2- HOROSCOPO ORIENTAL

0- SALIR DEL PROGRAMA
"""
os.system('cls')
print(x)
opc=input("Ingrese una opción: ")
if not(opc.isnumeric()):
    pass
else:
    opc=int(opc)
while (opc!=0):
    if opc==1:
        os.system('cls')
        signo=""
        cont = 0
        for i in range(3):
            dia=input("Ingrese el dia de su nacimiento (1 a 31): ")
            if(dia.isnumeric()):
                dia =int(dia)
                if dia>0 and dia<32:
                    mes = input("Ingrese el mes de Nacimiento (1 a 12): ").upper()
                    
                    #if mes.isnumeric():
                        #mes=int(mes)
                    
                    if mes=="1" or mes=="2" or mes=="3" or mes=="4" or mes=="5" or mes=="6" or mes=="7" or mes=="8" or mes=="9" or mes=="10" or mes=="11" or mes=="12" or mes=="01" or mes=="02" or mes=="03" or mes=="04" or mes=="05" or mes=="06" or mes=="07" or mes=="08" or mes=="09" or mes=="010" or mes=="011" or mes=="012" or mes=="ENERO" or mes=="ENERO" or mes=="FEBRERO" or mes=="MARZO" or mes=="ABRIL" or mes=="MAYO" or mes=="JUNIO" or mes=="JULIO" or mes=="AGOSTO" or mes=="SEPTIEMBRE" or mes=="OCTUBRE" or mes=="NOVIEMBRE" or mes=="DICIEMBRE":
                        anio = input("Ingrese el año de nacimiento (formato -> 1999): ")
                        if anio.isnumeric():
                            anio=int(anio)
                            if anio<2025:
                                if dia==31 and (mes==4 or mes==6 or mes==9 or mes==11):
                                    print("Ingrese fecha valida")
                                elif dia>29 and mes=="2":
                                    print("Ingrese fecha valida")
                                elif dia==29 and mes=="2" and anio%4!=0:
                                    print("Ingrese fecha valida")
                                else:
                                    
                                    if (((mes=="2" or mes=="03") or mes=="FEBRERO") and (dia==29) and (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) ):
                                        print("Su signo es de Piscis. AÑO BISIESTO")
                                        print("Sí, Piscis tiende a ver el mundo a través de lentes de sol color de rosa, pero su alma romántica\nse basa en un profundo sentido de la intuición, la sensibilidad y la empatía que le ayudan a conectar\ncon la gente a un nivel más profundo, incluso más allá\nde lo que el mundo ve.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                                
                                    if ((mes=="3" or mes=="03" or mes=='MARZO' )and dia>20) or ((mes=="4" or mes=="04" or mes=='ABRIL') and dia<20):
                                        print("Su signo es de Aries.")
                                        print("Aries siempre esté dispuesto a lanzarse de cabeza a un desafío.\nEsta actitud positiva significa que ellos no dejan que los contratiempos de la vida\nlos paren durante mucho tiempo. Para ellos\nsiempre hay una nueva montaña que conquistar.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
    
                                    if ((mes=="4" or mes=="04" or mes=='ABRIL' ) and dia>19) or ((mes=="5"  or mes=="05" or mes=='MAYO') and dia<21):
                                        print("Su signo es de Tauro.")
                                        print("Como signo de tierra, el toro de la esfera zodiacal es conocido\npor mantener los pies muy bien puestos en el suelo, son personas prácticas y responsables.\nSon una constante en la vida de todos, este sentido\nde la fiabilidad es lo que ayuda a sus amigos recurran a ellos\ncuando las cosas se ponen difíciles.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                                        
                                    if ((mes=="5" or mes=="05" or  mes=="MAYO"  )and dia>20) or ((mes=="6"  or mes=="06" or mes=="JUNIO" )and dia<21):
                                        print("Su signo es de Géminis.")
                                        print("Las gemelas del zodiaco tienen una refrescante dualidad que les\nhace atraer a la gente como un imán. Inquisitivas, pero adaptables, juguetonas, pero sensibles,\n¡así eres tú, Géminis! Algunos podrían llamarte indecisa,\npero este sentido de la curiosidad por lo que el mundo tiene\n que ofrecerte significa que las cosas nunca serán\naburridas para ti.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
        
                                    if ((mes=="6"  or mes=="06" or mes=="JUNIO" )and dia>20) or ((mes=="7"  or mes=="07" or mes=="JULIO" )and dia<23):
                                        print("Su signo es de Cáncer.")
                                        print("Con un mundo emocional dictado por la pasión, la calidez y un espíritu afectuoso,\nun Cáncer es más leal que nadie. Es el signo más hogareño de la rueda zodiacal,\nsus seres queridos se sienten realmente en casa cuando están\njunto a ellos.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                                
                                    if ((mes=="7"  or mes=="07"  or mes=="JULIO" ) and dia>22) or ((mes=="8"  or mes=="08" or mes=="AGOSTO") and dia<23):
                                        print("Su signo es de Leo.")
                                        print("Extrovertidos, alegres y teatrales, ¡nadie podría acusar a Leo de sufrir por falta de confianza!\nEllos saben lo que quieren en la vida y no tienen reparos en conseguirlo.\nPuede que el mundo piense que les encanta ser el centro de atención,\npero es obvio que las cámaras los adoran.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                            
                                    if ((mes=="8"  or mes=="08" or mes=="AGOSTO" ) and dia>22) or ((mes=="9"  or mes=="09" or mes=="SEPTIEMBRE" ) and dia<23):
                                        print("Su signo es de Virgo.")
                                        print("Si quieres que algo se haga, llama a cualquiera. Pero si quieres algo bien hecho, llama a un Virgo.\nMetódicos, meticulosos y detallistas hasta el extremo. Si el mundo es un caos,\nestá claro que solo los de este signo lo pueden poner en orden.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                        
                                    if ((mes=="9"  or mes=="09" or mes=="SEPTIEMBRE" ) and dia>22) or ((mes=="10"  or mes=="10" or mes=="OCTUBRE") and dia<23):
                                        print("Su signo es de Libra.")
                                        print("La armonía y la paz ocupan un lugar destacado en la carta de presentación de tu signo del zodiaco, y con razón.\nSimbolizado por la balanza, son conocidos por el sentido de la equidad y\nla justicia, que los impulsan a establecer el equilibrio en todos\nlos aspectos de su vida.")
                                        os.system("pause")
                                        os.system('cls')
                                        break
                            
                                    if ((mes=="10"  or mes=="010" or mes=="OCTUBRE") and dia>22) or ((mes=="11"  or mes=="011" or mes=="NOVIEMBRE")and dia<22):
                                        print("Su signo es de Escorpio.")
                                        print("Entre los signos más incomprendidos del zodíaco. Muchos los ven como agresivos y conflictivos, pero en realidad\ntienen pasión por defender las causas perdidas. Su naturaleza profundamente\napasionada significa que nunca se rendirán sin luchar.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                            
                                    if ((mes=="11"  or mes=="011" or mes=="NOVIEMBRE")and dia>21) or ((mes=="12"  or mes=="012" or mes=="DICIEMBRE") and dia<22):
                                        print("Su signo es de Sagitario.")
                                        print("Como signo de fuego, tu búsqueda del conocimiento está destinada a llevarte a grandes lugares. Espíritu errante,\ntu personalidad inconformista no echa raíces fácilmente, no cuando todavía\nte queda un mundo por descubrir.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                                
                                    if ((mes=="12"  or mes=="012" or mes=="DICIEMBRE" )and dia>21) or ((mes=="1"  or mes=="01" or  mes=="ENERO" )and dia<20):
                                        print("Su signo es de Capricornio.")
                                        print("Metódicos, prácticos y decididos, los Capricornio no se detienen cuando tienen un objetivo en mente.\nA ellos no les gustan las charlas triviales ni los halagos vanidosos, por lo que su\ncírculo íntimo es pequeño pero muy leal.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                                
                                    if (((mes=="1" or mes=="01") or mes=="ENERO" )and dia>19) or ((mes=="2"  or mes=="02" or mes=="FEBRERO" )and dia<19):
                                        print("Su signo es de Acuario.")
                                        print("No se deje engañar por la palabra ‘acuario’. Este signo de aire no es de los que se atan a ideales arbitrarios.\nA riesgo de ganarse la reputación de distantes y distanciadas, este signo analítico\ne innovador prefiere situarse al margen de la multitud\nen lugar de seguiral rebaño.")
                                        os.system('pause')
                                        os.system('cls')
                                        break
                            
                                    if ((mes=="2"  or mes=="02" or mes=="FEBRERO" )and dia>18 and dia <=28) or ((mes=="3"  or mes=="03" or mes=="MARZO" )and dia<21):
                                        print("Su signo es de Piscis.")
                                        print("Sí, Piscis tiende a ver el mundo a través de lentes de sol color de rosa, pero su alma romántica\nse basa en un profundo sentido de la intuición, la sensibilidad y la empatía que le ayudan a conectar\ncon la gente a un nivel más profundo, incluso más allá\nde lo que el mundo ve.")
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
        else:
            print("Error. Ingreso un dato incorrecto")
            cont += 1
            os.system('pause')
            os.system('cls')
        if cont == 3:
            print("Lo siento ha agotado sus posibilidades")
            os.system('pause')
            os.system('cls')        
    print(x)
    opc=input("Ingrese una opción: ")
    if not(opc.isnumeric()):
        pass
    else:
        opc=int(opc)
else:
    os.system('cls') 
    print("¡Gracias por usar nuestro programa!")
           