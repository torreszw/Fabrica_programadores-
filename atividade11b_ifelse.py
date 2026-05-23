nome = int(input('digite sua nome:'))
idade = int(input('digite sua idade:'))
cnh = input('possui CNH sim ou não:')
if idade >= 18:
    if cnh == 'sim':
        print(f'{nome} você pode dirigir')
    else:
        print(f'{nome} você NÂO pode dirigir')
else:
    print(f'{nome} você é menor de idade')