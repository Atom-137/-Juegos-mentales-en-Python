def guardar_datos(matrizdatos,usuario,puntostotales):

  archivo = open("datosUsuarios.txt","a")
  
  archivo.write("\n"+"Nombre del usuario: ")
  archivo.write(user+"\n")
  archivo.write("Notas obtenidas"+"\n")
  archivo.write(str(matrizdatos)+"\n")
  archivo.write("Obtuvo en total: \n")
  archivo.write(str(puntostotales)+" pts""\n")
  
  archivo.close()

resultado= int()
import random
def problemamatematico(frace, posicionf):
	fraces = [str() for ind0 in range(16)]
	fraces[0] = "En la nevera había 7 huevos y hemos cogido 4 para hacer una tortilla. ¿Cuántos huevos quedarán en la nevera?"
	fraces[1] = "En el armario de mi habitación tengo 6 camisas, 3 pantalones y 2 chaquetas. ¿Cuántas prendas tengo en total?"
	fraces[2] = "La mamá de José lo envió al mercado por 20 naranjas, sin embargo el pobre no se fijó, y la bolsa en la que las empacó estaba rota.  Si por el camino perdió 7 naranjas ¿con cuántas llegó a su casa?"
	fraces[3] = "Calcula cuántas luces tiene fundidas mi árbol de navidad si en total tiene 296 luces pero solo se encienden 177."
	fraces[4] = "En la estantería del salón de mi casa hay 336 libros en total colocados en 6 estantes. Sabiendo que cada estantería tiene el mismo número de libros, calcula cuántos libros hay en cada estantería."
	fraces[5] = "Un niño tenía 42 bolitas y ganó el doble de esta cantidad. ¿Cuántas bolitas tendrá ahora?"
	fraces[6] = "Cada día hago 4 problemas. Cuando termino la libreta cuento un centenar de problemas. ¿En cuántos días he hecho estos deberes?"
	fraces[7] = "Un niño mete 3 monedas en su hucha cada día. Cuando la llena encuentra 792 monedas. ¿Cuántos días tardó en llenarla?"
	# NIVEL 2
	fraces[8] = "Del gallinero he cogido 24 huevos por la mañana y 37 por la tarde. ¿Cuántos huevos he cogido en todo el día?"
	fraces[9] = "Ayer Tomás compró una camiseta de Q.15 y una mochila de Q.23, pero le hicieron un descuento y, en total, solo pagó Q.35. ¿Cuánto descuento le hicieron?"
	fraces[10] = "Un caracol quiere llegar a la copa de un árbol. Para hacerlo pasa el día entero subiendo  su tallo, pero en la noche descansa y su peso hace que caiga varios metros hacia el suelo.  Si en el día avanza 8 metros y en la noche retrocede 5 ¿al cabo de cuatro días completos, a cuantos metros estará del suelo?"
	fraces[11] = "El pirata Barba Plata me ha dicho que ha encontrado un tesoro en una isla desierta que tenía en total 3.000 monedas de oro repartidas por igual en 3 cofres. Además, en cada cofre había también 200 monedas de plata y el doble de monedas de bronce que de plata. ¿Cuántas monedas había en total en cada cofre?"
	fraces[12] = "En el parque de atracciones, nos hemos montado en La rueda loca, que es muy divertida. Nos ha dicho el vigilante que ha funcionado 40 veces y siempre llena, llevando 5 niños cada viaje. Otra atracción, El dragón púrpura, ha llevado 3 veces más niños que La rueda loca. ¿Cuántos niños se han montado en El dragón púrpura?"
	fraces[13] = "En una cesta había 52 huevos y se rompieron la cuarta parte. ¿Cuántos huevos quedaron útiles para la venta?"
	fraces[14] = "Desde Toledo, el autobús hasta el pueblo de Luis cuesta Q.177, justo 3 veces más que lo que cuesta ir hasta el pueblo de Marta. ¿Cuánto cuesta el autobús hasta el pueblo de Marta?"
	fraces[15] = "¿Cuántos minutos tardará en desalojarse un local con 1750 personas, si cada minuto salen 5?"
	resultado = fraces[posicionf-1]
	return resultado

def problemalogico(frace, posicionf):
	fraces = [str() for ind0 in range(16)]
	fraces[0] = "Si Ángela habla bajo que Rosa y Celia habla alto que Rosa, ¿habla Ángela alto o bajo que Celia??"
	fraces[1] = "Tenemos cuatro perros: un galgo, un dogo, un alano y un podenco. Éste último come más que el galgo; el alano come más que el galgo y menos que el dogo, pero éste come más que el podenco. ¿Cuál de los cuatro será más barato de mantener?"
	fraces[2] = "En una hilera de cuatro casas, los Brown viven al lado de los Smith pero no al lado de los Bruce. Si los Bruce no viven al lado de los Jones, ¿quiénes son los vecinos inmediatos de los Jones?"
	fraces[3] = "Completar la oración siguiente colocando palabras en los espacios: Ningún pobre es emperador, y algunos avaros son pobres: luego: algunos emperador no son... ."
	fraces[4] = "Tomás, Pedro, Jaime, Susana y Julia realizaron un test. Julia obtuvo mayor puntuación que Tomás, Jaime puntuó más bajo que Pedro pero más alto que Susana, y Pedro logró menos puntos que Tomás. ¿Quién obtuvo la puntuación más alta?"
	fraces[5] = "¿Sabes de alguna letrita, que si la vuelta le das, enseguida se convierte de consonante en vocal?"
	fraces[6] = "Tarta, pero no es la comida; Mu, pero no el sonido de la vaca; Do, pero no la nota musical ¿Qué es? "
	fraces[7] = "En Melilla hay tres,en Madrid ninguna, en Castilla, dos y en Galicia una. ¿quien soy?"
	# NIVEL 2
	fraces[8] = "De cuatro corredores de atletismo se sabe que C ha llegado inmediatamente detrás de B, y D ha llegado en medio de A y C. ¿Podría calcular el orden de llegada (ejemplo: a-b-c-d)?"
	fraces[9] = "Seis amigos desean pasar sus vacaciones juntos y deciden, cada dos, utilizar diferentes medios de transporte; sabemos que Alejandro no utiliza el carro ya que éste acompaña a Benito que no va en avión. Andrés viaja en avión. Si Carlos no va acompañado de Darío ni hace uso del avión, podría decirnos en qué medio de transporte llega a su destino Tomás."
	fraces[10] = "Cuando María preguntó a Mario si quería casarse con ella, este contestó: No estaría mintiendo si te dijera que no puedo no decirte que es imposible negarte que si creo que es verdadero que no deja de ser falso que no vayamos a casarnos. María se mareó. ¿Puede ayudarla diciéndola si Mario quiere o no quiere casarse(si-no)?"
	fraces[11] = "A lo largo de una carretera hay cuatro pueblos seguidos: los Rojos viven al lado de los Verdes pero no de los Grises; los Azules no viven al lado de los Grises. ¿Quiénes son pues los vecinos de los Grises?"
	fraces[12] = "El Padre de Ana tiene 4 hijas. Una se llama Ena, otra Ina y otra Ona. ¿Cómo se llama la otra hija?"
	fraces[13] = "Un caballo blanco entró en el Mar Negro. ¿Cómo salió?"
	fraces[14] = "Este banco está ocupado por un padre y por un hijo: El padre se llama Juan y el hijo ya te lo he dicho."
	fraces[15] = "Corren más que los minutos pero... nunca llegan los primeros!!! ¿qué son?"
	resultado = fraces[posicionf-1]
	return resultado

q = int()
men = int()
f = int()
user = str()
# matriz para las notas totales inicia con una fila y 3 columnas
filas = 10
filasnots = 10
# filas pra la matriz final
filasfi = 1
ocupado = 2
notas = [[str() for ind0 in range(3)] for ind1 in range(filas)]
puntajes = [int() for ind0 in range(filasnots)]
print("Bienvenido a MEGAMENTE ")
print("El juego que probara tu capacidad matemática y lógica")
print("Empecemos")
print("¿Como te llamas?")
# Guardar el nombre dle jugador
user = input()
print("Bienvenido ",user,"!")
print("¿Estas listo para aceptar los desafíos?")
print("1.SI               0. NO")
q = int(input())
# Evaluar si ingreso 1,2 o un numero diferente.
while q!=1 and q!=0:
  print("Esta no es una opcion válida debe ingresar 1 para SI y 2 para NO")
  q = int(input())
# vavariable para guardar el nombre del jugador
user = user
# Empezar el juego
# Declararaciones problemas logicos y matematicos
contador = int()
contadorerror = int()
contadorepeticion = int()
puntosgenerales = int()
nivel = int()
ale = int()
ale2 = int()
ale3 = int()
x = int()
r1 = int()
r2 = int()
r3 = int()
fracess = str()
op = str()
# Inicio del juego
if q==1:
  while True:
    print("MENÚ")
    print("1. Problemas matemáticos")
    print("2. Problemas lógicos")
    print("3. Completar serie numérica")
    print("4. Salir.")
    men = int(input())
    # Inicia el juego
    if men==1:
      # Declaraciones para Prblemas Matemáticos
      letra = [str() for ind0 in range(4)]
      letra[0] = "a"
      letra[1] = "b"
      letra[2] = "c"
      letra[3] = "d"
      respuestafrace = [str() for ind0 in range(16)]
      respuestafrace[0] = "3"
      respuestafrace[1] = "11"
      respuestafrace[2] = "13"
      respuestafrace[3] = "119"
      respuestafrace[4] = "56"
      respuestafrace[5] = "126"
      respuestafrace[6] = "25"
      respuestafrace[7] = "264"
      respuestafrace[8] = "61"
      respuestafrace[9] = "3"
      respuestafrace[10] = "12"
      respuestafrace[11] = "1600"
      respuestafrace[12] = "600"
      respuestafrace[13] = "39"
      respuestafrace[14] = "59"
      respuestafrace[15] = "350"
      # Problmeas matemáticos
      print("Genial ",user,"!")
      print("BIENVENIDO PROBLEMAS MATEMATICOS")
      print("INSTRUCCIONES: LEA CADA ENUNCIADO Y COLOQUE LA RESPUESTA CORRECTA")
      print("NIVEL 1")
      nivel = 1
      r1 = 99
      r2 = 98
      r3 = 97
      contadorespeticion = 0
      puntosgenerales = 0
      while nivel==1 and contador<3:
        contadorepeticion = contadorepeticion+1
        while True:# no hay 'repetir' en python
          ale3 = random.randint(1,8)
          if contadorepeticion==1:
            r1 = ale3
          if contadorepeticion==2:
            r2 = ale3
          if contadorepeticion==3:
            r3 = ale3
          if r1!=r2 and r2!=r3 and r3!=r1: break
        ale = random.randint(1,4)
        print(problemamatematico(resultado,ale3))
        for x in range(1,5):
          ale2 = random.randint(1,1000)
          if ale!=x:
            print(letra[x-1],".",ale2,"  ", end="")
          if ale==x:
            print(letra[x-1],".",respuestafrace[ale3-1],"  ", end="")
        op = input()
        if str.lower(op)==letra[ale-1]:
          contador = contador+1
          print(user," ESTA CORRECTO")
        else:
          print(user," ESTA INCORRECTO")
          contador = contador+1
          contadorerror = contadorerror+1
        if (nivel==1 and contador>2):
          nivel = 2
          if contadorerror>0:
            contador = contador-contadorerror
          if contador==2:
            puntosgenerales = puntosgenerales+3
            print(user," DEBES SEGUIR PRACTICANDO")
            print("HAZ OBTENIDO ",puntosgenerales," PUNTOS")
          if contador==3:
            puntosgenerales = puntosgenerales+5
            print("FELICIDADES ",user," NIVEL COMPLETO")
            print("HAZ OBTENIDO ",puntosgenerales," PUNTOS")
          if contador<2:
            print(user," DEBES SEGUIR PRACTICANDO, INICIA DE NUEVO")
            print("PRESIONA UNA TECLA, PARA COMENZAR")
            tecla = input()
            print("") # no hay forma directa de borrar la pantalla con Python estandar
            contador = 0
            contadorerror = 0
            nivel = 1
            puntosgenerales = 0
      print("Fin nivel 1")
      print("****")
      if ocupado==2:
        for fil in range(2,filas+1):
          for col in range(1,4):
            if col==1 and fil==2:
              notas[fil-1][col-1] = "PROBLEMAS MATEMATICOS"
              filasfi = filasfi+1
            if col==2 and fil==2:
              notas[fil-1][col-1] = "     NIVEL 1"
        ocupado = ocupado+1
        puntajes[0] = puntosgenerales
      else:
        for fil in range(ocupado,filas+1):
          for col in range(1,4):
            if col==1 and fil==ocupado:
              notas[fil-1][col-1] = "PROBLEMAS MATEMATICOS"
              filasfi = filasfi+1
            if col==2 and fil==ocupado:
              notas[fil-1][col-1] = "     NIVEL 1"
        puntajes[ocupado-2] = puntosgenerales
        ocupado = ocupado+1
      puntosgenerales = 0
      # 1 continuar 2 regresar al menu 0 salir del juego
      print("CONTINUAR 1.SI 2.Menu Principal 0.SALIR DEL JUEGO")
      salir = float(input())
      print("") # no hay forma directa de borrar la pantalla con Python estandar
      if salir==1:
        print("GENIAL ESTAS EN EL NIVEL 2 COMENCEMOS, PRESIONA UNA TECLA")
        tecla = input()
        print("") # no hay forma directa de borrar la pantalla con Python estandar
        contador = 3
        r1 = 99
        r2 = 98
        r3 = 97
        contadorepeticion = 0
        while nivel==2 and contador<6:
          contadorepeticion = contadorepeticion+1
          while True:# no hay 'repetir' en python
            ale3 = random.randint(9,16)
            if contadorepeticion==1:
              r1 = ale3
            if contadorepeticion==2:
              r2 = ale3
            if contadorepeticion==3:
              r3 = ale3
            if r1!=r2 and r2!=r3 and r3!=r1: break
          ale = random.randint(1,4)
          print(problemamatematico(resultado,ale3))
          for x in range(1,5):
            ale2 = random.randint(1,10000)
            if ale!=x:
              print(letra[x-1],".",ale2,"  ", end="")
            if ale==x:
              print(letra[x-1],".",respuestafrace[ale3-1],"  ", end="")
          op = input()
          if str.lower(op)==letra[ale-1]:
            contador = contador+1
            print(user," ESTA CORRECTO")
          else:
            print(user," ESTA INCORRECTO")
            contador = contador+1
            contadorerror = contadorerror+1
          if (nivel==2 and contador>5):
            nivel = 1
            if contadorerror>0:
              contador = contador-contadorerror
            if contador==4 or contador==5 and contadorerror>1:
              puntosgenerales = puntosgenerales+3
              print(user," DEBES SEGUIR PRACTICANDO")
              print("HAZ OBTENIDO ",puntosgenerales," PUNTOS")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              contador = 0
              nivel = 1.
              contadorerror = 0
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
            if contador>=5 and contadorerror<2:
              puntosgenerales = puntosgenerales+5
              print("SUPER ",user," NIVEL COMPLETO")
              print("HAZ OBTENIDO ",puntosgenerales," PUNTOS")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
              contador = 0
              nivel = 1
              contadorerror = 0
            if contador>1 and contador<4:
              print("HAZ OBTENIDO ",puntosgenerales," PUNTOS")
              print(user," DEBES SEGUIR PRACTICANDO, INICIA DE NUEVO")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
              contador = 0
              nivel = 1
              contadorerror = 0
        print("Fin nivel 2")
        print("****")
        if ocupado==2:
          for fil in range(2,filas+1):
            for col in range(1,4):
              if col==1 and fil==2:
                notas[fil-1][col-1] = "PROBLEMAS MATEMATICOS"
                filasfi = filasfi+1
              if col==2 and fil==2:
                notas[fil-1][col-1] = "     NIVEL 2"
          ocupado = ocupado+1
          puntajes[1] = puntosgenerales
        else:
          for fil in range(ocupado,filas+1):
            for col in range(1,4):
              if col==1 and fil==ocupado:
                notas[fil-1][col-1] = "PROBLEMAS MATEMATICOS"
                filasfi = filasfi+1
              if col==2 and fil==ocupado:
                notas[fil-1][col-1] = "     NIVEL 2"
          puntajes[ocupado-2] = puntosgenerales
          ocupado = ocupado+1
        puntajes[1] = puntosgenerales
        print("Feilicidades, has completado todos los niveles.")
        print("Menu Principal, presiona una tecla")
        tecla = input()
        print("") # no hay forma directa de borrar la pantalla con Python estandar
    elif men==2:
      # Problemas lógicos
      contado = int()
      contadorerro = int()
      contadorepeticio = int()
      puntosgenerale = int()
      nive = int()
      ale33 = int()
      k = int()
      r11 = int()
      r22 = int()
      r23 = int()
      opf = str()
      respuestafrac = [str() for ind0 in range(16)]
      respuestafrac[0] = "bajo"
      respuestafrac[1] = "galgo"
      respuestafrac[2] = "brown"
      respuestafrac[3] = "avaros"
      respuestafrac[4] = "julia"
      respuestafrac[5] = "n"
      respuestafrac[6] = "tartamudo"
      respuestafrac[7] = "l"
      respuestafrac[8] = "b-c-d-a"
      respuestafrac[9] = "carro"
      respuestafrac[10] = "si"
      respuestafrac[11] = "verdes"
      respuestafrac[12] = "ana"
      respuestafrac[13] = "mojado"
      respuestafrac[14] = "esteban"
      respuestafrac[15] = "segundos"
      print("BIENVENIDO PROBLEMAS LOGICOS")
      print("INSTRUCCIONES: LEA CADA ENUNCIADO Y ESCRIBA SOLO UNA PALABRA SEGUN LA RELACION DE CADA PREGUNTA")
      print("NIVEL 1")
      nive = 1
      r11 = 99
      r22 = 98
      r23 = 97
      contadorespeticion = 0
      puntosgenerale = 0
      while nive==1 and contado<3:
        contadorepeticio = contadorepeticio+1
        while True:# no hay 'repetir' en python
          ale33 = random.randint(1,8)
          if contadorepeticio==1:
            r11 = ale33
          if contadorepeticio==2:
            r22 = ale33
          if contadorepeticio==3:
            r23 = ale33
          if r11!=r22 and r22!=r23 and r23!=r11: break
        print(problemalogico(resultado,ale33))
        opf = input()
        if str.lower(opf)==respuestafrac[ale33-1]:
          contado = contado+1
          print(user," ESTA CORRECTO")
        else:
          print(user," ESTA INCORRECTO")
          contado = contado+1
          contadorerro = contadorerro+1
        if (nive==1 and contado>2):
          nive = 2
          if contadorerro>0:
            contado = contado-contadorerro
          if contado==2:
            puntosgenerale = puntosgenerale+3
            print(user," DEBES SEGUIR PRACTICANDO")
            print("HAZ OBTENIDO ",puntosgenerale," PUNTOS")
          if contado==3:
            puntosgenerale = puntosgenerale+5
            print("FELICIDADES ",user," NIVEL COMPLETO")
            print("HAZ OBTENIDO ",puntosgenerale," PUNTOS")
          if contado<2:
            print(user," DEBES SEGUIR PRACTICANDO, INICIA DE NUEVO")
            print("PRESIONA UNA TECLA, PARA COMENZAR")
            tecla = input()
            print("") # no hay forma directa de borrar la pantalla con Python estandar
            contado = 0
            contadorerro = 0
            nive = 1
            puntosgenerale = 0
            r11 = 99
            r22 = 98
            r23 = 97
            contadorespeticion = 0
      print("Fin nivel 1")
      print("**********")
      if ocupado==2:
        for fil in range(2,filas+1):
          for col in range(1,4):
            if col==1 and fil==2:
              notas[fil-1][col-1] = "PROBLEMAS LOGICOS"
              filasfi = filasfi+1
            if col==2 and fil==2:
              notas[fil-1][col-1] = "     NIVEL 1"
        ocupado = ocupado+1
        puntajes[0] = puntosgenerale
      else:
        for fil in range(ocupado,filas+1):
          for col in range(1,4):
            if col==1 and fil==ocupado:
              notas[fil-1][col-1] = "PROBLEMAS LOGICOS"
              filasfi = filasfi+1
            if col==2 and fil==ocupado:
              notas[fil-1][col-1] = "     NIVEL 1"
        puntajes[ocupado-2] = puntosgenerale
        ocupado = ocupado+1
      # 1 continuar 2 regresar al menu 0 salir del juego
      print("CONTINUAR 1.SI 2.Menu Principal 0.SALIR DEL JUEGO")
      salir = float(input())
      print("") # no hay forma directa de borrar la pantalla con Python estandar
      if salir==1:
        print("GENIAL ESTAS EN EL NIVEL 2 COMENCEMOS, PRESIONA UNA TECLA")
        tecla = input()
        print("") # no hay forma directa de borrar la pantalla con Python estandar
        contado = 3
        r11 = 99
        r22 = 98
        r23 = 97
        contadorepeticio = 0
        puntosgenerale = 0
        while nive==2 and contado<6:
          contadorepeticio = contadorepeticio+1
          while True:# no hay 'repetir' en python
            ale33 = random.randint(9,16)
            if contadorepeticio==1:
              r11 = ale33
            if contadorepeticio==2:
              r22 = ale33
            if contadorepeticio==3:
              r23 = ale33
            if r11!=r22 and r22!=r23 and r23!=r11: break
          print(problemalogico(resultado,ale33))
          opf = input()
          if str.lower(opf)==respuestafrac[ale33-1]:
            contado = contado+1
            print(user," ESTA CORRECTO")
          else:
            print(user," ESTA INCORRECTO")
            contado = contado+1
            contadorerro = contadorerro+1
          if (nive==2 and contado>5):
            nive = 1
            if contadorerro>0:
              contado = contado-contadorerro
            if contado==4 or contado==5 or contadorerro>2:
              puntosgenerale = puntosgenerale+3
              print(user,"DEBES SEGUIR PRACTICANDO")
              print("HAZ OBTENIDO ",puntosgenerale," PUNTOS")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              contado = 0
              nive = 1.
              contadorerro = 0
              r11 = 99
              r22 = 98
              r23 = 97
              contadorespeticio = 0
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
            if contado>=5 and contadorerro<2:
              puntosgenerale = puntosgenerale+5
              print("SUPER ",user," NIVEL COMPLETO")
              print("HAZ OBTENIDO ",puntosgenerale," PUNTOS")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
              contado = 0
              nive = 1
              contadorerro = 0
              r11 = 99
              r22 = 98
              r23 = 97
              contadorespeticio = 0
            if contado>1 and contado<4:
              print("HAZ OBTENIDO ",puntosgenerale," PUNTOS")
              print("NOMBRE DEL JUGA"," DEBES SEGUIR PRACTICANDO, INICIA DE NUEVO")
              print("PRESIONA UNA TECLA, PARA COMENZAR")
              tecla = input()
              print("") # no hay forma directa de borrar la pantalla con Python estandar
              contado = 0
              nive = 1
              contadorerro = 0
              r11 = 99
              r22 = 98
              r23 = 97
              contadorespeticio = 0
        print("Fin nivel 2")
        print("****")
        if ocupado==2:
          for fil in range(2,filas+1):
            for col in range(1,4):
              if col==1 and fil==2:
                notas[fil-1][col-1] = "PROBLEMAS LOGICOS"
                filasfi = filasfi+1
              if col==2 and fil==2:
                notas[fil-1][col-1] = "     NIVEL 2"
          ocupado = ocupado+1
          puntajes[0] = puntosgenerale
        else:
          for fil in range(ocupado,filas+1):
            for col in range(1,4):
              if col==1 and fil==ocupado:
                notas[fil-1][col-1] = "PROBLEMAS LOGICOS"
                filasfi = filasfi+1
              if col==2 and fil==ocupado:
                notas[fil-1][col-1] = "     NIVEL 2"
          print(ocupado)
          puntajes[ocupado-2] = puntosgenerale
          ocupado = ocupado+1
        print("Feilicidades, has completado todos los niveles.")
        print("Menu Principal, presiona una tecla")
        tecla = input()
        print("") # no hay forma directa de borrar la pantalla con Python estandar
    elif men==3:
      # completar serie numérica
      print("Hola ",user,"!")
      intentos = 1
      puntosnivel=0
      num_secreto = 50
      print("A continuacion debera resolver 3 ejercicios lógicos, ¡Puede avanzar con 2 correctas! ")
      print("Presione cualquier letra para continuar")
      letra_ingresada = input()
      print("") # no hay forma directa de borrar la pantalla con Python estandar
      print("Siguiendo el siguiente orden (10, 20, 30, 40...) ¿Cuál es el siguiente numero en continuar?")
      num_ingresado = int(input())
      while num_secreto!=num_ingresado and intentos>1:
        if num_secreto>num_ingresado:
          print("No")
        else:
          print("No")
        intentos = intentos-1
        print("Le quedan ",intentos," intentos:")
        num_ingresado = float(input())
      if num_ingresado==num_secreto:
        print("¡Exacto, Eres una máquina!")
      else:
        print("No acerto, siga con la siguiente")
      intentos = 1
      num_secreto = (3)
      print("Si tenemos los números (3,6,9,12,15,18,21...) ¿Son multiplos de?")
      num_ingresado = float(input())
      while num_secreto!=num_ingresado and intentos>1:
        if num_secreto>num_ingresado:
          print("No")
        else:
          print("No")
        intentos = intentos-1
        print("Le quedan ",intentos," intentos:")
        num_ingresado = float(input())
      if num_secreto==num_ingresado:
        print("¡Exacto! Sigue así.")
      else:
        print("No acerto, siga con la siguiente")
      intentos = 1
      num_secreto = (8)
      print("Si en una fiesta hay un pastel con 36 porciones y solo llegaron 28 personas ¿Cuantos pedazos de pastel sobran?")
      num_ingresado = float(input())
      while num_secreto!=num_ingresado and intentos>1:
        if num_secreto>num_ingresado:
          print("No")
        else:
          print("No")
        intentos = intentos-1
        print("Le quedan ",intentos," intentos:")
        num_ingresado = float(input())
      if num_secreto==num_ingresado:
        print(user,"¡Exacto, Ganaste! Haz obtenido 10 puntos")
        puntosnivel = 10
      else:
        
        print("Perdiste")
      print("Fin nivel 1")
      print("******")
      ocupado = ocupado
      if ocupado==2:
        for fil in range(2,filas+1):
          for col in range(1,4):
            if col==1 and fil==2:
              notas[fil-1][col-1] = "COMPLETAR SERIE NUMERICA"
              filasfi = filasfi+1
            if col==2 and fil==2:
              notas[fil-1][col-1] = "  NIVEL 1"
        ocupado = ocupado+1
        puntajes[0] = puntosnivel
      else:
        for fil in range(ocupado,filas+1):
          for col in range(1,4):
            if col==1 and fil==ocupado:
              notas[fil-1][col-1] = "COMPLETAR SERIE NUMERICA"
              filasfi = filasfi+1
            if col==2 and fil==ocupado:
              notas[fil-1][col-1] = "  NIVEL 1"
        puntajes[ocupado-2] = puntosnivel
        ocupado = ocupado+1
      # 1 continuar 2 regresar al menu 0 salir del juego
      print("CONTINUAR 1.SI 2.Menu Principal 0.SALIR DEL JUEGO")
      salir = float(input())
      print("") # no hay forma directa de borrar la pantalla con Python estandar
      if salir==1:
        print("Fin nivel 2")
        print("****")
        ocupado = ocupado
        if ocupado==2:
          for fil in range(2,filas+1):
            for col in range(1,4):
              if col==1 and fil==2:
                notas[fil-1][col-1] = "COMPLETAR SERIE NUMERICA"
                filasfi = filasfi+1
              if col==2 and fil==2:
                notas[fil-1][col-1] = "  NIVEL 2"
          ocupado = ocupado+1
          puntajes[0] = 10
        else:
          for fil in range(ocupado,filas+1):
            for col in range(1,4):
              if col==1 and fil==ocupado:
                notas[fil-1][col-1] = "COMPLETAR SERIE NUMERICA"
                filasfi = filasfi+1
              if col==2 and fil==ocupado:
                notas[fil-1][col-1] = "  NIVEL 2"
          puntajes[ocupado-2] = 10
          ocupado = ocupado+1
        print("Feilicidades, has completado todos los niveles.")
        print("Menu Principal, presiona una tecla")
        tecla = input()
        print("") # no hay forma directa de borrar la pantalla con Python estandar
    else:
      # salir
      salir = 0
    if salir==0: break
# Matriz para mostrar los datos
matrizmostrardatos = [[str() for ind0 in range(3)] for ind1 in range(filasfi)]
# Encabezado matriz.
i = 1
print("Estos son sus resultados")
print(" ")
for fi in range(1,2):
  for co in range(1,4):
    if co==1:
      matrizmostrardatos[fi-1][co-1] = "Nombre del nivel"
    elif co==2:
      matrizmostrardatos[fi-1][co-1] = "Nivel alcanzado"
    elif co==3:
      matrizmostrardatos[fi-1][co-1] = "Punteo"
# escribir encabezado
for fils in range(1,2):
  for cols in range(1,4):
    print(matrizmostrardatos[fils-1][cols-1],"          ", end="")
  print(" ")
# Mostrar matriz final con los datos 
for f in range(2,filasfi+1):
  for c in range(1,4):
    matrizmostrardatos[f-1][c-1] = notas[f-1][c-1]
    print(matrizmostrardatos[f-1][c-1],"     ", end="")
    if c==3:
      print("   ",puntajes[i-1]," pts")
      i = i+1
  print(" ")
# SUMAR CALIFICACIONES
total = 0
for i in range(1,filasnots+1):
  total = total+puntajes[i-1]
# Salir
print("En total obtuviste ")
print(total," pts")
print(user,"! Felicidades por haber completado todos los desafíos")
print("Eres un buen jugador")
print("Vuelve pronto. Te esperamos")
print("*******")



guardar_datos(matrizmostrardatos,user,total)


