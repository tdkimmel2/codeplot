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

############ALL MC############
"""
f1 = "/home/tkimmel/Research/root/allmfrecon.root"
title = "D^{*} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All MC"
#outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_4p5flavorcut_BCS_fixedm0_fixedNs.png"
outname = "/home/tkimmel/Research/plots/alldtokpi/klRecon_3p26939flavorcut_BCS_fixedm0_fixedNs.png"
"""
############K0SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/k0signalmfrecon.root"
title = "D^{*} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/k0signal/ksRecon_Looseflavorcut_BCS_fixedm0_fixedNs.png"
"""

############KLSIGNAL MC############
f1 = "/home/tkimmel/Research/root/klsignalmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K_{L}^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/klSignalMC/klRecon_TMFit.png"

#outname = "/home/tkimmel/Research/plots/nullL"

########CUT########
#cut=""
cut = "abs(dsflag)==1"
#cut="dsPmag>5 && bcsflag==1"# Loose flavor cut and BCS
#cut="dsPmag>4.5 && bcsflag==1"# Medium flavor cut and BCS
#cut="dsPmag>3.26939 && bcsflag==1"# Tight flavor cut and BCS


tree = "dslrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

#deltam = RooRealVar("deltam","deltam",0.138,0.18)
deltam = RooRealVar("deltam","deltam",0.138,0.2)
#x = RooRealVar("deltam","deltam",0.138,0.18)
nb = RooRealVar("nb","nb",-1,1)
nbgm1 = RooRealVar("nbgm1","nbgm1",-1,1)
nbgm2 = RooRealVar("nbgm2","nbgm2",-1,1)
coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
coskpizcm = RooRealVar("coskpizcm","coskpizcm",-1,1)
cosdpipcm = RooRealVar("cosdpipcm","cosdpipcm",-1,1)
pipp = RooRealVar("pipp","pipp",0,1)
dsPmag = RooRealVar("dsPmag","dsPmag",0,10)
mfchi2 = RooRealVar("mfchi2","mfchi2",0,60)
gmthetacms = RooRealVar("gmthetacms","gmthetacms",0,3.14)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
#kpdiff = RooRealVar("kpdiff","kpdiff",-5,5)
#dnb = RooRealVar("dnb","dnb",-1,1)
dsflag = RooRealVar("dsflag","dsflag",-40,40)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,kpdiff)
#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,dnb)


vars = RooArgSet(deltam,dsflag)
#vars = RooArgSet(deltam,nb,dsPmag,mfchi2,gmthetacms)
#vars = RooArgSet(deltam,nb,dsPmag,bcsflag)


data = RooDataSet("data", "raw data", t, vars, cut)

#data = RooDataSet("data", "raw data", t, vars, "nb > 0.690")# mfsig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.854")# k0sig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.642")# mfsig pi0training 13 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.834")# k0sig pi0training 13 variables


#Function Variables

##Chebyshev
#c0 = RooRealVar("c_{0}","c_{0}",-1,1)
#c1 = RooRealVar("c_{1}","c_{1}",-1,1)
#c2 = RooRealVar("c_{2}","c_{2}",-1,1)

##Voigtian
#voigmean = RooRealVar("<>_{signal}", "<>_{signal}", 0.145, 0, 0.5)
#voigwidth = RooRealVar("width_{signal}", "#width_{signal}", 0.0005, 0, 0.1)
#voigsigma = RooRealVar("#sigma_{signal}", "#sigma_{signal}", 0.0005, 0, 0.1)

##Breit Wigner
#bwmean = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0, 0.2)
#bwwidth = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0009, 0, 0.1)

##Bifurcated Gaussian
#gausmean = RooRealVar("#mu","#mu_{sig}",0.1453,0.145,0.146)
##gausmean.setConstant()
#gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.001,0.0005,0.01)# Signal MC
#gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.001,0.0005,0.01)# Signal MC

##Novosibirsk
#peak = RooRealVar("#mu","#mu",0.1453,0.145,0.146)
##gausmean.setConstant()
#width = RooRealVar("#sigma","#sigma",0.001,0.0005,0.01)# Signal MC
#tail = RooRealVar("tail","tail",0.001,0.0005,0.01)# Signal MC

##Gaussian
#gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.1453,0.145,0.146)
#gaussigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0009,0.0001,0.001)
#

##################################################################################
##################################################################################
##################################################################################

# DstD0BG
m0 = RooRealVar("m_{0}", "m_{0}", 0.13957, 0.138, 0.14)
A = RooRealVar("A", "A", -50, 50)
B = RooRealVar("B", "C", 0, 100)
C = RooRealVar("C", "C", 0, 10)
#m0.setConstant()

mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.1453,0.145,0.146)
#gausmean.setConstant()
sigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0007,0.0001,0.01)# Signal MC
a1 = RooRealVar("#alpha_{1}","#alpha_{1}",1.205,0,5)
#n1 = RooRealVar("n1","n1",10,1,10)
n1 = RooRealVar("n_{1}","n_{1}",7.42,0,20)
a2 = RooRealVar("#alpha_{2}","#alpha_{2}",1.203,0,5)
n2 = RooRealVar("n_{2}","n_{2}",1.9,0,20)
#n1.setConstant()
#n2.setConstant()

##################################################################################
##################################################################################
##################################################################################

#nsig = RooRealVar("N_{Signal}","nsig",0,1000)# All MC
nsig = RooRealVar("N_{Signal}","nsig",0,1000000)# Signal MC
nbkg = RooRealVar("N_{Bkg}","nbkg",0,1000000)
#nbkg = RooRealVar("N_{Bkg}","nbkg",0,10000000)

#cheby = RooChebychev("Chebychev","Chebychev",deltam,RooArgList(c0,c1,c2))
#bkg = RooAddPdf("bkg","bkg",RooArgList(cheby,dstd0),RooArgList(frac))
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
#dstd0 = RooDstD0BG("DstD0BG","DstD0BG",deltam,m0,d,a,b)
#sig = RooBifurGauss("sig","Bifurcated Gaussian Signal Fcn", deltam, gausmean, gaussigmaL, gaussigmaR) #Use for Gaussian Signal
#sig = RooNovosibirsk("sig","Novosibirsk Signal Fcn", deltam, peak, width, tail) #Use for Gaussian Signal

#All MC
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal
#Signal MC
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal
sig = MyDblCB("sig","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2) #Use for Double Crystal Ball signal
#sig = MyDblCB.MyDblCB("sig","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2) #Use for Double Crystal Ball signal
#sig = MyDblCB("sig","Double Sided Crystal Ball Signal Fcn") #Use for Double Crystal Ball signal

bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,m0,C,A,B)
frac = RooRealVar("frac","frac",0,1)

#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);

SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))
#pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(frac))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = sig.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));

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
deltam.setRange("ThreeSigma",mu.getVal() - 3*sigma.getVal(),mu.getVal() + 3*sigma.getVal())


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
pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
#pdf.plotOn(frame1, RooFit.Components(bkg),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.93))# Higher parameter box
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.9))# Medium parameter box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.60))# Lower parameter box
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
pullFrame.GetXaxis().SetTitle("#DeltaM_{D^{*}D^{0}} (GeV/c^{2})")
pullFrame.GetXaxis().SetTitleOffset(1.1)
pullFrame.GetXaxis().SetTitleSize(0.12)

pullFrame.SetMaximum(10)
pullFrame.SetMinimum(-10)
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
tex2.Draw()

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
