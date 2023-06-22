#######################################################
 # Název projektu: Kalkulačka
 # Soubor: IMath.h
 # Datum: 9.3.2023
 # Poslední změna: 9.3.2023
 # Autor: Vojtěch Teichmann
 # Tým: Tomojavo
 # 
 # Popis: Matematická knihovna
#######################################################
from IMath_h import *

    ##
    # @file Implementace funkcí ze souboru IMath_h
    # @brief V souboru IMath_h je dokumentace funkcí

class IMath_h:

    def init(self):
        pass

    def sum(self, num1: float, num2: float) -> float:
        return num1 + num2
    
    def sub(self, num1: float, num2: float) -> float:
        return num1 - num2

    def div(self, num1: float, num2: float) -> float:
        if num2 == 0.0:
            raise ZeroDivisionError("Div err")
        return num1 / num2

    def mult(self, num1: float, num2: float) -> float:
        return num1 * num2

    def fact(self, num: int) -> int:
        factorial = 1

        if isinstance(num, float):
            raise ValueError("Číslo je desetinné")
        if num < 0:
            raise ValueError("Číslo je záporné")
        if num == 0:
            return 1
        
        for i in range(1, num + 1):
            factorial = factorial*i
        return factorial

    def pow(self, num: float, exponent: int) -> float:

        if isinstance(exponent, float):
            raise ValueError("Neni cele cislo")
        if num == 0.0:
            if exponent == 0:
                raise ValueError("Neni def")
        if exponent == 0:
            return 1

        result = (round(num ** exponent, 11))
        return result

    def sqrt(self, degree: int, num: float) -> float:

        if isinstance(degree, float):
            raise ValueError("Desetinné číslo")
        if num < 0.0:
            raise ValueError("Číslo je záporné")
        if degree == 0:
            raise ZeroDivisionError("Dělení nulou")
        result = (round(num ** (1/degree), 11))
        return result

    def mod(self, num1: int, num2: int) -> int:

        if isinstance(num1, float) or isinstance(num2, float):
            raise ValueError("Math err")


        if num2 == 0:
            raise ZeroDivisionError("Div err")
        if (num1 < 0) ^ (num2 < 0):
            result = -result
        
        result = num1 % num2

        return result
