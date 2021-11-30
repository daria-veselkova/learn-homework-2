"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta
import locale


locale.setlocale(locale.LC_TIME, "russian")


def print_days():
    date_now = date.today()
    date_yesterday = date_now - timedelta(days=1)
    date_30_days_ago = date_now - timedelta(days=30)

    print(f'Вчера было {date_yesterday.strftime("%x")}')
    print(f'Сегодня {date_now.strftime("%x")}')
    print(f'30 дней назад было {date_30_days_ago.strftime("%x")}')


def str_2_datetime(date_string):
    datetime_object = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return f'После перевода строки в объект datetime получилось {datetime_object}'

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
