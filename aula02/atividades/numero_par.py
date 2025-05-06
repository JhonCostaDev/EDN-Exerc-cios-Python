# Faça um programa que recebe um número e diga se ele é par ou impar!

def get_number() -> int:
    '''This function takes and validate a integer number'''
    while True:
        try:
            integer = input("Digite um número inteiro:\n")
            integer = int(integer)
            
        except (ValueError, TypeError) as e:
            print(f'{e}: Entrada inválida, tente novamente.')
        else:
            return integer

def main():
    print('============ Par ou Ímpar ============')
    number = get_number()
    result = 'Par' if number % 2 == 0 else 'Ímpar'
    print(f'O número {number} é um número: {result}')

if __name__ == '__main__':
    main()