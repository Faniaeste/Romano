from utils.utiles import *
from romanos_exception import RomanNumberError

class NumeroRomano:
    def __init__(self,valor):
        self.valor = valor
        self.valor_entero = 0
        self.valor_romano = ''
        if isinstance(self.valor,str):  
            #si valor es entero
            self.entero_a_romano(valor)
        elif isinstance(self.valor,int):
            #si el valor es string
            self.romano_a_entero(valor)

    def entero_a_romano(self, numero:int) -> str:
        if numero < 0 or numero > 3999:
            raise RomanNumberError("El limite esta entre mayor a 0 y 3999")
        
        if numero == 0:
            return ""
        
        numero = "{:0>4d}".format(numero)
        numero_list = list(numero)
        self.valor_romano = ''
        cont = 0
        valor_num = 1000
        while cont < len(numero_list):
            numero_list[cont] = int(numero_list[cont]) * valor_num
            self.valor_romano += dic_entero_a_romano.get(numero_list[cont],'')
            cont += 1
            valor_num /= 10

        return self.valor_romano
    
    def romano_a_entero(self, romano:str)->int:
        list_romano = list(romano)
        self.valor_entero = 0
        caracter_anterior = ''
        cont_repes = 0
        caracter_ante_anterior = ''

        for caracter in list_romano:
            if caracter == caracter_anterior:
                if caracter == "D" or caracter == "L" or caracter == "V":
                    raise RomanNumberError("Los caracteres 'D' 'L'y'V' no se pueden repetir")
                
                cont_repes += 1
                if cont_repes > 2:
                    raise RomanNumberError("No se puede repetir el valor más de tres veces")
            else:
                cont_repes = 0

            if dic_romano_a_entero.get(caracter_anterior,0) < dic_romano_a_entero.get(caracter,0):

                if caracter_anterior and caracter_anterior in "VLD":
                    raise RomanNumberError('V,L Y D no se pueden restar')
        
                if caracter_anterior and caracter not in regla_restas[caracter_anterior]:
                    raise RomanNumberError(f"{caracter_anterior} sólo se puede restar de {regla_restas[caracter_anterior][0]} y {regla_restas[caracter_anterior][1]}")
                
                self.valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2

                if caracter_anterior and (caracter_ante_anterior == caracter_anterior) and caracter_anterior in "IXC":
                    raise RomanNumberError("I,X,C ya no pueden restarse porque tiene dos repeticiones")



            caracter_ante_anterior = caracter_anterior    
            caracter_anterior = caracter
            self.valor_entero += dic_romano_a_entero.get(caracter,0)

            
   
        return self.valor_entero
    
    # Devuelve un string de cualquier parametro de una clase
    def __repr__(self):
        if isinstance(self.valor,str):  
            return str(self.valor_entero)
        elif isinstance(self.valor,int):
            return (self.valor_romano)
        
aplicacion = NumeroRomano('IV')
aplicacion2 = NumeroRomano (35)
print(aplicacion)
print(aplicacion2)