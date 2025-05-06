# Faça um programa que receba a idade do usuário e diga se o mesmo já pode votar

from classificacao_etaria import get_user_age #Importando uma função do exercício anterior

def verify_vote(age:int) -> str:
    if age < 16:
        return 'Não pode votar!'
    elif age <= 18 or age > 65:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'
    
    
def main():
    print("====== Verifica se pode Votar ====== ")
    age = get_user_age()
    can_vote = verify_vote(age=age)
    print(can_vote)

if __name__ == '__main__':
    main()