from enum import Enum
from typing import TypedDict

# Estados de una casilla
class EstadoCasilla(Enum):
	OCULTO = 1,
	BANDERA = 2,
	DESTAPADO = 3,
	MINA = 4

# Estados del juego
class EstadoJuego(Enum):
	JUGANDO = 1,
	MENU = 2,

# Atributos de una casilla
class Casilla(TypedDict):
	estado: EstadoCasilla
	minas: int

# Atributos de una mina
class Mina(TypedDict):
	x: int
	y: int