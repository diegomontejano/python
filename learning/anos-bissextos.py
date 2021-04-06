ano=int(input("Digite um ano para saber se é bissexto: ")) 
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano {} É BISSEXTO.".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO.".format(ano))

    #Todo número dividido por 2 com RESTO(%) 0 é PAR, e com RESTO(%) 1 é IMPAR. Também aplicamos este método para descobrir anos bissextos, mas substituindo o 2 pelo 4, sendo RESTO(%) 0 é PAR (366: bissexto), e com RESTO(%) 1 é IMPAR (365: não bissexto).