#Desafio da aula 4
#
#Utilizando a programação por blocos crie um algoritmo que crie
#uma lista com cinco valores e com estes 5 valores ache a media entre eles.
#Lembrando, a conta para achar a media entre os valores
# é realizada somando todos os valores e dividido pelo número de valores somados.

def lista_valores(y):
    x = []
    #y = int(input("Insira o tamanho da lista: "))
    for n in range(y):
        x.append(int(input("Informe o número: ")))

    return (x)

#print(lista_valores())

def soma(y):
    n = lista_valores(y)
    soma_total = 0
    for p in n:
        soma_total = soma_total + p

    print("Total: %d" % soma_total)

    return (soma_total)

def media(x,y):

    m = x / y

    return(m)

y = int(input("Insira o tamanho da lista: "))
total = soma(y)
medi = media(total, y)

print("Sua média será de %2.f" % medi)

