# import the time module
import time
'''
class ab:  
# define the countdown func.
	def countdown(self, t):
		while t:
			mins, secs = divmod(t, 60)
			timer = '{:2d}'.format(secs)
			print(timer, end="\r")
			time.sleep(1)
			t -= 1
		  
	print('Fire in the hole!!')
	  
	  
	# input time in seconds
	#t = input("Enter the time in seconds: ")
	  
	# function call
	countdown(x, int(5))
'''
def countdown(t):

	while t:
	    mins, secs = divmod(t, 60)
	    timer = '{:02d}:{:02d}'.format(mins, secs)
	    print(timer, end="\r")
	    time.sleep(1)
	    t -= 1
	  
	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))
