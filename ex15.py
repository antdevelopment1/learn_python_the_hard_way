#This line below says we want import featues/methods from the sys Python set.
#Rather than give all the featues at once Python gives you what you plan to use
#argv is a variable name that is given and used commonly in programming
#The variable holds the argument you pass to your pythoin script when you run it.
from sys import argv
script, filename = argv
txt = open(filename)
#The open method is called on filename and saved in a variable called txt
print "Here's your file %r:" % filename
#We print the filename
print txt.read()
#We print what has been saved in txt and read it by calling a read method
print "Type the filename again:"
file_again = raw_input("> ")
#We are asked to type the filename maybe to confirm that this is the file we want.
txt_again = open(file_again)
#Here we save the filename that was passed when we were prompted for what file
#We then call the open method on file_name and save that value to txt_again
print txt_again.read()
#We print the value of txt_again after calling a read method on that value
#Allowing us to read the file
