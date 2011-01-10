#!/usr/bin/env python

import os, sys, string, re

##################################################################################################################################
#### User Section

log_file_locations = [
  'crab_Mu_Run2010A/res/',
  'crab_Mu_Run2010B/res/'
]

output_filename = 'MuonDataSets_event_printout.txt'

#### End of User Section
##################################################################################################################################


runs = {}

evt_count = 0

for directory in log_file_locations:
  filenamelist = []
  for filename in os.listdir(directory):
    if(not os.path.isfile(os.path.join(directory,filename)) or not re.search('.stdout$',filename)):
      continue
    #print filename
    log_file = open(os.path.join(directory,filename))
    log_lines = log_file.readlines()
    for line in log_lines:
      if(not re.search('^USER: ',line)):
        continue
      stripped_line = line.replace('USER: ','')
      run = int(stripped_line.split()[0])
      event = int(stripped_line.split()[2])
      m = re.search(' -- \w+$', stripped_line)
      evt_count = evt_count + 1
      if run not in runs.keys():
        runs[run] = {}
        runs[run][event] = stripped_line[:m.start()]
      else:
        runs[run][event] = stripped_line[:m.start()]

print "%i events printed out"%(evt_count)

outputFile = open(output_filename,'w')

run_keys = runs.keys()
run_keys.sort()

print "Ordering events..."

for run in run_keys:
  event_keys = runs[run].keys()
  event_keys.sort()
  for event in event_keys:
    #print runs[run][event]
    outputFile.write(runs[run][event]+'\n')

outputFile.close()

print "Ordered list of events saved to '%s'"%(output_filename)
