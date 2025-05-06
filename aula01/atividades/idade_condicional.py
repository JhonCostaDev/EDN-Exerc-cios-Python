# Crie um programa que verifica a idade do usuário e diga se ele é maior ou menor de idade:

def get_user_age():
    while True:
        try:
            age = input("Digite sua idade\n")
            age = int(age)
            if age < 1 or age > 120:
                raise ValueError('Digite uma idade entre 1 e 120')
        except ValueError as e:
            print(f'{e}: Entrada inválida, tente novamente.')
        else:
            return age
        
def verify_age(age):
    if age < 11:
        return 'Criança'
    elif age < 18:
        return 'Adolescente'
    elif age < 65:
        return 'Adulto'
    else:
        return 'Idoso'
    
def main():
    age = get_user_age()
    age_category = verify_age(age=age)
    print(f'Você é {age_category}' )

if __name__ == '__main__':
    main()