def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

palavra_secreta = "yuri alberto"
enforcou = False
acertou =  False

while (not enforcou and not acertou):
    chute = input("Qual é a letra ?")

    for  letra in palavra_secreta:
      if(chute == letra):
          print(chute)


print("jogando...")
print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
