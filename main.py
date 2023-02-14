import random
import os
 
def obternome():
    for x in os.listdir():
        if x.endswith(".txt"):
            return x

def criarFicheiro():
    filename = input("Insira o nome do ficheiro > ")
    filename += ".txt"
    file = open(filename, "x")

def inserirQuote():
    filename = obternome()
    file = open(filename, "a")
    quote = input("Insira uma Quote > ")
    quote 
    file.write(quote + "\n")
    file.close
    
def verQuote():
    i = getNumLines()
    file = obternome()
    with open(file, 'r') as fp:
        content = fp.readlines()
        print(content)
    print(content[i])

def getNumLines():
    file = obternome()
    with open(file, 'r') as fp:
        numLinhas = len(fp.readlines())
        i = random.randint(0, numLinhas-1)
    return i


opcao = input("Insira a Opção desejada:\n0-Criar novo ficheiro\n1-Inserir Quote\n2-Ver uma quote\n3-Sair\n> ")
if(opcao == "0"):
    criarFicheiro()
elif(opcao == "1"):
    inserirQuote()
elif(opcao == "2"):
    verQuote()
else:
    exit()
    