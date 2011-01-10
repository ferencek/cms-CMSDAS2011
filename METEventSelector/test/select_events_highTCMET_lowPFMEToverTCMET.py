#!/usr/bin/env python

import os, sys, string, re

help = """

How to use:

./select_events_highTCMET_lowPFMEToverTCMET.py input_file output_file MET_threshold MET_ratio_threshold

Example: ./select_events_highTCMET_lowPFMEToverTCMET.py MuonDataSets_event_printout.txt TCMET_gt_400GeV_PFMEToverTCMET_lt_0.02.txt 400 0.02

"""

if len(sys.argv)<5:
  print help
  sys.exit(0)

outputFile_name = sys.argv[2]
outputFile_evtPick_name = sys.argv[2].replace('.txt','')+'.list'

outputFile = open(outputFile_name,'w')
outputFile_evtPick = open(outputFile_evtPick_name,'w')
threshold = float(sys.argv[3])
r_threshold = float(sys.argv[4])

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
  if( tcMET<=threshold ):
    continue
  input_evt_count = input_evt_count+1
  if( (pfMET/tcMET)>=r_threshold ):
    continue
  outputFile.write(i)
  outputFile_evtPick.write("%i:%i:%i\n"%(run,lumi,event))
  #print i
  output_evt_count = output_evt_count+1

outputFile.close()
outputFile_evtPick.close()

print 'Total number of events with TCMET>%.0f GeV: %i'%(threshold,input_evt_count)
print 'Total number of events with TCMET>%.0f GeV and PFMET/TCMET<%.4f: %i'%(threshold,r_threshold,output_evt_count)
print "Selected events saved to '%s' and '%s'"%(outputFile_name,outputFile_evtPick_name)
