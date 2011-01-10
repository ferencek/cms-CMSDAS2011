import FWCore.ParameterSet.Config as cms

eventSelector = cms.EDAnalyzer('METEventSelector',
    METThreshold = cms.double(100.)
)
