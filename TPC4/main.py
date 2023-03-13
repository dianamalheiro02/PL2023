#Resposta a TPC4
import json
import re

padrao_header=r"Número,Nome,Curso(,?Notas?(?P<Notas>{\d,\d})?(?:::)?(?P<agregator>\w*)?(?:.*))?"
padrao_content=r"(?P<Número>\d*),(?P<Nome>.*[^\W\d_]),(?P<curso>.*[^\W\d_]),?(?P<Notas>[\d,]*)?\n?"

def csv_to_json(csv_file_path,json_file_path):
    # Abre o arquivo CSV e lê o conteúdo
    with open(csv_file_path, 'r') as csv_file:

        read = csv_file.readlines()
        header = read[0]
        content = read[1::]

        #print(header)
        #print(content)

        headerP = re.compile(padrao_header)
        contentP = re.compile(padrao_content)

        #deling with header:
        headerMatch=re.search(headerP,header)
        limit=(0,0)
        agregacao=False

        if headerMatch:
            m = headerMatch.groupdict()
            if m['agregator'] is not None:
                agregacao=True
            else:
                agregacao=False

            if m['Notas'] is not None:
                if ',' not in m['Notas']:
                    limit = (int((m['Notas'])[1]),int((m['Notas'])[1]))
                else:
                    limit = (int((m['Notas'])[1]),int((m['Notas'])[-2]))

        #dealing with content
        data={}
        notas=[]
        sum=0

        for l in content:
            contentMatch=re.fullmatch(contentP,l)

            if contentMatch:
                cm=contentMatch.groupdict()
                notas = list(filter(str.strip, cm['Notas'].split(',')))

                if limit[0] <= len(notas) <= limit[1]:
                    if agregacao:
                        type = m['agregator']

                        if type == 'sum':
                            for n in notas:
                                sum+=int(n)
                            
                            cm['Notas']=sum

                        elif type == 'media':
                            media=0
                            for n in notas:
                                media+=int(n)/2

                            cm['Notas']=media
                        
                        elif type == 'maior':
                            maior=notas.sort(reverse=True)
                            cm['Notas']=maior[0]

                        elif type == 'menor': 
                            menor=notas.sort(reverse=False)
                            cm['Notas']=menor[0]

                    data[cm['Número']] = cm
         
        try:
            output = list(data.items())
            print(output)
            with open(json_file_path, 'w') as file:
                json.dump(output, file, indent=4)
        except Exception as e:
            print(e)

    
    # Converte a lista em JSON e retorna o resultado
    #output=list(data.items())
    #return json.dumps(output)

# Exemplo de uso 1
csv_file_path = 'alunos.csv'
json_file_path = 'alunos.json'
json_data = csv_to_json(csv_file_path,json_file_path)
#print(json_data)
#with open("alunos.json", "w") as arquivo:     
#    json.dump(json_data, arquivo, indent=4)

# Exemplo de uso 2
csv_file_path = 'alunos2.csv'
json_file_path = 'alunos2.json'
json_data = csv_to_json(csv_file_path,json_file_path)
#print(json_data)
#with open("alunos2.json", "w") as arquivo:     
#    json.dump(json_data, arquivo, indent=4)

# Exemplo de uso 3
csv_file_path = 'alunos3.csv'
json_file_path = 'alunos3.json'
json_data = csv_to_json(csv_file_path,json_file_path)
#print(json_data)
#with open("alunos3.json", "w") as arquivo:     
#    json.dump(json_data, arquivo, indent=4)
