import random
import casino_data

random.seed(19)


def show_help():
    print(casino_data.HELP_TEXT)


def make_bet(balance, amount):
    return balance - amount


def spin():
    number = random.randint(1, 2)

    if number == 1:
        return "even"
    else:
        return "odd"


def random_result():
    number = random.randint(1, 100)

    if number <= casino_data.JACKPOT_CHANCE:
        return "jackpot"
    elif number <= casino_data.JACKPOT_CHANCE + casino_data.LOSING_STREAK_CHANCE:
        return "losing_streak"
    else:
        return "none"


print(casino_data.WELCOME_TEXT)

balance = 1000
wins = 0
losses = 0
losing_streak = 0

show_help()

while True:
    command = input("Введите команду: ")

    if command == "exit":
        print("Игра завершена.")
        print("Итоговый баланс:", balance)
        break

    elif command == "balance":
        print("Ваш баланс:", balance)

    elif command == "history":
        print("Победы:", wins)
        print("Поражения:", losses)

    elif command == "help":
        show_help()

    elif command.startswith("bet "):
        rest = command[4:]
        amount_text, space, bet = rest.partition(" ")

        if not space or " " in bet or not amount_text or not bet:
            print("Ошибка! Формат: bet <сумма> <even/odd>")
            continue

        if not amount_text.isdigit():
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

        balance = make_bet(balance, amount)

        event = "none"

        if losing_streak == 0:
            event = random_result()

        if event == "jackpot":
            print(casino_data.JACKPOT_TEXT)

        elif event == "losing_streak":
            print(casino_data.LOSING_STREAK_TEXT)
            losing_streak = 2

        if losing_streak > 0:
            if bet == "even":
                result = "odd"
            else:
                result = "even"

            losing_streak = losing_streak - 1
        else:
            result = spin()

        print("Результат:", result)

        if bet == result:
            if event == "jackpot":
                balance = balance + amount * 3
            else:
                balance = balance + amount * 2

            wins = wins + 1
            print("Вы выиграли!")

        else:
            losses = losses + 1
            print("Вы проиграли!")

        print("Текущий баланс:", balance)

    else:
        print("Неизвестная команда. Попробуйте снова.")