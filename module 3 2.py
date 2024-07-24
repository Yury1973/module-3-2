def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '.com' not in sender and '.net' not in sender and '.ru' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif '.com' not in sender and '.net' not in sender and '.ru' not in recipient:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif '@' not in sender or '@' not in recipient:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса', 'urban.fan@gmail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
