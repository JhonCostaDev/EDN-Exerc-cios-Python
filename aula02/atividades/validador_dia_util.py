# Faça um programa que diga se o dia da semana é um dia útil! !=

def get_user_day(week_days):
    while True:
        try:
            day = input("Digite o dia\n")
            if day not in week_days:
                raise
        except:
            pass

def check_business_day(day):
    pass


def main():
    week_days = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    day = get_user_day()
    

if __name__ == '__main__':
    main()