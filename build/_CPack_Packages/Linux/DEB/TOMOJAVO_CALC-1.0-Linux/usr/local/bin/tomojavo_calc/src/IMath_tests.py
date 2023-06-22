#######################################################
 # Název projektu: Kalkulačka
 # Soubor: IMath_tests.py
 # Datum: 13.3.2023
 # Poslední změna: 16.4.2023
 # Autor: Monika Záhradníková
 # Tým: Tomojavo
 #
 # Popis: Testy funkcí pro matematickou knihovnu
#######################################################

#!/usr/bin/env python
import unittest
from Math import IMath_h

##
# Vytvoření testovací třídy @class test_functions,
# která dědí ze třídy TestCase z testovacího modulu

class test_functions(unittest.TestCase):

    ##
    # @brief Testuje funkci sum, která sečte dvě čísla.
    def test_sum(self):

        self.assertEqual(IMath_h.sum(self, 2, 3), 5)
        self.assertEqual(IMath_h.sum(self, -2, 3), 1)
        self.assertEqual(IMath_h.sum(self, 2.0, -3.0), -1)

        self.assertAlmostEqual(IMath_h.sum(self, 1_000_000_000_000.555, 200.222), 1_000_000_000_200.777, 3)
        self.assertAlmostEqual(IMath_h.sum(self, -100.0123456789, 50.22222), -49.7901256789, 11)

        self.assertAlmostEqual(IMath_h.sum(self, 2.0 / 4, 1.0 / 4), 3.0 / 4, 11)
        self.assertAlmostEqual(IMath_h.sum(self, -23 / 10, 7 / 12), -103 / 60, 11)
        self.assertAlmostEqual(IMath_h.sum(self, 2.033 / 7, -1.5 / 4), -74 / 875, 11)

    ##
    # @brief Testuje funkci sub, která odečte dvě čísla.
    def test_sub(self):

        self.assertEqual(IMath_h.sub(self, 2, 3), -1)
        self.assertEqual(IMath_h.sub(self, -2, 3), -5)
        self.assertEqual(IMath_h.sub(self, 2.0, -3.0), 5.0)

        self.assertAlmostEqual(IMath_h.sub(self, 1_000_000_000_000.555, 200.222), 999_999_999_800.333, 3)
        self.assertAlmostEqual(IMath_h.sub(self, -100.0123456789, 50.22222), -150.2345656789, 11)

        self.assertAlmostEqual(IMath_h.sub(self, 2.0 / 4, 1.0 / 4), 1.0 / 4, 11)
        self.assertAlmostEqual(IMath_h.sub(self, -23 / 10, 7 / 12), -173 / 60, 11)
        self.assertAlmostEqual(IMath_h.sub(self, 2.033 / 7, -1.5 / 4), 2329 / 3500, 11)

    ##
    # @brief Testuje funkci mult, která vynásobí dvě čísla.
    def test_mult(self):

        self.assertEqual(IMath_h.mult(self, 2, 3), 6)
        self.assertEqual(IMath_h.mult(self, -2, 3), -6)
        self.assertEqual(IMath_h.mult(self, 2, -3), -6)
        self.assertEqual(IMath_h.mult(self, -2, -3), 6)
        self.assertEqual(IMath_h.mult(self, 234_567, 134_567), 31_564_977_489)

        self.assertAlmostEqual(IMath_h.mult(self, 100.555, 200.222), 20133.32321, 10)
        self.assertAlmostEqual(IMath_h.mult(self, -0.01234, 50.22222), -0.6197421948, 11)

        self.assertAlmostEqual(IMath_h.mult(self, -23 / 10, 7 / 12), -161 / 120, 11)
        self.assertAlmostEqual(IMath_h.mult(self, 2.033 / 7, -1.5 / 4), -6099 / 56000, 11)

    ##
    # @brief Testuje funkci div, která vydělí dvě čísla.
    def test_div(self):

        self.assertEqual(IMath_h.div(self, 10, 10), 1)
        self.assertEqual(IMath_h.div(self, 6, 3), 2)
        self.assertEqual(IMath_h.div(self, 6, -3), -2)
        self.assertEqual(IMath_h.div(self, -6, 3), -2)
        self.assertEqual(IMath_h.div(self, -6, -3), 2)
        self.assertEqual(IMath_h.div(self, 0, 10), 0)
        self.assertEqual(IMath_h.div(self, 31_564_977_488, 2), 15_782_488_744)
        self.assertEqual(IMath_h.div(self, 3_117_528_640_829_092_564_800, 98_765_432_100), 31_564_977_488)

        self.assertAlmostEqual(IMath_h.div(self, 200.222, 3), 66.74066666666667, 11)

        self.assertAlmostEqual(IMath_h.div(self, -23 / 10, 7 / 12), -138 / 35, 11)
        self.assertAlmostEqual(IMath_h.div(self, 2.033 / 7, -1.5 / 4), -2033 / 2625, 11)

    ##
    # @brief Testování funkce div, je-li druhý operand num2 roven nule.
    # @param num2 se nesmí rovnat nule
    def test_zero_div(self):

        with self.assertRaises(ZeroDivisionError):
            IMath_h.div(self, 5, 0)

    ##
    # @brief Testuje funkci fact, která vypočítá faktoriál ze zadaného čísla.
    def test_fact(self):

        self.assertEqual(IMath_h.fact(self, 0), 1)
        self.assertEqual(IMath_h.fact(self, 1), 1)
        self.assertEqual(IMath_h.fact(self, 6), 720)

    ##
    # @brief Testování funkce fact, je-li operand num záporné číslo.
    # @param num nesmí být záporné číslo
    def test_fact_neg_num(self):

        with self.assertRaises(ValueError):
            IMath_h.fact(self, -1)
            IMath_h.fact(self, -5)

    ##
    # @brief Testování funkce fact, je-li operand num desetinné číslo.
    # @param num nesmí být desetinné číslo
    def test_fact_float_num(self):

        with self.assertRaises(ValueError):
            IMath_h.fact(self, 1.1)
            IMath_h.fact(self, -2.5)

    ##
    # @brief Testuje funkci pow, která vypočítá mocninu čísla.
    def test_pow(self):

        self.assertEqual(IMath_h.pow(self, 2, 0), 1)
        self.assertEqual(IMath_h.pow(self, 2, 1), 2)
        self.assertEqual(IMath_h.pow(self, 2, -1), 1 / 2)
        self.assertEqual(IMath_h.pow(self, 5, 2), 25)
        self.assertEqual(IMath_h.pow(self, -5, 2), 25)
        self.assertEqual(IMath_h.pow(self, -5, 3), -125)
        self.assertEqual(IMath_h.pow(self, -5, -3), -1 / 125)

        self.assertEqual(IMath_h.pow(self, 1, 100), 1)
        self.assertEqual(IMath_h.pow(self, 0, 100), 0)
        self.assertEqual(IMath_h.pow(self, 12, 10), 61_917_364_224)

        self.assertAlmostEqual(IMath_h.pow(self, 200.222, 3), 8_026_669.581341049, 11)
        self.assertAlmostEqual(IMath_h.pow(self, 0.23456, 3), 0.012905114402, 11)

    ##
    # @brief Testování funkce pow, je-li operand exponent desetinné číslo.
    # @param exponent nesmí být desetinné číslo
    def test_pow_float_exp(self):

        with self.assertRaises(ValueError):
            IMath_h.pow(self, 2, 1.5)
            IMath_h.pow(self, 2, -1.5)

    ##
    # @brief Testování funkce pow, je-li operand exponent roven nule a současně i operand num roven nule.
    # @param exponent se nesmí rovnat nule
    # @param num se nesmí rovnat nule
    def test_pow_zero(self):

        with self.assertRaises(ValueError):
            IMath_h.pow(self, 0, 0)

    ##
    # @brief Testuje funkci sqrt, která vypočítá odmocninu čísla.
    def test_sqrt(self):

        self.assertEqual(IMath_h.sqrt(self, 1, 1), 1)
        self.assertEqual(IMath_h.sqrt(self, 2, 1), 1)
        self.assertEqual(IMath_h.sqrt(self, 100, 1), 1)
        self.assertEqual(IMath_h.sqrt(self, 2, 0), 0)

        self.assertEqual(IMath_h.sqrt(self, 1, 5), 5)
        self.assertEqual(IMath_h.sqrt(self, 2, 9), 3)
        self.assertEqual(IMath_h.sqrt(self, -1, 5), 0.2)

        self.assertAlmostEqual(IMath_h.sqrt(self, -10, 10), 0.79432823472, 11)
        self.assertAlmostEqual(IMath_h.sqrt(self, -2, 5), 0.4472135955, 11)
        self.assertAlmostEqual(IMath_h.sqrt(self, 10, 10), 1.25892541179, 11)
        self.assertAlmostEqual(IMath_h.sqrt(self, 2, 3.55555), 1.88561661002, 11)
        self.assertAlmostEqual(IMath_h.sqrt(self, 5, 10.123456), 1.58878730109, 11)

    ##
    # @brief Testování funkce sqrt, je-li operand degree roven nule.
    # @param degree se nesmí rovnat nule.
    def test_sqrt_zero_degree(self):

        with self.assertRaises(ZeroDivisionError):
            IMath_h.sqrt(self, 0, 0)
            IMath_h.sqrt(self, 0, 2)

    ##
    # @brief Testování funkce sqrt,
    # je-li operand degree desetinné číslo.
    def test_sqrt_float_degree(self):

        with self.assertRaises(ValueError):
            IMath_h.sqrt(self, 1.5, 5)
            IMath_h.sqrt(self, -1.5, 10)

    ##
    # @brief Testování funkce sqrt, je-li operand num záporné číslo.
    # @param num nesmí být záporné číslo
    def test_sqrt_neg_num(self):

        with self.assertRaises(ValueError):
            IMath_h.sqrt(self, 2, -1)
            IMath_h.sqrt(self, 3, -10)

    ##
    # @brief Testuje funkci mod, která vypočítá zbytek po celočíselném dělení.
    def test_mod(self):

        self.assertEqual(IMath_h.mod(self, 2, 2), 0)
        self.assertEqual(IMath_h.mod(self, 3, 2), 1)
        self.assertEqual(IMath_h.mod(self, 10, 4), 2)
        self.assertEqual(IMath_h.mod(self, 5, 10), 5)
        self.assertEqual(IMath_h.mod(self, 123_456_789, 1234), 25)

        self.assertEqual(IMath_h.mod(self, -2, 2), 0)
        self.assertEqual(IMath_h.mod(self, -3, 2), -1)
        self.assertEqual(IMath_h.mod(self, 10, -4), 2)
        self.assertEqual(IMath_h.mod(self, -10, -4), -2)

    ##
    # @brief Testování funkce mod, je-li operand num2 roven nule.
    # @param num2 se nesmí rovnat nule.
    def test_mod_zero_num2(self):

        with self.assertRaises(ZeroDivisionError):
            IMath_h.mod(self, 0, 0)
            IMath_h.mod(self, 2, 0)

    ##
    # @brief Testování funkce mod, jsou-li operandy num1 a num2 záporná čísla.
    # @param num1 nesmí být záporné číslo
    # @param num2 nesmí být záporné číslo
    def test_mod_float_nums(self):

        with self.assertRaises(ValueError):
            IMath_h.mod(self, 2, 1.5)
            IMath_h.mod(self, 1.5, 2)
            IMath_h.mod(self, 1.5, 5.5)


if __name__ == '__main__':
    unittest.main()
