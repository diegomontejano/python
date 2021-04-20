mercado = []

for i in range(3):
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor: "))
    mercado.append([nome, quantidade, valor])
print(mercado)