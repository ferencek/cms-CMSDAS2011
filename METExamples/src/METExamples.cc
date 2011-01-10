// -*- C++ -*-
//
// Package:    METExamples
// Class:      METExamples
//
/**\class METExamples METExamples.cc CMSDAS2011/METExamples/src/METExamples.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  "Dinko Ferencek"
//         Created:  Tue Jan  4 14:32:10 CST 2011
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//TFile Service
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
// GenMET
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETFwd.h"
// CaloMET
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETFwd.h"
// TCMET
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
// PFMET
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
// pat::MET
#include "DataFormats/PatCandidates/interface/MET.h"
// ROOT
#include <TH1D.h>


//
// class declaration
//

class METExamples : public edm::EDAnalyzer {
   public:
      explicit METExamples(const edm::ParameterSet&);
      ~METExamples();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      // ----------member data ---------------------------
      edm::InputTag genMETTag;       // input tag for generator-level MET
      edm::InputTag caloMETTag;      // input tag for raw calorimeter MET
      edm::InputTag tcMETTag;        // input tag for track-corrected MET
      edm::InputTag pfMETTag;        // input tag for particle flow MET
      edm::InputTag caloMETPATTag;   // input tag for PAT calorimeter MET
      edm::InputTag tcMETPATTag;     // input tag for PAT track-corrected MET
      edm::InputTag pfMETPATTag;     // input tag for PAT particle flow MET

      edm::Service<TFileService> fs;

      TH1D *h_GenMET;
      TH1D *h_CaloMET;
      TH1D *h_TCMET;
      TH1D *h_PFMET;

      bool accessPATMET;
      TH1D *h_GenMET_PAT;
      TH1D *h_CaloMET_PAT;
      TH1D *h_CaloMETuncorr_PAT;
      TH1D *h_TCMET_PAT;
      TH1D *h_PFMET_PAT;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
METExamples::METExamples(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   genMETTag     = iConfig.getParameter<edm::InputTag>("GenMETTag" );
   caloMETTag    = iConfig.getParameter<edm::InputTag>("CaloMETTag");
   tcMETTag      = iConfig.getParameter<edm::InputTag>("TCMETTag"  );
   pfMETTag      = iConfig.getParameter<edm::InputTag>("PFMETTag"  );
   accessPATMET  = iConfig.getParameter<bool>("AccessPATMET"  );
   caloMETPATTag = iConfig.getParameter<edm::InputTag>("CaloMETPATTag");
   tcMETPATTag   = iConfig.getParameter<edm::InputTag>("TCMETPATTag"  );
   pfMETPATTag   = iConfig.getParameter<edm::InputTag>("PFMETPATTag"  );
}


METExamples::~METExamples()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called once each job just before starting event loop  ------------
void
METExamples::beginJob()
{
   // book all histograms
   h_GenMET  = fs->make<TH1D>("h_GenMET",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
   h_CaloMET = fs->make<TH1D>("h_CaloMET",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
   h_TCMET   = fs->make<TH1D>("h_TCMET",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
   h_PFMET   = fs->make<TH1D>("h_PFMET",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
   if(accessPATMET) {
     h_GenMET_PAT        = fs->make<TH1D>("h_GenMET_PAT",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
     h_CaloMET_PAT       = fs->make<TH1D>("h_CaloMET_PAT",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
     h_CaloMETuncorr_PAT = fs->make<TH1D>("h_CaloMETuncorr_PAT",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
     h_TCMET_PAT         = fs->make<TH1D>("h_TCMET_PAT",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
     h_PFMET_PAT         = fs->make<TH1D>("h_PFMET_PAT",";#slash{E}_{T} [GeV];Events/(2 GeV)",100,0,200);
   }
}

// ------------ method called to for each event  ------------
void
METExamples::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   edm::Handle<reco::GenMETCollection> genmet;
   if(iEvent.getByLabel(genMETTag, genmet)) h_GenMET->Fill(genmet->front().pt());

   edm::Handle<reco::CaloMETCollection> calomet;
   if(iEvent.getByLabel(caloMETTag, calomet)) h_CaloMET->Fill(calomet->front().pt());

   edm::Handle<reco::METCollection> tcmet;
   if(iEvent.getByLabel(tcMETTag, tcmet)) h_TCMET->Fill(tcmet->front().pt());

   edm::Handle<reco::PFMETCollection> pfmet;
   if(iEvent.getByLabel(pfMETTag, pfmet)) h_PFMET->Fill(pfmet->front().pt());

   if(accessPATMET) {
     edm::Handle<pat::METCollection> calometPAT;
     if(iEvent.getByLabel(caloMETPATTag, calometPAT)) {
       h_CaloMET_PAT->Fill(calometPAT->front().pt());
       h_CaloMETuncorr_PAT->Fill(calometPAT->front().uncorrectedPt(pat::MET::uncorrALL));
       h_GenMET_PAT->Fill(calometPAT->front().genMET()->pt());
     }

     edm::Handle<pat::METCollection> tcmetPAT;
     if(iEvent.getByLabel(tcMETPATTag, tcmetPAT)) h_TCMET_PAT->Fill(tcmetPAT->front().pt());

     edm::Handle<pat::METCollection> pfmetPAT;
     if(iEvent.getByLabel(pfMETPATTag, pfmetPAT)) h_PFMET_PAT->Fill(pfmetPAT->front().pt());
   }
}

// ------------ method called once each job just after ending the event loop  ------------
void
METExamples::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(METExamples);
