#Resposta a TPC4
import json
import re

padrao_header=r"Número,Nome,Curso(,?Notas?(?P<Notas>{\d,\d})?(?:::)?(?P<agragator>\w*)?(?:.*))?"
padrao_conteudo=r"(?P<Número>\d*),(?P<Nome>.*[^\W\d_]),(?P<curso>.*[^\W\d_]),?(?P<Notas>[\d,]*)?\n?"

def convert_csv_to_json(csv_file):
    with open(csv_file, 'r') as file:
        info=file.readlines()
        header = info[0]
        conteudo = info[:1]

        headerP=re.compile(padrao_header)
        conteudoP=re.compile(padrao_conteudo)

        match=re.search(headerP,header)
        limite=(0,0)
        flag=False

        if match:
            matchFound=match.groupdict()
            flag=True if matchFound('agregator') else False

            if matchFound['Notas'] is not None:
                if ',' not in matchFound['Notas']:
                    limite=(int((matchFound['Notas'])[1]),int((matchFound['Notas'])[1]))

                else:
                    limite=(int((matchFound['Notas'])[1]),int((matchFound['Notas'])[-2]))

        data={}
        notas=[]
        x=0

        for line in conteudo:
            matchConteudo=re.fullmatch(conteudoP,line)

            if conteudoP:
                matchC=matchConteudo.groupdict()
                notas=list(filter(str.strip,matchC['Notas'].split(',')))

                if limite[0] <= len(notas) <= limite[1]:
                    if flag:
                        agregador = matchFound['agregador']
                        if type == 'sum':
                            for n in notas:
                                x+=int(n)
                            
                            matchC['Notas']=x

                        elif type == 'media':
                            media=[]
                            for i,n in enumerate(notas):
                                media.append(int(n)/2)
                        
                    data[matchC['Número']]=matchC
                        
        try:
            res=data
            with open('alunos.json','w') as fileOut:
                json.dump(res,fileOut,indent=4)

        except Exception as e:
            print(e)
        

convert_csv_to_json('alunos.csv')
convert_csv_to_json('alunos2.csv')
convert_csv_to_json('alunos3.csv')
