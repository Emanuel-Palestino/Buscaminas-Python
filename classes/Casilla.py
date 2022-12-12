from flet import (
    UserControl,
    ImageFit,
    Image,
    ImageRepeat,
    Container,
    GestureDetector,
    DragUpdateEvent

)

import classes

class Casilla(UserControl):
    def __init__(self, x: int, y: int, srcArchivo, agregar_bandera,quitar_bandera,activar_crono,selfa):
        super().__init__()
        self.x = x
        self.y = y
        self.selfa = selfa
        self.srcArchivo = srcArchivo
        self.activar_crono = activar_crono
        self.agregar_bandera = agregar_bandera
        self.quitar_bandera = quitar_bandera
        self.estado_bandera = False # False => sin Bandera :True => Con bandera
        self.cuerpo = GestureDetector(
            on_tap=self.destapar_casilla,
            on_secondary_tap=self.cambio_estado_bandera,
            content=Container(
                padding=0,
                content= Image(
                    src=f"{self.srcArchivo}",
                    width= 60,
                    height=60,
                    fit=ImageFit.COVER,
                    repeat=ImageRepeat.NO_REPEAT,
                )
            )
        )
  
    def destapar_casilla(self,e:DragUpdateEvent):
        self.activar_crono(self.selfa)
        


    def cambio_estado_bandera(self,e:DragUpdateEvent):
        if not self.estado_bandera:
            self.cuerpo.content.content.src = "assets/casilla_bandera.png"
            self.agregar_bandera(self.selfa)

        else:
            self.quitar_bandera(self.selfa)
            self.cuerpo.content.content.src = "assets/casilla.png"


        self.estado_bandera = not self.estado_bandera
        super().update()
        self.update()

    def build(self):
        return self.cuerpo
