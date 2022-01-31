class Binary:

    def binary_gap_without_library(self, n):
        binary_conversion = self.binary_converter(n)
        gap_max = 0
        gap_counter = 0

        for number in binary_conversion:
            if(number == '0'):
                gap_counter += 1
            else:
                if(gap_max < gap_counter):
                    gap_max = gap_counter
                
                gap_counter = 0

        return binary_conversion, gap_max

    def binary_gap_with_library(self, n):
        if(n <= 0):
            n = 0

        binary_conversion = str(bin(n))[2:]
        gap_max = 0
        gap_counter = 0

        for number in binary_conversion:
            if(number == '0'):
                gap_counter += 1
            else:
                if(gap_max < gap_counter):
                    gap_max = gap_counter
                
                gap_counter = 0
        
        return binary_conversion, gap_max

    # Logical process are there:
    # http://recursostic.educacion.es/secundaria/edad/4esotecnologia/quincena5/4q2_contenidos_2c.htm
    def binary_converter(self, integer_number):
        if(integer_number <= 0):
            integer_number = 0

        binary = ''
        while integer_number // 2 != 0:
            binary = str(integer_number % 2) + binary
            integer_number //= 2
        
        binary = str(integer_number) + binary

        return binary
