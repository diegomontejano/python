preco=(float(input("Insira o valor do produto: ")))
desc=float(input("Insira o valor do desconto: "))
final=preco-desc
print("Seu produto custará R${:.2f} com R${:.2f} de desconto.".format(final, desc))
