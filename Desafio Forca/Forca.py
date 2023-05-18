import random

palavras = ["gato", "cachorro", "carro", "lagoa", "puc", "audi", "mustang", "orlando", "nova york", "porche"]
palavra = random.choice(palavras)
chances = 10
atualmente = ['_'] * len(palavra)

print("\n***Jogo Da Forca***\n")
print(f"\n***Regras***\n")
print("Você tem 6 chances para acertar a palavra.\nSe você não acertar, já era!!")
print(f"\n**GOOD GAME***\n")

for tentativas in range(chances):
    letra = input(f"\nDigite uma letra: ")
    print(f"\nTentativas: {tentativas+1}\n") 
    if letra in palavra:
        print(f"\nA letra que você colocou tem na palavra\n")
        for item in range(len(palavra)):
            if letra == palavra[item]:
                atualmente[item] = letra
    else:
        print(f"\nA letra que você colocou não tem na palavra\n")
    
    print(" ".join(atualmente))
    
    if '_' not in atualmente:  
        break

if '_' in atualmente:
    print("\nVocê perdeu, acabaram suas tentativas\n")
else:
    print("\nVocê acertou a palavra, PARABÉNSSS!!\n")

print(f"A palavra era {palavra}")
