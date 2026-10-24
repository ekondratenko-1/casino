print("Добро пожаловать в казино «Удача»!") 
print("Начальный баланс:", 1000) 
print("Команды: bet <сумма> <even/odd>, balance, history, exit")
balance = 1000 
wins = 0 
losses = 0 
turns = 0
while True: 
    command = input("Введите команду: ")
    first = ""
    amount_text = ""
    bet = ""
    word = 1
    invalid_format = False

    for char in command:
        if char == " ":
            if word < 3:
                word = word + 1
            else:
                invalid_format = True
        else:
            if word == 1:
                first = first + char
            elif word == 2:
                amount_text = amount_text + char
            elif word == 3:
                bet = bet + char

    if first == "exit" and word == 1:
        print("Игра завершена.")
        print("Итоговый баланс:", balance)
        break

    elif first == "balance" and word == 1:
        print("Ваш баланс:", balance)

    elif first == "history" and word == 1:
        print("Победы:", wins)
        print("Поражения:", losses)

    elif first == "bet":
        if invalid_format or word != 3:
            print("Ошибка! Формат: bet <сумма> <even/odd>")
            continue

        if amount_text == "" or bet == "":
            print("Ошибка! Формат: bet <сумма> <even/odd>")
            continue

        valid_amount = True

        for digit in amount_text:
            if digit < "0" or digit > "9":
                valid_amount = False

        if not valid_amount:
            print("Ошибка! Сумма должна быть целым положительным числом.")
            continue

        amount = int(amount_text)

        if amount <= 0:
            print("Ставка должна быть больше нуля.")
            continue

        if amount > balance:
            print("Недостаточно средств!")
            continue

        if bet != "even" and bet != "odd":
            print("Ошибка! Ставка должна быть even или odd.")
            continue

        turns = turns + 1

        if turns % 2 == 0:
            result = "even"
        else:
            result = "odd"

        print("Результат:", result)

        if bet == result:
            balance = balance + amount
            wins = wins + 1
            print("Вы выиграли!")
        else:
            balance = balance - amount
            losses = losses + 1
            print("Вы проиграли!")

        print("Текущий баланс:", balance)

    else:
        print("Неизвестная команда. Попробуйте снова.")