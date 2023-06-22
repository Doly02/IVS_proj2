#######################################################
 # Název projektu: Kalkulačka
 # Soubor: IMath.h
 # Datum: 9.3.2023
 # Poslední změna: 9.3.2023
 # Autor: Vojtěch Teichmann
 # Tým: Tomojavo
 # 
 # Popis: Deklarace funkcí pro matematickou knihovnu
#######################################################
class IMath_h:

    ##
    # @brief: Inicializace
    # @param: self První operand
    def init(self):
        pass

    ##
    # @brief: Sečte dvě čísla.
    # @param: self První operand
    # @param: num1 Druhý operand.
    # @param: num2 Třetí operand.
    # @return: Výsledek operace sčítání.

    def sum(self, num1: float, num2: float) -> float:
        pass

    ##
    # @brief: Odečte dvě čísla
    # @param: self První operand
    # @param: num1 Druhý operand.
    # @param: num2 Třetí operand.
    # @return: Výsledek operace odečítání.

    def sub(self, num1: float, num2: float) -> float:
        pass

    ##
    # @brief: Vynásobí dvě čísla
    # @param: self První operand
    # @param: num1 Druhý operand.
    # @param: num2 Třetí operand.
    # @return: Výsledek operace násobení.

    def mult(self, num1: float, num2: float) -> float:
        pass

    ##
    # @brief: Vydělí dvě čísla
    # @param: self První operand
    # @param: num1 Druhý operand.
    # @param: num2 Třetí operand.
    # @return: Výsledek operace dělení
    # @throws: ZeroDivisionError Pokud je třetí operand (num2) roven nule

    def div(self, num1: float, num2: float) -> float:
        pass

    ##
    # @brief: Vypočítá faktoriál ze zadaného čísla
    # @param: self První operand
    # @param: num Celočíslený operand
    # @return: Výsledek operace faktoriál
    # @throws: ValueError Pokud je operand (num) desetinné číslo
    # @throws: ValueError Pokud je operand (num) záporné číslo

    def fact(self, num: int) -> int:
        pass

    ##
    # @brief: Vypočítá mocninu čísla
    # @param: self První operand
    # @param: num Druhý operand
    # @param: exponent Třetí operand
    # @return: Číslo num umocněné číslem exponent 
    # @throws: ValueError Pokud je operand (exponent) desetinné číslo
    # @throws: ValueError Pokud je číslo 0 umocněné číslem 0 (nedefinované)

    def pow(self, num: float, exponent: int) -> float:
        pass

    ##
    # @brief: Vypočítá odmocninu čísla
    # @param: self První operand
    # @param: degree Druhý operand
    # @param: num Třetí operand
    # @return: Číslo num je odmocněno číslem degree
    # @throws: ZeroDivisionError Pokud je Druhý operand (degree) roven nule

    def sqrt(self, degree: int, num: float) -> float:
        pass

    ##
    # @brief: Vypočítá zbytek po celočíselném dělení
    # @param: self První operand
    # @param: num1 Druhý operand
    # @param: num2 Třetí operand
    # @return: Zbytek po celočíselném dělení
    # @throws: ZeroDivisionError Pokud je třetí operand (num2) roven nule
    
    def mod(self, num1: int, num2: int) -> int:
        pass  
