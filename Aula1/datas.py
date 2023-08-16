#Temos que improtar o módulo datetime
from datetime import datetime
data_corrente = datetime.now()
#a função now retorna um objeto datetime
print('Hoje é: ' + str(data_corrente))

#existem funções para manipulação de datas
from datetime import datetime, timedelta
data_corrente = datetime.now()
#time delta é usado para definir um período de tempo
um_dia =timedelta(days=1)
ontem = data_corrente - um_dia
#ontem = 2020-02-06 16:17:18.6945 -- timedelta

#Funções para fromatação de datas
from datetime import datetime
data_corrente = datetime.now()
print('Dia: ' + str(data_corrente.day))
print('Mês: ' + str(data_corrente.month))
print('Ano: ' + str(data_corrente.year))

#input sempre devolve datas como strings, é necessário converter
from datetime import datetime
nasc = input('Informe a data(dd/mm/yyyy):')
data_nasc = datetime.strptime(nasc,'%d/%m/%Y')
print('Nascimento: ' + str(data_nasc))



