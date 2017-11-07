#!/usr/bin/env python
#-*- encoding=utf-8 -*-

import rospy

from std_msgs.msg import String
# from std_msgs.msg import Int32
import sys
import os
from create_dict import create_dict as cd

prev_person = ''
edited_text_pub = ''

current_time = 0
last_time = 0
interval = 10.0

input_text_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/input/say_hello.txt"

def get_dict():
	person_dict = cd()
	return person_dict


def make_text_callback(data):
	global prev_person, last_time, current_time
	person_chinese_names = get_dict()
	person = data.data

	if (person in person_chinese_names) and not (person == prev_person):
		# hello_file = open(input_text_path, 'w')
		say_hello = person_chinese_names[person] + ", 您好"
		# hello_file.write(say_hello)
		# hello_file.close()
		edited_text_pub.publish(say_hello)
		last_time = rospy.get_time()
		# print 'written'
	current_time = rospy.get_time()
	if current_time - last_time > interval:
		prev_person = ''
	else:
		prev_person = person


if __name__ == "__main__":
	rospy.init_node("input_text_node")
	rospy.Subscriber("detected_person", String, make_text_callback)
	edited_text_pub = rospy.Publisher("edited_text", String, queue_size = 1)

	last_time = rospy.get_time()
	current_time = rospy.get_time()

	try:
		while not rospy.is_shutdown():
			pass
	except rospy.ROSInterruptException:
		pass
