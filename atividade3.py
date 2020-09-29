cpf=[]
apto=[]
nome=[]
senha=[]
def funcaoUsuarios(x, y, nome, cpf, senha, apto):
    print("")
    print("O nome do usuário ", x,"é ",nome[y])
    print("O cpf do usuário ", x,"é ",cpf[y])
    print("A senha do usuário ", x,"é ",senha[y])
    print("O usuário ", x," esta apto? ",apto[y])
def cadastro():
    apto.append(input("Insira o seu apto: "))
    cpf.append(input("Insira o seu cpf: "))
    nome.append(input("Insira o seu nome: "))
    senha.append(input("Insira o seu senha: "))
quantidadepessoas = (int(input("Insira o número de pessoas que irão realizar o teste: ")))
for x in range(quantidadepessoas):
    ap=""
    print("")
    user = 0
    variavel = 0
    peso = (float(input("Insira o seu peso: ")))
    idade = (int(input("Insira a sua idade: ")))
    tempo = (float(input("Insira quanto tempo você dormiu nas últimas 24h(em horas)! ")))
    if idade > 16 and idade < 69:
        variavel = variavel + 1
    else:
        ap = "idade " + ap
    if peso > 50:
        variavel = variavel + 1
    else:
        ap = "peso " + ap
    if tempo > 6:
        variavel = variavel + 1
    else:
        ap = "sono " + ap

    if variavel == 3:
        print("É um doador válido!")
        alternativa=(input("Quer se cadastrar? (s/n): "))
        if (alternativa == "s"):
            user = user + 1
            cadastro()
        else:
            pass
    else:
        print("Não está apto à doação!")
for x in range(user):
    contador = x + 1
    funcaoUsuarios(contador, x, nome, cpf, senha, apto)