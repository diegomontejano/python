preco=float(input("Insira o preço do litro: "))
consumo=float(input("Insira o consumo por litro: "))
km=float(input("Insira o km da viagem: "))
media=(km/consumo)*preco
print("Você gastará R${:.2f} neste trajeto.".format(media))
