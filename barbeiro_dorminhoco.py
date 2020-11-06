from threading import Thread
from time import sleep

class Semaforo:
    def __init__(self, initial_value):
        self.value = initial_value

    def up(self):
        self.value += 1
    
    def down(self):
        if self.value == 0: self.__wait__()
        else: self.value -= 1
    
    def get_value(self):
        return self.value

    def __wait__(self):
        print("Alguma lógica que faz o processo entrar em estado de espera")

class Mutex(Semaforo):
    def up(self):
        if self.value == 1: raise Exception("Recurso já esta livre")
        else: 
            self.value = 1
    
    def down(self):
        if self.value == 0: raise Exception("Recurso já está ocupado")
        else:
            self.value = 0

cadeiras = 5
espera = 0
clientes_semaforo = Semaforo(0)
barbeiro_mutex = Mutex(0)
mutex = Mutex(1)

class BarbeiroThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def corta_cabelo(self):
        print("snip")
        sleep(1)
        print("snip")

    def run(self):
        global espera
        global clientes_semaforo
        global barbeiro_mutex
        global mutex

        while(True):
            clientes_semaforo.down
            mutex.down

            espera -= 1

            barbeiro_mutex.up
            mutex.up

            self.corta_cabelo()

class ClienteThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global espera
        global clientes_semaforo
        global barbeiro_mutex
        global mutex
        global cadeiras

        while(True):
            sleep(0.5)
            if espera < cadeiras:
                print("opa, to na fila")
                espera += 1
                clientes_semaforo.up
                mutex.up

                barbeiro_mutex.down
            else: 
                mutex.up
                print("fui!")

def main():
    cliente_thread = ClienteThread()
    barbeiro_thread = BarbeiroThread()

    cliente_thread.start()
    barbeiro_thread.start()

    cliente_thread.join()
    barbeiro_thread.join()

main()