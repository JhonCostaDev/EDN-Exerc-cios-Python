import os

#==================================================
def read_files_names(dictionary):
   
    list_all_files =  sum(dictionary.values(), [])
    list_all_files = [x for x in list_all_files if x != '__pycache__']
 
    return {key: value for key, value in enumerate(list_all_files)}


#===================================================


def switch(option, folder, dicitionary):
    '''Essa funcao recebe(opcao, caminho pasta, dicionario) do usuario e retorna a string para a funcao os.system() que chama o arquivo .py para execucao'''
    #return 'aula01/atividades/alguma_coisa.py'
    a = []
    for fol in folder:
        files = os.listdir(fol)
        for fol_files in files:
            print(f'{fol}{fol_files}')
    # Tomorrow i'll implement this solution at the mainly python's file!
    # don't forget to merge this solution at the first function
        #print(f'{fol}{os.listdir(fol)}')
        ##a.append(f'{folder}{os.listdir(fol)}')
    #return a
    # if option == 0:
    #     print(f'{folder[option]}{dicitionary.get(option)}')


#===================================================
def main():
    list_all_files = os.listdir() 
    folder_atividades = [f'{item}/atividades/' for item in list_all_files if item.startswith('aula')]
    #folder_atividades

    folder_atividades.sort()

    dict_files = {x: os.listdir(folder_atividades[x]) for x in range(len(folder_atividades))}

    dict_all_files = read_files_names(dict_files)
    #print(switch(1, 'atividades', dict_files))
    print(switch(0, folder_atividades, dict_all_files))

    
    #print(folder_atividades)

if __name__ == '__main__':
    main()
