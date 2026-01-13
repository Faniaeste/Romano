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
"""
diccionario = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
unidades ={1:'I', 2:'II', 3: 'III',4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'VX'}
decenas = {10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC'}
centenas = {100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM'}
millares ={1000:'M', 2000:'MM', 3000:'MMM'}

dic_entero_a_romano = {
    1:'I', 2:'II', 3: 'III',4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'VX'
    10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC'
    100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM'
    1000:'M', 2000:'MM', 3000:'MMM'}

class RomanNumberError( Exception ):
    pass

#a-1994 -> MCMXCIV
def entero_a_romano(numero):
    numero = str(numero)#Transformar en cadena el valor (numero)
    numero_list = list(numero)#Guardar una lista['1','9','9','4']
    print(numero_list)
    valor_romano = ''
    cont = 0
    valor_num = 1000
    while cont < len(numero_list):
        numero_list[cont] = int(numero_list[cont]) * valor_num
        cont += 1
        valor_num /= 10
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
""" 
#--------------------------PRIMERA PRUEBA FALLIDA-----------------------------------------------------------------
"""          
print(numero_list)#['1','9','9','4']





return valor_romano

print(entero_a_romano(1994))

#1994
#['1','9','9','4']