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
  
  //// Read Data File
  TChain* chain_data = new TChain("dspkstree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      

  double thetaks;
  double coskspiz;

  chain_data->SetBranchAddress("thetaks",&thetaks);
  chain_data->SetBranchAddress("coskspiz",&coskspiz);  

  TCanvas *c1 = new TCanvas("c1","",1000,800);

  TH2F *h2f = new TH2F("h2f","h2f",100,-1,1,100,0,3.1415);

  // Import the data points
  
  for(int i=0; i<chain_data->GetEntries(); i++)
    {
      
      chain_data->GetEntry(i);
      
      h2f->Fill(coskspiz,thetaks);
    }
    
  // variables and parameters                                                           
  
   
  gStyle->SetOptTitle(0);
  c1->cd(); h2f->Draw("COLZ");
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetLeftMargin(0.1233333);
  c1->SetRightMargin(0.01333333);
  c1->SetTopMargin(0.01851852);
  c1->SetBottomMargin(0.1375);
  c1->SetFrameBorderMode(0);
  c1->SetFrameBorderMode(0);

  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetaks.pdf","pdf");
  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetaks.eps","eps");

}
