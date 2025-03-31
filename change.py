def change():
    expense = 23.75
    money = 100
    Pesos = (money-expense)
    Centavos = (((Pesos)-(int(Pesos))) * 100) 
    print (f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{int(Pesos)}\nCentavos:\n{int(Centavos)}')
