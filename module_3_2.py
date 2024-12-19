def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or (
        not (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"))
    ):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    else:
        if sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
            return
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

# Проверки из задания
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')