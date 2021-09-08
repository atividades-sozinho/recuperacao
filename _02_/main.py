from recuperacao._02_.soma import SomaEstatica

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
lista = [a, b]
total = SomaEstatica.soma(lista)
print('A soma entre estes números é', total)



