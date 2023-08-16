from datetime import datetime, timedelta
data = input('Informe a data (dd/mm/yyyy): ')
data_obj = datetime.strptime(data, '%d/%m/%Y')
data = data_obj.weekday()
if(data == 2):
  print('Quarta-feira')
if(data == 3):
  print('Quinta-feira')
if(data == 4):
  print('Sexta-Feira')
if(data == 5):
  print('Sábado')
if(data == 6):
  print('Domingo')
if(data == 0):
  print('Segunda-feira')
if(data == 1):
  print('Terça-Feira')

