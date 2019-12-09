import datetime 
import random

nomes = []
cpfs = []
codigos_de_estudante = []
anos_de_ingresso = []
periodos = []
senhas = []
materias = {}

primeiro_periodo = ["1 -FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO (80 hr)",
"2- INTRODUÇÃO ÀS TECNOLOGIAS WEB (EAD) (40 hr)",
"3- LÓGICA MATEMÁTICA E MATEMÁTICA DISCRETA (80 hr)",
"4- ALGORITMOS E LÓGICA DA PROGRAMAÇÃO (80 hr)",
"5- INGLÊS TÉCNICO (80 hr)",
"6- FILOSOFIA (80 hr)"]


segundo_periodo = ["0- MATEMATICA PARA SISTEMAS DE INFORMACAO (80 hr)",
"1- FUNDAMENTOS DA GESTAO ORGANIZACIONAL  (80 hr)",
"2- ARQUITETURA E ORGANIZACAO DE COMPUTADORES  (80 hr)",
"3- LINGUAGEM DE PROGRAMACAO  (80 hr)",
"4- SOCIOLOGIA DAS ORGANIZACOES  (80 hr)", 
"5- ESTATÍSTICA APLICADA (80 hr)",
"6- FUNDAMENTOS DE BANCO DE DADOS (80 hr)", 
"7- SISTEMAS OPERACIONAIS (80 hr)", 
"8- METODOLOGIA CIENTÍFICA (80 hr)",
"9- OPTATIVA HUMANÍSTICA (40 hr)"]
    


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
    print ("OLÁ, {}, !".format(nomes[codigo_de_aluno]))
    digitou_para_sair = False
    while not digitou_para_sair:
        print ("1. ADICIONAR MATÉRIA")
        print ("2. REMOVER MATÉRIA")
        print ("3. ATESTADO DE MATRÍCULA")
        print ("4. SAIR")
        entrada = int(input(">>> "))
        if entrada == 1:
            adicionar_materia(codigo_de_aluno)
        elif entrada == 2:
            remover_materia(codigo_de_aluno)
        elif entrada == 3:
            atestado_de_matricula (codigo_de_aluno)
        else:
            digitou_para_sair = True
            return
    


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
    materias[codigo_do_aluno] = []
    codigos_de_estudante.append(codigo_do_aluno)
    nomes.append(nome)
    cpfs.append(cpf)
    anos_de_ingresso.append(ano_de_ingresso)
    print(primeiro_periodo)
    print(periodo)
    if periodo == 1:
        for elemento_primeiro in primeiro_periodo:
            print("rodando")
            materias[codigo_do_aluno].append(elemento_primeiro)
    else:
        periodos.append(periodo)
    senhas.append(senha)
    return chave_aluno, codigo_do_aluno




def cadastro():
    print("-" * 15)
    print("CADASTRO")
    print ("-" * 15)
    digite_seu_nome = input("DIGITE SEU NOME: ")
    digite_seu_cpf = input ("DIGITE SEU CPF: ")
    digite_seu_ano_de_ingresso = input ("DIGITE SEU ANO DE INGRESSO: ")
    digite_seu_periodo = input ("DIGITE SEU PERÍODO: ")
    digite_sua_senha = input("DIGITE SUA SENHA: ")
    chave_aluno, codigo_do_aluno = novo_estudante(digite_seu_nome, digite_seu_cpf, digite_seu_ano_de_ingresso, digite_seu_periodo, digite_sua_senha)
    print ("CADASTRO EFETUADO COM SUCESSO! SEU NÚMERO DE MATRÍCULA É: {}".format(codigo_do_aluno))
    menu_principal(chave_aluno)

def adicionar_materia (codigo_de_aluno):
    periodo = int(input("DIGITE SEU PERÍODO (1 ou 2): "))
    if periodo == 1:
        print ("NÃO É POSSÍVEL ADICIONAR MATÉRIA")
        return
    if len (materias[codigo_de_aluno]) >= 6:
        print ("NÃO É POSSÍVEL ADICIONAR MATÉRIA")
        return
    for x in segundo_periodo:
        print(x)
    while True:
        adicionando_materia = int (input ("ESCOLHA A MATÉRIA PARA SER ADICIONADA: "))
        materias[codigo_de_aluno].append(segundo_periodo[adicionando_materia])
        if len(materias[codigo_de_aluno]) >= 6:
            break


        
  


def remover_materia(codigo_de_aluno):
    periodo = int(input("DIGITE SEU PERÍODO (1 ou 2): "))
    if periodo == 1:
        print ("NÃO É POSSÍVEL ADICIONAR MATÉRIA")
        return
    print(materias[codigo_de_aluno])
    remover = input("DESEJA REMOVER ALGUMA MATÉRIA? (S/N)")
    if remover == 'S':
        removendo = int (input ("ESCOLHA A MATÉRIA PARA REMOVER:"))
        if len(materias[codigo_de_aluno]) <= 4:
            print ("NÃO É POSSÍVEL REMOVER MAIS MATÉRIAS")
            return
        materias[codigo_de_aluno].pop(removendo)


def atestado_de_matricula(codigo_de_aluno):
    print("NOME: {}".format(nomes[codigo_de_aluno]))
    print("PERÍODO: {}".format(periodos[codigo_de_aluno]))
    print("MATRÍCULA: {}".format(codigos_de_estudante[codigo_de_aluno]))
    print ("-" * 30)
    print("MATERIAS MATRICULADAS")
    print ("-" * 30)
    for z in materias[codigo_de_aluno]:
        print(z)
    


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

