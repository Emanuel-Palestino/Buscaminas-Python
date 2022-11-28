from definitions import EstadoJuego, EstadoCasilla, Mina
from utils import colocarMinas

def menu():
	opcion = EstadoJuego.MENU
	
	while opcion == EstadoJuego.MENU:
		print('BUSCAMINAS')
		tamaño = int(input('Ingresa el tamaño del tablero\n'))

		# Crear tablero
		tablero = [[{"estado": EstadoCasilla.OCULTO , "minas": 0} for i in range(tamaño)] for j in range(tamaño)]

		# Lista de Minas
		minas: list[Mina] = colocarMinas(tamaño, tablero, 0, 0)

		opcion = EstadoJuego.JUGANDO
		while opcion != EstadoJuego.MENU:
			opcion = input('Acciones:\n<d> Destapar | <b> Bandera | <q> Quitar Bandera | <s> Salir\n')



if __name__ == '__main__':
	menu()