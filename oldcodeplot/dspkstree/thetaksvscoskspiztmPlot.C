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
void thetaksvscoskspiztmPlot()

{
  
  //Read Data File
  TChain* chain_data = new TChain("dspkstree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      
  //Define variables
  double thetaks;
  double coskspiz;
  int whoru;

  //Define data for calculating bins
  RooRealVar roothetaks("thetaks","thetaks",0,3.1415);
  RooRealVar roocoskspiz("coskspiz","coskspiz",-1,1);

  //Set which branches to use
  chain_data->SetBranchAddress("thetaks",&thetaks);
  chain_data->SetBranchAddress("coskspiz",&coskspiz);  
  chain_data->SetBranchAddress("whoru",&whoru);

  //Calculate bin widths based on data, lb is left bin and rb is right bin
  int nBins = 100;
  double lb = roothetaks.getMin(); double rb = roothetaks.getMax();
  double binWidth=(rb-lb)/nBins*1000;

  //Bin widths for second variable, tb is top bin and bb is bottom bin
  double bb = roocoskspiz.getMin(); double tb = roocoskspiz.getMax();
  double binWidth2=(tb-bb)/nBins*1000;

  //Create canvas
  TCanvas *c1 = new TCanvas("c1","",1000,800);
  gPad->SetLeftMargin(0.15); gPad->SetBottomMargin(0.15);

  //Create histogram(s)
  TH2F *h2f = new TH2F("h2f","h2f",nBins,lb,rb,nBins,bb,tb);

 
  //Fill data points
  for(int i=0; i<chain_data->GetEntries(); i++)
    {
      chain_data->GetEntry(i);
      if(whoru==1) continue;      

      h2f->Fill(thetaks,coskspiz);
    }
    
   
  //Formating and Drawing the Plot
  gStyle->SetOptTitle(0);
  c1->cd();
  h2f->Draw("COLZ");
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetLeftMargin(0.1233333);
  c1->SetRightMargin(0.01333333);
  c1->SetTopMargin(0.01851852);
  c1->SetBottomMargin(0.1375);
  c1->SetFrameBorderMode(0);
  c1->SetFrameBorderMode(0);
 
  //TAxis* xaxis = 0;
  //TAxis* yaxis = 0;
  //xaxis = c1->GetXaxis();
  //frame = c1.DrawFrame(0.,0.,1.,1.);
  //frame->SetXTitle("x");
  //frame->SetYTitle("y");
  //c1.Modified();

  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetakstm.pdf","pdf");
  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetakstm.eps","eps");
  c1->Print("/home/taylor/Research/plots/dspkstree/coskspizvsthetakstm.png","png");

}
