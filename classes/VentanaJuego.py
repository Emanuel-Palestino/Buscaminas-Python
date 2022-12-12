import flet as ft
from flet import (
    UserControl, 
    MainAxisAlignment, 
    CrossAxisAlignment,
    Row, 
    Image, 
    FontWeight, 
    Text, 
    colors, 
    Container, 
    alignment,
    Column,
    GestureDetector,
    ElevatedButton
)
from classes.Casilla import Casilla

from classes.Cronometro import Cronometro
class VentanaJuego(UserControl):
    def __init__(self,tam: int = 0):
        super().__init__()
        self.tam = tam
        self.tablero_estado = False
        self.banderas = 0
        self.tablero = self.construir_tablero()
        self.cronometro = Container(content=Text("{:02d}:{:02d}".format(0,0) , weight=FontWeight.W_600, size=30,color=colors.BLACK))
        
    def agregar_bandera(self,e):
        self.banderas += 1
        self.encabezado.controls[0].controls[1].value = self.banderas
        self.update()
        
    def quitar_bandera(self,e):
        self.banderas -= 1
        self.encabezado.controls[0].controls[1].value = self.banderas
        super().update()
    
    def activar_crono(self, e):
        if self.tablero_estado == False:
            self.tablero_estado = True
            self.cronometro.content = Cronometro()
        self.update()
    
    def construir_tablero(self):
        itemsCol: Casilla = []
        for i in range(self.tam):
            items = []
            for j in range(self.tam):
                casilla = Casilla(i,j,"assets/casilla.png", self.agregar_bandera, self.quitar_bandera,self.activar_crono, self)    
                items.append(casilla)
            itemsCol.append(ft.Row(controls = items, spacing = 0,alignment=MainAxisAlignment.CENTER))
        return Column(controls =itemsCol,spacing = 0, horizontal_alignment=CrossAxisAlignment.CENTER)
    
    def build(self):
        self.encabezado = Row(
            alignment= MainAxisAlignment.SPACE_EVENLY,
            controls= [
                Row(
                    controls=[
                        Image(
                        src = f"bomb.png",
                        height=40,
                        width=40
                        ),
                        Text(
                            f"{self.tam}",
                            size=30,
                            weight=FontWeight.W_600,
                            color=colors.BLACK,
                            width=100
                        ),
                    ]
                ),
                Row(
                    controls=[
                        Image(
                        src = f"flag.png",
                        height=40,
                        width=40
                        ),
                        Text(
                            f"{self.banderas}",
                            size=30,
                            weight=FontWeight.W_600,
                            color=colors.BLACK,
                            width=100
                        ),
                    ]
                ),
                Row(
                    controls=[
                        Image(
                        src = f"clock.png",
                        height=40,
                        width=40
                        ),
                        Container(content=self.cronometro,width=100)
                    ]
                ),
            ]
        )
        
        return Column(controls=[self.encabezado, self.tablero], alignment = MainAxisAlignment.CENTER)
        
        



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
        