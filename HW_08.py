from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Визначаємо поточний день та день наступного понеділка
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    next_monday = today + timedelta(days=(7 - today.weekday()))

    # Створюємо словник, де ключі - дні тижня, значення - список ім'янинників на цей день
    birthdays = {}
    for i in range(7):
        day = next_monday + timedelta(days=i)
        birthdays[day.strftime('%A')] = []

    # Додаємо ім'янинників відповідно до їх дня народження
    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year)
        if birthday < today:
            # Якщо день народження вже був у цьому році, додаємо наступний рік
            birthday = birthday.replace(year=today.year + 1)
        day_diff = (birthday - today).days
        if day_diff < 7:
            # Якщо день народження відбувається протягом наступного тижня, додаємо до списку ім'янинників на цей день
            birthday_day = next_monday + timedelta(days=day_diff)
            birthdays[birthday_day.strftime('%A')].append(name)
        else:
            # Якщо день народження не відбувається протягом наступного тижня, не додаємо його до списку
            pass

    # Виводимо список ім'янинників на кожен день тижня
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    users = [{"name": "Anton", "birthday": datetime(day=15, month=4, year=1991)},
             {"name": "Kola", "birthday": datetime(day=14, month=4, year=1992)},
             {"name": "Anton", "birthday": datetime(day=13, month=4, year=1993)},
             {"name": "Ivan", "birthday": datetime(day=12, month=4, year=1994)},
             {"name": "Vano", "birthday": datetime(day=11, month=4, year=1995)},
             {"name": "Olga", "birthday": datetime(day=12, month=4, year=1994)},
             {"name": "Anna", "birthday": datetime(day=13, month=4, year=1993)}]
    get_birthdays_per_week(users)