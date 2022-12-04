from flet import (
    UserControl,
    ImageFit,
    Image,
    ImageRepeat,
    Container,
    GestureDetector,
    DragUpdateEvent
    
)




class Casilla(UserControl):
    def __init__(self, x: int, y: int, srcArchivo: str = ""):
        super().__init__()
        self.x = x
        self.y = y
        self.srcArchivo = srcArchivo
        self.estado_bandera = False # False => sin Bandera :True => Con bandera
        self.cuerpo = GestureDetector(
            # on_tap=self.cambio_estado,
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
        
    def cambio_estado_bandera(self,e:DragUpdateEvent):
        if not self.estado_bandera:
            self.cuerpo.content.content.src = "assets/casilla_bandera.png"
            
            
        else:
            self.cuerpo.content.content.src = "assets/casilla.png"
            
             
        self.estado_bandera = not self.estado_bandera 
        self.update()
        
    def build(self):
        return self.cuerpo
    