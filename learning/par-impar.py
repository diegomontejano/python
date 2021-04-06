num = int(input("Digite um número inteiro: "))
if (num % 2 == 0): # Todo número dividido por 2 com RESTO(%) 0 é PAR, e com RESTO(%) 1 é IMPAR. Também aplicamos este método para descobrir anos bissextos, mas substituindo o 2 pelo 4, sendo RESTO(%) 0 é PAR (366: bissexto), e com RESTO(%) 1 é IMPAR (365: não bissexto)
    print("{} é par!".format(num))
else:
    print("{} é impar!".format(num))