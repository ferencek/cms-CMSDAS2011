import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
# Bring log reporting to a nice level
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Summary report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# Input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
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
    )
)

# Output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('METExamplesRECOAOD_output.root')
)

# Load METExamples module
process.load('CMSDAS2011.METExamples.metexamples_cfi')

# Path definition
process.p = cms.Path(process.metExamplesRECOAOD)

# Schedule definition
process.schedule = cms.Schedule(process.p)
