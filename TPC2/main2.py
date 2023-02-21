#Resposta melhorada a TPC2 - tem ciclos while e escolha de voltar a usar a calculadora

run=1

while run != 0:  
    string = input("Somador ON/OFF:\n")

    string = string.rstrip().split(' ')

    soma=0
    on=0

    for element in string:
        if element == "ON" or element == "on":
            on = 1

        if element == "OFF" or element == "off":
            on = 0
            soma = 0

        if element.isnumeric() == True:
            if on == 1:
                soma = soma + int(element)

        if element == "=":
            if on == 1:
                print("Soma: %d" % soma)
                soma = 0
            else:
                print("Sem operações a realizar.")

    repete = 1
    
    while repete != 0: 
        
        again = input("\nDeseja continuar? [Y/N] ")
        
        if again == "N" or again == "n" or again == "Y" or again == "y":
            repete = 0

            if again == "N" or again == "n":
                print("A terminar...")
                run = 0
            else:
                run = 1

        else:
            print("Inválido.")
             
    print(" ")
