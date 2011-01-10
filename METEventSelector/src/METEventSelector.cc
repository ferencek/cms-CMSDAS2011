// -*- C++ -*-
//
// Package:    METEventSelector
// Class:      METEventSelector
//
/**\class METEventSelector METEventSelector.cc CMSDAS2011/METEventSelector/src/METEventSelector.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  "Dinko Ferencek"
//         Created:  Sun Jan  9 12:39:12 CST 2011
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

// CaloMET
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETFwd.h"
// TCMET
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
// PFMET
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"

//
// class declaration
//

class METEventSelector : public edm::EDAnalyzer {
   public:
      explicit METEventSelector(const edm::ParameterSet&);
      ~METEventSelector();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      // ----------member data ---------------------------
      double metThreshold;
      std::string metAlgo[3];
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
METEventSelector::METEventSelector(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   metThreshold   = iConfig.getParameter<double>("METThreshold");
   metAlgo[0] = "PFMET";
   metAlgo[1] = "TCMET";
   metAlgo[2] = "CaloMET";
}


METEventSelector::~METEventSelector()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
METEventSelector::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   bool pass = false;
   int index = -1;
   double met[3] = {0.};

   edm::Handle<reco::PFMETCollection> pfmet;
   iEvent.getByLabel("pfMet", pfmet);

   met[0] = pfmet->front().pt();
   if( met[0]>metThreshold && pass == false ) {
     pass = true;
     index = 0;
   }

   edm::Handle<reco::METCollection> tcmet;
   iEvent.getByLabel("tcMet", tcmet);

   met[1] = tcmet->front().pt();
   if( met[1]>metThreshold && pass == false ) {
     pass = true;
     index = 1;
   }

   edm::Handle<reco::CaloMETCollection> calomet;
   iEvent.getByLabel("met", calomet);

   met[2] = calomet->front().pt();
   if( met[2]>metThreshold && pass == false ) {
     pass = true;
     index = 2;
   }

   if(pass) {
     // USER: Run LS Event CaloMet TCMET PFMET -- METAlgo
     std::cout<<"USER: "<<iEvent.id().run()<<" "<<iEvent.luminosityBlock()<<" "<<iEvent.id().event()<<" "<<met[2]<<" "<<met[1]<<" "<<met[0]<<" -- "<<metAlgo[index]<<std::endl;
   }
}


// ------------ method called once each job just before starting event loop  ------------
void
METEventSelector::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
METEventSelector::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(METEventSelector);
