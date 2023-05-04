a = input('Você deseja a tabuada ou o numero exato?')

if  a.find('ex' or 'EX' or 'Ex'):
    try:   
        ntb = int(input('X'))
        ran = int(input('{} x ?'.format(ntb)))
        ran = range(ran)
        for i in ran:
            result = ntb * i
            print('{} x {} = {}'.format(ntb,i,result))
    except ValueError:
        print('Coloque um numero valido')


else:
    try:   
        ntb = int(input('X'))
        ran = int(input('{} x ?'.format(ntb)))

        result = ntb * ran
        print('{} x {} = {}'.format(ntb,ran,result))
    except ValueError:
            print('Coloque um numero valido')

    