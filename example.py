import socket
import time

host = "192.168.2.209"
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
        time.sleep(0.4)

        return True
    except socket.error as e:
        print(f"Ошибка сокета: {e}")
        return False
    finally:
        # Закрываем соединение
        s.close()
        print("Соединение закрыто")


def reverse():
    command_m1_speed = bytes([0xff, 0x02, 0x01, 100, 0xff])
    result = send_command(command_m1_speed)

    command_m2_speed = bytes([0xff, 0x02, 0x02, 100, 0xff])
    result = send_command(command_m2_speed)

    command_defolt = bytes([0xff, 0x01, 0x03, 180, 0xff])
    result = send_command(command_defolt)


    # for i in range(0, 180, 60):
    #     command_m1_turn = bytes([0xff, 0x01, 0x03, i, 0xff])
    #     result = send_command(command_m1_turn)
    #
    #     command_m2_turn = bytes([0xff, 0x01, 0x04, i, 0xff])
    #     result = send_command(command_m2_turn)
    #
    #     print('Поворот на угол: ', i)
    #
    # command_defolt = bytes([0xff, 0x33, 0x00, 0x00, 0xff])
    # result = send_command(command_defolt)
    # print('Команда на возврат в исходное положение отправлена: ', result)

    # command_m1_turn = bytes([0xff, 0x02, 0x01, 100, 0xff])
    # result = send_command(command_m1_turn)
    # command_m2_turn = bytes([0xff, 0x02, 0x02, 100, 0xff])
    # result = send_command(command_m2_turn)



# while True:
command_direction = bytes([0xff, 0x00, 0x01, 0x00, 0xff])
result = send_command(command_direction)
    # command_m1_speed = bytes([0xff, 0x02, 0x01, 100, 0xff])  # 5552Пример отправки команды
    # result = send_command(command_m1_speed)
    # command_m2_speed = bytes([0xff, 0x02, 0x02, 100, 0xff])  # 5552Пример отправки команды
    # result = send_command(command_m2_speed)

    # command2 = bytes([0xff, 0x06, 0x02, 0x00, 0xff])  # 5552Пример отправки команды
    # result = send_command(command2)
    # command_defolt = bytes([0xff, 0x33, 0x00, 0x00, 0xff])
    # result = send_command(command_defolt)
    # for i in range(0, 180, 30):
    #
    #     command3 = bytes([0xff, 0x01, 0x03, i, 0xff])  #
    #     result = send_command(command3)
    #     command4 = bytes([0xff, 0x01, 0x04, i, 0xff])  #
    #     result = send_command(command4)
    #     print('Done ', i)

    #command_servo = bytes([0xff, 0x01, 0x04, 150, 0xff])
    #result = send_command(command_servo)
    # reverse()

# print('Команда на установку цвета отправлена: ', result)

