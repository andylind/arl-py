#! /usr/bin/python
#
# 
# This file is a part of the arl-py software package, and is 
# licensed under the New BSD License.
# A `LICENSE' file should have been included with this source.
#
# Copyright (c) 2010 Andy Lind

import yapgvb
import csv, sys

# This class allows a 2 column csv edge list to be visualized in an image file
class graphBuilder:
    def __init__(self, inputFilename):
        self.inputFilename = inputFilename
        self.graphData = yapgvb.Digraph()
        # Read in the csv file data
        self.edgeReader = csv.reader(open(self.inputFilename), delimiter=',')
        # Read each row of the csv data into the graph
        for field1, field2 in self.edgeReader:
            self.node1 = self.graphData.add_node(
                field1, 
                label=field1)
            self.node2 = self.graphData.add_node(
                field2, 
                label=field2)
            self.graphData.add_edge(self.node1, self.node2)               
    def createPngImage(self, outputFilename):
        self.outputFilename = outputFilename
        self.graphData.layout(yapgvb.engines.dot)
        self.graphData.render(outputFilename) 


# Runs program and handles command line arguments
# argv[0] is the csv imput file, argv[1] is the png output file   
def main(argv):
    # Create new graph and output an image of the graph
    myGraph = graphBuilder(argv[0])
    myGraph.createPngImage(argv[1])
         
if __name__ == '__main__':
    main(sys.argv[1:])
