# autor: Maria Eduarda
# Projeto: IMC com input e f-string

# Declaração de variáveis
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso / (altura * altura)
# exibindo os resultados 
print(f"o seu imc é: {imc:.2f}")