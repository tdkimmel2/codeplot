from ROOT import *
#from ROOT import gInterpreter, gSystem
#from ROOT import RooFit
import math, os, sys

sys.path.append('/home/tkimmel/Research/codeplot/dtokpi/fits/')
gInterpreter.ProcessLine('#include "RooCruijff.h"')
gSystem.Load('RooCruijff.cxx')
gROOT.ProcessLineSync(".x MyDblCB.cxx")
gSystem.Load('MyDblCB.cxx')
gInterpreter.ProcessLine('#include "MyDblCB.h"')


#############Systematics#############
"""
f1 = "/home/tkimmel/Research/root/systematics/dsSystematics.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From D* Systematics MC"
outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/kl_MC"

f1 = "/home/tkimmel/Research/root/systematics/dsSystematicsData.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From D* Systematics Data"
outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/kl_Data"
"""

#############Partial Data#############
"""
f1 = "/home/tkimmel/Research/root/partialData.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Partial Belle Dataset"
outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData"

f1 = "/home/tkimmel/Research/root/partialMC_2.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Partial Generic Monte Carlo"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_kpPCut.png"
"""

############Full Stream MC############
f1 = "/home/tkimmel/Research/root/fullStream.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From a Full Stream of MC"
#title = "D*^{+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From a Full Stream of MC"
#title = "D*^{-} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{-}: From a Full Stream of MC"
outname = "/home/tkimmel/Research/plots/fullStream/klRecon_fullStream"
#title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From a Partial MC"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_parialMC"
#outname = "/home/tkimmel/Research/plots/fullStream/nullL"

############ALL MC############
"""
#f1 = "/home/tkimmel/Research/root/allmfrecon.root"
#title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_allGeneric"
f1 = "/home/tkimmel/Research/root/allmfrecon_exp55Stream2.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Stream 2 Exp. 55 MC"
outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_allGeneric_exp55Stream2"
"""

############KLSIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/klsignalmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/klSignalMC/klRecon_kpPCut_klSignal.png"
#outname = "/home/tkimmel/Research/plots/klSignalMC/klRecon_TMFit.png"
#outname = "/home/tkimmel/Research/plots/klSignalMC/klRecon_withCuts_klSignalMC.png"
#outname = "/home/tkimmel/Research/plots/klSignalMC/klRecon_withCuts_pionDup_klSignalMC.png"
"""

#outname = "/home/tkimmel/Research/plots/nullL"

#deltam = RooRealVar("deltam","deltam",0.138,0.154)
#deltam = RooRealVar("deltam","deltam",0.139,0.153)
deltam = RooRealVar("deltam","deltam",0.14,0.152)
#deltam = RooRealVar("deltam","deltam",0.141,0.151)
# Asymmetric Windows
#deltam = RooRealVar("deltam","deltam",0.14,0.155)# 1
#outname+="asymWindow1"
#deltam = RooRealVar("deltam","deltam",0.14,0.1535)# 2
#outname+="asymWindow2"


########CUT########
#cut=""
#cut="kpP<3.5 && pizP>=1"
#outname += "_kpPCut_pizPCut"
#cut="bcsflag==1 && nb>0.832"
#cut="kpP<3.5 && nb>0.63 && bcsflag==1"
#outname += "_withCuts_kpPCut"
#cut="kpP<3.5 && pizP>=1 && nb>0.63 && bcsflag==1"
#outname += "_withCuts_kpPCut_pizPCut"
#cut="kpP<3.5 && pizP>=1 && nb>0.832 && bcsflag==1"
#outname += "_withCuts_kpPCut_pizPCut"

#cut="kpP<3.5 && pizP>=1 && nb>0.832 && bcsflag==1 && exp==43"
#outname += "_withCuts_kpPCut_pizPCut"
cut="kpP<3.5 && pizP>=1 && nb>0.832 && bcsflag==1 && exp!=43"
outname += "_withCuts_kpPCut_pizPCut_noExp43"

#cut="kpP<3.5 && pizP>=1 && nb>0.832 && bcsflag==1 && chrgflag==1"
#outname += "_withCuts_kpPCut_pizPCut_positive"
#cut="kpP<3.5 && pizP>=1 && nb>0.832 && bcsflag==1 && chrgflag==-1"
#outname += "_withCuts_kpPCut_pizPCut_negative"

#cut="dsPmag>3 && nb>0.832"# Loose flavor cut and k0sig 10BSR
#cut = "abs(dsflag)==1"

tree = "dslrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

kpP = RooRealVar("kpP","kpP",0,3.5)
pizP = RooRealVar("pizP","pizP",0,6)
nb = RooRealVar("nb","nb",-1,1)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
chrgflag = RooRealVar("chrgflag","chrgflag",-1,1)
exp = RooRealVar("exp","exp",0,99)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000

#vars = RooArgSet(deltam)
#vars = RooArgSet(deltam,kpP)
vars = RooArgSet(deltam,kpP,pizP,nb,bcsflag,chrgflag,exp)
#vars = RooArgSet(deltam,dsflag)
#vars = RooArgSet(deltam,bcsflag,nb)


data = RooDataSet("data", "raw data", t, vars, cut)

#Function Variables

# Global Signal Mean
mu = RooRealVar("#mu","#mu",0.1453,0.1457)

# Sigmas
gaussigma = RooRealVar("#sigma","#sigma",0.00058,0.00061)
#gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.0009,0.0019)
#gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.0008,0.0019)

#######SignalMC#######
ratioL = RooRealVar("ratioL","ratioL",1.925645)
ratioR = RooRealVar("ratioR","ratioR",2.221548)
outname += "_fixedSigmaRatios"

#ratioL = RooRealVar("ratioL","ratioL",1.928107)
#ratioR = RooRealVar("ratioR","ratioR",2.224706)
#outname += "_plusSigma"
#ratioL = RooRealVar("ratioL","#sigma_{L}/#sigma",1.923182)
#ratioR = RooRealVar("ratioR","#sigma_{R}/#sigma",2.218390)
#outname += "_minusSigma"

gaussigmaL = RooFormulaVar("#sigmaL","#sigmaL","@0*@1",RooArgList(gaussigma,ratioL))
gaussigmaR = RooFormulaVar("#sigmaR","#sigmaR","@0*@1",RooArgList(gaussigma,ratioR))

frac = RooRealVar("R","R",0,1)

# DstD0BG
m0 = RooRealVar("m_{0}","m_{0}",0.138,0.1395)
A = RooRealVar("A","A",-40,0)
B = RooRealVar("B","B",0,3)
C = RooRealVar("C","C",0,0.1)
##################################################################################
##################################################################################
##################################################################################

nsig = RooRealVar("N_{Signal}","nsig",90000,140000)
nbkg = RooRealVar("N_{Bkg}","nbkg",900000,1100000)
#nsig = RooRealVar("N_{Signal}","nsig",0,20000)
#nbkg = RooRealVar("N_{Bkg}","nbkg",0,150000)

#######Sum of Double-Sided Crystal Ball and Breit Wigner#######
gauss = RooGaussian("gauss","Gaussian Signal Fcn", deltam,mu,gaussigma)
bifurG = RooBifurGauss("bifurG","Bifurcated Gaussian Signal Fcn", deltam,mu,gaussigmaL,gaussigmaR)

sig = RooAddPdf("sig","Gauss + Bifur Gauss Sig Fcn",RooArgList(gauss,bifurG),RooArgList(frac))
GAUSS = RooArgSet(gauss)
BIFURG = RooArgSet(bifurG)
###############################################################

bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,m0,C,A,B)
SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE));
#outname += "_Minuit2"

#Figure of Merit
#deltam.setRange("FullRange",0.138,0.18)
#deltam.setRange("ThreeSigma",0.1436,0.1474) #Ks Three Sigma Window
#deltam.setRange("ThreeSigma",0.1428,0.1481) #Kl Three Sigma Window


#All MC
#deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigma.getVal(),gausmean.getVal() + 3*gaussigma.getVal())

#Signal MC
#deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigma.getVal(),gausmean.getVal() + 3*gaussigma.getVal())
#deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigmaL.getVal(),gausmean.getVal() + 3*gaussigmaR.getVal())
#deltam.setRange("ThreeSigma",peak.getVal() - 3*width.getVal(),peak.getVal() + 3*width.getVal())

###Three Sigma###
#deltam.setRange("ThreeSigma",mu.getVal() - 3*sigma.getVal(),mu.getVal() + 3*sigma.getVal())
###Bifurcated Gaussian Asym. Three Sigma###
deltam.setRange("ThreeSigma",mu.getVal() - 3*gaussigmaL.getVal(),mu.getVal() + 3*gaussigmaR.getVal())


#print(gaussigma.getVal())
#print(fitRes.printValue(gaussigma))
#print("sig pdf is of type: %s"%(type(pdf)))
#sigdist = sig.Multiply(nsig.getValV())
#print("Number of Signal, Background = %s, %s"%(nsig.getValV(),nbkg.getValV()))
sigint = sig.createIntegral(vars,RooFit.Range("ThreeSigma"))
bkgint = bkg.createIntegral(vars,RooFit.Range("ThreeSigma"))
sigintv = sigint.getVal()
bkgintv = bkgint.getVal()
sigfom = sigintv*nsig.getValV()
bkgfom = bkgintv*nbkg.getValV()
#print("%s,%s"%(sigintv,bkgintv))
FoM = sigfom/math.sqrt(sigfom + bkgfom)

# Create a new canvas
canvas = TCanvas("canvas", "canvas", 800, 800)
histPad = TPad("histPad", "Histogram Pad", 0.0, .35, 1.0, 1.0)
residPad = TPad("residPad", "Residual Pad",0.0, 0.0, 1.0, .35)
histPad.SetLeftMargin(0.15)
histPad.SetTopMargin(0.13)
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

frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title(title))
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

###########Gauss & BifGauss###########
#pdf.plotOn(frame1, RooFit.Components(GAUSS),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(BIFURG),RooFit.LineColor(kCyan))
#pdf.plotOn(frame1, RooFit.Components(BWIG),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(DBLCB),RooFit.LineColor(kBlue))
######################################

pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(bkg),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.99, 0.90))# Higher parameter box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.99, 0.8))# Medium parameter box

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.99, 0.68))# Lower parameter box
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.66, 0.99, 0.58))# Lower few parameter box
#outname += "_paramOff"

#frame1.getAttFill('pdf_paramBox').SetFillStyle(0)
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
#pullFrame.GetXaxis().SetTitle("#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})")
pullFrame.GetXaxis().SetTitle("#DeltaM_{D*D^{0}} (GeV/c^{2})")
pullFrame.GetXaxis().SetTitleOffset(1.1)
pullFrame.GetXaxis().SetTitleSize(0.12)

pullFrame.SetMaximum(6)
pullFrame.SetMinimum(-6)
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
tex2 = TLatex(0.1,0.1,"#frac{S}{#sqrt{S+B}} = %.3f"%FoM)
tex2.SetTextSize(0.1)
tex2.SetNDC()
#tex2.Draw()

outname += ".png"
canvas.Print(outname)

"""
ws = RooWorkspace("ws")
getattr(ws,'import')(data)
getattr(ws,'import')(pdf)

fOutput = TFile("Workspace_allmfkl54pinbcoskpizcosdpipcmpippdspPmagcutsbcs","RECREATE")
#fOutput = TFile("Workspace_allmfkl54pinbcoskpizcosdpipcmpippcutsbcs","RECREATE")
ws.Write()
fOutput.Write()
fOutput.Close()
"""
