import os, random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

with open("palavras.txt", "r") as arquivoPalavras:
    linhas = arquivoPalavras.readlines()
    stringpalavras = " ".join(linhas)
    listaPalavras = stringpalavras.split()

palavraSecreta = random.choice(listaPalavras).upper()

tentativas = []
palavraSecretaList = list(palavraSecreta)
palavraSecretaCheck = []
tentativasErradas = []

for elemento in palavraSecretaList:
    if elemento == " ":
        palavraSecretaCheck.append(" ")
    else:
        palavraSecretaCheck.append("_")
        
tentativasnum = 8
preliminar = ""

for i, letra in enumerate(palavraSecretaCheck) :
    print (preliminar + palavraSecretaCheck[i], end=" ")

while (tentativasnum > 1) :
    print(" ")
    letraTentada = input("Digite o palpite de letra: ").upper()
    tentativas.append(letraTentada)

    if letraTentada in palavraSecretaList :
        for i, letra in enumerate(palavraSecretaList) :
            if letra == letraTentada :
                palavraSecretaCheck[i] = letraTentada
                correto = 1
                clear()


        if '_' not in palavraSecretaCheck:
            print(f"Parabéns!, a palavra secreta era {palavraSecreta}")
            break
    
    if letraTentada not in palavraSecretaList :
        tentativasnum = tentativasnum - 1   
        print (palavraSecretaCheck)
        correto = 0
        clear()

    for i, letra in enumerate(palavraSecretaCheck) :
        print (preliminar + palavraSecretaCheck[i], end=" ")

    if (correto == 1) :
        print(" ")
        print("Letra correta!")

    if (correto == 0) :
        print (" ")
        print("Letra incorreta.")
        tentativasErradas.append(letraTentada)

    print(" ")
    print(f"Restam {tentativasnum} tentativas")
    print(f"Tentativas erradas: {tentativasErradas}")


if '_' in palavraSecretaCheck:
    print("Suas tentativas acabaram, tente novamente.")
    
