import os


def read_files_names(dictionary):
   
    list_all_files =  sum(dictionary.values(), [])
 
    return {key+1: value for key, value in enumerate(list_all_files)}

list_all_files = os.listdir() 

class_folders = [f'{item}/atividades' for item in list_all_files if item.startswith('aula')]
#class_folders

class_folders.sort()

dict_files = {x+1: os.listdir(class_folders[x]) for x in range(len(class_folders))}

dict_all_files = read_files_names(dict_files)


a = [1,2,3]
b = [4,5,6]
print(class_folders)
