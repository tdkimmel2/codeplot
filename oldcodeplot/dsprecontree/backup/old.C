#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooConstVar.h"
#include "RooChebychev.h"
#include "RooAddPdf.h"
#include "RooMCStudy.h"
#include "RooPlot.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TH2.h"
#include "RooFitResult.h"
#include "TStyle.h"
#include "TDirectory.h"

using namespace RooFit;
void thetaksvscoskspizPlot()

{
 
  // Fit observables                                                                           
  RooRealVar thetaks("thetaks", "thetaks", 0, 2*3.1415);
  RooRealVar coskspiz("coskspiz", "coskspiz", -1, 1);
  //RooRealVar whoru("whoru", "whoru", 1, 2);

  //RooDataSet* data = new RooDataSet("data", "raw data", RooArgSet(d0mass, whoru));
  RooDataSet* data =  new RooDataSet("data", "raw data", RooArgSet(thetaks, coskspiz));

  // fit variables

  //Float_t x_d0mass, x_whoru;
  Double_t thetaks, coskspiz;
    
  //// Read Data File
  TChain* chain_data = new TChain("dspkstree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      
  
  // Number of entries/events in the datafile
  Int_t nevt = (int)chain_data->GetEntries();
  Int_t n_kept(0);
  
  chain_data->SetBranchAddress("thetaks", &x_thetaks);
  chain_data->SetBranchAddress("coskspiz", &x_coskspiz);

  TCanvas *c1 = new TCanvas("c1","",1000,800);

  TH2F *h2f = new TH2F("h2f","h2f",100,-1,1,100,0,2*3.1415);

  // Import the data points
  
  for(int i=0; i<dspkstree->GetEntries(); i++)
    {
      
      dspkstree->GetEntry(i);
      
      // fit region event selection

      //if(x_deltam2 < 0.5 || x_deltam2 > 0.7) continue;
      //if(x_d0mass < 1.706 || x_d0mass > 1.994) continue;	
      //if(x_whoru == 1) continue;
                                                         
      //whoru.setVal(x_whoru);
   
      //data->add(RooArgSet(d0mass, whoru));                                                    
      
      h2f->Fill(coskspiz,thetaks);
    }
    
  // variables and parameters                                                           
  
   
  gStyle->SetOptTitle(0);
  c1->cd(); h2f->Draw("COLZ");
  //c1->Range(-0.539869,-55.42274,5.097836,103.4985);
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetLeftMargin(0.1233333);
  c1->SetRightMargin(0.01333333);
  c1->SetTopMargin(0.01851852);
  c1->SetBottomMargin(0.1375);
  c1->SetFrameBorderMode(0);
  c1->SetFrameBorderMode(0);

  yframe->SetStats(0);
  yframe->GetXaxis()->SetTitle("#DeltaM^{2} From MC Data");
  yframe->GetXaxis()->CenterTitle(true);
  yframe->GetXaxis()->SetLabelOffset(0.006);
  yframe->GetXaxis()->SetTitleOffset(1.12);
  yframe->GetYaxis()->CenterTitle(true);
  yframe->GetYaxis()->SetTitleOffset(1.45);

  yframe->Draw();
 
  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetaks.pdf","pdf");
  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetaks.eps","eps");

}
