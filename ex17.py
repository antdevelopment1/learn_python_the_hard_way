from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too. How?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Hit RETURN to continue, CTRL_C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright. All done."

out_file.close()
in_file.close()
