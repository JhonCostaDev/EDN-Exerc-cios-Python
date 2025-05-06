# Faça uma calculadora que efetua as 4 operações básicas entre dois números utilizando a estrutura Try / Except

def choose_operation():
    print('''
============== Calculadora ==============
          1 - Soma
          2 - Subtração
          3 - Multiplicação
          4 - Divisão
          0 - Sair
''')
    while True:
        try:
            operation = input("Escolha umas das operações acima:\n")
            operation = int(operation)
            if operation < 0 or operation > 4:
                raise ValueError("Escolha um número entre 0 e 4")
        except(ValueError, TypeError) as e:
            print(e)
        else:
            return operation

def get_number(string):
    while True:
        try:
            number = input(string)
            number = float(number)

        except (TypeError, ValueError) as e:
            print(e)
        else:
            return number
add = lambda x, y: x + y
minus = lambda x, y: x - y
times = lambda x, y: x * y
        
def divide_by(x, y):
    try:
        result = x / y 
    except ZeroDivisionError as e:
        print(f'Erro: {e}')
    else:
        return result
    
def display_result(n1, n2, op):
    if op == 1:
        print(f'{n1} + {n2} = {add(n1, n2)}')
    elif op == 2:
        print(f'{n1} - {n2} = {minus(n1, n2)}')
    elif op == 3:
        print(f'{n1} x {n2} = {times(n1, n2)}')
    elif op == 4:
        print(f'{n1} / {n2} = {divide_by(n1, n2)}')
    else:
        return False

def main():
    print("================= Calculadora de 2 numeros =================")
    operation = choose_operation()
    if operation != 0:
        number_1 = get_number('Digite o primeiro número:\n')
        number_2 = get_number('Digite o segundo número:\n')
        display_result(number_1, number_2, operation)

if __name__ == '__main__':
    main()
