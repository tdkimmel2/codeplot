from ROOT import *
#from ROOT import gInterpreter, gSystem
import math, os

gInterpreter.ProcessLine('.L RooCruijff.cxx++')

f1 = "/home/taylor/Research/root/smallccset.root"
tree = "pi0tree"
f = TFile(f1,"READ")
t = f.Get(tree)

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.035,0.235)
pi0mass = RooRealVar("pi0mass", "pi0mass",0.085,0.185)
whomi = RooRealVar("whomi", "whomi",0,1)
lb = pi0mass.getMin()
rb = pi0mass.getMax()
nBins = 42
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(pi0mass, whomi)


data = RooDataSet("data", "raw data", t, vars, "whomi==1")

#Function Variables

#Cruijff
crumu = RooRealVar("#mu","Mean of Cruijff",0.1348,0.125,0.145)
crusigmaR = RooRealVar("#sigma_{CR}","Cruijff SigmaR",0.0044,0,0.01)
crusigmaL = RooRealVar("#sigma_{CL}","Cruijff SigmaL",0.00514,0,0.01)
crualphaR = RooRealVar("#alpha_{R}","Cruijff AlphaR",0.084,0,1)
crualphaL = RooRealVar("#alpha_{L}","Cruijff AlphaL",0.144,0,1)

nsig = RooRealVar("N_{Signal}","nsig",0,100000)

sig = RooCruijff("sig","Cruijff Signal Fcn",pi0mass,crumu,crusigmaL,crusigmaR,crualphaL,crualphaR) #Use for signal Cruijff
SIG = RooArgSet(sig)
pdf = RooAddPdf("pdf","sig",RooArgList(sig),RooArgList(nsig))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));

#Figure of Merit
#pi0mass.setRange("FullRange",0.035,0.235)
#pi0mass.setRange("FullRange",0.085,0.185)
#pi0mass.setRange("ThreeSigma",0.1436,0.1474) #Ks Three Sigma Window
#pi0mass.setRange("ThreeSigma",0.1428,0.1481) #Kl Three Sigma Window
#sigint = sig.createIntegral(vars,RooFit.Range("FullRange"))
#bkgint = bkg.createIntegral(vars,RooFit.Range("FullRange"))
#sigintv = sigint.getVal()
#bkgintv = bkgint.getVal()
#print("%s,%s"%(sigintv,bkgintv))
#FoM = sigintv/math.sqrt(sigintv + bkgintv)
#FoM = sigintv

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

#frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title("From MC: #pi^{0} Mass"))
frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title("From Inclusive MC: #pi^{0} Mass"))
pullFrame = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title(""))
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
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
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

#FOM = "#frac{S}{#sqrt{S+B}} = %.3f"%FoM
#tex2 = TLatex(0.1,0.1,FOM)
#tex2.SetTextSize(0.1)
#tex2.SetNDC()
#tex2.Draw()

canvas.Print("/home/taylor/Research/plots/nbpi0/pi0mass_cruijff_fit_smallinclusive.pdf")
canvas.Print("/home/taylor/Research/plots/nbpi0/pi0mass_cruijff_fit_smallinclusive.eps")
canvas.Print("/home/taylor/Research/plots/nbpi0/pi0mass_cruijff_fit_smallinclusive.png")

