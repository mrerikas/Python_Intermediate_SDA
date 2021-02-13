"""
Aplikacija
1 Ekranas/pasirinkimas:
    a) Prisijungti
    b) Užsiregistruoti
2.1) Prisjungit:
    a) Įvesti duomenis
    b) Peržiūrėti duomenis
2.2) Užsiregistruoti:
    a) Suvesti registracijos duomenis
Reikalavimai:
1) Panaudoti abstract class klasei kuri nuskaitys duomenis
2) Sukurti Model klasę (Vartotojas, Priminimas)
"""
from abc import ABC, abstractmethod
from typing import Type

DB = None


class Model(ABC):
    @abstractmethod
    def to_dict(self):
        """
        Remember classes with __slots__ hint: {key:getattr(a,key) for key in a.__slots__}
        :return:
        """
        pass


class Vartotojas(Model):
    pass


class Priminimas(Model):
    pass


class ReaderInterface(ABC):
    @abstractmethod
    def ask_for_input(self, model: Type[Model]) -> Model:
        """
        Ask user to input all the values required for the model and return the model object
        :param a:
        :param b:
        :return:
        """


class InputReader(ReaderInterface):
    def ask_for_input(self, model: Type[Model]) -> Model:
        return Vartotojas()
