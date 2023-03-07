#Resposta a TPC3
import re
import json

def processosAno(file):
    #file = open("processos.txt",'r')
    dictionary = {}

    for line in file.readlines():
        x = re.search(r':\d{4}', line) 

        if x!=None:   
            ano=x[0]
            if ano in dictionary:
                dictionary[ano]+=1
            else:
                dictionary[ano]=1
    
    for key,value in dictionary.items():
        print(f"{key}:  | Frequência: {value}")


def nomeSeculo(seculo,file):
    nomeProprio={}
    apelido={}

    #file = open("processos.txt",'r')
    for line in file.readlines():
        x = re.search(r':\d{4}', line)

        if x!=None:
            aux=x.group()
            aux2=aux.strip(":")
            ano=int(aux2)

            if ano < seculo:
                y = re.findall(r":[A-Za-z\s]+:",line)

                for name in y:
                    #aux = name.group()
                    aux2 = name.strip(":")
                    nome = aux2.split(" ")
                    
                    a = len(nome)
                    primeiro=nome[0]
                    ultimo=nome[a-1]

                    if primeiro in nomeProprio:
                        nomeProprio[primeiro]+=1
                    else:
                        nomeProprio[primeiro]=1

                    if ultimo in apelido:
                        apelido[ultimo]+=1
                    else:
                        apelido[ultimo]=1

    list1=sorted(nomeProprio, key = nomeProprio.get, reverse=True)
    res=0
    while res<5: 
        if res in range(len(list1)):
            print(list1[res])
        res+=1

    #for i in sorted(nomeProprio, key = nomeProprio.get, reverse=True):
    #    print(i, nomeProprio[i])

    print("\n")

    list2=sorted(apelido, key = apelido.get, reverse=True)
    res=0
    while res<5: 
        if res in range(len(list2)):
            print(list2[res])
        res+=1
    
    #for i in sorted(apelido, key = apelido.get, reverse=True):
    #    print(i, apelido[i]) 
    
    print("\n")


def relacaoStats(file):
    #file = open("processos.txt",'r')
    res={}

    for line in file.readlines():
        x=re.findall(r'(Irmao\.|Tio|Sobrinho|Primo|Irmaos|Pai\.|Filho\.|Sobrinhos|Avo\s|,Neto\s|Tios|Filhos\.|Primos|,Bisavo)',line)

        for relacao in x:
            if relacao in res:
                res[relacao]+=1
            else:
                res[relacao]=1

    return res


def main():
    opcao = input("--- MENU ---:\n1. Calcula a frequência de processos por ano.\n2. Saber os 5 nomes próprios e apelidos mais usados por século.\n3. Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.\n4. Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.\n\nEscoha a opção a realizar:")

    file = open("processos.txt",'r')
    
    match opcao:
        case "1":
            processosAno(file)
            #result1 = processosAno()
            #for key,value in result1:
            #    print(f"{key}:  | Frequência: {value}\n")

        case "2":
            print("Os 5 nomes e apelidos mais populares, ordenados por séculos são, respetivamente:")
            print("Século 17: ")
            nomeSeculo(1700,file)
            print("Século 18: ")
            nomeSeculo(1800,file)
            print("Século 19: ")
            nomeSeculo(1900,file)
            print("Século 20: ")
            nomeSeculo(2000,file)

        case "3":
            result3 = relacaoStats(file)
            for key,value in result3.items():
                print(f"{key}:  | Frequência: {value}")

        case "4":
            #file = open("processos.txt",'r')
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
