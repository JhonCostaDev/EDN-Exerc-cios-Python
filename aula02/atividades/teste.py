week_days = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
#filtrar casos ('espacos', '-', '')
d = ''.join('sexta'.replace(' ', '').replace('feira', '').replace('-', '').split('-'))
print(week_days[2].replace(' ', '').replace('feira', '').replace('-', '').split('-'))

r = ''.join(week_days[2].replace(' ', '').replace('feira', '').replace('-', '').split('-'))
print(d.replace(' ', '').split('-'))
print(d in week_days[:5])



#𝐶 = (( 𝐹 − 32) × 5 )/ 9
f = 80

celsius = 30
c = (f - 32) * 5 / 9

#fahrenheit = (celsius * 9/5) +32
fahrenheit = (celsius * 9/5) +32
# print(fahrenheit)
# print(c)
