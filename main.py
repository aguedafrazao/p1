import datetime 
import random

"""criar codigo do estudante retorna uma string onde os quatro primeiros digitos 
   representam o ano de curso e os cinco últimos são números aleatórios indo de 0 até 99999"""
def criar_codigo_estudante():
    ano_atual = datetime.datetime.now().year 
    random_numeros = random.randint(0, 99999)
    return "{}{}".format(ano_atual, random_numeros)


if __name__ == "__main__":
    codigo_estudante = criar_codigo_estudante()
    print (codigo_estudante)