
from random import *
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo
    def __repr__(self):
        return f"{self.numero} de {self.palo}"
class Mano():
    def __init__(self, nombre, valor):
        self.cartas_de_mano = ConjuntoDeCartas()
        self.nombre = nombre
        self.valor = valor
        self.estado = True
    def __str__(self):
        return self.nombre
class ConjuntoDeCartas:
    def __init__(self):
        self.conjunto_cartas = []
        self.conjunto_diccionario = {}
    def agregarCarta (self, carta): 
        self.conjunto_cartas.append(carta)
    def agregarCartas (self, cartas):
        self.conjunto_cartas.extend(cartas)
    def agruparCon (self, otroConjuntoDeCartas):
         nuevoConjunto = ConjuntoDeCartas()
         nuevoConjunto.agregarCartas (self.conjunto_cartas) 
         nuevoConjunto.agregarCartas (otroConjuntoDeCartas) 
         return nuevoConjunto
    def mezclar_conjunto(self):
        shuffle(self.conjunto_cartas)
    def crear_dicc(self):
        self.diccionario = {}
        for cartas in self.conjunto_cartas:
            if cartas.numero in self.diccionario:
                self.diccionario[cartas.numero] += 1
            else:
                self.diccionario[cartas.numero] = 1
        self.conjunto_diccionario = self.diccionario
        # return self.conjunto_diccionario
    def editar_conjunto(self):
            self.conjunto_cartas = [Carta(14,"diamante"), Carta(2,"diamante"),
                                    Carta(3,"diamante"),Carta(4,"trebol"),Carta(5,"corazon"),
                                    Carta(5,"trebol"),Carta(5,"diamante"),Carta(9,"trebol"),
                                    Carta(5,"pica")]
    def vaciar_conjunto(self):
        self.conjunto_cartas = []
        self.diccionario = {}    


class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mano = ConjuntoDeCartas()
        self.mano_final = ConjuntoDeCartas()
        self.mano_posible = Mano("adios", 1)
        self.contador_victorias = 0
    def __repr__(self) -> str:
        return self.nombre
    def valor_mano (self):
        return self.mano_posible.valor


    def reinicio(self):
        self.mano.vaciar_conjunto()
        self.mano_final.vaciar_conjunto
    def crear_mano_final (self, cartas_mesa):
        self.mano_final.conjunto_cartas = self.mano.conjunto_cartas + cartas_mesa 
    def carta_alta(self):
        valor_carta_alta = max(self.mano_final.conjunto_diccionario.keys())
        self.mano_posible = Mano("carta alta", 1)
        return valor_carta_alta
    def buscar_par(self):
        if 2 in self.mano_final.conjunto_diccionario.values():
            self.mano_posible = Mano("par", 2)
    def buscar_doble_par(self):
        contador_pares = 0
        for x in self.mano_final.conjunto_diccionario.values():
            if x == 2:
                contador_pares += 1
            if contador_pares >= 2:
                self.mano_posible = Mano("doble par", 3)
    def buscar_trio(self):
        if 3 in self.mano_final.conjunto_diccionario.values():
            self.mano_posible = Mano("trio", 4)
    def buscar_color(self):
        contador_corazon = 0  
        contador_diamantes = 0
        contador_treboles = 0
        contador_picas = 0
        for cartas in self.mano_final.conjunto_cartas:
            if cartas.palo == "pica":
                contador_picas += 1
            if cartas.palo == "corazon":
                contador_corazon += 1
            if cartas.palo == "diamante":
                contador_diamantes += 1
            if cartas.palo == "trebol":
                contador_treboles += 1
        if contador_diamantes == 5 or contador_corazon == 5 or contador_picas == 5 or contador_treboles == 5:
           self.mano_posible = Mano("color", 5)
    def buscar_escalera(self,lista_valores = []):
        
        if len(lista_valores) == 0:
            lista_valores = [cartas for cartas in self.mano_final.conjunto_diccionario.keys()]
        if 14 in lista_valores:
            lista_valores.append(1)
        lista_valores.sort()
       
        for valores  in lista_valores:
            contador = 0  
            for x in range (valores,valores+5):
                if x in lista_valores:
                    contador+=1
                if contador == 5:
                    self.mano_posible = Mano("escalera", 6)
                    lista_valores = []
                    return True
    def buscar_full(self):
        diccionario_valores = self.mano_final.conjunto_diccionario.values()
        if 3 in diccionario_valores and 2 in diccionario_valores :
            self.mano_posible = Mano("full house", 7)
    def buscar_poker(self):
        diccionario_valores = self.mano_final.conjunto_diccionario.values()
        if 4 in diccionario_valores:
            self.mano_posible = Mano("poker", 8)
            return "tiene poker"   
    def buscar_escalera_color(self):
        lista_pica = []
        lista_corazon = []
        lista_diamante = []
        lista_trebol = []
        contador_diamantes = 0
        contador_treboles = 0
        contador_corazon = 0
        contador_picas = 0

        
        for cartas in self.mano_final.conjunto_cartas: #["pica", "corazon", "diamante", "trebol"]
            if cartas.palo == "pica":
                contador_picas += 1
                lista_pica.append(cartas.numero)
            if cartas.palo == "corazon":
                contador_corazon += 1
                lista_corazon.append(cartas.numero)
            if cartas.palo == "diamante":
                contador_diamantes += 1
                lista_diamante.append(cartas.numero)
            
            if cartas.palo == "trebol":
                contador_treboles += 1
                lista_trebol.append(cartas.numero)

                
        if contador_diamantes >= 5:
            if self.buscar_escalera(lista_diamante) == True:
                self.mano_posible = Mano("escalera de color", 9)
        if contador_corazon >= 5:
            print(lista_corazon)
            if self.buscar_escalera(lista_corazon) == True:
                self.mano_posible = Mano("escalera de color", 9)
        if contador_picas >= 5:
            print(lista_pica)
            if self.buscar_escalera(lista_pica) == True:
                self.mano_posible = Mano("escalera de color", 9)
        if contador_treboles >= 5:
            print(lista_trebol)
            if self.buscar_escalera(lista_trebol) == True:
                self.mano_posible = Mano("escalera de color", 9)
    def determinar_mano(self):
        self.carta_alta()
        self.buscar_par()
        self.buscar_doble_par()
        self.buscar_trio()
        self.buscar_color()
        self.buscar_escalera()
        self.buscar_full()
        self.buscar_poker()
        self.buscar_escalera_color()
        return self.mano_posible
    



    def __repr__(self):
        return f"{self.nombre}"
class Juego:
    def __init__(self):
        self.lista_jugadores = []
        self.mesa = ConjuntoDeCartas()
        self.mazo = ConjuntoDeCartas()
        self.valores = [0]
        self.ganador = []
        self.empate = []
    
    def registrar_jugador(self, nombre):
        self.lista_jugadores.append(Jugador(nombre))
    def eliminar_jugadores(self,nombre):
        for jugador in self.lista_jugadores:
            if jugador.nombre == nombre:
                self.lista_jugadores.remove(jugador)
    def crear_mazo(self):
        contador = 0
        palos = ["pica", "corazon", "diamante", "trebol"]
        while contador<4:
            un_palo = [Carta(x,palos[contador]) for x in range(2,15)]
            contador+=1
            self.mazo.agregarCartas(un_palo)

    def Repartir(self):
        shuffle(self.mazo.conjunto_cartas)
        cartas_repartidas = 0
        jugador_a_repartir = 1
        contador_cartas_mesa = 0
        for carta in self.mazo.conjunto_cartas:
            if cartas_repartidas < (len(self.lista_jugadores))*2:
                self.lista_jugadores[jugador_a_repartir-1].mano.agregarCarta(carta)
                jugador_a_repartir +=1
                cartas_repartidas+=1
                if jugador_a_repartir == len(self.lista_jugadores)+1:
                    jugador_a_repartir = 1           
            else:
                 self.mesa.agregarCarta(carta)
                 contador_cartas_mesa +=1
                 if contador_cartas_mesa == 5:
                    break             
    def preparar_ronda(self):
        for jugador in self.lista_jugadores:
            jugador.crear_mano_final(self.mesa.conjunto_cartas)
        for jugador in self.lista_jugadores:
            jugador.mano_final.crear_dicc() 
    def reiniciar(self):
        self.mazo.vaciar_conjunto()
        self.mesa.vaciar_conjunto()
        for jugador in self.lista_jugadores:
            jugador.reinicio()
    def quien_gana(self):
        self.ganador = []
        self.empate = []
        self.valores = [0]
        for x in range (0,len(self.lista_jugadores)):

            valor = self.lista_jugadores[x].valor_mano()
            if valor == max(self.valores):
                self.valores = []
                self.ganador.append(self.lista_jugadores[x])
                self.empate += self.ganador
                self.valores.append(valor)
                self.ganador = []
            if valor > max(self.valores):
                self.ganador = []
                self.valores = []
                self.empate = []
                self.ganador.append(self.lista_jugadores[x])
                self.valores.append(valor)
        if len(self.empate) > 0:
            return f"empataron {self.empate}"
        if len(self.ganador)== 1:
            self.ganador[0].contador_victorias += 1
            return f"el ganador es {self.ganador}"
        
            
               

            
        
            
               



prueba = Juego()


# while True:
#         cantidad_jugadores = int(input("cuantos van a jugar?: "))
#         for x in range (0, cantidad_jugadores):
#             nombre = input(f"como se llama el jugador numero {x+1}: ")
#             prueba.registrar_jugador(nombre)
#         rondas_a_jugar = int(input("¿cuantas rondas van a jugar?: "))
#         prueba.Repartir()
#         prueba.preparar_ronda()
while True:
    eleccion = int(input(f"1. editar lista de jugadores (minimo 2)\n" "2. jugar\n"
                         "¿que desea hacer?: "))
    if eleccion == 1:
        eleccion_jugadores = int(input(f"1. agregar jugadores\n" "2.eliminar jugadores\n"
                                 "3. mostrar lista de jugadores\n"
                                "¿que desea hacer?: ")) 
        if eleccion_jugadores == 1:
            cantidad_jugadores = int(input("¿cuantos van a agregar?: "))
            for x in range (0, cantidad_jugadores):
                nombre = input(f"como se llama el jugador numero {x+1}: ")
                prueba.registrar_jugador(nombre)
        if eleccion_jugadores == 2:
            nombre_jugador_eliminado = input("¿como se llama el jugador a eliminar?: ")
            prueba.eliminar_jugadores(nombre)
        if eleccion_jugadores == 3:
            for jugadores in prueba.lista_jugadores:
                print(jugadores.nombre)
    if eleccion == 2:
        cantidad_rondas = int(input("cantidad de rondas a jugar: ")) 
        contador_rondas = 0
        for x in range (0, cantidad_rondas):
            contador_rondas +=1
            print (f"ronda numero {contador_rondas}.........................................................")
            prueba.crear_mazo()
            prueba.Repartir()
            prueba.preparar_ronda()  
            
            for jugador in prueba.lista_jugadores:
                print(jugador, jugador.mano_final.conjunto_cartas, jugador.determinar_mano())  
            print(prueba.quien_gana())
            for jugador in prueba.lista_jugadores:
                print(f"el jugador {jugador} ha ganado {jugador.contador_victorias} veces")
            prueba.reiniciar()