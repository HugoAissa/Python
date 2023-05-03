des = float(input('Digite a porcentagem do desconto'))
n = float(input('Digite o numero sem desconto'))


a = des/100 * n
result = n - a

print('O valor do seu desconto será de {}\nO valor final será de {}'.format(a,result))
