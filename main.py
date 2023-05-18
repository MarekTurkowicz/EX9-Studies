import abc
import math

class Figura(abc.ABC):

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def przesun(self, x: float, y: float):
        self._x += x
        self._y += y

    @abc.abstractmethod
    def skaluj(self, value: float):
        pass

    @abc.abstractmethod
    def pole(self):
        pass

    @abc.abstractmethod
    def obwod(self):
        pass


class Kolo(Figura):
    def __init__(self, x: float, y: float, r: float) -> None:
        super().__init__(x, y)
        self._r = r

    def skaluj(self, sk: float) -> None:
        self._r *= sk

    def pole(self) -> float:
        return math.pi * self._r * self._r

    def obwod(self) -> float:
        return 2 * math.pi * self._r


class Kwadrat(Figura):
    def __init__(self, x: float, y: float, bok: float) -> None:
        super().__init__(x, y)
        self._bok = bok

    def skaluj(self, sk: float) -> None:
        self._bok *= sk

    def pole(self) -> float:
        return self._bok * self._bok

    def obwod(self) -> float:
        return 4 * self._bok


def pole_obwod_liczenie(list, pl, ol):
    for element in list:
        pl += element.pole()
        ol += element.obwod()
    return pl, ol


    koloo = Kolo(2.0, 3.0, 4.0)
    kwadratt = Kwadrat(2.0, 3.0, 4.0)
    listt = [koloo, kwadratt]

    pole_lista = 0
    obwod_lista = 0

    pole_lista, obwod_lista = pole_obwod_liczenie(listt, pole_lista, obwod_lista)
    print(f"pole dla listy: {pole_lista}, oraz obwod: {obwod_lista}")

    for element in listt:
        element.przesun(8.0, 8.0)

    pole_lista, obwod_lista = pole_obwod_liczenie(listt, pole_lista, obwod_lista)
    print(f"pole dla listy: {pole_lista}, oraz obwod: {obwod_lista}")

if __name__ == '__main__':


    koloo = Kolo(2.0, 3.0, 4.0)
    kwadratt = Kwadrat(2.0, 3.0, 4.0)
    figury = [koloo, kwadratt]

    pole_lista = 0
    obwod_lista = 0

    pole, obwod = pole_obwod_liczenie(figury, pole_lista, obwod_lista)
    print(f"Łączne pole figur: {pole:.2f}, łączny obwód: {obwod:.2f}")

    for figura in figury:
        figura.przesun(2.0, 2.0)

    pole, obwod = pole_obwod_liczenie(figury, pole_lista, obwod_lista)
    print(f"Łączne pole figur po przesunięciu: {pole:.2f}, łączny obwód po przesunięciu: {obwod:.2f}")

    for figura in figury:
        figura.skaluj(2)

    pole, obwod = pole_obwod_liczenie(figury, pole_lista, obwod_lista)
    print(f"Łączne pole figur po skalowaniu: {pole:.2f}, łączny obwód po skalowaniu: {obwod:.2f}")
