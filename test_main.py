from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(1000, 3, 8) == 1537
	assert simple_work_calc(44, 44, 44) == 88
	assert simple_work_calc(238, 11, 93) == 260

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15 
	assert work_calc(20, 1, 2, lambda n: n*n) == 530 
	assert work_calc(30, 3, 2, lambda n: n) == 300 
	assert work_calc(4, 5, 7, lambda n: n**n) == 256
	assert work_calc(11, 32, 23, lambda n: n**1/2) == 5.5
	assert work_calc(11, 2, 23, lambda n: n+n) == 22

