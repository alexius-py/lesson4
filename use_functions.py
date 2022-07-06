"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
def balance(transaction_up, balances):
    result = balances + transaction_up
    return result

def product(transacton_down, balances):
    name_product = input('Введите наименование товара: ')
    dict_product[name_product] = transacton_down
    return dict_product

def history(dict_product):
    for key, val in dict_product.items():
        print(key, '=', val, 'руб.')

balances = 0
dict_product = {}
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. Показать баланс')
    print('5. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        transaction_up = int(input('Введите сумму пополнения: '))
        balances = balance(transaction_up, balances)
        # print(balances)
    elif choice == '2':
        transaction_down = int(input('Введите сумму товара: '))
        balances = balances - transaction_down
        if balances < 0:
            print('Пополните счёт')
        else:
            dict_product = product(transaction_down, balances)
    elif choice == '3':
        history(dict_product)
    elif choice == '4':
        print('Ваш баланс', balances, 'руб.')
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')