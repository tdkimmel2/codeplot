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
  RooRealVar deltam2("thetaks", "thetaks", 0, 2*3.1415);
  RooRealVar d0mass("coskspiz", "coskspiz", -1, 1);
  //RooRealVar whoru("whoru", "whoru", 1, 2);

  //RooDataSet* data = new RooDataSet("data", "raw data", RooArgSet(d0mass, whoru));
  RooDataSet* data =  new RooDataSet("data", "raw data", RooArgSet(thetaks, coskspiz));

  // fit variables

  //Float_t x_d0mass, x_whoru;
  Double_t x_thetaks, x_coskspiz;
    
  //// Read Data File
  TChain* chain_data = new TChain("dspkstree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      
  
  // Number of entries/events in the datafile
  Int_t nevt = (int)chain_data->GetEntries();
  Int_t n_kept(0);
  
  chain_data->SetBranchAddress("thetaks", &x_thetaks);
  chain_data->SetBranchAddress("coskspiz", &x_coskspiz);

  TCanvas *c1 = new TCanvas("c1","",1000,800);

  TH2F *h2f = new TH2F("h2f","h2f",

  // Import the data points
  
  for(int i=0; i < nevt; i++)
    {
      
      chain_data->GetEntry(i);
      
      thetaks.setVal(x_thetaks);
      coskspiz.setVat(x_coskspiz);
      //whoru.setVal(x_whoru);
   
      //data->add(RooArgSet(d0mass, whoru));                                                    
      data->add(RooArgSet(thetaks));
      data->add(RooArgSet(coskspiz));

      n_kept++;
    }
    
  // variables and parameters                                                           
  
   
  RooPlot* yframe = deltam2.frame(45); 
  data->plotOn(yframe);
  pdf.plotOn(yframe);
  pdf.plotOn(yframe, Components(gauss), FillColor(kCyan), DrawOption("F"));
  //pdf.plotOn(yframe, Components(gauss2), FillColor(kGreen), DrawOption("F"));
  pdf.plotOn(yframe, Components(poly), LineColor(kRed), LineWidth(3), LineStyle(4));                      
  pdf.paramOn(yframe, Layout(0.5, 0.93, 0.95)); //Plots the pdf parameters on yframe with Layout(xmin, xmax, ymin) ymax is at the end of the last parameter line
  //TCanvas *c = new TCanvas("c", "c",404,207,1004,662);
  gStyle->SetOptTitle(0);
  c->Range(-0.539869,-55.42274,5.097836,103.4985);
  c->SetFillColor(0);
  c->SetBorderMode(0);
  c->SetBorderSize(2);
  c->SetLeftMargin(0.1233333);
  c->SetRightMargin(0.01333333);
  c->SetTopMargin(0.01851852);
  c->SetBottomMargin(0.1375);
  c->SetFrameBorderMode(0);
  c->SetFrameBorderMode(0);

  yframe->SetStats(0);
  yframe->GetXaxis()->SetTitle("#DeltaM^{2} From MC Data");
  yframe->GetXaxis()->CenterTitle(true);
  yframe->GetXaxis()->SetLabelOffset(0.006);
  yframe->GetXaxis()->SetTitleOffset(1.12);
  yframe->GetYaxis()->CenterTitle(true);
  yframe->GetYaxis()->SetTitleOffset(1.45);

  yframe->Draw();
 
  c->Print("/home/taylor/Research/plots/dspkstree/roofit/coskspizvsthetaks.pdf","pdf");
  c->Print("/home/taylor/Research/plots/dspkstree/roofit/coskspizvsthetaks.eps","eps");

}
