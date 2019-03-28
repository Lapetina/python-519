"""
Desafio da aula 03

Utilizando a programação por blocos, crie um algoritmo que receba dois valores, o
primeiro deles será o peso em quilogramas, o segundo, a altura em metros.
Com estes dados, faremos o cálculo do IMC(Índice de massa corporal), realizado com a
seguinte fórmula:

PESO / (ALTURA * ALTURA)

Após executar a fórmula, informe o resultado da operação e a classificação dos dados, de
acordo com a tabela das anotações.

Tabela:
menor que 18.5 = Baixo peso
maior que 18.5 e menor que 24,9 = Peso ideal
maior que 25 e menor que 29,9 = Sobrepeso
maior que 30 e menor que 34,9 = Obesidade 1º
maior que 35 e menor que 39,9 = Obesidade 2º
maior que 40 = Obesidade grave

"""

def calcular_imc(peso, altura):
    taxa = peso / (altura * altura)
    return taxa

kg = float(input("Digite seu peso:"))
kg = round(kg, 2)

a = float(input("Digite sua altura:"))
a = round(a, 2)

taxa = calcular_imc(kg,a)

if taxa < 18.5:
    print("Baixo do peso, IMC %.2f" % taxa)

elif taxa >18.5 and taxa<24.9:
    print("Peso ideal, IMC %2.f" % taxa)

elif taxa > 25 and  taxa<29.9:
    print("Sobrepeso %2.f" % taxa)

elif taxa > 30 and taxa<34.9:
    print("Obesidade 1º, IMC %2.f" % taxa)

elif taxa > 35 and taxa<39.9:
    print("Obesidade 2º,  IMC %2.f" % taxa)

else:
    print("Obesidade grave, IMC %2.f" % taxa)