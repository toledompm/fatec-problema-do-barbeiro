from threading import Thread
from time import sleep
from random import randint

LOW_END_WAIT_TIME = 5
HIGH_END_WAIT_TIME = 10


class Semaforo:
    def __init__(self, initial_value):
        self.value = initial_value

    def up(self):
        self.value += 1

    def down(self):
        if self.value == 0:
            self.__wait__()
            self.down
        else:
            self.value -= 1

    def get_value(self):
        return self.value

    def __wait__(self):
        global LOW_END_WAIT_TIME
        sleep(LOW_END_WAIT_TIME)


class Mutex(Semaforo):
    def up(self):
        self.value = 1


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
        print("próximo!")

    def run(self):
        global espera
        global clientes_semaforo
        global barbeiro_mutex
        global mutex

        while(True):
            clientes_semaforo.down()

            mutex.down()
            espera -= 1

            barbeiro_mutex.up()
            mutex.up()

            self.corta_cabelo()


class ClienteThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global LOW_END_WAIT_TIME
        global HIGH_END_WAIT_TIME

        global espera
        global clientes_semaforo
        global barbeiro_mutex
        global mutex
        global cadeiras

        while(True):
            sleep(randint(LOW_END_WAIT_TIME, HIGH_END_WAIT_TIME)/10)
            mutex.down()
            if espera < cadeiras:
                print("opa, to na fila")
                espera += 1

                clientes_semaforo.up()
                mutex.up()

                barbeiro_mutex.down()
            else:
                mutex.up()
                print("fui!")


def main():
    cliente_thread = ClienteThread()
    barbeiro_thread = BarbeiroThread()

    cliente_thread.start()
    barbeiro_thread.start()

    cliente_thread.join()
    barbeiro_thread.join()


main()
