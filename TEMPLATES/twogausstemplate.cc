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
void dmmassfittrueh101()

{
 
  // Fit observables                                                                           
  RooRealVar mass("mass", "mass",1.83,1.94);
  RooRealVar whoru("whoru", "whoru",1,2);
  RooRealVar chisqnew("chisqnew", "chisqnew",0,400);

  RooDataSet* data = new RooDataSet("data", "raw data",RooArgSet(mass,whoru,chisqnew));
  
  // fit variables

  Float_t x_mass,x_whoru,x_chisqnew;
    
  //// Read Data File
  TChain* chain_data = new TChain("h101");                                         
  chain_data->Add("test.root");                                                      
  
  // Number of entries/events in the datafile
  Int_t nevt = (int)chain_data->GetEntries();
  Int_t n_kept(0);
  
  chain_data->SetBranchAddress("mass",&x_mass);
  chain_data->SetBranchAddress("whoru",&x_whoru);
  chain_data->SetBranchAddress("chisqnew",&x_chisqnew);

  // Import the data points
  
  for(int i=0; i<nevt;i++)
    {
      
      chain_data->GetEntry(i);
      
      // fit region event selection

      if(x_mass < 1.83 || x_mass > 1.94) continue;                                            
      if(x_whoru == 1) continue;
      //if(x_chisqnew > 400) continue;
                                                          
      mass.setVal(x_mass);
      whoru.setVal(x_whoru);
      chisqnew.setVal(x_chisqnew);
   
      data->add(RooArgSet(mass,chisqnew,whoru));                                                    

      n_kept++;
    }
    
  // variables and parameters                                                           

  // For D mass
  
  // Gaussian Function
  
  RooRealVar sigmean("<>_{signal}","<>_{signal}",1.865,1.85,1.87);
  RooRealVar sigwidth1("#sigma_{signal1}","#sigma_{signal1}",0.0178,0.0,0.09);  

  // Second Gaussian
  
  RooRealVar sigwidth2("#sigma_{signal2}", "sigma_{signal2}",0.004359,0, 0.005);
   
  RooGaussian gauss1("gauss1","gaussian PDF",mass,sigmean,sigwidth1);
  RooGaussian gauss2("gauss2","gaussian PDF", mass,sigmean,sigwidth2);
 
  RooRealVar frac("frac", "frac",0.197,0.0, 1.0);
  RooAddPdf pdf("pdf", "pdf", RooArgList(gauss1,gauss2), RooArgList(frac));
   
  RooFitResult* fitRes = pdf.fitTo(*data);
   
  RooPlot* yframe = mass.frame(45); 
  data->plotOn(yframe);
  pdf.plotOn(yframe);
  pdf.plotOn(yframe, Components(gauss2), FillColor(kGreen), DrawOption("F"));
  pdf.plotOn(yframe, Components(gauss1), FillColor(kCyan), DrawOption("F"));                      
  pdf.paramOn(yframe);
  TCanvas *c = new TCanvas("c", "c",404,207,454,462);
  gStyle->SetOptTitle(0);
  c->Range(-1.039869,-85.42274,5.097836,103.4985);
  c->SetFillColor(0);
  c->SetBorderMode(0);
  c->SetBorderSize(2);
  c->SetLeftMargin(0.1733333);
  c->SetRightMargin(0.01333333);
  c->SetTopMargin(0.01851852);
  c->SetBottomMargin(0.1875);
  c->SetFrameBorderMode(0);
  c->SetFrameBorderMode(0);

  yframe->SetStats(0);
  yframe->GetXaxis()->SetTitle("D mass (GeV/c^{2})");
  yframe->GetXaxis()->CenterTitle(true);
  yframe->GetXaxis()->SetLabelOffset(0.006);
  yframe->GetXaxis()->SetTitleOffset(1.12);
  yframe->GetYaxis()->CenterTitle(true);
  yframe->GetYaxis()->SetTitleOffset(1.45);
  yframe->Draw();
 
}
