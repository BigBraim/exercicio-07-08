from math import hypot
print('')
class test:
    co = float(input('Insira o cateto oposto: '))
    ca = float(input('Insira o cateto adjacente: '))
    h = hypot(co, ca)
    print('A hipotenusa irá medir {:.2f}'.format(h))

continuar = input('você quer continuar? ')

match continuar:
    case 'S'|'s':
        while test:
            co = float(input('Insira o cateto oposto: '))
            ca = float(input('Insira o cateto adjacente: '))
            h = hypot(co, ca)
            print('A hipotenusa irá medir {:.2f}'.format(h))
            break


    case 'N'|'n':
        print('Fim')

