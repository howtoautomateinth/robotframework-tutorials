from py_mini_racer import py_mini_racer
import os 

def execute_custom_js():
	ctx = py_mini_racer.MiniRacer()
	current_location = os.getcwd()
	examplejs = open(current_location + "/library/example_function.js")
	resultexec = ctx.eval(examplejs.read())
	return resultexec