import FWCore.ParameterSet.Config as cms

metExamplesRECOAOD = cms.EDAnalyzer('METExamples',
    GenMETTag     = cms.InputTag("genMetTrue"),
    CaloMETTag    = cms.InputTag("met"),
    TCMETTag      = cms.InputTag("tcMet"),
    PFMETTag      = cms.InputTag("pfMet"),
    AccessPATMET  = cms.bool(False),
    CaloMETPATTag = cms.InputTag("patMETs"),
    TCMETPATTag   = cms.InputTag("patMETsTC"),
    PFMETPATTag   = cms.InputTag("patMETsPF")
)
