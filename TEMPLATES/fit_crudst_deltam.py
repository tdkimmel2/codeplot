from ROOT import *
from ROOT import gInterpreter, gSystem
import math, os

gInterpreter.ProcessLine('.L RooCruijff.cxx++')
gInterpreter.ProcessLine('.L RooVoigtian.cxx++')
#gSystem.Load('RooCruijff.cxx++')


f1 = "/home/taylor/Research/root/dtokpi.root"
tree = "dsprecontree"
#cut = "&&pi0mass>0.109&&pi0mass<0.138&&pi0MF_chisq<65"
#datatype = filename.split(".root")[0].split("_")[-1]
#decay = filename.split(".root")[0].split("/")[-1]
#outfileFormat = "./plots/"+datatype+"/"+tree+"/"+decay+"_"+tree
f = TFile(f1,"READ")
t = f.Get(tree)

deltam = RooRealVar("deltam", "deltam", 0.138, 0.18)

lb = deltam.getMin()
rb = deltam.getMax()
nBins=41
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(deltam)

data = RooDataSet("data", "raw data", t, vars)


#Shape Variables

#Cruijff
crumu = RooRealVar("#mu","Mean of Cruijff",0.145,0,0.2)
crusigmaR = RooRealVar("#sigma_{CR}","Cruijff SigmaR",0.003,0,1)
crusigmaL = RooRealVar("#sigma_{CL}","Cruijff SigmaL",0.003,0,1)
crualphaR = RooRealVar("#alpha_{R}","Cruijff AlphaR",0.1303,0,10)
crualphaL = RooRealVar("#alpha_{L}","Cruijff AlphaL",0.1306,0,10)

#Voigtian
voigmean = RooRealVar("<>_{signal}", "<>_{signal}", 0.145, 0.143, 0.147)
voigwidth = RooRealVar("width_{signal}", "#width_{signal}", 0.0005, 0, 0.01)
voigsigma = RooRealVar("#sigma_{signal}", "#sigma_{signal}", 0.0005, 0, 0.01)

#Breit Wigner
bwmu = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0.143, 0.147)
bwgamma = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0005, 0, 0.01)

#DstDBG
dm0 = RooRealVar("dm0", "dm0", 0.137, 0.138, 0.140)
d = RooRealVar("d", "d", 0.0114, 0, 2)
a = RooRealVar("a", "a", 1, 0, 5)
b = RooRealVar("b", "b", 3, 0, 10)

nsig = RooRealVar("N_{Signal}","nsig",0,100000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,100000)

#Define Fitting Functions

bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,dm0,d,a,b)
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for signal Voigtian
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmu,bwgamma) #Use for signal Breit Wigner
sig = RooCruijff("sig","Cruijff Signal Fcn",deltam,crumu,crusigmaL,crusigmaR,crualphaL,crualphaR) #Use for signal Cruijff
#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);
SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 

#fitRes = pdf.fitTo(dGeneric,RooFit.Extended(kTRUE), RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(dSig1, RooFit.Save(kTRUE), RooFit.Range("Full"));
fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(dchib1Sig_1k, RooFit.Save(kTRUE), RooFit.Range("Full"));




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
#nSignal=t1.Draw("deltamChi>>h1","pi0mass>0.114&&pi0mass<0.138&&pi0tru==1&&pi0MF_chisq<69&&pi0MF_chisq>0&&costhggCM>-0.07&&costhggCM<0.76&&dipiRecm>9.65&&dipiRecm<9.95")
#nSignal=t1.Draw("deltam>>h1")
#print("%.0f signal events plotted in the histogram"%nSignal)

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
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
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

#dh_chib1_sig.plotOn(frame1)
#dh_chib2_sig.plotOn(frame1)
#dh_chib1_bkg.plotOn(frame1)
#dh_chib2_bkg.plotOn(frame1)
#dh_gen_bkg.plotOn(frame1)
#bkg.plotOn(frame1)
#fitRes.Print()
# Sanity Check... 

canvas.Print("/home/taylor/Research/plots/dtokpi/deltam_cruijff+dstd0bg_fit.pdf")
canvas.Print("/home/taylor/Research/plots/dtokpi/deltam_cruijff+dstd0bg_fit.eps")
canvas.Print("/home/taylor/Research/plots/dtokpi/deltam_cruijff+dstd0bg_fit.png")

