__author= 'Antonio Getsemani'

def SumaArreglo(ListaNumero):
    if len(ListaNumero) == 1:
        return ListaNumero[0]
    else:
        return ListaNumero[0] + SumaArreglo(ListaNumero[1:])
print(SumaArreglo([2,3,4,1]))