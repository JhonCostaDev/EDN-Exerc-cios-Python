# Faça um programa que receba do usuário o valor de um produto e calcule seu valor final com base no desconto (%) dado pelo usuário


def get_user_prince():  
    while True:
        try:
            price = input("Digite o valor do produto:\n")
            price = float(price)

            if price <= 0:
                raise ValueError("O valor deve ser positivo")
        except ValueError as e:
            print(f'{e}: Digite um valor válido maior que zero!')
        else:
            return price


def get_user_discount():
    while True:
        try:
            discount = input("Digite o valor do (%)):\n")
            discount = float(discount)
            if discount <=0 or discount > 100:
                raise ValueError("O desconto não pode ser negativo ou maior que o próprio valor do produto!")
        except ValueError as e:
            print(f'{e}: Digite um valor válido maior que zero!')
        else:
            return discount

calulate_price = lambda price, discount : price - (price * (discount / 100))

def main():
    price = get_user_prince()
    discount = get_user_discount()
    
    total = calulate_price(price, discount)
    
    print(f'Valor com desconto: R${total}')
if __name__ == '__main__':
    main()