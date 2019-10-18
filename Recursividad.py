class PuntosPlano:

    def __init__(self, promediox, promedioy, px1, px2, py1, py2):
        self.px = promediox
        self.py = promedioy
        self.puntox1 = px1
        self.puntox2 = px2
        self.puntoy1 = py1
        self.puntoy2 = py2

    def punto1(self):
        print("inserte el punto x")
        self.puntox1 = int(input())
        print("inserte el punto y")
        self.puntoy1 = int(input())

    def punto2(self):
        print("inserte el punto x")
        self.puntox2 = int(input())
        print("inserte el punto y")
        self.puntoy2 = int(input())

    def dividir_X(self):
        if self.puntox1 < self.puntox2:
            self.promediox = self.puntox2 - self.puntox1

        else:
            self.puntox1 - self.puntox2
        return self.promediox
        print(self.promediox)

    def dividirY(self):
        if self.puntoy1 < self.puntoy2:
            promedioy = self.puntoy2 - self.puntoy1
        else:
            self.puntoy1 - self.puntoy2

        return promedioy
        print(self.promedioy)
