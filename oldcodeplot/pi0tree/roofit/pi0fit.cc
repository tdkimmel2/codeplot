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
void pi0fit()

{
 
  // Fit observables  
  RooRealVar pi0mass("pi0mass", "pi0mass", 0.1183, 0.1497);
  //RooRealVar whoru("whoru", "whoru", 1, 2);

  //RooDataSet* data = new RooDataSet("data", "raw data", RooArgSet(d0mass, whoru));
  RooDataSet* data =  new RooDataSet("data", "raw data", RooArgSet(pi0mass));

  // fit variables

  //Float_t x_d0mass, x_whoru;
  Double_t x_pi0mass;
    
  //// Read Data File
  TChain* chain_data = new TChain("pi0tree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      
  
  // Number of entries/events in the datafile
  Int_t nevt = (int)chain_data->GetEntries();
  Int_t n_kept(0);
  
  chain_data->SetBranchAddress("pi0mass", &x_pi0mass);
  //chain_data->SetBranchAddress("whoru", &x_whoru);

  // Import the data points
  
  for(int i=0; i < nevt; i++)
    {
      
      chain_data->GetEntry(i);
      
      // fit region event selection

      if(x_pi0mass < 0.1183 || x_pi0mass > 0.1497) continue;                                            
      //if(x_whoru == 1) continue;
                                                          
      pi0mass.setVal(x_pi0mass);
      //whoru.setVal(x_whoru);
   
      //data->add(RooArgSet(d0mass, whoru));                                                    
      data->add(RooArgSet(pi0mass));

      n_kept++;
    }
    
  // variables and parameters                                                           
  
  // Gaussian Function
  
  RooRealVar sigmean1("<>1_{signal}", "<>_{signal}", 0.135, 0.130, 0.140);
  //RooRealVar sigmean2("<>2_{signal}", "<>_{signal2}", 0.130, 0.135);
  RooRealVar sigwidth1("#sigma_{signal1}", "#sigma_{signal}", 0.0178, 0.0, 0.09);
  //RooRealVar sigwidth2("#sigma_{signal2}", "sigma_{signal2}",0.024,0,0.1);  
  RooRealVar c0("Cheby.Poly c_{0}", "Cheby. Poly c_{0}", 0.174, -0.5, 0.5);
  RooRealVar c1("Cheby.Poly c_{1}", "Cheby. Poly c_{1}", -0.15817, -0.5, 0.5);
  //RooRealVar c2("Cheby.Poly c_{2}", "Cheby.Poly c_{2}", -20.0, 20.0);
  //RooRealVar argpar("argpar", "argus shape parameter", -100, 0) ; 
  //RooRealVar cutoff("cutoff", "argus cutoff", 0.3, 0, 100);

  //RooArgusBG argus("argus", "Argus PDF", d0mass, cutoff, argpar) ; 
  RooGaussian gauss1("gauss1", "gaussian PDF", pi0mass, sigmean1, sigwidth1);
  //RooGaussian gauss2("gauss2", "gaussian PDF", d0mass, sigmean1, sigwidth2);
  RooChebychev poly("poly", "poly", pi0mass, RooArgList(c0,c1));
 
  //RooRealVar frac1("frac1", "frac1", 0.0, 1.0);
  RooRealVar frac("frac", "frac",0.0, 1.0);
  //RooAddPdf gauss("gauss", "gauss", RooArgList(gauss1,gauss2), RooArgList(frac1));
  RooAddPdf pdf("pdf", "pdf", RooArgList(gauss1, poly), RooArgList(frac));
   
  RooFitResult* fitRes = pdf.fitTo(*data);
   
  RooPlot* yframe = pi0mass.frame(45); 
  data->plotOn(yframe);
  pdf.plotOn(yframe);
  pdf.plotOn(yframe, Components(gauss1), FillColor(kCyan), DrawOption("F"));
  //pdf.plotOn(yframe, Components(gauss2), FillColor(kGreen), DrawOption("F"));
  pdf.plotOn(yframe, Components(poly), LineColor(kRed), LineWidth(3), LineStyle(4));                      
  pdf.paramOn(yframe, Layout(0.12, 0.54, 0.9)); //Plots the pdf parameters on yframe with Layout(xmin, xmax, ymin) ymax is at the end of the last parameter line
  TCanvas *c = new TCanvas("c", "c",404,207,1004,662);
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
  yframe->GetXaxis()->SetTitle("#pi^{0} Mass (GeV/c^{2})");
  yframe->GetXaxis()->CenterTitle(true);
  yframe->GetXaxis()->SetLabelOffset(0.006);
  yframe->GetXaxis()->SetTitleOffset(1.12);
  yframe->GetYaxis()->CenterTitle(true);
  yframe->GetYaxis()->SetTitleOffset(1.45);

  yframe->Draw();
 
  c->Print("/home/taylor/Research/plots/pi0tree/roofit/pi0fit.pdf","pdf");
  c->Print("/home/taylor/Research/plots/pi0tree/roofit/pi0fit.eps","eps");
  c->Print("/home/taylor/Research/plots/pi0tree/roofit/pi0fit.png","png");

}
