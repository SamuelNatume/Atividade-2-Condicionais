idade = float(input("Digite a sua idade em anos: "))
tempo_de_serviço = float(input("Digite o seu tempo de serviço em anos: "))

if idade >= 65 or tempo_de_serviço >= 30 or idade >= 60 and tempo_de_serviço >= 25:
    print("Pode se aposentar")

else:
    print("Ainda não pode se aposentar")