#!/usr/bin/python
__author__ = 'mevans'



import sys, getopt

def main(argv):

    print "trace 1"
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    foobar = ["one","two","three"]
    z = '|'.join(foobar)
    x = "check join with:".join("this is a joined string")
    print "z=" + z
    print "opts:" + str(opts)
    print "args:" + str(args)


#    sys.exit(0)
    inputfile = ''
    outputfile = ''

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        if opt in ("-i", "--ifile"):
            inputfile = arg
        else:
            inputfile = "not specified"
        if opt in ("-o", "--ofile"):
             outputfile = arg

    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

if __name__ == "__main__":
#   main(sys.argv[1:])
    main(sys.argv)