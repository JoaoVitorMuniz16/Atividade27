pali = input('Digite um palavra: ').upper().replace(' ','')
if pali == pali[:: -1]:
    print('A palavra é Palindroma','\n')
    print('Palavra Invertida: {}'.format(pali),'\n')
else:
    print('A palavra não é Palindroma','\n')
print('Palavra Digitada: {} '.format(pali),'\n')