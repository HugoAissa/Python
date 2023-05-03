
n = float(input('Digite seu salario atual'))
des = float(input('Digite qual a porcentagem que deseja aumentar'))

a = des/100 * n
result = n + a

print('Você recebeu {}% de desconto, então recebera {}R$'.format(des,result))
