n = int(input('Digite um numero de 0 a 9999'))
calcu = n % 10
n = n - calcu
calcd = n % 10
n = (n - calcd)/10

print('Unidade: {} \n Dezena: {} \n '.format(calcu,calcd))


