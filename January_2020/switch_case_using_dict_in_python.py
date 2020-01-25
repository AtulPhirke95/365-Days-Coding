def one():
	return "You are in function one"
def two():
	return "You are in function two"
def three():
	return "You are in function three"
def four():
	return "You are in function four"

def switch(func):
	dict = {"one":one,"two":two,"three":three,"four":four}
	function = dict.get(func.lower(),"function not defined")
	return function()

var = switch("Two")
print(var)
