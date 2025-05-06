# Faça um programa que converte temperatura de Celsius para Fahrenheit
# fahrenheit = (celsius * 9/5) +32
# 𝐶 = (( 𝐹 − 32) × 5 )/ 9
def menu() -> int:
    '''This function show the main Menu and return a option choose by the user'''
    print('''
========= Conversor de Temperatura =========
          
          Escolha uma das opções abaixo
=============================================
          1 - Celcius para Fahrenheit
          2 - Fahrenheit para Celcius
          0 - Sair
=============================================          
''')
    while True:    
        try:
            user_option = input('Digite uma das opções acima!\n')
            user_option = int(user_option)
            if user_option < 0 or user_option > 2:
                raise ValueError('Número inválido, Escolha 1, 2 ou 0!')
        except (ValueError, TypeError) as e:
            print(f'{e}: Digite um número inteiro, 1, 2 ou 0!')
        else:
            return user_option

def get_temperature() -> float:
    '''This function receive and validate the temperature typed by user'''
    while True:    
        try:
            temperature = input('Digite a temperatura:\n')
            temperature = float(temperature)
                    
        except (ValueError, TypeError) as e:
            print(f'{e}: ')
        else:
            return temperature

def convert_fahrenheit_celcius(temperature_fahrenheit) -> float:
    '''This function convert the temperature from fahrenheit to celcius'''
    return (temperature_fahrenheit - 32) * 5 / 9
    

def convert_celcius_fahrenheit(temperature_celcius) -> float:
    '''This function convert the temperature from celcius to fahrenheit'''
    return (temperature_celcius * 9/5) +32

def main() -> None:
    print('============ Conversor de Temperatura ============')
    user_option = menu()
    if user_option != 0:
        user_entry = get_temperature()
        if user_option == 1:
            result = convert_celcius_fahrenheit(user_entry)
            print(f'{user_entry}º celcius equivale a {result}º fahrenheit!')
        else:
            result = convert_fahrenheit_celcius(user_entry)
            print(f'{user_entry}º fahrenheit equivale a {result}º celcius!')
    else:
            print("Fim do programa")
    print("Operação concluída!")
    

if __name__ == '__main__':
    main()