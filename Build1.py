import sublime
import sublime_plugin
import subprocess
#from subprocess import call
import os

class CBuildCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = self.view.window().active_view().file_name()
		head , tail = os.path.split(file_name)
		file = tail.split(".")
		#print(head)
		#call(["cd" , head] , shell = True)
		name = head + "\\" + file[0] + ".exe"
		print(name)
		try:
			#call(["del" , head] , shell = True)
			#print("aman")
			inp = head + "\\input.txt"
			out = head + "\\output.txt"
			print(inp)
			print(out)
			#print(call(["g++" , file_name] , shell = True))
			print(subprocess.check_output([name , "<"  , inp ,  ">"  , out] , shell = True).decode('utf-8'))
			#print(result.stdout , result.stderr)
			#call([name , "<"  , inp ,  ">"  , out] , shell = True)
		except Exception as e:
			print("Some problem occured")
			print(e)
		
		
		#call("a.exe < input.txt > output.txt")

		#self.view.insert(edit, 0, "Hello, World!")
