import time
from random import randint
import socket

import key_control

class MotionMaker():

    def __init__(self):
        self.DNA = list()
        self.HOST = "localhost"
        self.PORT = 9999
        self.running = True

    def makeCon(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            s.bind((self.HOST, self.PORT))
        except socket.error as err:
            print('Bind failed. Error Code : '.format(err))
        s.listen(10)
        print("Socket Listening")
        self.conn, self.addr = s.accept()


    def receve(self):

        data = self.conn.recv(1024)
        clientInput = data.decode(encoding='UTF-8')
        print(clientInput)
        listOfCommands = clientInput.split(";")[:-1]
        for oneCommand in listOfCommands:
            print(oneCommand)
            words = oneCommand.split(" ")
            command = words[0]
            if command == "make_mouse_move:":
                self.make_mouse_move(x=int(words[1]), y=int(words[2]))
            elif command == "start_placing:":
                self.start_placing()
            elif command == "stop_placing:":
                self.stop_placing()
            elif command == "start_digging:":
                self.start_digging()
            elif command == "stop_digging:":
                self.stop_digging()
            elif command == "hot_bar:":
                self.hot_bar(index=int(words[1]))
            elif command == "stop_jump:":
                self.stop_jump()
            elif command == "start_jump:":
                self.start_jump()
            elif command == "open_inv:":
                self.open_inv()
            elif command == "start_player_move:":
                self.start_player_move()
            elif command == "stop_player_move:":
                self.stop_player_move()
            elif command == "stop:":
                self.running = False
                self.stop_player_move()
                self.stop_jump()
                self.stop_placing()
                self.stop_digging()
                self.hot_bar(0)
            elif command == "reload:":
                self.stop_player_move()
                self.stop_jump()
                self.stop_placing()
                self.stop_digging()
                self.hot_bar(0)
                self.open_inv()
                time.sleep(0.1)
                self.make_mouse_move(400, -40)
                self.start_digging()
                self.stop_digging()
                self.open_inv()
                time.sleep(0.1)
                self.make_mouse_move(400, -40)
                self.start_digging()
                self.stop_digging()





    def make_mouse_move(self, x, y):
        key_control.Mouse(key_control.MOUSEEVENTF_MOVE, x, y)

    def start_placing(self):
        key_control.Mouse(key_control.MOUSEEVENTF_RIGHTDOWN)

    def stop_placing(self):
        key_control.Mouse(key_control.MOUSEEVENTF_RIGHTUP)

    def start_digging(self):
        key_control.Mouse(key_control.MOUSEEVENTF_LEFTDOWN)

    def stop_digging(self):
        key_control.Mouse(key_control.MOUSEEVENTF_LEFTUP)

    def digging(self, timer_time=None):
        key_control.Mouse(key_control.MOUSEEVENTF_LEFTDOWN)
        if time == None:
            msg = ""
            while msg != "blockBreak:":
                time.sleep(1)
                data = self.conn.recv(1024)
                clientInput = data.decode(encoding='UTF-8')
                words = clientInput.split(" ")
                msg = words[0]
        else:
            time.sleep(timer_time)
        key_control.Mouse(key_control.MOUSEEVENTF_LEFTUP)

    def hot_bar(self, index=None):
        listOfSlots = [0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x10]
        if index == None:
            rand_int_x = randint(0, len(listOfSlots)-1)
            key_control.Keyboard(listOfSlots[rand_int_x], 0x0008)
            key_control.Keyboard(listOfSlots[rand_int_x], 0x000108 | 0x0002)
        else:
            key_control.Keyboard(listOfSlots[index], 0x0008)
            key_control.Keyboard(listOfSlots[index], 0x000108 | 0x0002)



    def stop_jump(self):
        key_control.Keyboard(0x39, 0x000108 | 0x0002)

    def start_jump(self):
        key_control.Keyboard(0x39, 0x0008)

    def open_inv(self):
        key_control.Keyboard(0x12, 0x0008)
        key_control.Keyboard(0x12, 0x000108 | 0x0002)


    def start_player_move(self):
        key_control.Keyboard(0x11, 0x0008)

    def stop_player_move(self):
        key_control.Keyboard(0x11, 0x000108 | 0x0002)

    def start2(self):
        time.sleep(1)
        while (self.running):
            self.receve()

    def start(self):
        time.sleep(1)
        while (self.running):
            self.random_hot_bar()
            randint2 = randint(0, 1900)
            if randint2 < 200:
                self.start_player_move()
            if randint2 >= 200 and randint2 < 400:
                self.stop_player_move()
            if randint2 >= 400 and randint2 < 600:
                self.start_digging()
            if randint2 >= 600 and randint2 < 800:
                self.stop_digging()
            if randint2 >= 800 and randint2 < 1000:
                self.make_rand_mouse_move()
            if randint2 >= 1000 and randint2 < 1200:
                self.start_jump()
            if randint2 >= 1200 and randint2 < 1400:
                self.stop_jump()
            if randint2 >= 1400 and randint2 < 1600:
                self.start_placing()
            if randint2 >= 1600 and randint2 < 1800:
                self.stop_placing()
            if randint2 >= 1800 and randint2 < 1900:
                self.open_inv()

            time.sleep(1)



mm = MotionMaker()
mm.makeCon()
mm.start2()

