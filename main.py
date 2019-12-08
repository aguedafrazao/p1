import datetime 
import random

nomes = []
cpfs = []
codigos_de_estudante = []
anos_de_ingresso = []
periodos = []
senhas = []


"""criar codigo do estudante retorna uma string onde os quatro primeiros digitos 
   representam o ano de curso e os cinco últimos são números aleatórios indo de 0 até 99999"""
def criar_codigo_estudante():
    ano_atual = datetime.datetime.now().year 
    random_numeros = random.randint(0, 99999)
    return "{}{}".format(ano_atual, random_numeros)

def buscar_aluno_por_matricula(matricula):
    index = 0
    for codigo_de_estudante in codigos_de_estudante:
        if codigo_de_estudante == matricula:
            return index
        index = index + 1
    return -1


def menu_principal(codigo_de_aluno):
    print ("COGIGO DE ALUNO PASSADO FOI: {} ".format(codigo_de_aluno))

def login():
    print("-" * 15)
    print("LOGIN")
    print ("-" * 15)
    matricula = input ("INFORME SEU NÚMERO DE MATRÍCULA: ")
    chave = buscar_aluno_por_matricula(matricula)

    if chave == -1:
        print ("MATRICULA NÃO ENCONTRADA")
        return
    

    senha = input ("INFORME SUA SENHA: ")
    if senhas[chave] != senha:
        print ("SENHA INCORRETA")
        return
    
    menu_principal(chave)


    


def novo_estudante(nome, cpf, ano_de_ingresso, periodo, senha):
    chave_aluno = len(nomes)
    codigo_do_aluno = criar_codigo_estudante()
    codigos_de_estudante.append(codigo_do_aluno)
    nomes.append(nome)
    cpfs.append(cpf)
    anos_de_ingresso.append(ano_de_ingresso)
    periodos.append(periodo)
    senhas.append(senha)
    return chave_aluno




def cadastro():
    print("-" * 15)
    print("CADASTRO")
    print ("-" * 15)
    digite_seu_nome = input("DIGITE SEU NOME: ")
    digite_seu_cpf = input ("DIGITE SEU CPF: ")
    digite_seu_ano_de_ingresso = input ("DIGITE SEU ANO DE INGRESSO: ")
    digite_seu_periodo = input ("DIGITE SEU PERÍODO: ")
    digite_sua_senha = input("DIGITE SUA SENHA: ")
    chave_aluno = novo_estudante(digite_seu_nome, digite_seu_cpf, digite_seu_ano_de_ingresso, digite_seu_periodo, digite_sua_senha)
    print (chave_aluno)
    print (nomes[chave_aluno])
    print (cpfs [chave_aluno])
    print (codigos_de_estudante[chave_aluno])
    print (anos_de_ingresso[chave_aluno])
    print (periodos[chave_aluno])
    print (senhas[chave_aluno])

def menu_inicial():
    pediu_para_sair = False
    while not pediu_para_sair:
        print("1. LOGIN")
        print("2. CRIAR CONTA")
        print("3. SAIR")
        entrada = int(input(">>> "))
        if entrada == 1:
            login ()
        elif entrada == 2:
            cadastro()
        else:
            pediu_para_sair = True


if __name__ == "__main__":
    
    menu_inicial()

