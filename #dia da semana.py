#dia da semana
from datetime import date

ano = int(input("Qual o ano?"))
mes = int(input("qual o mes?"))
dia = int(input("qual o dia?"))

data = date(ano, mes, dia)
if data.weekday() == 0:
    print("Segunda-Feira")
    
elif data.weekday() == 1:
    print("Terça-Feira")

elif data.weekday() == 2:
    print("Quarta-Feira")

elif data.weekday() == 3:
    print("Quinta-Feira") 

elif data.weekday() == 4:
    print("Sexta-Feira") 

elif data.weekday() == 5:
    print("Sábado")
    
else:
    print("Domingo")