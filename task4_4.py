def dodaj(x, y):
  return x + y
def odejmij(x, y):
  return x - y
def pomnóż (x, y):
  return x * y
def podziel (x, y):
  return x / y
choice = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
num1 = float(input('Podaj składnik 1:'))
num2 = float(input('Podaj składnik 2:'))
if choice == '1':
  print("Dodaję", num1,'i',num2, '\nWynik to ', dodaj(num1,num2))
elif choice == '2':
  print("Odejmuję", num1,'od',num2,'\nWynik to', odejmij(num1,num2))
elif choice == "3":
  print("Mnoże", num1,'razy',num2,'\nWynik to', pomnóż (num1,num2))
elif choice == "4":
  print("Dzielę", num1,'przez',num2,'\nWynik to', podziel (num1,num2))
else:
  print('Nieporawna wartość')