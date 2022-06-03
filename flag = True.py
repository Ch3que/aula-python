flag = True 
contador = 0
media =0 

numero = int(input("digite um numero"))

soma= numero 
menorNumero = numero
maiorNumero= numero 
 
if numero == 0: 
    flag =False 
else:
    contador = contador + 1 

while flag: 
    numero = int(input("digite um numero"))
    if numero !=0:
        soma += numero 
        contador += 1 

        if numero > maiorNumero:
            maiorNumero = numero 
        if numero < menorNumero:
            menorNumero = numero     
    else: 
        flag = False

if soma != 0:
    media =soma / contador 

print(f"a soma é:{soma}\n a media é: {media}\nO maior numero é: {maiorNumero}\nO menor numero è: {menorNumero}")
