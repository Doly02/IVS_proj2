#######################################################
 # Název projektu: Kalkulačka
 # Soubor: IMath.h
 # Datum: 9.4.2023
 # Poslední změna: 13.4.2023
 # Autor: Vojtěch Teichmann
 # Tým: Tomojavo
 # 
 # Popis: profiling
#######################################################

from Math import IMath_h
import cProfile
import fileinput
import sys

##
# @brief vypočítává sumu z čísel ze seznamu
# @param data - seznam čísel k sečtení
# @return suma z čísel

def calculate_sum(data):
    current_sum = 0
    math = IMath_h()
    for number in data:
        current_sum = math.sum(current_sum, number)
    return current_sum

##
# @brief vypočítává aritmetický průměr ze součtu všech prvků a počtů prvků
# @param total_sum - celkový součet prvků
# @param n - počet prvků
# @return aritmetický průměr 

def calculate_arithmetic_mean(total_sum, n):
    math = IMath_h()
    return math.div(total_sum, n)

##
# @brief vypočítává směrodatnou odchylku
# @param data - seznam jednotlivých měření
# @param mean_value - aritmetický průměr měření
# @param n - počet měření v seznamu
# @return směrodatnou odchylku

def calculate_standard_deviation(data, mean_value, n):
    current_sum = 0
    math = IMath_h()
    first = math.div(1, math.sub(n, 1))
    second = math.mult(n, math.pow(mean_value, 2))
    for number in data:
        third = math.pow(number, 2)
        current_sum = math.sum(current_sum, third)
    fourth = math.mult(first, math.sub(current_sum, second))
    return math.sqrt(2, fourth)


def main():

    if not sys.stdin.isatty():
        data = []
        for line in fileinput.input():
            for number in line.split():
                if not number.isdigit():
                    print(f"Chyba: řádek '{line.strip()}' neobsahuje platné číslo")
                    return
                data.append(float(number))
    else:
        print("Chyba: musíte zadat vstupní soubor")
        return
    
    total_sum = calculate_sum(data)
    n = len(data)
    arithmetic_mean = calculate_arithmetic_mean(total_sum, n)
    print(f"{arithmetic_mean}")
    ##cProfile.runctx(f'calculate_standard_deviation(data, arithmetic_mean, n)', globals(), locals())


if __name__ == '__main__':
    main()