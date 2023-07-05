from breezypythongui import EasyFrame 
class LabelDemo(EasyFrame):
	"""Displays a greeting in a window."""
	def __init__(self):
		"""Sets up the window and the label.""" 
		EasyFrame.__init__(self) 
		self.addLabel(text = "Hello world!", row = 0, column = 0)
# Instantiates and pops up the window.
if __name__ == "__main__":
    LabelDemo().mainloop()