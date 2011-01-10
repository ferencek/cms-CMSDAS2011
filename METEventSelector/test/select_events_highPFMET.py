#!/usr/bin/env python

import os, sys, string, re

help = """

How to use:

./select_events_highPFMET.py input_file output_file MET_threshold

Example: ./select_events_highPFMET.py MuonDataSets_event_printout.txt PFMET_gt_2000GeV.txt 2000

"""

if len(sys.argv)<4:
  print help
  sys.exit(0)

outputFile_name = sys.argv[2]
outputFile_evtPick_name = sys.argv[2].replace('.txt','')+'.list'

outputFile = open(outputFile_name,'w')
outputFile_evtPick = open(outputFile_evtPick_name,'w')
threshold = float(sys.argv[3])

file = open(sys.argv[1])

list = file.readlines()

input_evt_count = 0
output_evt_count = 0

for i in list:
  line = i.strip().split()
  run = int(line[0])
  lumi = int(line[1])
  event = int(line[2])
  caloMET = float(line[3])
  tcMET = float(line[4])
  pfMET = float(line[5])
  if( pfMET>100 ):
    input_evt_count = input_evt_count+1
  if( pfMET>threshold ):
    outputFile.write(i)
    outputFile_evtPick.write("%i:%i:%i\n"%(run,lumi,event))
    #print i
    output_evt_count = output_evt_count+1

outputFile.close()
outputFile_evtPick.close()

print "Total number of events with PFMET>100 GeV: %i"%(input_evt_count)
print "Total number of events with PFMET>%.0f GeV: %i"%(threshold,output_evt_count)
print "Selected events saved to '%s' and '%s'"%(outputFile_name,outputFile_evtPick_name)
