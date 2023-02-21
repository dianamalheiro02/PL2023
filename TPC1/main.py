# Resposta a TPC1
from math import inf

class SickPerson:
    def __init__(self,idade,sexo,tensao,colestrol,batimento):#temDoenca):
        self.idade=idade
        self.sexo=sexo
        self.tensao=tensao
        self.colestrol=colestrol
        self.batimento=batimento
        #self.temDoenca=temDoenca

    def __str__(self):
        return f"Idade: {self.idade}, Sexo: {self.idade}, Tensao: {self.idade}, Colestrol: {self.idade}, Batimento: {self.idade}" #Tem Doenca: {self.idade}"

def parse(file):
    personBuffer=[]
    idadeMax=0
    mC=0
    maiorC=0

    crs = open(file, "r")
    crs.readline()

    for line in crs:
        line = line.rstrip().split(',')
        #print(line[5])
        if line[5] == "1":
            sp = SickPerson(int(line[0]),line[1],int(line[2]),int(line[3]),int(line[4]))
            personBuffer.append(sp)

            if(sp.idade>idadeMax):
                idadeMax=sp.idade
            if(sp.colestrol<mC):
                mC=sp.colestrol
            if(sp.colestrol>maiorC):
                maiorC=sp.colestrol
    print(len(personBuffer))
    return personBuffer, idadeMax, mC, maiorC

def sexDivision(personBuffer):
    masc=0
    fem=0

    #filter(lambda item: item[] expression, iterable)
    lmasc = list(filter(lambda x:x.sexo=='M',personBuffer))
    masc = len(lmasc)
    m=masc/len(personBuffer)

    lfem = list(filter(lambda x:x.sexo=='F',personBuffer))
    fem = len(lfem)
    f=fem/len(personBuffer)

    return {"Masculino": (float(m)), "Feminino": float(f)}
        #print("Masc: %f" % m)
        #print("Fem: %f" % f)

def ageDivision(personBuffer,idadeMax):
    min=30
    max=idadeMax

    dictionary = {}
        
    while min <= max:
        age = list(filter(lambda x:min<x.idade<min+5,personBuffer))
        dictionary[f"[{min}-{min+4}]"]=len(age)/len(personBuffer)
        #print(f"[{min}-{min+4}]: {len(age)}")
        min = min + 5

    return dictionary

def colDivision(personBuffer,colMin,colMax):
    min=colMin
    max=colMax

    dictionary={}

    while min <= max:
        col = list(filter(lambda x:min<x.colestrol<min+10,personBuffer))
        dictionary[f"[{min}-{min+9}]"]= len(col)/len(personBuffer)
        #print(f"[{min}-{min+9}]: {len(col)}")
        min = min + 10
        
    return dictionary

def get_tabela(distribution):
    res = ""
    for key, value in distribution.items():
        res += f"{key: ^20} | {(value * 100): ^20}\n"
    return res

def main():
    buffer, idade, minC, maxC = parse('myheart.csv')
    distribution = {1: sexDivision(buffer), 2: ageDivision(buffer, idade), 3: colDivision(buffer, minC, maxC)}
    escolha = 1
    while escolha != 0:
        escolha = int(input("Qual distribuicao deseja visualizar: \n1 - Sexo\n2 - Idade\n3 - Colesterol\n0- Sair: "))
        if escolha != 0:
            distributionVar = distribution[escolha]
            #print(distribution)
            print(get_tabela(distributionVar))

if __name__ == "__main__":
    main()
