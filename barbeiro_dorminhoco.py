class Semaforo:
    def __init__(self):
        self.value = 0

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
        if self.value == 1: return (False, "Recurso já está livre")
        else: 
            self.value = 1
            return (True, "Recurso liberado")
    
    def down(self):
        if self.value == 0: return (False, "Recurso já está ocupado")
        else:
            self.value = 0
            return (True, "Recurso consumido")
