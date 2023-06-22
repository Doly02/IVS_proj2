#######################################################
 # Název projektu: Kalkulačka
 # Soubor: link_lib_w_gui.py
 # Datum: 22.3.2023
 # Poslední změna: 22.3.2023
 # Autor: Tomas Dolak 
 # Tým: Tomojavo
 # 
 # Popis: propojeni matematicke knihovny s GUI 
#######################################################
##
# @file link_lib_w_gui.py
# @author Tomas Dolak
#
# @brief Propojeni matematicke knihovny s GUI.
##

# import potrebnych knihoven 
from Math import IMath_h
from tkinter import *

mathlib = IMath_h()
# implementace funkci
class buttons:
    def __init__(self):
        self.last_button_equal = False
        self.f_num = 0
        global counter
        counter = 0
    
    ###
    #@brief Zobrazi textovy vstup (cislo) na obrazovku
    #@param self - povinny argument
    #param: entry widget - ovladaci prvek 
    #@param: number - cislo 0-9
    #
     
    def button_click(self, entry, number):
        global f_num
        if self.last_button_equal:
            entry.delete(0, END)
            self.last_button_equal = False
            
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, str(current) + str(number))



    ###
    #@brief Funkce zobrazi vysledek podle druhu operace
    #    pokud:  operace addition        ->  vystup = a + b
    #            operace substraction    ->  vystup = a - b
    #            operace multiplication  ->  vystup = a * b
    #            operace division        ->  vystup = a / b
    #            operace modulo          ->  vystup = a % b
    #            operace pow             ->  vystup = a^b
    #            operace sqrt            ->  vystup = sqrt[a]{b}
    #@param self - povinny argument
    #@param: entry widget - ovladaci prvek 
    #
    

    def button_equal(self, entry):
        global counter
        counter = 0
        second_number = entry.get()

        global result
        result = 0 
        entry.delete(0, END)

        if math == "addition":
            result = mathlib.sum(float(f_num),eval(second_number))
            counter = 0
            
        if math == "subtraction":
            result = mathlib.sub(float(f_num),eval(second_number))
            
        if math == "multiplication":
            result = mathlib.mult(float(f_num),eval(second_number))
            
        if math == "division":
            try:
                result = mathlib.div(float(f_num),eval(second_number))
            except ZeroDivisionError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
        if math == "modulo":
            try:
                result = mathlib.mod(f_num, eval(second_number))
            except ValueError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
            except ZeroDivisionError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
        if math == "pow":
            try:
                result = mathlib.pow(float(f_num),eval(second_number))
            except ValueError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
        if math == "sqrt":
            try:
                result = mathlib.sqrt(eval(f_num),eval(second_number))
            except ValueError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
            except ZeroDivisionError as e:
                entry.delete(0, END)
                entry.insert(0, str(e))
                return
        entry.insert(0, result)
        self.last_button_equal = True
        
    ###
    #@brief Vymaze obsah displeje kalkulacky
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_clear(self, entry):
        global result
        result = 0
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka plus, signal ze se budouVýstupem programu je pouze jedno číslo – výběrová směrodatná odchylka – které program vypíše na standardní výstup. scitat dve cisla
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_add(self, entry):
        first_number = entry.get()
        global math
        global f_num
        global counter
        math = "addition"
        if counter > 1:
            self.button_equal(self, entry)
        else:
            if first_number:  
                f_num = float(first_number)
            else:
                f_num = 0.0
        entry.delete(0, END)


    ###
    #@brief Funkce tlacitka minus, signal ze se budou odecitat dve cisla
    #@param self - povinny argument
    #@param: entry widget - ovladaci prvek 
    #
        
    def button_subtract(self,entry):
        first_number = entry.get()
        global math
        global f_num
        math = "subtraction"
        if first_number:  
            f_num = float(first_number)
        else:
            f_num = 0.0
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka nasobeni, signal ze se budou nasobit dve cisla
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_multiply(self,entry):
        first_number = entry.get()
        global f_num
        global math
        global operation
        math = "multiplication"
        f_num = float(first_number)
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka deleno, signal ze se budou delit dve cisla
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_divide(self,entry):
        first_number = entry.get()
        global f_num
        global operation
        global math
        math = "division"
        f_num = float(first_number)
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka faktorial, vezme prvni cislo a vypocita jeho faktorial, vysledek se zobrazi na vystupu
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_fact(self, entry):
        first_number = entry.get()
        global f_num 
        #f_num = float(first_number)
        entry.delete(0, END)
        try:
            entry.insert(0, mathlib.fact(eval(first_number)))
        except ValueError as e:
            entry.delete(0, END)
            entry.insert(0, str(e))
            return

        
    ###
    #@brief Funkce tlacitka mocnina, signal ze se bude mocnit
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_pow(self,entry):
        first_number = entry.get()
        global f_num
        global math
        global operation
        math = "pow"
        f_num = float(first_number)
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka mocniny, prvni cislo first_number-> vysledek first_number^2, vysledek se zobrazi na vystupu
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_pow2(self,entry):
        first_number = entry.get()
        global f_num
        global operation
        f_num = float(first_number)
        entry.delete(0, END)

        entry.insert(0, mathlib.pow(f_num,2))

    ###
    #@brief Funkce tlacitka odmocniny, prvni cislo first_number-> sqrt(first_number), vysledek se zobrazi na vystupu
    #@param self - povinny argument
    #@param: entry widget - ovladaci prvek 
    #
        
    def button_sqr2(self,entry):
        first_number = entry.get()
        global f_num
        f_num = eval(first_number)
        entry.delete(0, END)
        try:
            entry.insert(0, mathlib.sqrt(f_num,2))
        except ValueError as e:
            entry.delete(0, END)
            entry.insert(0, str(e))
            return
        except ZeroDivisionError as e:
            entry.delete(0, END)
            entry.insert(0, str(e))
            return
    ###
    #@brief Funkce tlacitka obecne odmocniny, signal ze se bude odmocnovat
    #@param self - povinny argument
    #@param: entry widget - ovladaci prvek 
    #    

    def button_sqr(self, entry):
        first_number = entry.get()
        global f_num
        global math
        global operation
        math = "sqrt"
        f_num = float(first_number)
        entry.delete(0, END)

    ###
    #@brief Funkce tlacitka modulo, signal ze se bude provadet operace modulo
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #

    def button_mod(self, entry):
        first_number = entry.get()
        global f_num
        global math
        global operation
        math = "modulo"
        f_num = eval(first_number)
        entry.delete(0, END)

       
    ###
    #@brief Funkce prida desetinnou carku na vystup
    #@param self - povinny argument
    #@param entry widget - ovladaci prvek 
    #
 
    def button_dot(self, entry):
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, str(current) + str("."))

    ###
    #@brief Funkce vymaze posledni cislo ze vstupu, vysledek na vystup
    #@param self - povinny argument 
    #@param entry widget - ovladaci prvek 
    #

    def button_del(self, entry):
        current = entry.get()
        entry.delete(first=len(current)-1,last="end")
       
     
        
    