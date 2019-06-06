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
void d0ksPlot()

{
  
  //Read Data File
  TChain* chain_data = new TChain("dspkstree");                                         
  chain_data->Add("/home/taylor/Research/root/dsprecon.root");                                                      
  //Define variables
  double d0mass;
  int whomi;

  //Define data for calculating bins
  RooRealVar rood0mass("d0mass","d0mass",1.66,2.06);

  //Set which branches to use
  chain_data->SetBranchAddress("d0mass",&d0mass);
  chain_data->SetBranchAddress("whomi",&whomi);

  //Calculate bin widths based on data, lb is left bin and rb is right bin
  int nBins = 100;
  double lb = rood0mass.getMin(); double rb = rood0mass.getMax();
  double binWidth=(rb-lb)/nBins*1000;

  //Create canvas
  TCanvas *c1 = new TCanvas("c1","",800,600);
  gPad->SetLeftMargin(0.15); gPad->SetBottomMargin(0.15);

  //Create histogram(s)
  TH1F *h1f = new TH1F("h1f","h1f",nBins,lb,rb);
  h1f->SetLineColor(kBlack);
  h1f->SetLineWidth(2);

  TH1F *h1f2 = new TH1F("h1f2","h1f2",nBins,lb,rb);
  TH1F *h1f3 = new TH1F("h1f3","h1f3",nBins,lb,rb);
 
  //Fill data points
  for(int i=0; i<chain_data->GetEntries(); i++)
    {
      //Get entries
      chain_data->GetEntry(i);
      //Window of acceptance
      if(d0mass<1.66 || d0mass>2.06)continue;
      h1f->Fill(d0mass);

      //Truth matching, h1f1 is true and h1f2 is not true
      if(whomi==2){
	h1f2->Fill(d0mass);}
      else{
	h1f3->Fill(d0mass);}
    }
    
   
  //Formating and Drawing the Plot
  gStyle->SetOptTitle(0);
  c1->cd();
  h1f->Draw();
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetLeftMargin(0.1333333);
  c1->SetRightMargin(0.02333333);
  c1->SetTopMargin(0.03851852);
  c1->SetBottomMargin(0.2375);
  c1->SetFrameBorderMode(0);
  c1->SetFrameBorderMode(0);
 
  //Format the frame Here (Main things are the title of the x & y axis.)
  h1f->SetStats(0);
  h1f->SetLineStyle(1);
 
  h1f->SetTitle("M_{D} from MC Data");
  h1f->GetXaxis()->CenterTitle(true);
  h1f->GetXaxis()->SetLabelOffset(0.01);
  h1f->GetXaxis()->SetLabelSize(0.05);
  h1f->GetXaxis()->SetTitle("M_{D^{0}} (GeV/c^{2})");
  h1f->GetXaxis()->SetTitleSize(0.05);
  h1f->GetXaxis()->SetTitleOffset(1.12);
  h1f->GetYaxis()->CenterTitle(true);
  h1f->GetYaxis()->SetTitleOffset(1.4);
  h1f->GetYaxis()->SetLabelSize(0.05);
  h1f->GetYaxis()->SetTitleSize(0.05);
  h1f->GetYaxis()->SetTitle(Form("Events/[%.3f MeV]",binWidth));
  //frame1->GetYaxis()->SetTitle(Form("Events/[%d Bins]",nBins)); // If you are not plotting agianst an energy, uncomment this -> Will display Events/[nBins]
  c1->Modified();
  //----------------------------------------------------------
  // Making the Legend
  //----------------------------------------------------------
  TLegend *leg1 = new TLegend(0.65,0.65, 0.87,0.85);
  leg1->SetFillColor(kWhite);
  leg1->SetLineColor(kWhite);
  leg1->SetTextSize(0.035);
  //leg1->AddEntry(frame1->findObject("hd"),"Total","l");
  //leg1->AddEntry(frame1->findObject("hd"),"Total","f");
  //leg1->AddEntry(frame1->findObject("hd2"),"Signal","f");
  //leg1->AddEntry(frame1->findObject("hd3"),"Background","f"); 
  // If you don't want filled histograms comment out the above 2 lines and uncomment the following 2 lines.
  //leg1->AddEntry(frame1->findObject("hd3"),"Background","l");
  //leg1->AddEntry(frame1->findObject("hd2"),"Background","l");
  //frame1->addObject(leg1);
  //frame1->Draw();

  //c1->Print("/home/taylor/Research/plots/dspkstree/d0ks.pdf","pdf");
  //c1->Print("/home/taylor/Research/plots/dspkstree/d0ks.eps","eps");

}
