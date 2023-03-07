#Resposta a TPC3
import re
import json

def processosAno():
    file = open("processos.txt",'r')
    x = re.findall(":\d{4}", file)
    dictionary = {}

    for element in x:
        dictionary[element]+=1

    return dictionary


def nomeSeculo(seculo):
    nomeProprio={}
    apelido={}

    file = open("processos.txt",'r')
    for line in file.readlines():
        #Ano
        x = re.findall(":\d{4}", line)
        ano=x.strip(":")

        if ano<seculo:
            #Nome todo
            y = re.findall(":[A-Za-z\s]+:",line)
    
            for name in y:
                aux = name.strip(":")
                nome = aux.split(" ")
                
                a = nome.len()
                primeiro=nome[0]
                ultimo=nome[a]

                nomeProprio[primeiro]+=1
                apelido[ultimo]+=1

    for i in sorted(nomeProprio, key = nomeProprio.get, reverse=True):
        print(i, nomeProprio[i])

    print("\n")

    for i in sorted(apelido, key = apelido.get, reverse=True):
        print(i, apelido[i]) 
    
    print("\n")


def relacao():
    file = open("processos.txt",'r')
    x=re.findall(",(?P<grau>\w+)",file)

    res={}
    for relacao in x:
        res[relacao]+=1

    return res


def main():
    opcao = input("--- MENU ---:\n1. Calcula a frequência de processos por ano.\n2. Saber os 5 nomes próprios e apelidos mais usados por século.\n3. Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.\n4. Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.\n\nEscoha a opção a realizar:")

    match opcao:
        case "1":
            result1 = processosAno()
            for key,value in result1:
                print(f"{key}:  | Frequência: {value}\n")

        case "2":
            print("Os 5 nomes e apelidos mais populares, ordenados por séculos são, respetivamente:")
            print("Século 17: ")
            nomeSeculo(1700)
            print("Século 18: ")
            nomeSeculo(1800)
            print("Século 19: ")
            nomeSeculo(1900)
            print("Século 20: ")
            nomeSeculo(2000)

        case "3":
            result3 = relacao()
            for key,value in result3:
                print(f"{key}:  | Frequência: {value}\n")

        case "4":
            file = open("processos.txt",'r')
            processo=[20]
            i=0
            while i<20:
                processo.append(file.readline())
                i+=1
                            
            with open("processos.json", "w") as arquivo:     
                json.dump(processo, arquivo, indent=4)

        case _:
            print(" ")


if __name__ == "__main__":
    main()
