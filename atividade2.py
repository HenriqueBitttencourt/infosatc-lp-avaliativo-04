palavra1 = input("Insira unma palavra: ")
palavra2 = input("Insira outra palavra: ")
palavra1 = palavra1[::-1]
if (palavra1 == palavra2):
    print("As palavras são as mesmas, e invertidas! ")
elif(palavra1 != palavra2):
    print("Não são a mesma palavra! ")