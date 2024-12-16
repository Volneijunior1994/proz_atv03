"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""
andar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,21]

for andar in range(1, 21):
    if andar == 13:
        continue
    print(andar)


while andar <= 20:
    if andar == 13:
        andar += 1
        continue
    print(andar)
    andar += 1    

for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)  
    
      
andar = 20
while andar >= 1:
    if andar == 13:
        andar -= 1
        continue
    print(andar)
    andar -= 1