from classes.VentanaJuego import VentanaJuego
from definitions import EstadoJuego, EstadoCasilla, Mina, Casilla, NumeroMinas
from utils import colocarMinas, mostrarTableroConsola, floodFill
import os
from flet import (
    app,
    Page
)


tableroG = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]


def main(pagina: Page):
    pagina.title = "Buscaminas" 
    pagina.scroll = "adaptive"
    pagina.bgcolor = "#61398A"
    pagina.window_height= 400
    pagina.window_width = 500
    pagina.window_resizable = False
    pagina.window_center()
    
    
    pagina.add(VentanaJuego())
    pagina.update()
    
    



def menu():
	opcion = EstadoJuego.MENU
	
	while opcion == EstadoJuego.MENU:
		# Limpiar pantalla
		if os.system('clear') == 1:
			os.system('cls')

		print('***************BUSCAMINAS***************\n')
		tamaño = int(input('Ingresa el tamaño del tablero: '))

		# Crear tablero
		tablero: list[list[Casilla]] = [[{'estado': EstadoCasilla.OCULTO , 'minas': 0} for i in range(tamaño)] for j in range(tamaño)]

		# Lista de Minas
		minas: list[Mina] = []

		# Comenzar el juego
		opcion = EstadoJuego.JUGANDO
		casillasDestapadas = 0
		while opcion == EstadoJuego.JUGANDO:
			# Limpiar pantalla
			if os.system('clear') == 1:
				os.system('cls')
			
			print('***************BUSCAMINAS***************\n')
			# Mostrar tablero
			mostrarTableroConsola(tablero)
		
			# Terminar juego si perdió
			if casillasDestapadas == -1:
				opcion = EstadoJuego.MENU
				input('SE TERMINÓ EL JUEGO... Pulse ENTER para continuar.')
				break
		
			# Mostrar Acciones
			print('Acciones:\n<d> Destapar | <b> Bandera | <q> Quitar Bandera | <t> Terminar Partida | <s> Salir')

			# Leer acción
			movimiento = input('Seleccione su acción con el formato: <letra accion> <posicion x> <posicion y> :\n').split()

			# Destapar una casilla
			if movimiento[0] == 'd':
				# Primer movimiento
				if casillasDestapadas == 0:
					minas = colocarMinas(tamaño, tablero, int(movimiento[1]), int(movimiento[2]))

				resultado = floodFill(int(movimiento[1]), int(movimiento[2]), tablero, minas, casillasDestapadas)
				if resultado == -1:
					casillasDestapadas = -1
				else:
					casillasDestapadas += resultado
			# Poner una bandera
			elif movimiento[0] == 'b':
				if tablero[int(movimiento[1])][int(movimiento[2])]['estado'] == EstadoCasilla.OCULTO:
					tablero[int(movimiento[1])][int(movimiento[2])]['estado'] = EstadoCasilla.BANDERA
			# Quitar una bandera
			elif movimiento[0] == 'q':
				if tablero[int(movimiento[1])][int(movimiento[2])]['estado'] == EstadoCasilla.BANDERA:
					tablero[int(movimiento[1])][int(movimiento[2])]['estado'] = EstadoCasilla.OCULTO
			# Termina la partida actual
			elif movimiento[0] == 't':
				opcion = EstadoJuego.MENU
			# Salir del juego
			elif movimiento[0] == 's':
				return

if __name__ == '__main__':
	app(target=main, assets_dir="assets")