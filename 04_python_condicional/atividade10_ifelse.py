nome = input("digite seu nome: ")
telefone = input("digite seu telefone: ")
cidade = input("digite sua cidade: ")
salario = float(input("digite seu salario: "))
if salario>= 1000:
    print(nome,"você possui uma renda boa!")
elif salario>=700:
    print(nome,"você possui uma renda razoável!") 
elif salario >=500:
    print(nome,"você possui uma renda baixa!")
else:
    print(nome,"você possui uma renda muito baixa!")