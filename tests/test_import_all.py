#!/usr/bin/env python
# -*- coding: utf-8 -*-
from imreadeval import *

def test_imread():
	import os
	test_image_directory = os.path.join(os.path.dirname(__file__), '..', 'images')
	filename = os.path.join(test_image_directory, r'squirrel.jpg')
	try:
		im = imread(filename)
	except Exception as e:
		assert False
		return
	assert True

def test_imread_eval():
	try:
		imread_eval()
	except Exception as e:
		assert False
		return
	assert True
