# Faça um programa que leia uma entrada do usuário e diga se é um palíndromo 

def palindrome(text:str) -> bool:
    '''This function takes a string and return a boolean if the string  '''
    return text.replace(' ', '') == text[::-1].replace(' ', '')


print(palindrome('arara'))


    
        

