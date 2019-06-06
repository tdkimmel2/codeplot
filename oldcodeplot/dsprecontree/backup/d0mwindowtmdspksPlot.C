#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooDataHist.h"
#include "RooGaussian.h"
#include "RooVoigtian.h"
#include "RooConstVar.h"
#include "RooChebychev.h"
#include "RooCBShape.h"
#include "RooGExpModel.h"
#include "RooAddPdf.h"
#include "RooProdPdf.h"
#include "RooMCStudy.h"
#include "RooPlot.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TString.h"
#include "RooFitResult.h"
#include "TStyle.h"
#include "TDirectory.h"
#include "TROOT.h"


using namespace RooFit;
void d0mwindowtmdspksPlot()

{
  
  int nBins = 100; 
  TFile *f1=new TFile("/home/taylor/Research/root/dsprecon.root"); //put file here
  TTree *t1=(TTree*) f1->Get("dspkstree"); //put tree name here


  //----------------------------------------------------------
  // Define Fit Observables      
  //----------------------------------------------------------
 
  RooRealVar dspmass("dspmass", "dspmass",1.81,2.21);

  //----------------------------------------------------------
  // This next bit calculates the bin width based on specified number of bins and the range of the RooRealVar defined above
  //----------------------------------------------------------
  double lb = dspmass.getMin(); double rb=dspmass.getMax();
  double binWidth=(rb-lb)/nBins*1000;

  
  // Create a new canvas
  TCanvas* canvas = new TCanvas("canvas", "canvas", 800, 500);
  gPad->SetLeftMargin(0.15) ; gPad->SetBottomMargin(0.15);


  //----------------------------------------------------------
  // Create the histogram(s)
  //----------------------------------------------------------
  TH1F *hd = new TH1F("hd","hd",nBins,lb,rb);
  hd->SetLineColor(kBlack);
  //hd->SetFillColor(kBlue);
  hd->SetLineWidth(2);
  t1->Draw("dspmass>>hd","d0mass < 1.994 && d0mass > 1.706","whoru==2");
  //Example: t1->Draw("pi0mass>>hd","pPi0<3"); //This is how you add cuts to what you want to plot. 

  //Uncomment this bit if you want to plot the background (You'll need to update the proper truth variable in the draw command.)
  TH1F *hd2 = new TH1F("hd2","hd2",nBins,lb,rb);
  hd2->SetLineColor(kBlue);
  //hd2->SetFillColor(kBlue);
  hd2->SetLineWidth(2);
  t1->Draw("dspmass>>hd2","whoru==2");

  TH1F *hd3 = new TH1F("hd3","hd3",nBins,lb,rb);
  hd3->SetLineColor(kRed);
  //hd3->SetFillColor(kRed);
  hd3->SetLineWidth(2);
  t1->Draw("dspmass>>hd3","whoru==1");

  

  //----------------------------------------------------------
  // Drawing the Plot
  //----------------------------------------------------------

  RooPlot* frame1 = dspmass.frame(Bins(nBins),Title("D*^{+} Mass From MC Data")); //Edit the Title of the plot here
  frame1->addTH1(hd);
  //frame1->addTH1(hd3);
  frame1->addTH1(hd2); //If using hd2, uncomment this line.

  // Format the frame Here (Main things are the title of the x & y axis.)
  frame1->SetStats(0);
  frame1->SetLineStyle(1);

  frame1->GetXaxis()->CenterTitle(true);
  frame1->GetXaxis()->SetLabelOffset(0.01);
  frame1->GetXaxis()->SetLabelSize(0.05);
  frame1->GetXaxis()->SetTitle("M_{D*^{+}} (GeV/c^{2})");
  frame1->GetXaxis()->SetTitleSize(0.05);
  frame1->GetXaxis()->SetTitleOffset(1.12);
  frame1->GetYaxis()->CenterTitle(true);
  frame1->GetYaxis()->SetTitleOffset(1.4);
  frame1->GetYaxis()->SetLabelSize(0.05);
  frame1->GetYaxis()->SetTitleSize(0.05);
  frame1->GetYaxis()->SetTitle(Form("Events/[%.3f MeV]",binWidth));
  //frame1->GetYaxis()->SetTitle(Form("Events/[%d Bins]",nBins)); // If you are not plotting agianst an energy, uncomment this -> Will display Events/[nBins]

  //----------------------------------------------------------
  // Making the Legend
  //----------------------------------------------------------

  TLegend *leg1 = new TLegend(0.15, 0.65, 0.35, 0.85); //(x1, y1, x2, y2)
  leg1->SetFillColor(kWhite);
  leg1->SetLineColor(kWhite);
  leg1->SetTextSize(0.035);
  leg1->AddEntry(frame1->findObject("hd"),"Truth Matched After D^{0} 5#sigma Mass Window","l");
  //leg1->AddEntry(frame1->findObject("hd"),"Total","f");
  //leg1->AddEntry(frame1->findObject("hd2"),"Signal","f");
  //leg1->AddEntry(frame1->findObject("hd3"),"Background","f"); 
  // If you don't want filled histograms comment out the above 2 lines and uncomment the following 2 lines.
  //leg1->AddEntry(frame1->findObject("hd3"),"Background","l");
  leg1->AddEntry(frame1->findObject("hd2"),"Truth Matched, No Mass Cut","l");
  frame1->addObject(leg1);

  frame1->Draw(); 
  
  canvas->Print("/home/taylor/Research/plots/dspkstree/d0mwindowtruthmatcheddspks.pdf","pdf"); 
  canvas->Print("/home/taylor/Research/plots/dspkstree/d0mwindowtruthmatcheddspks.eps","eps");

 
}
