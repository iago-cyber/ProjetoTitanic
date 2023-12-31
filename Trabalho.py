import pandas as pd
from matplotlib import pyplot as plt

# lendo o arquivo de dados
dataFrame = pd.read_csv('dados/dados4.csv')

# separando variaveis pra facilitar a escrita
sexColumn = dataFrame["sex"]
sexMode = sexColumn.mode()[0]

# limpeza de nulos por garantia, substituindo o vazio pela moda dos dados
sexColumn.fillna(sexMode, inplace=True)

# inicialização de variaveis para contagem da quantidade de cada sexo
intMaleCount = 0
intFemaleCount = 0

# for para a contagem da quantidade em cada sexo
for item in sexColumn:
    if(item == "male"):
        intMaleCount += 1
    elif( item == "female"):
        intFemaleCount += 1

# mostra a quantidade no terminal
print("\nNo barco haviam "+str(intMaleCount)+" homens e haviam "+str(intFemaleCount)+" mulheres\n")

# separando variaveis pra facilitar a escrita
ageColumn = dataFrame["age"]
ageMode = ageColumn.mode()[0]

# limpeza dos dados
ageColumn.fillna(ageMode , inplace=True)
dataFrame["age"] = ageColumn.astype(int)

# criação do arquivo e escrita dos dados
arquivo = open("Resposta01.txt","w")
arquivo.write(str(dataFrame[["name","sex","age"]].to_string()))
arquivo.close()

# separando variaveis pra facilitar a escrita
survivedColumn = dataFrame["survived"]
survivedMode = survivedColumn.mode()[0]

# limpeza dos dados
survivedColumn.fillna(survivedMode , inplace=True)

# inicialização de variaveis para contagem da quantidade de mortos
survivedCount = 0
deadCount = 0

# for para a contagem da quantidade de mortos
for item in survivedColumn:
    if(item == 0):
        deadCount += 1
    elif( item == 1):
        survivedCount += 1

# colocando os dados em um array para ser usado no grafico de pizza
lstDadosSurvived = [deadCount,survivedCount]

# grafico de pizza
plt.pie(lstDadosSurvived, labels = ['Mortos','Sobreviventes'], autopct='%1.0f%%')
plt.show()

# preparando as variaveis da coluna tarifa
fareColumn = dataFrame["fare"]
fareMode = fareColumn.mode()[0]

# limpando os dados da coluna tarifa
fareColumn.fillna(fareMode, inplace=True)


# grafico de disperção
plt.scatter ( ageColumn, fareColumn, alpha=0.5 )
plt.title("idade por tarifa")
plt.xlabel("idade")
plt.ylabel("tarifa")
plt.show()