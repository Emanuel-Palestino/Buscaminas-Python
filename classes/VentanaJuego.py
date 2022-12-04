import flet as ft
from flet import (
    UserControl, 
    MainAxisAlignment, 
    Row, 
    Image, 
    FontWeight, 
    Text, 
    colors, 
    Container, 
    alignment,
    Column,
    GestureDetector
)
from classes.Casilla import Casilla

from classes.Cronometro import Cronometro
class VentanaJuego(ft.UserControl):
    def __init__(self,tam: int = 0):
        super().__init__()
        self.tam = tam
        self.banderas = 0
        self.tablero = self.construir_tablero()
    
    def construir_tablero(self):
        itemsCol: Casilla = []
        for i in range(self.tam):
            items = []
            for j in range(self.tam):
                casilla = Casilla(i,j,"assets/casilla.png")    
                items.append(casilla)
            itemsCol.append(ft.Row(controls = items, spacing = 0))
        return ft.Column(controls =itemsCol,spacing = 0)
    
        
    def build(self):
        self.count = ft.Text(f"{self.banderas}")
        return GestureDetector(on_secondary_tap =  lambda e : print("Click padre"),
            content = ft.Column([self.count, self.tablero])
        )



# class VentanaJuego (UserControl):
    
#     def __init__(self):
#         super().__init__()
#         self.flags= 10
#         self.cromometro = Cronometro()
#         self.tablero = Text("Tablero")
        
        

#     def build(self):
        
#         self.encabezado = Row(
#             alignment= MainAxisAlignment.SPACE_EVENLY,
#             controls= [
#                 Row(
#                     controls=[
#                         Image(
#                         src = f"flag.png",
#                         height=40,
#                         width=40
#                         ),
#                         Text(
#                             f"{self.flags}",
#                             size=30,
#                             weight=FontWeight.W_600,
#                             color=colors.BLACK,
#                             width=100
#                         ),
#                     ]
#                 ),
#                 Row(
#                     controls=[
#                         Image(
#                         src = f"clock.png",
#                         height=40,
#                         width=40
#                         ),
#                         Container(content=self.cromometro,width=100)
#                     ]
#                 ),
#             ]
#         )
        
#         return Column(controls=[self.encabezado, self.tablero])
        