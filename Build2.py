import sublime
import sublime_plugin
import subprocess
from subprocess import call
import os

class CExecuteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = self.view.window().active_view().file_name()
		head , tail = os.path.split(file_name)
		file = tail.split(".")
		name = head + "\\" + file[0] + ".exe"
		print(name)
		#print(head)
		#call(["cd" , head] , shell = True)
		#head = head + "\\a.exe"
		#print(head)
		try:
			#print(subprocess.check_output(["cd" , head]))
			print("aman1")
			print(subprocess.check_output(["g++" , file_name , "-o" , name] , shell = True))
			#call([head , "<"  ,  "input.txt" ,  ">"  , "output.txt"] , shell = True)
		except Exception as e:
			print("Some problem occured")
			print(e)
		
		
		#call("a.exe < input.txt > output.txt")

		#self.view.insert(edit, 0, "Hello, World!")
