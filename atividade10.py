print("Digite as suas duas notas bimestrais\n")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print("Selecione a Universidade")
print("1. PUCPR")
print("2. UNICAMP")

media = (nota1 + nota2) / 2

escolha = int(input("Digite sua escolha (1 ou 2): "))

if escolha == 1:

    if media >= 7.0:
        print("Aprovado")
    elif 4.0 <= media < 7.0:
        print("Em exame")
    else:
        print("Reprovado")

elif escolha == 2:
    
    if media >= 5.0:
        print("Aprovado")
    else:
        print("Reprovado")