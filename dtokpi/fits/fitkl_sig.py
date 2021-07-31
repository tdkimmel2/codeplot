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


#f1 = "/home/tkimmel/Research/root/k0signalrecon.root"
#f1 = "/home/tkimmel/Research/root/kssignalrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_k0sigtrain10vars.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon.root"

############KL SIGNAL MC############
f1 = "/home/tkimmel/Research/root/klsignalmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal MC"
#title = "Truth Matched D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/klSignalMC/klSignal_withCuts.png"
#outname = "/home/tkimmel/Research/plots/klSignalMC/withCuts_wideWindow.png"

####################################
###########ALL GENERIC MC###########
"""
f1 = "/home/tkimmel/Research/root/allmfrecon.root"
title = "Truth Matched D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} All Generic MC"
outname = "/home/tkimmel/Research/plots/alldtokpi/LGaussBifurGSig_dsflag_2p765FlavorCut_140t152.png"
"""
####################################

########CUT########
#cut="dsPmag>3.416 && abs(dsflag)==1"
#cut="dsPmag>2.765 && abs(dsflag)==1"
#cut="dsPmag>3 && abs(dsflag)==1"# Loose flavor cut and BCS
#cut="abs(dsflag)==1"# dsflag truth match
cut=""# No cut


f = TFile(f1,"READ")
tree = "dslrecontree"
t = f.Get(tree)

#deltam = RooRealVar("deltam", "deltam", 0.142, 0.15)
#deltam = RooRealVar("deltam", "deltam", 0.138, 0.154)
#deltam = RooRealVar("deltam", "deltam", 0.139, 0.153)
deltam = RooRealVar("deltam", "deltam", 0.14, 0.152)
chrgflag = RooRealVar("chrgflag","chrgflag",-1,1)
dsPmag = RooRealVar("dsPmag","dsPmag",0,10)
dsPmagcms = RooRealVar("dsPmagcms","dsPmagcms",0,10)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
whomi = RooRealVar("whomi", "whomi", 0, 5)
dsflag = RooRealVar("dsflag", "dsflag", -40, 40)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
#nBins = 50
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000

vars = RooArgSet(deltam)
#vars = RooArgSet(deltam,dsflag,dsPmag)
data = RooDataSet("data", "raw data", t, vars, cut)

#Function Variables

# Global Signal Mean
#mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0.146)
mu = RooRealVar("#mu","#mu",0.1454,0.1456)

#Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.145465,0.144,0.146)
gaussigma = RooRealVar("#sigma","#sigma",0.0007338,0.0004,0.0009)

##Bifurcated Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0.146)
gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.001897,0.001,0.0019)
gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.001576,0.001,0.0017)

#DstD0BG
m0 = RooRealVar("m_{0}", "m_{0}",0.139595,0.1375,0.1396)
A = RooRealVar("A", "A",-0.1351,-1,1)
B = RooRealVar("B", "B",-2.56941,-10,5)
C = RooRealVar("C", "C",0.04415,0,1)

# Double Sided Crystal Ball
#sigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0005,0.01)# Signal MC
#mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0.146)
a1 = RooRealVar("#alpha_{1}","#alpha_{1}",0,5)
n1 = RooRealVar("n_{1}","n_{1}",0,50)
a2 = RooRealVar("#alpha_{2}","#alpha_{2}",0,5)
n2 = RooRealVar("n_{2}","n_{2}",0,20)

##################################################################################
##################################################################################
##################################################################################

nsig = RooRealVar("N_{Signal}","nsig",0,1000000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,100000)

##########################Two Signals##########################
#dblcb = MyDblCB("dblcb","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2)
#DBLCB = RooArgSet(dblcb)
gauss = RooGaussian("gauss","Gaussian Signal Fcn", deltam,mu,gaussigma)
bifurG = RooBifurGauss("bifurG","Bifurcated Gaussian Signal Fcn", deltam,mu,gaussigmaL,gaussigmaR)

frac = RooRealVar("R","R",0,1)
sig = RooAddPdf("sig","DblCB + BreitWigner Sig Fcn",RooArgList(gauss,bifurG),RooArgList(frac))
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

#fitRes = sig.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(7), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE));

#Figure of Merit
#All MC
#deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigma.getVal(),gausmean.getVal() + 3*gaussigma.getVal())
#Signal MC
#deltam.setRange("ThreeSigma",mu.getVal() - 3*sigma.getVal(),mu.getVal() + 3*sigma.getVal())

#print("sig pdf is of type: %s"%(type(pdf)))
#sigdist = sig.Multiply(nsig.getValV())
#print("Number of Signal, Background = %s, %s"%(nsig.getValV(),nbkg.getValV()))
#sigint = sig.createIntegral(vars,RooFit.Range("ThreeSigma"))
#bkgint = bkg.createIntegral(vars,RooFit.Range("ThreeSigma"))
#sigintv = sigint.getVal()
#bkgintv = bkgint.getVal()
#sigfom = sigintv*nsig.getValV()
#bkgfom = bkgintv*nbkg.getValV()
##print("%s,%s"%(sigintv,bkgintv))
#FoM = sigfom/math.sqrt(sigfom + bkgfom)

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

###########BWig and DblCB###########
#pdf.plotOn(frame1, RooFit.Components(GAUSS),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(BIFURG),RooFit.LineColor(kCyan))
#pdf.plotOn(frame1, RooFit.Components(BWIG),RooFit.LineColor(kBlue))
#pdf.plotOn(frame1, RooFit.Components(DBLCB),RooFit.LineColor(kBlue))
####################################

pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.995, 0.90))

"""
sig.plotOn(frame1, RooFit.LineColor(kBlack))
sig.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.9))
"""

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
#tex2 = TLatex(0.1,0.1,"#frac{S}{#sqrt{S+B}} = %.3f"%FoM)
#tex2.SetTextSize(0.1)
#tex2.SetNDC()
#tex2.Draw()

canvas.Print(outname)

#canvas.Print("/home/tkimmel/Research/plots/SGaussianSig.png")
#canvas.Print("/home/tkimmel/Research/plots/SBreitWignerSig.png")
#canvas.Print("/home/tkimmel/Research/plots/SVoigtianSig.png")
#canvas.Print("/home/tkimmel/Research/plots/SBifurGaussianSig.png")
#canvas.Print("/home/tkimmel/Research/plots/SNovosibirskSig.png")
#canvas.Print("/home/tkimmel/Research/plots/allSignalBkgFits/SDoubleCBSig_whomi.png")
#canvas.Print("/home/tkimmel/Research/plots/allSignalBkgFits/SDoubleCBSig_whomi_kssignalMC.png")

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
