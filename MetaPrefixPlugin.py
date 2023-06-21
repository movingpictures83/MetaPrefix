import sys

import PyPluMA
import PyIO

class MetaPrefixPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
        self.infile = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"])
        self.prefixfile = open(PyPluMA.prefix()+"/"+self.parameters["prefixfile"])

    def run(self):
        self.prefixes = dict()
        for line in self.prefixfile:
            mydata = line.strip().split('\t')
            self.prefixes[mydata[0]] = mydata[1]

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        self.infile.readline()
        outfile.write("\"Sample\",\"Group\"\n")
        for line in self.infile:
            contents = line.strip().split(',')
            sample = contents[0]
            outfile.write(sample+",")
            for key in self.prefixes:
               if (sample.startswith('\"'+key)):
                 outfile.write("\""+self.prefixes[key]+"\"\n")
