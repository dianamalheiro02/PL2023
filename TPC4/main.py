#Resposta a TPC4
import csv
import json

def csv_to_json(csv_file_path):
    # Abre o arquivo CSV e lê o conteúdo
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Converte cada linha em um dicionário e adiciona a uma lista
        data = [row for row in csv_reader]
    # Converte a lista em JSON e retorna o resultado
    return json.dumps(data)

# Exemplo de uso
csv_file_path = 'alunos.csv'
json_data = csv_to_json(csv_file_path)
#print(json_data)
with open("alunos.json", "w") as arquivo:     
    json.dump(json_data, arquivo, indent=4)
