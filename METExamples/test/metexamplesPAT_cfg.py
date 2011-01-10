## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# Bring log reporting to a nice level
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## ------------------------------------------------------
#  NOTE: you can use a bunch of core tools of PAT to
#  taylor your PAT configuration; for a few examples
#  uncomment the lines below
## ------------------------------------------------------
from PhysicsTools.PatAlgos.tools.coreTools import *

## remove certain objects from the default sequence
removeAllPATObjectsBut(process, ['METs'])

## ------------------------------------------------------
#  NOTE: to run PAT on CMSSW_3_8_X AOD please switch the
#  use and embedding of bTagInfos for patJets off. These
#  are not part of the AOD anymore. The bTagDosciminators
#  supported by the BTag POG are still available and will
#  be embedded.
## ------------------------------------------------------
#process.patJets.addBTagInfo = False
#process.patJets.tagInfoSources = []

# Add tcMET and pfMET
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')

# Output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('METExamplesPAT_output.root')
)

# Load METExamples module
process.load('CMSDAS2011.METExamples.metexamples_cfi')
process.metExamplesPAT = process.metExamplesRECOAOD.clone()
process.metExamplesPAT.AccessPATMET = True

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
process.GlobalTag.globaltag = 'START38_V14::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
process.source.fileNames = [
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0017/885CA661-99FC-DF11-8488-0018F3D096F8.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0017/766E3B50-9DFC-DF11-9185-001A928116EC.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/DA354D81-93FC-DF11-9255-001A92971ADC.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/D6273077-90FC-DF11-B982-00304867BFC6.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/C6A23B03-8EFC-DF11-9061-001A928116D2.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/AC55627F-8EFC-DF11-AC58-001A92971B3C.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/96A14300-8DFC-DF11-BFB0-00304867918A.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/4AAB90FF-8CFC-DF11-B76A-003048679228.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/2888E972-92FC-DF11-89FB-0018F3D096BE.root',
    '/store/relval/CMSSW_3_8_7/RelValTTbar/GEN-SIM-RECO/START38_V13-v1/0016/1038F173-92FC-DF11-BB88-0018F3D09682.root'
]
process.maxEvents.input = -1

# Summary report
process.options.wantSummary = True

# Path definition
process.p = cms.Path(process.patDefaultSequence*process.metExamplesPAT)

# Delete predefined Endpath (needed for running with CRAB)
del process.out
del process.outpath

# Schedule definition
process.schedule = cms.Schedule(process.p)
