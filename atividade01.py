x = float(input("Escolha um número entre 0, 1 ou 2: "))
if x == 0:
    print("zero")

elif x == 1:
    print("um")

elif x == 2:
    print("dois")

else:
    print("ERRO")





# Programa para verificar se número são pares ou ímpares 
# O programa deve parar caso sejam informados 5 números pares ou 
# Caso a soma dos ímpares informados passe de 30
# Vamos informar as somas e as quantidades 
# utilizar "break e continue"

numPares = 0
numImpares = 0
somaPares = 0
somaImpares = 0


while True:
    num = int(input("DIgite um número inteiro e positivo: "))
    if num < 0:
        print("O número não pode ser negativo.")
        continue
    if num % 2 == 0:
        numPares += 1   
        somaPares += num
    else:
        numImpares += 1
        somaImpares += num
    if numPares == 5 or somaImpares > 30:
        break
    
print(f"Soma dos pares: {somaPares}")
print(f"Número de pares: {numPares}")

print(f"Soma dos ímpares: {somaImpares}")
print(f"Número de ímpares: {numImpares}")







  
