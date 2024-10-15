import socket

import time



host = "192.168.1.209"

port = 2001





def send_command(command):

    try:

        # Создаем сокет

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f"Соединение с {host}:{port}")



        # Устанавливаем соединение

        s.connect((host, port))

        print(f"Отправка команды: {command}")



        # Отправляем команду

        s.sendall(command)



        # Добавляем небольшой задержку между отправками команд

        time.sleep(1)



        return True

    except socket.error as e:

        print(f"Ошибка сокета: {e}")

        return False

    finally:

        # Закрываем соединение

        s.close()

        print("Соединение закрыто")





# Первая команда

while True:

    for color in range(1, 6):



        command = bytes([0xff, 0x06, color, 0x00, 0xff])# Пример отправки команды

        result = send_command(command)

print('Команда на установку цвета отправлена: ', result)








