import datetime


def yesterday():
    return datetime.date.today() - datetime.timedelta(1)


print(yesterday())
