from flet import *

from classes.Casilla import Casilla
from classes.VentanaJuego import VentanaJuego
from definitions import NumeroMinas


def main(pagina: Page):
    pagina.title = "Buscaminas" 
    pagina.scroll = "adaptive"
    pagina.update()
    pagina.window_resizable = True
    pagina.theme_mode = "light"
    pagina.window_height= 700
    pagina.window_width = 1080
    pagina.window_center()
    pagina.fonts= {
        "comforta": "/fonts/Comfortaa-VariableFont_wght.ttf"
    
    }
    # pagina.add(VentanaJuego(10))
   
    def route_change(route):
        
        def cambio_ruta(e):
            print(f"Valor seleccionado: {drop_down.value}")
            t.value = f"{drop_down.value}"
            print(f"Routing drop_down: {t.value}")
            
        def cambio_pagina(e):
            print(f"Routing: /{t.value}")
            pagina.go(f"/{t.value}")
            
        
        pagina.views.clear()
       
        t = Text()
        drop_down = Dropdown( 
                on_change=cambio_ruta,
                
                hint_text="Escoje la dificultad",
                hint_style= TextStyle(color="#000000"),
                focused_bgcolor= "#000000",
                focused_border_color= "#000000",
                label_style=TextStyle(color="#000000"),
                options=[
                    dropdown.Option("Facil"),
                    dropdown.Option("Medio"),
                    dropdown.Option("Dificil"),
                ],
                width=200,
                
        )
        
        jugar = ElevatedButton(
            on_click= cambio_pagina,
            content= Row(
                width=300,
                alignment= MainAxisAlignment.CENTER,
                controls=[
                    Image(
                        src="/explosion.png",
                        width= 90,
                        height=90,
                        fit=ImageFit.COVER,
                        repeat=ImageRepeat.NO_REPEAT,
                    ),
                    Container(padding= padding.only(right=10)),
                    Text(
                        "Jugar",
                        font_family= "comforta",
                        size=40,
                    )
                ]
            )
        )
        
        pagina.views.append(
            View(
                "/",
                [
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Row(
                                alignment= MainAxisAlignment.CENTER,
                                controls=[
                                    Text("Buscaminas",font_family="comforta", size=100,color=colors.BLACK),
                                    Container(padding=padding.only(right=40)),
                                    Image(
                                        src="/bomb.png",
                                        width= 120,
                                        height=120,
                                        fit=ImageFit.COVER,
                                        repeat=ImageRepeat.NO_REPEAT,
                                    )
                                ]
                            ),
                            Container(padding= padding.only(top=7)),
                            drop_down, 
                            Container(padding= padding.only(top=10)),
                            jugar, 
                        ]
                    )
                    # AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                    # ElevatedButton("Visit Store", on_click=lambda _: pagina.go("/store")),
                ],
                bgcolor = "#cacbcf",
                padding = padding.only(top = 200),
            )
        )
    
        if pagina.route == "/Facil":
            pagina.window_height= 550
            pagina.window_width = 500
            pagina.window_center()
            pagina.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Facil"), bgcolor=colors.SURFACE_VARIANT),
                        VentanaJuego(6),
                    ],
                )
            )
        if pagina.route == "/Medio":
            pagina.window_height= 720
            pagina.window_width = 700
            pagina.window_center()
            pagina.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Medio"), bgcolor=colors.SURFACE_VARIANT),
                        VentanaJuego(9),
                    ],
                )
            )
        if pagina.route == "/Dificil":
            pagina.window_height= 790
            pagina.window_width = 790
            pagina.window_center()
            pagina.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Dificil"), bgcolor=colors.SURFACE_VARIANT),
                        VentanaJuego(10),
                    ],
                )
            )
        
        pagina.update()
    
    
    def view_pop(view):
        pagina.views.pop()
        top_view = pagina.views[-1]
        pagina.window_height= 700
        pagina.window_width = 1080
        pagina.window_center()
        pagina.go(top_view.route)

    pagina.on_route_change = route_change
    pagina.on_view_pop = view_pop
    pagina.go(pagina.route)
    
    print(pagina.route)


if __name__ == '__main__':
	app(target=main, assets_dir="assets")