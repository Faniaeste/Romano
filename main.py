"""
1- Crear una función que pase de entero >0 y <4000 a romano.
2- Cualquier otra entrada da error.
3- Limite 3999.

casos prueba
a-1994 -> MCMXCIV
b-4000 ->RomanNumberError() el valor debe ser menor a 4000
c-"una cadena" -> RomanNumberError

M -> 1000
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1

diccionario = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
unidades ={1:'I', 2:'II', 3: 'III',4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'VX'}
decenas = {10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC'}
centenas = {100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM'}
millares ={1000:'M', 2000:'MM', 3000:'MMM'}
"""
#--------------------------PRIMERA PRUEBA FALLIDA-----------------------------------------------------------------
"""
    for i in range(0,len(numero_list)):
        if i == 0:
            numero_list[i] = int(numero_list[i]) * 1000
            valor_romano += millares.get(numero_list[i])#M
        if i == 1:
            numero_list[i] = int(numero_list[i]) * 100
            valor_romano += centenas.get(numero_list[i])#CM
        if i == 2:
            numero_list[i] = int(numero_list[i]) * 10
            valor_romano += decenas.get(numero_list[i])#XC
        if i == 3:
            numero_list[i] = int(numero_list[i])
            valor_romano += unidades.get(numero_list[i])#IV
        
            if len(numero) == 3:
                numero = '0' + numero
            elif len(numero) == 2:
                numero = '00' + numero
            elif len(numero) == 1:
                numero = '000' + numero
"""            
           
"""           for i in range(0,len(list_romano)):
            if i != 0:
            if dic_romano_a_entero.get(list_romano[i-1]) < dic_romano_a_entero.get(list_romano[i]):
            valor_entero -= dic_romano_a_entero.get(list_romano[i-1])
            valor_entero += dic_romano_a_entero.get(list_romano[i]) - dic_romano_a_entero.get(list_romano[i-1])
            else:
            valor_entero += dic_romano_a_entero.get(list_romano[i])
            else: 
            valor_entero = dic_romano_a_entero.get(list_romano[i])
""" 
"""
            if caracter_anterior == 'I' and (caracter != 'V' or caracter != 'X'):
                valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2
                
            
            elif caracter_anterior == 'I' and (caracter != 'V' or caracter != 'X'):
                valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2
            
            else:
                raise RomanNumberError('"X"sólo se puede restar de "V" y "X"')
"""           

 
#--------------------------PRIMERA PRUEBA FALLIDA-----------------------------------------------------------------
dic_romano_a_entero = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

dic_entero_a_romano = {
    1:'I', 2:'II', 3: 'III',4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'VX',
    10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',
    1000:'M', 2000:'MM', 3000:'MMM'}

regla_restas = {'I':('V','X'),'X':('L','C'),'C':('D','M')}

class RomanNumberError( Exception ):
    pass

#a-1994 -> MCMXCIV
def romano_a_entero(romano:str)->int:
    list_romano = list(romano)
    valor_entero = 0
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
            
            valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2

            if caracter_anterior and (caracter_ante_anterior == caracter_anterior) and caracter_anterior in "IXC":
                raise RomanNumberError("I,X,C ya no pueden restarse porque tiene dos repeticiones")



        caracter_ante_anterior = caracter_anterior    
        caracter_anterior = caracter
        valor_entero += dic_romano_a_entero.get(caracter,0)

            
   
    return valor_entero

#print(romano_a_entero("IIX"))


def entero_a_romano(numero:int )->str:
    if numero < 0 or numero > 3999:
        raise RomanNumberError("El limite esta entre mayor a 0 y 3999")
    
    if numero == 0:
        return ""
    

    numero = "{:0>4d}".format(numero)
    numero_list = list(numero)
    valor_romano = ''
    cont = 0
    valor_num = 1000
    while cont < len(numero_list):
        numero_list[cont] = int(numero_list[cont]) * valor_num
        valor_romano += dic_entero_a_romano.get(numero_list[cont])
        cont += 1
        valor_num /= 10

    return valor_romano