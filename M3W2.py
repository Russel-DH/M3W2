def send_email(message, recipient, sender = "university.help@gmail.com"):
    # проверка на корректность е-мэйл отправителя и получателя
    msg = []
    error = 0
    if ".ru" in recipient or ".com" in recipient or ".net" in recipient:
        error = 0
    else:
        error = 1
    if ".ru" in sender or ".com" in sender or ".net" in sender:
        error = 0
    else:
        error = 1
    if "@" not in recipient or "@" not in sender or error == 1:
        msg.append(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == recipient:
        msg.append("Невозможно отправить письмо самому себе")
    if sender == "university.help@gmail.com":
        msg.append(f'Письмо успешно отправлено с адреса "{sender}" на адрес "{recipient}"')
    else:
        msg.append(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "{sender}" на адрес "{recipient}"')
    #print(msg)
    print(msg[0])

send_email(input("Type message: "), input("Type recipient's e-mail: "), input("Type sender's e-mail: "))
print()
print("End of file")