# -*- coding: utf-8 -*-
class FizzBuzz:
    def convert(self, number):
        stringReturn = ""

        if (number % 3 == 0):
            stringReturn = "Fizz"

        if (number % 5 == 0):
            stringReturn += "Buzz"

        if (len(stringReturn) == 0):
            stringReturn = str(number)

        return stringReturn
