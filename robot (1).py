import socket
import time


class RobotControl:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.commands = {
            'forward': 0x01,  # Двигаться вперед
            'backward': 0x02,  # Двигаться назад
            'turn_left': 0x03,  # Повернуть налево
            'turn_right': 0x04,  # Повернуть направо
            'stop': 0x00  # Остановиться
        }

    def _build_command(self, header, data_bytes):
        """Собирает общую структуру команды с контрольными байтами"""
        return bytes([0xff] + header + data_bytes + [0xff])

    def send_to_robot(self, command):
        """Отправка команды роботу через сокет"""
        try:
            # Создаем сокет
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Соединение с {self.host}:{self.port}")

            # Устанавливаем соединение
            s.connect((self.host, self.port))
            print(f"Отправка команды: {command}")

            # Отправляем команду
            s.sendall(command)

            # Добавляем небольшую задержку между отправками команд
            time.sleep(1)

            return True
        except socket.error as e:
            print(f"Ошибка сокета: {e}")
            return False
        finally:
            # Закрываем соединение
            s.close()
            print("Соединение закрыто")

    def move_direction(self, command):
        """Двигает робота в заданном направлении"""
        command_byte = self.commands.get(command, 0x00)
        return self._build_command([0x00], [command_byte, 0x00])

    def set_left_motor_speed(self, speed):
        """Устанавливает скорость левого двигателя (от 0 до 100)"""
        return self._build_command([0x02], [0x01, speed])

    def set_right_motor_speed(self, speed):
        """Устанавливает скорость правого двигателя (от 0 до 100)"""
        return self._build_command([0x02], [0x02, speed])

    def move_robot(self, command, speed=50):
        """Комбинированная функция для движения робота с установкой скорости"""
        return self.move_direction(command) + self.set_left_motor_speed(speed) + self.set_right_motor_speed(speed)

    def set_servo_position(self, servo_id, angle):
        """Управляет положением одного сервопривода (угол от 0 до 180)"""
        if 0 <= angle <= 180:
            return self._build_command([0x01], [servo_id, angle])
        else:
            raise ValueError("Angle must be between 0 and 180 degrees")

    def set_robohand_position(self, angle1, angle2, angle3, angle4):
        """Управляет положением всех четырех сервоприводов роборуки"""
        return (self.set_servo_position(0x01, angle1) +
                self.set_servo_position(0x02, angle2) +
                self.set_servo_position(0x03, angle3) +
                self.set_servo_position(0x04, angle4))

    def set_defolt_robohand(self):
        return self._build_command([0x33], [0x00, 0x00])

    def set_rgb_lights(self, mode, color=0x00):
        """Устанавливает режим RGB-светодиодов"""
        if mode == 'normal':
            return self._build_command([0x06], [0x00, color])
        elif mode == 'irfollow':
            return self._build_command([0x06], [0x01, color])
        elif mode == 'trackline':
            return self._build_command([0x06], [0x02, color])
        elif mode == 'mode1':
            return self._build_command([0x06], [0x03, color])
        elif mode == 'mode2':
            return self._build_command([0x06], [0x04, color])
        else:
            raise ValueError("Invalid RGB mode")

    def set_car_lights(self, state):
        """Управляет фарами робота (включение/выключение)"""
        if state == 'on':
            return self._build_command([0x33], [0x00, 0x00])
        elif state == 'off':
            return self._build_command([0x33], [0x01, 0x00])
        else:
            raise ValueError("Invalid light state")

    def press_the_button(self):
        self.set_robohand_position()

    def grab_the_cube(self):
        """Последовательность действий для схватывания кубика"""
        # Подъехать к кубику
        self.send_to_robot(self.move_robot('forward', speed=50))
        time.sleep(2)  # Подождать 2 секунды, чтобы робот подъехал к кубику

        # Повернуть роборуку в нужное положение
        self.send_to_robot(self.set_robohand_position(90, 90, 90, 90))
        time.sleep(1)  # Подождать 1 секунду, чтобы роборука повернулась

        # Схватить кубик
        self.send_to_robot(self.set_robohand_position(45, 45, 45, 45))
        time.sleep(1)  # Подождать 1 секунду, чтобы роборука схватила кубик

        # Поднять кубик
        self.send_to_robot(self.set_robohand_position(0, 0, 0, 0))
        time.sleep(1)  # Подождать 1 секунду, чтобы роборука подняла кубик

        print("Кубик схвачен")

    def follow_path(self, path):
        """Следовать по пути, найденному алгоритмом A*"""

        for i in range(len(path) - 1):
            current = path[i]
            next_pos = path[i + 1]
            direction = self.get_direction(current, next_pos)
            self.send_to_robot(self.move_robot(direction, speed=50))
            time.sleep(1)  # Подождать 1 секунду между движениями

    def get_direction(self, current, next_pos):
        """Определить направление движения на основе текущей и следующей позиции"""
        if next_pos[0] > current[0]:
            return 'forward'
        elif next_pos[0] < current[0]:
            return 'backward'
        elif next_pos[1] > current[1]:
            return 'turn_right'
        elif next_pos[1] < current[1]:
            return 'turn_left'
        else:
            return 'stop'




