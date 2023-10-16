import Calculator

equation = ""

def show(value):
    global equation
    equation += value
    Calculator.label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    Calculator.label_result.config(text=equation)
    
def calculator():
    global equation
    if equation != "":
        try:
            Calculator.label_result.config(text=eval(equation))
        except SyntaxError:
            Calculator.label_result.config(text="Error")
    
    
    