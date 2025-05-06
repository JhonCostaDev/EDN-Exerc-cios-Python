# Faça um programa que recebe a altura e peso do usuário e calcule sua IMC
# imc = peso / altura ** 2

def get_user_weight() -> float:
    '''This function takes and validates a weight typed by user'''
    while True:
        try:
            weight = input("Digite seu peso (kg):\n")
            weight = float(weight)

            if weight < 0.245 or weight > 634:
                raise ValueError('Peso mínimo: 0.245gramas\nPeso máximo: 634Kg') # valores de peso mínimo e máximo já registrados.
        except ValueError as e:
            print(f'Erro {e}: Digite um valor entre 0.245gramas e 634Kg')
        else:
            return weight
        
        
def get_user_height() -> float:
    '''This function takes a height value from the user and validates it.'''
    while True:
        try:
            height = input("Digite sua altura (cm):\n")
            height = float(height)

            if height < 0.24 or height > 2.79:
                raise ValueError('Altura mínima: 0.24cm\nAltura máxima: 2.79cm') # valores de altuma mínima e máxima já registrados.
        except ValueError as e:
            print(f'Erro {e}: Digite um valor entre 0.24cm e 2.79cm')
        else:
            return height
        
# BMI - Body Mass Index
# This lambda function calculate the BMI
calculate_bmi = lambda weight, height : weight / (height**2)

def classify_bmi(bmi:float) -> tuple:
    '''This function takes a BMI value and returns a tuple containing its classification and associated risk factor.'''
    
    if bmi < 18.5:
        return ('Magreza','Aumentado')
    elif bmi < 25:
        return ('Peso normal', 'Normal')
    elif bmi < 30:
        return ('Sobrepeso', 'Aumentado')
    elif bmi < 35:
        return ('Obesidade grau I', 'Moderado')
    elif bmi < 40:
        return ('Obesidade grau II', 'Grave')
    else:
        return ('Obesidade grau III (mórbida)',	'Muito grave')
    
def show_results(v_bmi:float, class_bmi:str, risk:str) -> None:
    '''This function takes three arguments and display a summary of the BMI '''
    print(f'''
IMC: {v_bmi:.2f} (kg/m²)
CLASSIFICAÇÃO: {class_bmi}
GRAU DE RISCO: {risk}
''')
    
def main() -> None:
    '''The main function'''
    print("======== Calculadora de Índice de Massa Corporea - IMC =======")
    # Take user's values
    weight = get_user_weight()
    height = get_user_height()

    value_bmi = calculate_bmi(weight=weight, height=height)
    classification_bmi, risk_factor = classify_bmi(value_bmi)

    show_results(value_bmi, classification_bmi, risk_factor)
    
    
    
if __name__ == '__main__':
    main()