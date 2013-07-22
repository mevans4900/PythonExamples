__author__ = 'mevans'

import sys

def printTestOne (y):
    """

    :param y: string to print
    """
    print y

def printTestTwo(y):
    pr = "the string arg is: %s" % y
    print pr


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

x = "this is a test"
print x
printTestOne(x)
printTestTwo(x)




