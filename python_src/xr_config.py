# coding:utf-8
"""
Source code for Raspberry Pi WiFi wireless video car robot driver
Author: Sence
Copyright: XiaoR Technology (Shenzhen Xiao Er Geek Technology Co., Ltd. www.xiao-r.com); WIFI Robot Forum www.wifi-robots.com
This code can be freely modified, but it is prohibited to use it for commercial profit purposes!
This code has been applied for software copyright protection, and legal action will be taken immediately upon discovery of infringement!
"""
"""
@version: python3.7
@Author  : xiaor
@Explain : Configuration file
@contact :
@Time    :2020/05/09
@File    :xr_config.py
@Software: PyCharm
"""

from socket import *
import numpy as np

CRUISING_FLAG = 0  			# Current loop mode, different flags enter different modes, changed by parameters sent from the upper computer software.
PRE_CRUISING_FLAG = 0  		# Pre-loop mode
CRUISING_SET = {'normal': 0, 'irfollow': 1, 'trackline': 2, 'avoiddrop': 3, 'avoidbyragar': 4, 'send_distance': 5,
		 'maze': 6, 'camera_normal': 7, 'camera_linepatrol': 8, 'facefollow':9, 'colorfollow':10, 'qrcode_detection':11}
CAMERA_MOD_SET = {'camera_normal': 0, 'camera_linepatrol': 1, 'facefollow':2, 'colorfollow':3, 'qrcode_detection':4}

ANGLE_MAX = 160  			# Maximum servo angle value to prevent servo jamming, can be set to a value less than 180
ANGLE_MIN = 15  			# Minimum servo angle value to prevent servo jamming, can be set to a value greater than 0

VOICE_MOD = 0
VOICE_MOD_SET = {'normal': 0, 'openlight': 1, 'closelight': 2, 'forward': 3, 'back': 4, 'left': 5,
		 'right': 6, 'stop': 7, 'nodhead': 8, 'shakehead':9}

PATH_DECT_FLAG = 0  		# Camera line detection flag, 0 for black line detection (light-colored ground, dark line); 1 for white line detection (dark-colored ground, light line)

LEFT_SPEED = 80  			# Robot left side speed
RIGHT_SPEED = 80  			# Robot right side speed
LASRT_LEFT_SPEED = 100  	# Previous robot left side speed
LASRT_RIGHT_SPEED = 100  	# Previous robot right side speed

SERVO_NUM = 1				# Servo number
SERVO_ANGLE = 90			# Servo angle
SERVO_ANGLE_LAST = 90		# Previous servo angle
ANGLE = [90, 90, 90, 90, 90, 90, 90, 5]		# Angles stored for 8 servos

DISTANCE = 0  			# Ultrasonic distance value
AVOID_CHANGER = 1  		# Ultrasonic obstacle avoidance start flag
AVOIDDROP_CHANGER = 1 	# Infrared drop prevention start flag

MAZE_TURN_TIME = 400    # Maze state turn angle setting

CAMERA_MOD = 0  		# Camera mode
LINE_POINT_ONE = 320  	# Camera line detection line 1 x-coordinate
LINE_POINT_TWO = 320  	# Camera line detection line 2 x-coordinate

CLAPPER = 4  			# Buzzer music beat
BEET_SPEED = 50  		# Buzzer playback speed
TUNE = 0  				# Piano pitch default is C, 0-6 corresponds to CDEFGAB

VREF = 5.12  			# Reference voltage value
POWER = 3  				# Power value 0-3
LOOPS = 0  				# Timing detection value
PS2_LOOPS = 0  			# Timing detection value

PROGRAM_ABLE = True		# System program running status

LIGHT_STATUS = 0  		# Headlight status
LIGHT_LAST_STATUS = 0  	# Previous headlight status
LIGHT_OPEN_STATUS = 0   # Headlight open status
STOP = 1  				# Headlight stop status
TURN_FORWARD = 2 		# Headlight forward status
TURN_BACK = 3			# Headlight backward status
TURN_LEFT = 4  			# Headlight left turn status
TURN_RIGHT = 5  		# Headlight right turn status
POWER_LIGHT = 1  		# Set power light group flag
CAR_LIGHT = 2  			# Set car light group flag

# RGB light color value settings, only these colors are allowed, no other colors can be set
COLOR = {'black': 0, 'red': 1, 'orange': 2, 'yellow': 3, 'green': 4, 'Cyan': 5,
		 'blue': 6, 'violet': 7, 'white': 8}

LOGO = "XiaoR GEEK"  # Information displayed on the OLED screen is in English
OLED_DISP_MOD = ["Normal Mode", "Infrared Follow", "Infrared Line Detection", "Infrared Drop Prevention", "Ultrasonic Obstacle Avoidance",
				 "Ultrasonic Distance Display", "Ultrasonic Maze Navigation", "Camera Debugging",
				 "Camera Line Detection", "Face Detection Follow", "Color Detection Follow", "QR Code Recognition",
				 ]  # Mode display is in Chinese
OLED_DISP_MOD_SIZE = 16  # Chinese characters occupy 16 pixels, change this value to 8 if the mode display font is changed to English

BT_CLIENT = False  	# Bluetooth client
TCP_CLIENT = False  # TCP client
RECV_LEN = 5 		# Length of received characters

# Bluetooth server parameter settings
BT_SERVER = socket(AF_INET, SOCK_STREAM)
BT_SERVER.bind(('', 2002))		# Bluetooth binds to port 2002
BT_SERVER.listen(1)

# TCP server parameter settings
TCP_SERVER = socket(AF_INET, SOCK_STREAM)
TCP_SERVER.bind(('', 2001))		# WIFI binds to port 2002
TCP_SERVER.listen(1)

# PS2 controller button definitions
PS2_ABLE = False		# PS2 controller connection status flag
PS2_READ_KEY = 0		# Read PS2 controller value
PS2_LASTKEY = 0			# Previous PS2 controller value
PS2_KEY = {'PSB_PAD_UP': 1, 'PSB_PAD_DOWN': 2, 'PSB_PAD_LEFT': 3, 'PSB_PAD_RIGHT': 4,
'PSB_RED': 5, 'PSB_PINK': 6, 'PSB_GREEN': 7, 'PSB_BLUE': 8}		# Left side up, down, left, right and right side function buttons of the controller

# Color detection follow color ranges
# Color range low threshold
COLOR_LOWER = [
	# Red
	np.array([0, 43, 46]),
	# Green
	np.array([35, 43, 46]),
	# Blue
	np.array([100, 43, 46]),
	# Purple
	np.array([125, 43, 46]),
	# Orange
	np.array([11, 43, 46])
]
# Color range high threshold
COLOR_UPPER = [
	# Red
	np.array([10, 255, 255]),
	# Green
	np.array([77, 255, 255]),
	# Blue
	np.array([124, 255, 255]),
	# Purple
	np.array([155, 255, 255]),
	# Orange
	np.array([25, 255, 255])
]
COLOR_FOLLOW_SET = {'red': 0, 'green': 1, 'blue': 2, 'violet': 3, 'orange': 4}		# Color follow function color range index settings, used in socket communication
COLOR_INDEX = 0			# Color range threshold index, changed in socket communication

BARCODE_DATE = None		# QR code recognition data
BARCODE_TYPE = None		# QR code recognition data type
