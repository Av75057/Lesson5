def deposit():
    return input('Введите сумму на сколько пополнить счет: ')

def run_deposit():
    history = {}
    account = 0
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            account +=int(deposit())
        elif choice == '2':
            purchase_amount = int(input('Введите сумму покупки: '))
            if purchase_amount > account:
                print('Денег не хватает.')
            else:
                name_purchase = input('Введите название покупки: ')
                history_temp = {name_purchase: purchase_amount}
                history.update(history_temp)
                account -= purchase_amount
        elif choice == '3':
                 for key, val in history.items():
                    print(f'Наименование: {key}  Цена: {val}')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')