







altura = float(input("Digite a sua altura: "))
sexo = input("Qual é o seu sexo (homem ou mulher?): ")

def peso_ideal_homem(altura):
    return (72.7 * altura) - 58

def peso_ideal_mulher(altura):
    return (62.1 * altura) - 44.7

if sexo == "homem":
    peso_ideal_homens = peso_ideal_homem(altura)
    print("Seu peso ideal é: {:.2f} kg".format(peso_ideal_homens))

elif sexo == "mulher":
    peso_ideal_mulheres = peso_ideal_mulher(altura)
    print("Seu peso ideal é: {:.2f} kg".format(peso_ideal_mulheres))

else:
    print("Sexo não reconhecido. Por favor, digite 'homem' ou 'mulher'.")


  
