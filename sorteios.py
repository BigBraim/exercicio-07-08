print('')
print('Selecione qual sorteio você quer')
print('R para roleta russa' )
print('L para sorteio de listas' )
nome = input('Escolha entre "R" e "L": ')

match nome:
    case 'R'|'r':
      import roletarussa

    case 'L'|'l':
     import sorteiolista