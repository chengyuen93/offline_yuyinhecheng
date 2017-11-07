#!/usr/bin/env python
#-*- encoding=utf-8 -*-

import rospy
import rospkg
import os


rospack = rospkg.RosPack()

facerec_path = rospack.get_path('arcsoft_facerec')

def create_dict():
	person_path = facerec_path + '/src/data_base'
	persons = os.listdir(person_path)
	person_dict = {}
	for person in persons:
		name_file_path = person_path + '/' + person + '/name.txt'
		name_file = open(name_file_path, 'r')
		chinese_name = name_file.readline().strip()
		name_file.close()
		person_dict.update({person:chinese_name})

	return person_dict