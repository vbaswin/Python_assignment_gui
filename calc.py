# Name: Aswin V B
# Rollno: 222
# Program Description: GUI Calculator that supports simple arithmetic operations using python


from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self)
		self.setTitle("Basic Calculator")
		self.setResizable(False)
		button_panel = self.addPanel(0, 0, background="pink", columnspan=6, rowspan=3)
		button_panel = self.addPanel(3, 0, background="lightblue", columnspan=6, rowspan=3)

		self.operator1_label = self.addLabel(text="Operator1", row = 0, column= 0,background="pink")
		self.operator1= self.addFloatField(value=0.0,row = 0, column=1, precision=2)
		self.operator1_label = self.addLabel(text="Operator2", row =1, column= 0,background="pink")
		self.operator2= self.addFloatField(value=0.0,row = 1, column=1, precision=2)
		self.result_label= self.addLabel(text="Result", row =2, column= 0, background="pink")
		self.result= self.addFloatField(value=0.0,row = 2, column=1, precision=2, state="readonly")

		self.add_button = self.addButton(text="+", row = 3, column=0, command=self.add)
		self.sub_button = self.addButton(text="-", row = 3, column=1, command=self.sub)
		self.mul_button = self.addButton(text="*", row = 3, column=2, command=self.mul)
		self.div_button = self.addButton(text="/", row = 4, column=0, command=self.div)
		self.div_button = self.addButton(text="%", row = 4, column=1, command=self.mod)
		self.div_button = self.addButton(text="**", row = 4, column=2, command=self.exp)
		self.clear_button = self.addButton(text="clr", row = 5, column=1, command=self.clear)

	def add(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 + op2)
	def sub(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 - op2)
	def mul(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 * op2)
	def div(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 / op2)
	def mod(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 % op2)
	def exp(self):
		op1 = self.operator1.getNumber()
		op2 = self.operator2.getNumber()
		self.result.setNumber(op1 ** op2)
	def clear(self):
		self.operator1.setNumber(0)
		self.operator2.setNumber(0)
		self.result.setNumber(0)


if __name__ == "__main__":
	LabelDemo().mainloop()
