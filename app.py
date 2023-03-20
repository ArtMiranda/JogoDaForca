import os, random, time
from termcolor import colored
from unidecode import unidecode

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

with open("palavras.txt", "r") as arquivoPalavras:
    linhas = arquivoPalavras.readlines()
    stringpalavras = " ".join(linhas)
    listaPalavras = stringpalavras.split()

palavraSecreta = unidecode(random.choice(listaPalavras).upper())

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

while (tentativasnum >= 1) :
    print(" ")
    print(" ")
    letraTentada = input("Digite o palpite de letra: ").upper()
    tentativas.append(letraTentada)

    while (len(letraTentada) != 1) :
        print(colored("Você deve digitar apenas uma letra", "red")) 
        letraTentada = input("Digite o palpite de letra: ").upper()

    if letraTentada in palavraSecretaList :
        for i, letra in enumerate(palavraSecretaList) :
            if letra == letraTentada :
                palavraSecretaCheck[i] = letraTentada
                correto = 1
                clear()


        if '_' not in palavraSecretaCheck:
            print (colored(f"Parabéns!, a palavra secreta era {palavraSecreta}", "blue"))
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
        print(" ")
        print(colored("Letra correta!", "green"))

    if (correto == 0) :
        print (" ")
        print (" ")
        print(colored("Letra incorreta.", "red"))
        tentativasErradas.append(letraTentada)

    print(f"Restam {tentativasnum} tentativas")
    print(colored(f"Tentativas erradas: {tentativasErradas}", "yellow"))


if '_' in palavraSecretaCheck:
    print(" _________")   # imprime a linha superior do enforcado
    time.sleep(0.5)

    print(" |         |")  # imprime a primeira linha vertical do enforcado
    time.sleep(0.5)

    print(" |         O")  # imprime a cabeça do enforcado
    time.sleep(0.5)

    print(" |        /|\\") # imprime os braços do enforcado
    time.sleep(0.5)

    print(" |        / \\") # imprime as pernas do enforcado
    time.sleep(0.5)

    print("_|_")           # imprime a base do enforcado
    time.sleep(3)

    clear()

    print(colored("Suas tentativas acabaram, tente novamente.", "yellow"))



if (tentativasnum < 1) :
    clear()
    print(colored(f"A palavra secreta era {palavraSecreta}, tente novamente!", "light_magenta"))