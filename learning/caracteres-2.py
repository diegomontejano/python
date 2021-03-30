# Fatiamento de caracteres é usado para selecionar APENAS os caracteres especificados. A sequência começa no 0, excluindo o último caracter.
frase=str("Curso em vídeo")

print("Curso" in frase) # Exibe se existe a palavra na frase com True/False
print(frase[0]) # Exibe o primeiro caracter
print(frase[:14]) # Exibe do primeiro caracter ao 14
print(frase[9:]) # Exibe do caracter 9 ao final
print(frase[6:14]) # Exibe do caracter 6 ao 14  
print(frase.replace("vídeo", "casa")) # Substitui os termos
print(frase.lower()) # deixa tudo em minúsculo
print(frase.upper()) # DEIXA TUDO EM MAIÚSCULO
print(frase.title()) # Deixa Primeira Letra Em Maiúsculo
print(frase.capitalize()) # Deixa primeira letra em maiúsculo
print(frase.strip()) # Remove os espaços vazios digitados no início e no final do campo input
print(frase.split()) # Cria uma lista das palavras com espaços entre elas
print("Am" + "e" *10 + "i") # Escreve o caracter X vezes... Ameeeeeeeeeei
