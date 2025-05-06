#Faça um programa que recebe as notas de um aluno até que seja escrito 'Fim' então calcule a média das notas digitadas
def main():
    grades = []
    print("========== Calcula Média =============")
    while True:
        try:
            grade = input('Digite a nota:\n').lower()
            if grade == 'fim':
                break
            grade = float(grade)

            if grade < 0 or grade > 10:
                raise ValueError('Apenas notas de 0 a 10')
        except(ValueError, TypeError) as e:
            print(f'Erro: {e}')
        else:
            grades.append(grade)

    average = sum(grades) / len(grades)
    print(f"A média das notas digitadas é de {average}")

if __name__ == '__main__':
    main()