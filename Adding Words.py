#The program is a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
def concatenate(*args):
	return '-'.join(args)
print(concatenate("I", "love", "Python", "!"))
