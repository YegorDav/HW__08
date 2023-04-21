from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Визначаємо поточний день та день наступного понеділка
    today = datetime.now().date()
    next_monday = today + timedelta(days=(7 - today.weekday()))

    start_period = next_monday - timedelta(days=2)
    end_period = next_monday + timedelta(days=4)

    # Створюємо словник, де ключі - дні тижня, значення - список ім'янинників на цей день
    birthdays = {}
    for i in range(7):
        day = next_monday + timedelta(days=i)
        birthdays[day.strftime('%A')] = []

    # Додаємо ім'янинників відповідно до їх дня народження
    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year).date()

        # Період днів народження
        if start_period <= birthday <= end_period:
            # Якщо день народження відбувається протягом вихідних, додаємо до списку ім'янинників на цей понеділок
            day_of_week = birthday.strftime('%A')
            if day_of_week in ("Sunday", "Saturday"):
                birthdays["Monday"].append(name)
            else:
                birthdays[day_of_week].append(name)
                
    # Виводимо список ім'янинників на кожен день тижня
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    users = [{"name": "Anton", "birthday": datetime(day=25, month=4, year=1994)},
             {"name": "Kola", "birthday": datetime(day=26, month=4, year=1995)},
             {"name": "Andrew", "birthday": datetime(day=22, month=4, year=1994)},
             {"name": "Ivan", "birthday": datetime(day=21, month=4, year=1993)},
             {"name": "Vano", "birthday": datetime(day=23, month=4, year=1995)},
             {"name": "Olga", "birthday": datetime(day=12, month=4, year=1994)},
             {"name": "Anna", "birthday": datetime(day=13, month=4, year=1993)}]
    get_birthdays_per_week(users)