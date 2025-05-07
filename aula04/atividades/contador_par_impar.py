# Faça um programa que receba números até o usuário digitar 'fim'. Após isso informe quantos dos números digitados são pares ou ímpares.


def verify_even_odd(list_numbers:int) -> tuple:
    "This function receives a list and separates the even ones from the odd ones"
    even = []
    odd = []

    for item in list_numbers:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    
    return even, odd


def main():
    numbers = []

    while True:
        number = input('Digite um número:\n')

        if number == 'fim':
            break
        try:
            number = int(number)

        except (ValueError, TypeError) as e:
            print(e)
        else:
            numbers.append(number)

    even, odd = verify_even_odd(numbers)

    print(f'Dos números digitados, {len(even)} são pares e {len(odd)} são ímpares')



if __name__ == '__main__':
    main()