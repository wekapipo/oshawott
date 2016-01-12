from sys import exit

def den():
	print "Welcome to the Den of Unbelievers."
	print "Choose your Punishment."
	print "1. 1000 Years of a Moody Wale. \n2. 2000 Years of MattyB Raps"
	
	choice = raw_input("> ")
	if choice == "1":
		print "You are forced to Listen to the worst music of all time for all of time. Game Over."
		exit(0)
	elif choice == "2":
		print "You listen to the second worst music of all time for all of time. Game Over."
		exit(0)
	else:
		print "Next time, learn to type a number choice guy. Now you suffer both punishments. Game Over"
		exit(0)

def circle():
	print "Welcome to the Circle of the Righteous"
	print "We Gon be Alright."
	exit(0)

def heathen():
	print "BEGONE HEATHEN"
	print "..."
	print "..."
	print "..."
	den()
	
def counsel():
	print "Welcome to the Counsel of Believers"
	print "Do you Believe the Album is flawless?"
	print "1. Of Course \n2. Ehh, It could be better"
	
	choice = raw_input("> ")
	if choice == "1":
		print "You have earned your way into the inner circle"
		print "..."
		print "..."
		print "..."
		circle()
	elif choice == "2":
		print "You are a Heathen"
		heathen()
	else:
		print "You must be some kind of Heathen"
		heathen()

def start():
	print "Is To Pimp a Butterfly the Greatest Album of All Time?"
	print "1. Yes \n2. No"
	
	choice = raw_input("> ")
	if choice == "1":
		counsel()
	elif choice == "2":
		den()
	else:
		print "Not a Valid Answer Fammo"
		start()

start()		
