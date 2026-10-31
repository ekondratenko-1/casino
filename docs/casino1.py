print("Добро пожаловать в казино «Удача»!")
print("Начальный баланс: 1000")
print("Команды: bet <сумма> <even/odd>, balance, history, exit")

balance = 1000
wins = 0
losses = 0
turns = 0
while True:
    command = input("Введите команду: ")
    command = command.strip()
    if command == "exit":
        print("Игра завершена.")
        print("Итоговый баланс:", balance)
        break

    elif command == "balance":
        print("Ваш баланс:", balance)

    elif command == "history":
        print("Победы:", wins)
        print("Поражения:", losses)

    elif command.startswith("bet "):
        parts = command.split()

        if len(parts) != 3:
            print("Ошибка! Формат: bet <сумма> <even/odd>")
            continue

        try:
            amount = int(parts[1])
        except ValueError:
            print("Ошибка! Сумма должна быть целым числом.")
            continue

        bet = parts[2]

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