largura = int(input('Digite a largura da sua parede'))
altura = int(input('Digite a altura da sua parede'))

area = altura * largura
result = area / 2**2 
result = area * 1000

print('A area da sua parade é {}ᵐ² \nPor conta disso Você ira precisar de {} litros de tinta'.format(area,result))
