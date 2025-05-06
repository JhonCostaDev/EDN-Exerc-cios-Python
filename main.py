import os
def menu(dictionary):
    os.system('cls') if os.name=='nt' else os.system('clear')
    
    print("Escolha o número de qual exercício vc quer executar ou aperte (ctrl + c) para sair!:\n")

    for key, value in dictionary.items():
        print(f'{key} - {value}')
        print('')

    while True:
        try:
            user_option = input("Digite o número do exercicio que você quer executar\n")
            user_option = int(user_option)

            

            if user_option < 0 or user_option > 12:
                raise ValueError('Escolha um número entre 0 e 12')

        except (TypeError, ValueError) as e:
            print(e)

        else:
            return user_option
    

def read_files_names(dictionary):
    aula01 = dictionary.get(0)
    aula02 = dictionary.get(1)
    aula03 = dictionary.get(2)
    all = aula01 + aula02 + aula03
    
    return {key: value for key, value in enumerate(all) if value !='__pycache__'}

def switch(option, folder, dict_all_files):
    match option:
        case 0:
            return f'python3 {folder[0]}/{dict_all_files.get(0)}'
        case 1:
            return f'python3 {folder[0]}/{dict_all_files.get(1)}'
        case 2:
            return f'python3 {folder[1]}/{dict_all_files.get(2)}'
        case 3:
            return f'python3 {folder[1]}/{dict_all_files.get(3)}'
        case 4:
            return f'python3 {folder[1]}/{dict_all_files.get(4)}'
        case 5:
            return f'python3 {folder[1]}/{dict_all_files.get(5)}'
        case 6:
            return f'python3 {folder[1]}/{dict_all_files.get(6)}'
        case 7:
            return f'python3 {folder[1]}/{dict_all_files.get(7)}'
        case 8:
            return f'python3 {folder[1]}/{dict_all_files.get(8)}'
        case 9:
            return f'python3 {folder[1]}/{dict_all_files.get(9)}'
        case 10:
            return f'python3 {folder[1]}/{dict_all_files.get(10)}'
        case 11:
            return f'python3 {folder[2]}/{dict_all_files.get(11)}'
        case 12:
            return f'python3 {folder[2]}/{dict_all_files.get(12)}'


def main():
    folder = "aula01/atividades", "aula02/atividades", "aula03/atividades"
    while True:
    
        dict_files = {x: os.listdir(folder[x]) for x in range(len(folder))}
    
        dict_all_files = read_files_names(dict_files) 
        option = menu(dict_all_files) 
        print(option)

        os.system(switch(option, folder, dict_all_files))
        input("Aperte Enter para continuar ou crtl + c para sair")

    

if __name__ == '__main__':
    main()