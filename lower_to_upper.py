import sublime
import sublime_plugin


class ChangeCaseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		points = self.view.sel()
		for point in points:
			text = self.view.substr(point);
			repl = self.changeCase(text);
		
			self.view.replace(edit,point,repl);
		#self.view.replace(edit,points,'demo')
		
	def changeCase(self,text):
		changedWord = '';
		for char in text:
			if char.isalpha():
				if char.isupper():
					changedWord = changedWord +  str(char.lower())
				else:
					upp = char.upper()
					changedWord = changedWord +  str(upp);
					#print(changedWord);
			else:
				changedWord = changedWord + char

		return changedWord


		#self.view.insert(edit, 0, "Hello, World!")
