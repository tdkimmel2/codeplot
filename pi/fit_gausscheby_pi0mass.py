from ROOT import *
#from ROOT import gInterpreter, gSystem
import math, os


f1 = "/home/tkimmel/Research/root/kssignalmfrecon.root"
tree = "dsrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

###############KS Signal MC################
title = "Charged #pi Mass: From K^{0}_{S} Signal MC"
outname = "/home/tkimmel/Research/plots/chargedPion/BW_ksSignalMC.png"

pimass = RooRealVar("pimass", "pimass",0.1395,0.1397)
lb = pimass.getMin()
rb = pimass.getMax()
nBins = 42
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(pimass)


data = RooDataSet("data", "raw data", t, vars)

#Function Variables

#Breit Wigner
bwmean = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0, 0.2)
bwwidth = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0005, 0, 0.1)

#Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.148,0,0.2)
gaussigma = RooRealVar("#sigma1_{sig}","#sigma1_{sig}",0.0006,0,0.1)
gaussigma2 = RooRealVar("#sigma2_{sig}","#sigma2_{sig}",0.006,0,0.1)

#DstD0BG
dm0 = RooRealVar("dm0", "dm0", 0.137, 0.135, 0.140);
d = RooRealVar("d", "d", 0.006, 0, 10);
a = RooRealVar("a", "a", 0, 20);
b = RooRealVar("b", "b", 0, 20);

#Chebychev
c0 = RooRealVar("c0","c0",-1,1)
c1 = RooRealVar("c1","c1",-1,1)
c3 = RooRealVar("c3","c3",-1,1)

nsig = RooRealVar("N_{Signal}","nsig",0,1000000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,1000000)

#bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",pimass,dm0,d,a,b)
bkg = RooChebychev("poly","Chebychev Bkg Fcn",pimass,RooArgList(c0,c1))
#sig = RooVoigtian("sig","Voigtian Signal Fcn",pimass,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", pimass,bwmean,bwwidth) #Use for Breit Wigner Signal
#sig = RooGaussian("sig","Gaussian Signal Fcn", pimass,gausmean,gaussigma) #Use for Gaussian Signal
#sig2 = RooGaussian("sig2","Gaussian Signal Fcn", pimass,gausmean,gaussigma2)
#frac1 = RooRealVar("frac1","frac1",0,1)
#sig = RooAddPdf("signal","Double Gaussian Signal Fcn", RooArgList(sig1,sig2),RooArgList(frac1))
#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);
SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
pdf = RooAddPdf("pdf","sig",RooArgList(sig))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = sig.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));

#Figure of Merit
pimass.setRange("FullRange",0.035,0.235)
#pimass.setRange("ThreeSigma",0.1436,0.1474) #Ks Three Sigma Window
#pimass.setRange("ThreeSigma",0.1428,0.1481) #Kl Three Sigma Window
sigint = sig.createIntegral(vars,RooFit.Range("FullRange"))
bkgint = bkg.createIntegral(vars,RooFit.Range("FullRange"))
sigintv = sigint.getVal()
bkgintv = bkgint.getVal()
#print("%s,%s"%(sigintv,bkgintv))
#FoM = sigintv/math.sqrt(sigintv + bkgintv)
FoM = sigintv

# Create a new canvas
canvas = TCanvas("canvas", "canvas", 800, 800)
histPad = TPad("histPad", "Histogram Pad", 0.0, .35, 1.0, 1.0)
residPad = TPad("residPad", "Residual Pad",0.0, 0.0, 1.0, .35)
histPad.SetLeftMargin(0.15)
histPad.SetTopMargin(0.15)
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

frame1 = pimass.frame(RooFit.Bins(nBins),RooFit.Title(title))
pullFrame = pimass.frame(RooFit.Bins(nBins),RooFit.Title(""))
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
#pdf.plotOn(frame1, RooFit.LineColor(kBlack))
sig.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
sig.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(bkg),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.85))
sig.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.85))
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
pullFrame.GetXaxis().SetTitle("#pi^{0} Mass (GeV/c^{2})")
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

FOM = "#frac{S}{#sqrt{S+B}} = %.3f"%FoM
tex2 = TLatex(0.1,0.1,FOM)
tex2.SetTextSize(0.1)
tex2.SetNDC()
#tex2.Draw()

canvas.Print(outname)
