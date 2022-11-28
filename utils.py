import numpy as np
from definitions import EstadoCasilla, Casilla, Mina

def floodFill(posX: int, posY: int, tablero: list[list[Casilla]], minas: list[Mina], casillasDestapadas: int) -> int:
	if tablero[posX][posY]['estado'] == EstadoCasilla.OCULTO:
		casillasDestapadas += 1
		# Marcar casilla como destapada
		tablero[posX][posY]['estado'] = EstadoCasilla.DESTAPADO

		# La casilla tiene una mina
		if tablero[posX][posY]['minas'] == -1:
			# Regresa -1 para identificar que perdió
			casillasDestapadas = -1
			# Destapar todas las minas
			for mina in minas:
				tablero[mina['x']][mina['y']]['estado'] = EstadoCasilla.MINA

		# La casilla no tiene minas
		elif tablero[posX][posY]['minas'] == 0:
			# Destapar casillas de alrededor
			posicionesAlrededor = [-1, 0, 1]
			for posicionX in posicionesAlrededor:
				for posicionY in posicionesAlrededor:
					casillasDestapadas = floodFill(posX + posicionX, posY + posicionY, tablero, minas, casillasDestapadas)

	return casillasDestapadas

def colocarMinas(cantidadMinas: int, tablero: list[list[Casilla]], posX: int, posY: int) -> list[Mina]:
	tamañoTablero: int = len(tablero[0])

	# Generar minas sin que se repita
	minas: list[Mina] = []
	while True:
		# Obtener coordenadas aleatoreamente
		nuevaMina: Mina = {
			"x": np.random.randint(low=0, high=tamañoTablero),
			"y": np.random.randint(low=0, high=tamañoTablero)
		}

		# Si no existe y no está en la posición destapada se agrega
		if not(nuevaMina in minas) and not(nuevaMina['x'] == posX and nuevaMina['y'] == posY):
			minas.append(nuevaMina)
		
		# Si ya están creadas todas las minas se sale del ciclo
		if len(minas) >= cantidadMinas:
			break


	# Asignar minas al tablero
	for mina in minas:
		tablero[mina['x']][mina['y']]['minas'] = -1


	# Rellenar casillas restantes del tablero
	for i, fila in enumerate(tablero):
		for j, columna in enumerate(fila):
			# Contar minas alrededor
			numeroMinas = 0
			# Si en la posición actual no hay mina
			if tablero[i][j]['minas'] != -1:
				# Contar alrededor de la posición actual
				posicionesAlrededor = [-1, 0, 1]
				for x in posicionesAlrededor:
					# Salir si se sale de las coordenadas del tablero
					if i + x < 0 or i + x >= tamañoTablero:
						continue

					for y in posicionesAlrededor:
						# Salir si se sale de las coordenadas del tablero
						if j + y < 0 or j + y >= tamañoTablero:
							continue

						# Incrementar el número de minas
						if tablero[i + x][j + y]['minas'] == -1:
							numeroMinas += 1
				
				# Agregar número de minas
				tablero[i][j]['minas'] = numeroMinas

	return minas