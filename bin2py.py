#!/usr/bin/python

import sys, getopt, binascii

# FIXME: propper handling of arguments

def main(argv):
   inputfile = ''
   outputfile = 'out.py'
   stdout = False
   try:
      opts, args = getopt.getopt(argv,"hi:og",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> [-o <outputfile>] [-g]'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> [-o <outputfile>] [-g]'
         print ''
         print ' -i   Input binary file to convert to python code.'
         print ' -o   Output file name. Default is \'' + outputfile + '\'.'
         print ' -g   Output result to stdout only. If used in combination with'
         print '      -o flag, result is writen to both stdout and file.'
         print ' -h   Print this help message.'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt == '-g':
         stdout = True
   print 'Input file is ', inputfile
   print 'Output file is ', outputfile

   with open(inputfile, 'rb') as input_file:
      hex_data = binascii.hexlify(input_file.read())
      hex_list = map(''.join, zip(hex_data[::2], hex_data[1::2]))

   hex_list_prefixed = [r'\x' + x for x in hex_list]

   hex_list_formated = 'result = [\'' + '\',\''.join(hex_list_prefixed) + '\']'

   with open(outputfile, 'w') as output_file:
      output_file.write(hex_list_formated)

   if stdout:
      print hex_list_formated

if __name__ == "__main__":
   main(sys.argv[1:])
