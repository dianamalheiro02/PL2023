#Resposta a TPC5
import re

op1=r'LEVANTAR'
op2=r'MOEDAS\s([0-9]+(c|e)(\,\s|\.))+'
op3=r'POUSAR'
op4=r'T\=((00[0-9]*)|(2[0-9]{8})|(601[0-9]{6})|(641[0-9]{6})|(808[0-9]{6})|(800[0-9]{6}))'
op5=r'ABORTAR'

p1=re.compile(op1)
p2=re.compile(op2)
p3=re.compile(op3)
p4=re.compile(op4)
p5=re.compile(op5)

moedasPssíveis={"5c","10c","20c","50c","1e","2e"}
telefoneNumbers={}

def getInput():
    operacao=input("")
    return operacao

def getSaldoEuro(moeda):
    res=moeda.strip("e")
    return int(res)
    
def getSaldoCent(moeda):
    res=moeda.strip("c")
    return int(res)


def validaChamada(aux,euro,cent):
    flag=0
    euroT=0
    centT=0

    if aux[0] == '0' and aux[1] == '0':
        if euro<1:   
            print("Saldo insuficiente.")
            flag=1
        elif euro == 1:
            if cent<50:
                print("Saldo insuficiente.")
                flag=1
            else:
                euroT=euro
                centT=cent-50
        else:
            euroT=euro-1
            if cent<50:
                centT=cent+(1-50)
            else:
                centT=cent-50

    elif aux[0]=='2':
        if euro<1:
            if cent<25:
                print("Saldo insuficiente.")
                flag=1
            else:
                centT=cent-25
        elif euro == 1:
            if cent>25:
                centT=cent-25
                euroT=euro
            else:
                centT=euro*100-(25-cent)        
                
    elif aux[0]=='6' and (aux[1]=='0' or aux[1]=='4') and aux[2]=='1':
        print("Chamada bloqueada. Dê outro número.")
        flag=2
        euroT=euro
        centT=cent
    
    elif aux[0]=='8' and aux[1]=='0' and aux[2]=='8':
        if euro<1:
            if cent<10:
                print("Saldo insuficiente.")
                flag=1
        elif euro==1:
            if cent>10:
                centT=cent-10
            else:
                centT=euro*100-(10-cent)

    return flag,euroT,centT

def dealWithInput(operacao):
    exit = 1
    cent = 0
    euro = 0

    levantou=0
    dinheiro=0
    chamou=0
    #abortou=0
    #pausou=0

    while exit!=0:
        a=re.match(p1,operacao)
        b=re.match(p2,operacao)
        c=re.match(p3,operacao)
        d=re.match(p4,operacao)
        e=re.match(p5,operacao)

        if a:
            print("Introduza moedas.")
            operacao=getInput()

            levantou=1
            exit+=1
        
        elif b:
            if exit == 1 or levantou==0:
                operacao="ABORTAR"
            else:
                listM=re.sub('MOEDAS ','',operacao)
                aux=re.sub('\,','',listM)
                listMoedas=re.sub('\.','',aux)

                moedas=listMoedas.split(" ")

                for moeda in moedas:
                    if moeda != "MOEDAS " and moeda not in moedasPssíveis:
                        print(f"{moeda} - moeda inválida;")
                    else:
                        if moeda == "1e" or moeda == "2e":
                            euro += getSaldoEuro(moeda)
                        else:
                            cent += getSaldoCent(moeda)
                
                print(f"Saldo = {euro}e{cent}c")
                
                dinheiro=1
                operacao=getInput()
                exit+=1

        elif c:
            if exit == 1  or chamou==0:
                operacao="ABORTAR"
            else:
                print(f"Troco = {euroT}e{centT}c; Volte sempre!")
                exit+=1
                operacao="ABORTAR"
            
        elif d:
            if exit == 1 or dinheiro==0:
                operacao="ABORTAR"
            else:
                aux=re.sub('T\=','',operacao)
                valid,euroT,centT=validaChamada(aux,euro,cent)
                if valid == 2:
                    print("Digite o novo número aqui: ")
                    operacao=getInput()
                if valid == 1:
                    print("Coloque mais moedas aqui: ")
                    operacao=getInput()
                
                exit+=1
                chamou=1 

        elif e:
            print(f"Cancelou a operação. Ficou com {euro}e{cent}c.")
            exit=0

if __name__ == "__main__":
    o=getInput()
    dealWithInput(o)
