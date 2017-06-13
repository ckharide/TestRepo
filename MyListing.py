
import os
import sys


def test():
	print 'Hello Test'


def getfilesCount():
  d = os.getcwd()
  print d
  print "current working directory {}.".format(d)
  count = 0
  ext = '.java'
  totalfiles = 0

  for dirname, dirnames, filenames in os.walk(d):
	for filename in filenames:
	  name = os.path.join(dirname,filename)
	  #print os.path.splitext(name)[1]
	  if (os.path.splitext(name)[1] == ext):
	  	totalfiles +=1
	  	count += countlines(name)
  return (count , totalfiles)

def countlines(name):
  f = open(name,'rb')
  lines = 0
  buf_size = 1024 * 1024
  read_f = f.read # loop optimization


  buf = read_f(buf_size)
  
  while buf:
    lines += buf.count('\n')
    buf = read_f(buf_size)
    return lines

if __name__ == '__main__':
  test()
  fc,files = getfilesCount()
  print "Total number of files and lines in the files are {} {}. ".format(files,fc)
