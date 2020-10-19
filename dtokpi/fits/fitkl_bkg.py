from ROOT import *
#from ROOT import gInterpreter, gSystem
#from ROOT import RooFit
import math, os

#gInterpreter.ProcessLine('#include "RooCruijff.h"')
#gInterpreter.ProcessLine('.L RooVoigtian.cxx++')
#gSystem.Load('RooCruijff.cxx++')
gROOT.ProcessLineSync(".x MyDblCB.cxx")
#gSystem.Load('MyDblCB.cxx')
#gInterpreter.ProcessLine('#include "MyDblCB.h"')


#f1 = "/home/tkimmel/Research/root/k0signalmfrecon.root"
#f1 = "/home/tkimmel/Research/root/kssignalmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_k0sigtrain10vars.root"
f1 = "/home/tkimmel/Research/root/allmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfdtokpi.root"
tree = "dsplrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

deltam = RooRealVar("deltam", "deltam", 0.138, 0.2)
dspPmag = RooRealVar("dspPmag","dspPmag",0,10)
kpdiff = RooRealVar("kpdiff", "kpdiff", -5, 5)
whomi = RooRealVar("whomi", "whomi", 0, 5)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
nBins = 50
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000

vars = RooArgSet(deltam,dspPmag,kpdiff,whomi)

#data = RooDataSet("data", "raw data", t, vars)# All
#data = RooDataSet("data", "raw data", t, vars, "abs(kpdiff)>0.28")# Background
data = RooDataSet("data", "raw data", t, vars, "whomi==0 && dspPmag>5")# Background
#data = RooDataSet("data", "raw data", t, vars, "whomi==0 && abs(kpdiff)>0.1")# Background

#Function Variables

##Chebyshev
#c0 = RooRealVar("c_{0}","c_{0}",-1,1)
#c1 = RooRealVar("c_{1}","c_{1}",-1,1)
#c2 = RooRealVar("c_{2}","c_{2}",-1,1)

##DstD0BG
dm0 = RooRealVar("dm0", "dm0", 0.1395, 0.136, 0.140)
a = RooRealVar("a", "a", -50, 20)
b = RooRealVar("b", "b", -20, 20)
d = RooRealVar("d", "d", 0.006, 0, 10)
#dm0.setConstant()

bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,dm0,d,a,b)

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = bkg.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));

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

frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC"))
pullFrame = deltam.frame(RooFit.Bins(nBins),RooFit.Title(""))
# Beautification Things
frame1.SetStats(0)
frame1.SetLineStyle(1)
frame1.GetXaxis().CenterTitle(kTRUE)
frame1.GetXaxis().SetLabelOffset(0.1)
frame1.GetXaxis().SetLabelSize(0.05)
frame1.GetXaxis().SetTitle("")
frame1.GetYaxis().CenterTitle(kTRUE)
frame1.GetYaxis().SetTitleOffset(1.4)
frame1.GetYaxis().SetLabelSize(0.05)
frame1.GetYaxis().SetTitleSize(0.05)
frame1.GetYaxis().SetTitle("Events/[%.3f MeV]"%binWidthMEV)

data.plotOn(frame1)
bkg.plotOn(frame1, RooFit.LineColor(kBlack))
bkg.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.35, 0.85, 0.5))
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

canvas.Print("/home/tkimmel/Research/plots/allSignalBkgFits/BackgroundL_all_flavorCut.png")

"""
ws = RooWorkspace("ws")
getattr(ws,'import')(data)
getattr(ws,'import')(pdf)

fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs","RECREATE")
#fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippcutsbcs","RECREATE")
ws.Write()
fOutput.Write()
fOutput.Close()
"""
