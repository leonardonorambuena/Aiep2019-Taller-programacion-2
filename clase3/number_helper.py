class NumberHelper():

    @staticmethod
    def is_par(number):
        return number % 2 == 0

    @staticmethod
    def is_prime(number):
        if number < 2:
            return False

        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def factorial(number):
        result = 1
        for i in range(number + 1):
            result *= i 

        return result
