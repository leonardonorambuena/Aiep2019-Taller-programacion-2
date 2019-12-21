'''
        Valida un rut chileno
        Ejemplos de uso:
        validator = RutValidator('xxxxxx-x')
        validator = RutValidator('xxxxxxx','x')
    '''
class RutValidator:
    def __init__(self, rut, dv = None):
        if dv == None:
            self.dv = rut[-1].upper()
        else:
            self.dv = dv[0].upper()

        self.numbers_list = [int(i) for i in rut if i.isdigit()]

        if self.dv.isdigit() and dv == None:
            self.numbers_list = self.numbers_list[:-1]

        self.numbers = int(''.join(map(str,self.numbers_list)))

        self.formated_numbers = '{:,}'.format(self.numbers).replace(',', '.')

        self.formated = f'{self.formated_numbers}-{self.dv}'


    def get_dv(self):
        self.inverted_numbers = self.numbers_list[::-1]
        multiplier = 2
        result = 0
        for i in self.inverted_numbers:
            result += i * multiplier
            multiplier = multiplier + 1
            if multiplier == 8:
                multiplier = 2

        result = 11 - (result%11)

        if result == 10:
            return 'K'
        if result == 11:
            return 0
            
        return str(result)

    def is_valid(self):
        return self.get_dv().upper() == self.dv.upper()        


        
    
