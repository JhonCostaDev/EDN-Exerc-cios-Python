# Faça um programa que verifica se um número digitado pelo usuário está no intervalo entre 10 e 20

from numero_par import get_number

def main():
    number = get_number()
    result = 'Fora da faixa <10 - 20> ' if number < 10 or number > 20 else 'Dentro da faixa <10 - 20>'
    print(f'O número {number} é um número: {result}')

if __name__ == '__main__':
    main()