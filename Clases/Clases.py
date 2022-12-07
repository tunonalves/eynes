<<<<<<< HEAD
#Clases
=======
import math

class circulo():
    __area = 0
    __perimetro = 0

    def __init__(self,radio):
        self.radio = radio

    def __Area(self):
        area = self.radio * math.sqrt(math.pi)
        return area

    def __Perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def getDatos(self):
        return "El Area es: {} "+ str(self.__Area())+" y el Perimetro es: {} "+ str(self.__Perimetro())


def valida():   
    try:
        radio = float(input("RADIO: "))
        if radio >= 1:
            calculos = circulo(radio)
            print(calculos.getDatos())
            valor = str(input("Desea ingresar otro valor? Y / N: "))
            valor.upper()
            if valor in ['y', 'Y', 'yes', 'Yes', 'YES']:
                valida()
            else:
                exit()
        else:
            print("El valor debe ser mayor que 0")
            valida()
    except ValueError:
        print("Valor erroneo")
        valida()
    except TypeError:
        print("Valor incorrecto")
        valida()

valida()
>>>>>>> clases
