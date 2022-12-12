from flet import (
    UserControl,
    Text,
    FontWeight,
    colors
)
import time, threading


class Cronometro(UserControl):
    def __init__(self):
        super().__init__()
        self.segundos = 1
        

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()


    def will_unmount(self):
        self.running = False

    def update_timer(self):
        
            while self.running:
                mins, secs = divmod(self.segundos, 60)
                self.crono.value = "{:02d}:{:02d}".format(mins, secs)
                self.update()
                time.sleep(1)
                self.segundos += 1

    def build(self):
        self.crono = Text(weight=FontWeight.W_600, size=30,color=colors.BLACK)
        return self.crono