#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_import_imread():
	import os
	from imreadeval import imread
	test_image_directory = os.path.join(os.path.dirname(__file__), '..', 'images')
	filename = os.path.join(test_image_directory, "squirrel.jpg")
	try:
		im = imread(filename)
	except Exception as e:
		assert False
		return
	assert True