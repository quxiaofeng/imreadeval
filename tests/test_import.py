#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_import_imread():
	import os
	import ..imreadeval
	test_image_directory = os.path.join(os.path.dirname(__file__), '..', 'images')
	filename = os.path.join(test_image_directory, r'squirrel.jpg')
	try:
		im = imreadeval.imread(filename)
	except Exception as e:
		assert False
		return
	assert True

def test_import_imread_eval():
	import ..imreadeval
	try:
		imreadeval.imread_eval()
	except Exception as e:
		assert False
		return
	assert True
