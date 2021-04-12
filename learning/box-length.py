def box(x):
    length = len(x)  # Cria uma caixa ajustável com a mesma qnt de caracteres da string
    if length:
        print("+", "-" * length, "+")
        print("|", x, "|")
        print("+", "-" * length, "+")

box("Diego")