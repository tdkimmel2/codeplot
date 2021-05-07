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
#gInterpreter.ProcessLine('.L RooVoigtian.cxx++')


#f1 = "/home/tkimmel/Research/root/klsignalmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_k0sigtrain10vars.root"
#f1 = "/home/tkimmel/Research/root/charmmfrecon_bcs.root"

#############Partial Data#############
"""
f1 = "/home/tkimmel/Research/root/partialData.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Partial Belle Dataset"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_kpPCut.png"

#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_fixedSigmasSignalMC_kpPCut.png"
outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_fixedSigmas&RSignalMC_kpPCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_fixedSigmasPartialMC_kpPCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_fixedSigmas&RPartialMC_kpPCut.png"

#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_fixedR_kpPCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_noParam.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_noDspPMagCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialData_Gaussian.png"
"""

"""
f1 = "/home/tkimmel/Research/root/partialMC.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Partial Generic Monte Carlo"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_kpPCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_kpPCut_noParam.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_kpPCut_Minuit2.png"

#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_fixedSigmas_kpPCut.png"
outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_fixedSigmas&R_kpPCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_noParam.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_noDsPMagCut.png"
#outname = "/home/tkimmel/Research/plots/partialData/klRecon_partialMC_Gaussian.png"
"""


############Full Stream MC############
f1 = "/home/tkimmel/Research/root/fullStream.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From a Full Stream of MC"
outname = "/home/tkimmel/Research/plots/fullStream/klRecon_fullStream_fixedSigmasSignalMC.png"

#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_fullStream_pionDup_noParam.png"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_fullStream_pionDup_Minuit2.png"

#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_GaussBifurG_narrowWindow.png"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_GaussBifurG_narrowWindow_noParam.png"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_GaussBifurG_narrowWindow_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_GaussBifurG_narrowWindow2_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/fullStream/klRecon_GaussBifurG_narrowWindow2_Minuit2.png"

############ALL MC############
"""
f1 = "/home/tkimmel/Research/root/allmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_kpPCut_allGeneric.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_kpPCut_allGeneric_noParam.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_kpPCut_fixedSigmas_allGeneric.png"
outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_kpPCut_fixedSigmas_allGeneric_lowParam.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_kpPCut_fixedSigmas_allGeneric_noParam.png"

#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_withCuts_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_3p416FlavorCut_BCS_nbn0p076.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_3p416FlavorCut_BCS.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow_fixedSigmas.png"

#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nb0p832_narrowWindow2_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nb0p832_narrowWindow2_fixedSigmas_minuit2.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow2_fixedSigmas.png"
"""

############K0SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/k0signalmfrecon.root"
title = "D^{*} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/k0signal/ksRecon_Looseflavorcut_BCS_fixedM0_fixedNs.png"
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

########CUT########
#cut=""
cut="kpP<3.5"
#cut="bcsflag==1 && nb>0.832"
#cut="dsPmag>3 && nb>0.832"# Loose flavor cut and k0sig 10BSR
#cut = "abs(dsflag)==1"

#cut="dsPmag>3.416 && bcsflag==1"
#cut="dsPmag>3.416 && bcsflag==1 && nb>-0.076"
#cut="dsPmag>2.765 && bcsflag==1"

#cut="dsPmag>2.765 && bcsflag==1 && nb>-0.076"
#cut="dsPmag>2.765 && bcsflag==1 && nb>0.832"

#cut="dsPmag>3 && bcsflag==1"# Loose flavor cut and BCS
#cut="dsPmag>3 && bcsflag==1 && nb>-0.076"# Loose flavor cut and BCS and k0sig 1SBR
#cut="dsPmag>4.5 && bcsflag==1"# Medium flavor cut and BCS
#cut="dsPmag>3.26939 && bcsflag==1"# Tight flavor cut and BCS


tree = "dslrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

#deltam = RooRealVar("deltam","deltam",0.138,0.2)
#deltam = RooRealVar("deltam","deltam",0.138,0.16)
#deltam = RooRealVar("deltam","deltam",0.139,0.153)
deltam = RooRealVar("deltam","deltam",0.14,0.152)
kpP = RooRealVar("kpP","kpP",0,3.5)
#dsPmag = RooRealVar("dsPmag","dsPmag",0,10)
nb = RooRealVar("nb","nb",-1,1)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)

"""
nbgm1 = RooRealVar("nbgm1","nbgm1",-1,1)
nbgm2 = RooRealVar("nbgm2","nbgm2",-1,1)
coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
coskpizcm = RooRealVar("coskpizcm","coskpizcm",-1,1)
cosdpipcm = RooRealVar("cosdpipcm","cosdpipcm",-1,1)
pipp = RooRealVar("pipp","pipp",0,1)
mfchi2 = RooRealVar("mfchi2","mfchi2",0,60)
gmthetacms = RooRealVar("gmthetacms","gmthetacms",0,3.14)
#kpdiff = RooRealVar("kpdiff","kpdiff",-5,5)
#dnb = RooRealVar("dnb","dnb",-1,1)
dsflag = RooRealVar("dsflag","dsflag",-40,40)
"""

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,kpdiff)
#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,dnb)


#vars = RooArgSet(deltam)
vars = RooArgSet(deltam,kpP)
#vars = RooArgSet(deltam,dsflag)
#vars = RooArgSet(deltam,bcsflag,nb)
#vars = RooArgSet(deltam,nb,dsPmag,mfchi2,gmthetacms)
#vars = RooArgSet(deltam,nb,dsPmag,bcsflag)


data = RooDataSet("data", "raw data", t, vars, cut)

#data = RooDataSet("data", "raw data", t, vars, "nb > 0.690")# mfsig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.854")# k0sig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.642")# mfsig pi0training 13 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.834")# k0sig pi0training 13 variables


#Function Variables

# Global Signal Mean
#mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0.146)
mu = RooRealVar("#mu","#mu",0.145,0.1458)

##Chebyshev
#c0 = RooRealVar("c_{0}","c_{0}",-1,1)
#c1 = RooRealVar("c_{1}","c_{1}",-1,1)
#c2 = RooRealVar("c_{2}","c_{2}",-1,1)

##Breit Wigner
#bwmean = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0, 0.2)
#bwwidth = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0009, 0, 0.1)

# Double Sided Crystal Ball
#mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.1454409,0.14539,0.146)
#gausmean.setConstant()
sigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0007,0.0001,0.01)# Signal MC
a1 = RooRealVar("#alpha_{1}","#alpha_{1}",1.205,0.9,2)
#n1 = RooRealVar("n1","n1",10,1,10)
n1 = RooRealVar("n_{1}","n_{1}",13,0,20)
a2 = RooRealVar("#alpha_{2}","#alpha_{2}",1.203,1,2)
n2 = RooRealVar("n_{2}","n_{2}",10,0,20)
#n1.setConstant()
#n2.setConstant()

##Gaussian
#gausmean = RooRealVar("#mu","#mu",0.1453,0.145,0.146)
gausmean = RooRealVar("#mu","#mu",0.1454,0.1453,0.146)
gaussigma = RooRealVar("#sigma","#sigma",0.0004,0.0010)
#gaussigma = RooRealVar("#sigma","#sigma",0.0004,0.0015)
#gaussigma = RooRealVar("#sigma","#sigma",0.0004,0.0008)# All generic

##Bifurcated Gaussian
"""
gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.0008,0.0019)
gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.0008,0.0021)
"""

#######SignalMC#######
scaleL = RooRealVar("scaleL","scaleL",1.921713)
scaleR = RooRealVar("scaleR","scaleR",2.233383)
#######PartialMC#######
#scaleL = RooRealVar("scaleL","scaleL",1.935953)
#scaleR = RooRealVar("scaleR","scaleR",2.359534)
gaussigmaL = RooFormulaVar("#sigmaL","#sigmaL","@0*@1",RooArgList(gaussigma,scaleL))
gaussigmaR = RooFormulaVar("#sigmaR","#sigmaR","@0*@1",RooArgList(gaussigma,scaleR))

#frac = RooRealVar("R","R",1)
#frac = RooRealVar("R","R",0.460)# Signal MC
frac = RooRealVar("R","R",0,1)

# DstD0BG
m0 = RooRealVar("m_{0}", "m_{0}", 0.13957, 0.1385, 0.142)
#m0 = RooRealVar("m_{0}", "m_{0}",0.138,0.142)
"""
A = RooRealVar("A", "A",-50,50)
B = RooRealVar("B", "C",-50,50)
#C = RooRealVar("C", "C",0,0.1)
C = RooRealVar("C", "C",0,1)
"""
A = RooRealVar("A", "A",-100,100)
B = RooRealVar("B", "C",-100,100)
#C = RooRealVar("C", "C",0,0.1)
C = RooRealVar("C", "C",0,1)
#m0.setConstant()

##################################################################################
##################################################################################
##################################################################################

#nsig = RooRealVar("N_{Signal}","nsig",0,20000)
#nsig = RooRealVar("N_{Signal}","nsig",0,1000)# Generic MC
nsig = RooRealVar("N_{Signal}","nsig",0,1000000)# Signal MC
nbkg = RooRealVar("N_{Bkg}","nbkg",0,10000000)

#cheby = RooChebychev("Chebychev","Chebychev",deltam,RooArgList(c0,c1,c2))
#bkg = RooAddPdf("bkg","bkg",RooArgList(cheby,dstd0),RooArgList(frac))
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
#dstd0 = RooDstD0BG("DstD0BG","DstD0BG",deltam,m0,d,a,b)
#sig = RooBifurGauss("sig","Bifurcated Gaussian Signal Fcn", deltam, gausmean, gaussigmaL, gaussigmaR) #Use for Gaussian Signal

#All MC
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma)
#Signal MC
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma)
#sig = MyDblCB("sig","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2)

#######Sum of Double-Sided Crystal Ball and Breit Wigner#######
gauss = RooGaussian("gauss","Gaussian Signal Fcn", deltam,mu,gaussigma)
bifurG = RooBifurGauss("bifurG","Bifurcated Gaussian Signal Fcn", deltam,mu,gaussigmaL,gaussigmaR)
dblcb = MyDblCB("dblcb","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2)
#bwig = RooBreitWigner("bwig","Breit Wigner Signal Fcn", deltam,mu,bwwidth)

sig = RooAddPdf("sig","Gauss + Bifur Gauss Sig Fcn",RooArgList(gauss,bifurG),RooArgList(frac))
#sig = gauss
GAUSS = RooArgSet(gauss)
BIFURG = RooArgSet(bifurG)
DBLCB = RooArgSet(dblcb)
#BWIG = RooArgSet(bwig)
###############################################################

bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,m0,C,A,B)

#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);

SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(frac))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE));

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

pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.99, 0.90))# Higher parameter box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.9))# Medium parameter box

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.63, 0.99, 0.68))# Lower parameter box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.67, 0.99, 0.56))# Lower few parameter box

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
