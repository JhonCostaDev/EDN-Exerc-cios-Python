# Faça um programa que diga se o dia da semana é um dia útil! !=

def get_user_day(week_days):
    while True:
        try:
            day = input("Digite o dia\n").lower()
            day = ''.join(day.replace(' ', '').replace('feira', '').replace('-', '').split('-'))
            if day not in week_days:
                raise ValueError('Dia inválido, Digite um dia da semana!')
        except ValueError as e:
            print(e)
        else:
            return day

def main():
    week_days = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    print('============ É dia Útil ============')
    day = get_user_day(week_days)
    is_business_day = 'Dia útil' if day in week_days[:5] else 'Fim de semana'
    print(is_business_day)
    

if __name__ == '__main__':
    main()