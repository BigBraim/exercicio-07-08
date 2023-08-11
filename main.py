print ('Escolha entre "número real", "hipotenusa", "sct"(seno, cosseno, tangente), e "sorteios" ')
print ('número real: N')
print ('hipotenusa: H')
print ('seno, cosseno e tangente: sct')
print ('sorteios: s')

nome = input('Escollha entre N, H, SCT, S: ')

match nome:
    case 'N'|'n':
        import numberreal

    case 'H'|'h':
        import hipotenusa

    case 'sct'|'SCT':
        import sct

    case 'S'|'s':
        import sorteios

    case _:
        ValueError
        print('ERRO: Digite apenas LETRAS entre N, H, SCT, S! ')


