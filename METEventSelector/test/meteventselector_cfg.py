import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.default.limit = 10
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2010B/Mu/AOD/Nov4ReReco_v1/0001/2424BB7E-93EA-DF11-9039-90E6BA0D09B6.root'
    )
)

process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
)


process.noscraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')

process.eventSelector = cms.EDAnalyzer('METEventSelector',
    METThreshold = cms.double(100.)
)

process.p = cms.Path( process.primaryVertexFilter*process.noscraping*process.HBHENoiseFilter*process.eventSelector )
