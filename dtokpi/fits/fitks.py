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


#f1 = "/home/tkimmel/Research/root/kssignalmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_k0sigtrain10vars.root"
#f1 = "/home/tkimmel/Research/root/charmmfrecon_bcs.root"

#############Systematics#############
"""
f1 = "/home/tkimmel/Research/root/systematics/dsSystematics.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From D* Systematics MC"
outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/ks_MC"
#outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/asymWindow1_ks_MC"
#outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/asymWindow2_ks_MC"

f1 = "/home/tkimmel/Research/root/systematics/dsSystematicsData.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From D* Systematics Data"
outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/ks_Data"
#outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/asymWindow1_ks_Data"
#outname = "/home/tkimmel/Research/plots/systematics/dStarFitting/asymWindow2_ks_Data"
"""

############Partial MC/Data############
"""
f1 = "/home/tkimmel/Research/root/partialData.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Partial Belle Dataset"
outname = "/home/tkimmel/Research/plots/partialData/ksRecon_partialData"

f1 = "/home/tkimmel/Research/root/partialMC.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Partial Generic Monte Carlo"
outname = "/home/tkimmel/Research/plots/partialData/ksRecon_partialMC"
#outname = "/home/tkimmel/Research/plots/partialData/ksRecon_partialMC_noParam"
#outname = "/home/tkimmel/Research/plots/partialData/ksRecon_partialMC_noDsPMagCut"
"""

############Full Stream MC############
f1 = "/home/tkimmel/Research/root/fullStream.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From a Full Stream of MC"
#title = "D*^{+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From a Full Stream of MC"
#title = "D*^{-} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{-}: From a Full Stream of MC"
outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_fullStream"
#title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From a Partial MC"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_partialMC"
#outname = "/home/tkimmel/Research/plots/fullStream/nullS"
############ALL MC############
"""
#f1 = "/home/tkimmel/Research/root/allmfrecon.root"
#title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_allGeneric"
f1 = "/home/tkimmel/Research/root/allmfrecon_exp55Stream2.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Stream 2 Exp. 55 MC"
outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_allGeneric_exp55Stream2"
"""
############K0 SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/k0signalmfrecon.root"
title = "D^{*} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC"
"""

############KS SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/kssignalmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC"
outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_ksSignal"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_ksSignal_noParam"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_TMFit"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_withCuts"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_withCuts_pionDup_ksSignalMC"
"""

#outname = "/home/tkimmel/Research/plots/nullS"

tree = "dsrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

deltam = RooRealVar("deltam","deltam",0.14,0.152)
#deltam = RooRealVar("deltam","deltam",0.141,0.151)# Narrow
# Asymmetric Windows
#deltam = RooRealVar("deltam","deltam",0.14,0.155)# 1
#deltam = RooRealVar("deltam","deltam",0.14,0.1535)# 2

nb = RooRealVar("nb","nb",-1,1)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
chrgflag = RooRealVar("chrgflag","chrgflag",-1,1)
dsflag = RooRealVar("dsflag","dsflag",-40,40)
pizP = RooRealVar("pizP","pizP",0,6)
exp = RooRealVar("exp","exp",0,99)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
#nBins = 75
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(deltam)
#vars = RooArgSet(deltam,pizP,nb,bcsflag,chrgflag)
vars = RooArgSet(deltam,pizP,nb,bcsflag,chrgflag,exp)
#vars = RooArgSet(deltam,dsflag)
#vars = RooArgSet(deltam,bcsflag,nb)

########CUT########
#cut="pizP>=1"# No cut
#outname += "_pizPCut"
#cut="bcsflag==1 && nb>0.832"
#cut="pizP>=1 && bcsflag==1 && nb>0.63"# Systematics cut
#outname += "_withCuts_pizPCut"
#cut="pizP>=1 && bcsflag==1 && nb>0.832"
#outname += "_withCuts_pizPCut"
#cut="pizP>=1 && bcsflag==1 && nb>0.832 && exp==43"
#outname += "_withCuts_pizPCut"
cut="pizP>=1 && bcsflag==1 && nb>0.832 && exp!=43"
outname += "_withCuts_pizPCut_noExp43"

#cut="pizP>=1 && bcsflag==1 && nb>0.832 && chrgflag==1"
#outname += "_withCuts_pizPCut_positive"
#cut="pizP>=1 && bcsflag==1 && nb>0.832 && chrgflag==-1"
#outname += "_withCuts_pizPCut_negative"

#cut="abs(dsflag)==1"# Truth Matched
#cut="pizP>0.5"# No cut

data = RooDataSet("data", "raw data", t, vars, cut)


#Function Variables

# Global Mean
mu = RooRealVar("#mu","#mu",0.1453,0.1456)

#Gaussian
gaussigma = RooRealVar("#sigma","#sigma",0.00034,0.00045)

##Bifurcated Gaussian
#gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.000903,0.0006,0.0015)
#gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.000762,0.0004,0.0013)

scaleL = RooRealVar("scaleL","scaleL",2.130243)
scaleR = RooRealVar("scaleR","scaleR",2.437086)
outname += "_fixedSigmaRatios"

#scaleL = RooRealVar("scaleL","scaleL",2.130831)
#scaleR = RooRealVar("scaleR","scaleR",2.437828)
#outname += "_plusSigma"
#scaleL = RooRealVar("scaleL","scaleL",2.129655)
#scaleR = RooRealVar("scaleR","scaleR",2.436344)
#outname += "_minusSigma"
gaussigmaL = RooFormulaVar("#sigmaL","#sigmaL","@0*@1",RooArgList(gaussigma,scaleL))
gaussigmaR = RooFormulaVar("#sigmaR","#sigmaR","@0*@1",RooArgList(gaussigma,scaleR))

frac = RooRealVar("R","R",0,1)

# DstD0BG
m0 = RooRealVar("m_{0}","m_{0}",0.138,0.1395)
A = RooRealVar("A","A",-30,0)
B = RooRealVar("B","B",-1,1)
C = RooRealVar("C","C",0,0.1)
#m0.setConstant()
#m0 = RooRealVar("m_{0}", "m_{0}", 0.13957039)# Charged pion mass
#outname += "_fixedm0"

nsig = RooRealVar("N_{Signal}","nsig",0,190000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,500000)
#nsig = RooRealVar("N_{Signal}","nsig",0,25000)
#nbkg = RooRealVar("N_{Bkg}","nbkg",0,50000)

####################Sum of Two Signal PDFs####################
gauss = RooGaussian("gauss","Gaussian Signal Fcn", deltam,mu,gaussigma)
bifurG = RooBifurGauss("bifurG","Bifurcated Gaussian Signal Fcn", deltam,mu,gaussigmaL,gaussigmaR)

sig = RooAddPdf("sig","Gauss + BifurGauss Sig Fcn",RooArgList(gauss,bifurG),RooArgList(frac))
GAUSS = RooArgSet(gauss)
BIFURG = RooArgSet(bifurG)
##############################################################
bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,m0,C,A,B)
SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(frac))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE));

#Figure of Merit
#All MC
#deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigma.getVal(),gausmean.getVal() + 3*gaussigma.getVal())
#Signal MC
#deltam.setRange("ThreeSigma",mu.getVal() - 3*sigma.getVal(),mu.getVal() + 3*sigma.getVal())
###Bifurcated Gaussian###
deltam.setRange("ThreeSigma",mu.getVal() - 3*gaussigmaL.getVal(),mu.getVal() + 3*gaussigmaR.getVal())

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

###########Two Sig Fncs###########
#pdf.plotOn(frame1, RooFit.Components(GAUSS),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(BIFURG),RooFit.LineColor(kCyan))
#pdf.plotOn(frame1, RooFit.Components(DBLCB),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(BWIG),RooFit.LineColor(kCyan))
##################################


pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(bkg),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))

pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.60, 0.95, 0.90))# Higher Parameter Box

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.65, 0.99, 0.63))# Lower Parameter Box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.68, 0.99, 0.57))# Lower Few Parameter Box
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

fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs","RECREATE")
#fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippcutsbcs","RECREATE")
ws.Write()
fOutput.Write()
fOutput.Close()
"""
