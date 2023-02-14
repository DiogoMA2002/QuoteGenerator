import random
import os
 
def obternome():
    for x in os.listdir():
        if x.endswith(".txt"):
            return x

def criarFicheiro():
    filename = input("Insert the filename > ")
    filename += ".txt"
    file = open(filename, "x")

def inserirQuote():
    filename = obternome()
    file = open(filename, "a")
    quote = input("Insert a Quote > ")
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


opcao = input("Chose a option:\n0-Create a new file\n1-Insert a Quote\n2-Generate a quote\n3-Exit\n> ")
if(opcao == "0"):
    criarFicheiro()
elif(opcao == "1"):
    inserirQuote()
elif(opcao == "2"):
    verQuote()
elif(opcao == "3"):
    exit()
else:
    print("Insert a valid Option")
    
