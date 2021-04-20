item = []
mercado = []

for i in range(3):
    item.append(input("Digite o nome do item: "))
    item.append(int(input("Digite a quantidade: ")))
    item.append(float(input("Digite o valor: ")))
    mercado.append(item[:]) #  Usamos [:] para alterarmos os valores deste "item", mentendo os valores do "item" original
    item.clear()
print(mercado) 