a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    print("Existem duas raízes reais distintas")

elif delta == 0:
    print("Existem duas raízes reais iguais")

else:   
    print("Existem duas raízes imaginárias conjugadas")