from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self)
		self.setTitle("Blue Window")
		self.setSize(2000, 1000)
		self.setBackground("Blue")
		self.setResizable(False)
# def main():
	# LabelDemo().mainloop()

if __name__ == "__main__":
	LabelDemo().mainloop()
