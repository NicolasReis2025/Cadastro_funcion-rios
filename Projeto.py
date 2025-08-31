def calcularMedia(salarios=None):
    if not salarios:
        return 0
    return sum(salarios) / len(salarios)

nomes = []
salarios = []

cont = 0

while True:
    cont += 1
    print(f"{cont}# funcionário: ")
    nome = str(input("nome: ('sair' para encerrar)  ")).lower()
    
    if nome == "sair":
        print("Programa encerrado!")
        break
    
    salario = float(input("Salário: "))

    nomes.append(nome)
    salarios.append(salario)
print()

if len(nomes) > 0:
    print("Funcionários cadastrados: ")
    for nome, salario in zip(nomes, salarios):
        print(f"Nome: {nome}\nSalário: R${salario:.2f}")
        print("-=-=-" * 10)
    
    print()
    maior_salario = max(salarios)
    pos_maior_salario = salarios.index(maior_salario)
    
    print("Maior salário:")
    print(f"Nome: {nomes[pos_maior_salario]}\nSalario: R${maior_salario:.2f}")
    print()

    menor_salario = min(salarios)
    pos_menor_salario = salarios.index(menor_salario)
    
    print("menor salário: ")

    print(f"Nome: {nomes[pos_menor_salario]}\nSalário: R${menor_salario:.2f}")
    print()        
    
    media_salarial = calcularMedia(salarios)

    print(f"Média salárial: R${media_salarial:.2f}\n")

else:
    print("Não foram cadastrados funcionários no programa!")        






