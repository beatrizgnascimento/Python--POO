from abc import ABC, abstractmethod

class EmpDomestica(ABC):
  def __init__(self, nome, tel):
    self.__nome = nome 
    self.__tel = tel
    
  @property
  def nome(self):
    return self.__nome
  
  @property
  def tel(self):
    return self.__tel

  @abstractmethod
  def calculaSalario(self):
    pass
  
class Horista(EmpDomestica):
  def __init__(self, nome, tel, horasTrabalhadas, valorHora):
    super().__init__(nome, tel)
    self.__horasTrabalhadas = horasTrabalhadas
    self.__valorHora = valorHora
    
  @property
  def horasTrabalhadas(self):
    return self.__horasTrabalhadas
  
  @property
  def valorHora(self):
    return self.__valorHora
  
  @valorHora.setter
  def valorHora(self, valorHora):
    self.__valorHora = valorHora
  
  def calculaSalario(self):
    return self.__valorHora * self.__horasTrabalhadas
  
class Diarista(EmpDomestica):
  def __init__(self, nome, tel, diasTrabalhados, valorDia):
    super().__init__(nome, tel)
    self.__diasTrabalhados = diasTrabalhados
    self.__valorDia = valorDia
    
  @property
  def diasTrabalhados(self):
    return self.__diasTrabalhados
  
  @property
  def valorDia(self):
    return self.__valorDia
  
  @valorDia.setter
  def valorDia(self, valorDia):
    self.__valorDia = valorDia
    
  def calculaSalario(self):
    return self.diasTrabalhados * self.valorDia
  
  
class Mensalista(EmpDomestica):
  def __init__(self, nome, tel, valorMensal):
    super().__init__(nome, tel)
    self.__valorMensal = valorMensal
    
  @property
  def valorMensal(self):
    return self.__valorMensal
  
  @valorMensal.setter
  def valorMensal(self, novo_valor):
      self.__valorMensal = novo_valor
    
  
  def calculaSalario(self):
    return self.__valorMensal
  
if __name__ == '__main__':
  horista = Horista('Gabriela', 12345678, 160, 12)
    
  diarista = Diarista('Giovana', 78191011, 20, 65)
    
  mensalista = Mensalista('Nerissa', 234234234, 1200)
    
    
  empregadas = [horista, diarista, mensalista]
    
  menor_salario = float('inf')
  
  print('Opções de empregadas\n')
      
  for empregada in empregadas:
     print('Nome: {} - Telefone: {} - Salário: {}'.format(empregada.nome, empregada.tel, empregada.calculaSalario()))

     salario = empregada.calculaSalario()
     
     if salario < menor_salario:
       menor_salario = salario
       empregada_menor_salario = empregada
       
  print('----------------------------------------------------')
  print('Opção mais barata\nNome: {} - Telefone: {} - Salário: {}'.format(empregada_menor_salario.nome, empregada_menor_salario.tel, empregada_menor_salario.calculaSalario()))
  