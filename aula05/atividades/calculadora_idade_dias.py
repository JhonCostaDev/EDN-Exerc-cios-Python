# Faça um programa que leia o ano de nascimento do usuário, e informe quantos dias de vida ele tem.

from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    try:
        if ano_nascimento > ano_atual:
            raise ValueError("Você não pode ter nascido no futuro!")
    except ValueError as e:
        print(e)
    else:
        idade_anos = ano_atual - ano_nascimento
        return f'Você tem {idade_anos * 365} dias de idade!'


print(calcular_idade_em_dias(1953))

