from ROOT import *
from ROOT import gInterpreter, gSystem
import math, os

#gInterpreter.ProcessLine('#include "RooCruijff.h"')
gInterpreter.ProcessLine('.L RooCruijff.cxx++')
gInterpreter.ProcessLine('.L RooVoigtian.cxx++')
#gSystem.Load('RooCruijff.cxx++')


f1 = "/home/taylor/Research/root/mfrecon.root"
tree = "dsptree"
f = TFile(f1,"READ")
t = f.Get(tree)

deltam = RooRealVar("deltam", "deltam", 0.1415, 0.15)

lb = deltam.getMin()
rb = deltam.getMax()
nBins=42
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(deltam)

data = RooDataSet("data", "raw data", t, vars)

#Function Variables

#Cruijff
crumu = RooRealVar("#mu","Mean of Cruijff",0.145,0,0.2)
crusigmaR = RooRealVar("#sigma_{CR}","Cruijff SigmaR",0.003,0,1)
crusigmaL = RooRealVar("#sigma_{CL}","Cruijff SigmaL",0.003,0,1)
crualphaR = RooRealVar("#alpha_{R}","Cruijff AlphaR",0.1303,0,10)
crualphaL = RooRealVar("#alpha_{L}","Cruijff AlphaL",0.1306,0,10)

#Voigtian
voigmean = RooRealVar("<>_{signal}", "<>_{signal}", 0.145, 0, 0.5)
voigwidth = RooRealVar("width_{signal}", "#width_{signal}", 0.0005, 0, 0.1)
voigsigma = RooRealVar("#sigma_{signal}", "#sigma_{signal}", 0.0005, 0, 0.1)

#Breit Wigner
bwmean = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0, 0.2)
bwwidth = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0005, 0, 0.1)

#Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0,0.2)
gaussigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0005,0,0.1)
gaussigma2 = RooRealVar("#sigma2_{sig}","#sigma2_{sig}",0.0000005,1)

#DstD0BG
dm0 = RooRealVar("dm0", "dm0", 0.137, 0.135, 0.140);
d = RooRealVar("d", "d", 0.006, 0, 10);
a = RooRealVar("a", "a", 0.42, 0, 10);
b = RooRealVar("b", "b", 2.35, 0, 10);

#Chebyshev
c0 = RooRealVar("Cheby.Poly c_{0}", "Cheby. Poly c_{0}", -0.04246, -1, 1); 
c1 =  RooRealVar("Cheby.Poly c_{1}", "Cheby. Poly c_{1}", 0.0424, -0.3, 0.3);

nsig = RooRealVar("N_{Signal}","nsig",0,100000)
nsig2 = RooRealVar("N2_{Signal}","nsig2",0,100000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,100000)

#bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,dm0,d,a,b)
bkg = RooChebychev("bkg","Chebychev Bkg Fcn",deltam,RooArgList(c0,c1))
sig = RooCruijff("sig","Cruijff Signal Fcn",deltam,crumu,crusigmaL,crusigmaR,crualphaL,crualphaR) #Use for signal Cruijff
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal
#sig2 = RooGaussian("sig2","Gaussian Signal Fcn", deltam,gausmean,gaussigma2)
#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);
SIG = RooArgSet(sig)
#SIG2 = RooArgSet(sig2)
BKG = RooArgSet(bkg)
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
pdf = RooAddPdf("pdf","sig",RooArgList(sig),RooArgList(nsig))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));


# Create a new canvas
canvas = TCanvas("canvas", "canvas", 800, 800)
histPad = TPad("histPad", "Histogram Pad", 0.0, .35, 1.0, 1.0)
residPad = TPad("residPad", "Residual Pad",0.0, 0.0, 1.0, .35)
histPad.SetLeftMargin(0.15) 
histPad.SetTopMargin(0.1)
histPad.SetBottomMargin(0.02)
histPad.SetGrid()
residPad.SetLeftMargin(0.15)
residPad.SetTopMargin(0.04)
residPad.SetBottomMargin(0.35)
residPad.SetGrid()
histPad.Draw()
residPad.Draw()
histPad.cd()  

fitRes.Print()
# Sanity Check
h1 = TH1F("h1","h1",nBins,lb,rb)

frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From MC")) 
pullFrame = deltam.frame(RooFit.Bins(nBins),RooFit.Title(""))
# Beautification Things
frame1.SetStats(0)
frame1.SetLineStyle(1)
frame1.GetXaxis().CenterTitle(kTRUE)
frame1.GetXaxis().SetLabelOffset(0.1)
frame1.GetXaxis().SetLabelSize(0.05)
frame1.GetXaxis().SetTitle("")
#frame1.GetXaxis().SetTitleSize(0.05)
#frame1.GetXaxis().SetTitleOffset(1.12)
frame1.GetYaxis().CenterTitle(kTRUE)
frame1.GetYaxis().SetTitleOffset(1.4)
frame1.GetYaxis().SetLabelSize(0.05)
frame1.GetYaxis().SetTitleSize(0.05)
frame1.GetYaxis().SetTitle("Events/[%.3f MeV]"%binWidthMEV)

data.plotOn(frame1)
#dchib1Sig_1k.plotOn(frame1)
#pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(bkg),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
#pdf.paramOn(frame1,Parameters(RooArgList(mu,sigmaL,sigmaR,alphaL,alphaR,nsig)),Format("NEU", AutoPrecision(2)), Layout(0.55, 0.89, 0.89))
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.93))
frame1.Draw()

hpull1 = frame1.pullHist()
pullFrame.addPlotable(hpull1,"P")
line1 = TLine(lb, 0, rb, 0)
line1.SetLineWidth(3)
line1.SetLineColor(kRed)
line1.SetLineStyle(7)


residPad.cd()
residPad.SetTickx()
residPad.SetTicky()
pullFrame.SetTitle("")
#pullFrame.GetXaxis().SetRangeUser(lb, ub)
pullFrame.GetXaxis().CenterTitle(kTRUE)
pullFrame.GetXaxis().SetLabelOffset(0.03)
pullFrame.GetXaxis().SetLabelSize(0.09)
pullFrame.GetXaxis().SetTitle("#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})")
pullFrame.GetXaxis().SetTitleOffset(1.1)
pullFrame.GetXaxis().SetTitleSize(0.12)
  
pullFrame.SetMaximum(5)
pullFrame.SetMinimum(-5)
pullFrame.GetYaxis().SetTitle("Pull")
pullFrame.GetYaxis().CenterTitle(kTRUE)
pullFrame.GetYaxis().SetTitleOffset(0.3)
pullFrame.GetYaxis().SetLabelSize(0.09);
pullFrame.GetYaxis().SetTitleSize(0.12)
pullFrame.Draw()
line1.Draw("same")

chisq = frame1.chiSquare()
chiSQ = "#chi^{2} = %.3f"%chisq
tex1 = TLatex(0.8,0.1,chiSQ)
tex1.SetTextSize(0.1)
tex1.SetNDC() 
tex1.Draw()
#expectedYield = "N_{Expected} = %.0f"%nSignal
#tex2 = TLatex(0.1,0.1,expectedYield)
#tex2.SetTextSize(0.1)
#tex2.SetNDC() 
#tex2.Draw()


canvas.Print("/home/taylor/Research/plots/dtokpi/chrgddeltam_cruijff+nobkg_fit.pdf")
canvas.Print("/home/taylor/Research/plots/dtokpi/chrgddeltam_cruijff+nobkg_fit.eps")
canvas.Print("/home/taylor/Research/plots/dtokpi/chrgddeltam_cruijff+nobkg_fit.png")

