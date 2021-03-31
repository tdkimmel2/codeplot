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

############Full Stream MC############
f1 = "/home/tkimmel/Research/root/fullStream.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From a Full Stream of MC"
outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_fullStream_pionDup.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow_noParam.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow2.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow2_fixedSigmas.png"
#outname = "/home/tkimmel/Research/plots/fullStream/ksRecon_GaussBifurG_narrowWindow2_Minuit2.png"

############ALL MC############
"""
f1 = "/home/tkimmel/Research/root/allmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_withCuts.png"
outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_withCuts_pionDup.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_Looseflavorcut_BCS_nbn0p076.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_Looseflavorcut_BCS_nbn0p076_fixedNs_n114p874_n25p509.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_Looseflavorcut_BCS_fixedNs_n19p418_n22p6871.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_Looseflavorcut_BCS_fixedNs_n123p9_n25p36.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_Looseflavorcut_nb0p832_fixedNs_n123p9_n25p36.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_Looseflavorcut_nb0p832.png"

#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_3p416FlavorCut_BCS_nbn0p076.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_3p416FlavorCut_BCS.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076.png"

#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow_noParam.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS_nbn0p076_narrowWindow_fixedSigmas_noParam.png"
#outname = "/home/tkimmel/Research/plots/alldtokpi/ksRecon_GaussBifurG_2p765FlavorCut_BCS_nb0p832_narrowWindow2_fixedSigmas.png"
"""

############K0 SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/k0signalmfrecon.root"
title = "D^{*} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC"
outname = "/home/tkimmel/Research/plots/k0Signal/ksRecon_Looseflavorcut_BCS_fixeddm0_fixedNs.png"
"""

############KS SIGNAL MC############
"""
f1 = "/home/tkimmel/Research/root/kssignalmfrecon.root"
title = "D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_TMFit.png"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_fixeddm0.png"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_fixeddm0PDGPionMass.png"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_fixeddm0MeasuredPionMass.png"
#outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_withCuts.png"
outname = "/home/tkimmel/Research/plots/ksSignalMC/ksRecon_withCuts_pionDup_ksSignalMC.png"
"""


#outname = "/home/tkimmel/Research/plots/nullS"

########CUT########
#cut="dsPmag>3 && nb>0.832"# Loose flavor cut and k0sig 10BSR
#cut="dsPmag>3 && bcsflag==1 && nb>-0.076"# Loose flavor cut and BCS and k0sig 1SBR

#cut="dsPmag>3.416 && bcsflag==1"# Loose flavor cut and BCS
#cut="dsPmag>3.416 && bcsflag==1 && nb>-0.076"# Loose flavor cut and BCS and k0sig 1SBR
#cut="dsPmag>2.765 && bcsflag==1"# Loose flavor cut and BCS
#cut="dsPmag>2.765 && bcsflag==1 && nb>-0.076"# Loose flavor cut and BCS and k0sig 1SBR
#cut="dsPmag>2.765 && bcsflag==1 && nb>0.832"# Loose flavor cut and BCS and k0sig 10SBR
#cut="bcsflag==1"# BCS
cut=""# No cut
#cut="abs(dsflag)==1"# Truth Matched


tree = "dsrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

#deltam = RooRealVar("deltam","deltam",0.138,0.2)
#deltam = RooRealVar("deltam","deltam",0.138,0.16)
#deltam = RooRealVar("deltam","deltam",0.139,0.153)
deltam = RooRealVar("deltam","deltam",0.14,0.152)
nb = RooRealVar("nb","nb",-1,1)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
chrgflag = RooRealVar("chrgflag","chrgflag",-1,1)
dsPmag = RooRealVar("dsPmag","dsPmag",0,11)
dsPmagcms = RooRealVar("dsPmagcms","dsPmagcms",0,15)
dsflag = RooRealVar("dsflag","dsflag",-40,40)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
#nBins = 75
nBins = 100
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(deltam,dsflag)
vars = RooArgSet(deltam,dsPmag,bcsflag,nb)

#vars = RooArgSet(deltam,nb,dsPmag)
#vars = RooArgSet(deltam,nb,dsPmag,mfchi2,gmthetacms)
#vars = RooArgSet(deltam,nb,nbgm1,nbgm2,coskpiz,coskpizcm,cosdpipcm,pipp,dsPmag)
#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dsPmag,kpdiff)
#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dsPmag,dnb)


data = RooDataSet("data", "raw data", t, vars, cut)

#data = RooDataSet("data", "raw data", t, vars, "nb > 0.690")# mfsig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.854")# k0sig pi0training 10 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.642")# mfsig pi0training 13 variables
#data = RooDataSet("data", "raw data", t, vars, "nb > 0.834")# k0sig pi0training 13 variables

#data = RooDataSet("data", "raw data", t, vars, "dsPmag>3.26939 && bcsflag==1")# flavorCut



#Function Variables

# Global Mean
mu = RooRealVar("#mu","#mu",0.145,0.1456)

##Chebyshev
#c0 = RooRealVar("c_{0}","c_{0}",-1,1)
#c1 = RooRealVar("c_{1}","c_{1}",-1,1)
#c2 = RooRealVar("c_{2}","c_{2}",-1,1)


# Double Sided Crystal Ball
#mu = RooRealVar("#mu_{sig}","#mu_{sig}",0.145,0.1456)
sigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.00045,0.0007)
a1 = RooRealVar("#alpha_{1}","#alpha_{1}",0.9,1.5)
n1 = RooRealVar("n_{1}","n_{1}",20,26)
a2 = RooRealVar("#alpha_{2}","#alpha_{2}",0.8,1.4)
n2 = RooRealVar("n_{2}","n_{2}",4,9)
#n1.setConstant()
#n2.setConstant()
#n1 = RooRealVar("n1","n1",8.12,7.5,9)
#n2 = RooRealVar("n2","n2",2.644,2,3)

#Gaussian
#gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.145465,0.144,0.146)
##gausmean.setConstant()
gaussigma = RooRealVar("#sigma","#sigma",0.0004837,0.0003,0.0007)

##Bifurcated Gaussian
gausmean = RooRealVar("#mu","#mu_{sig}",0.1453,0.145,0.146)
#gausmean.setConstant()
gaussigmaR = RooRealVar("#sigma_{R}","#sigma_{R}",0.001217,0.0007,0.0017)
gaussigmaL = RooRealVar("#sigma_{L}","#sigma_{L}",0.001051,0.0006,0.0015)

"""
#scaleL = RooRealVar("scaleL","scaleL",2.141589) #140t152
#scaleR = RooRealVar("scaleR","scaleR",2.491547) #140t152
scaleL = RooRealVar("scaleL","scaleL",2.168022) #139t153
scaleR = RooRealVar("scaleR","scaleR",2.557849) #139t153
gaussigmaL = RooFormulaVar("#sigmaL","#sigmaL","@0*@1",RooArgList(gaussigma,scaleL))
gaussigmaR = RooFormulaVar("#sigmaR","#sigmaR","@0*@1",RooArgList(gaussigma,scaleR))
"""

#frac = RooRealVar("R","R",0.582)
frac = RooRealVar("R","R",0.582,0,1)

# DstD0BG
m0 = RooRealVar("m_{0}", "m_{0}", 0.139416, 0.138, 0.14)
#m0 = RooRealVar("m_{0}", "m_{0}", 0.13957, 0.1394, 0.1396)
A = RooRealVar("A", "A", -100, 100)
B = RooRealVar("B", "B", -100, 100)
C = RooRealVar("C", "C", 0, 1)
#m0.setConstant()

#nsig = RooRealVar("N_{Signal}","nsig",0,5000)# All MC
#nsig = RooRealVar("N_{Signal}","nsig",0,10000)# All MC
nsig = RooRealVar("N_{Signal}","nsig",0,1000000)# Signal MC
#nbkg = RooRealVar("N_{Bkg}","nbkg",0,10000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,10000000)

#cheby = RooChebychev("Chebychev","Chebychev",deltam,RooArgList(c0,c1,c2))
#dstd0 = RooDstD0BG("DstD0BG","DstD0BG",deltam,dm0,d,a,b)
#bkg = RooAddPdf("bkg","bkg",RooArgList(cheby,dstd0),RooArgList(frac))
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
#sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal


#sig = MyDblCB("sig","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2) #Use for Double Crystal Ball signal

####################Sum of Two Signal PDFs####################
gauss = RooGaussian("gauss","Gaussian Signal Fcn", deltam,mu,gaussigma)
bifurG = RooBifurGauss("bifurG","Bifurcated Gaussian Signal Fcn", deltam,mu,gaussigmaL,gaussigmaR)

dblcb = MyDblCB("dblcb","Double Sided Crystal Ball Signal Fcn", deltam,mu,sigma,a1,n1,a2,n2)
#frac = RooRealVar("frac_{sig}","frac_{sig}",0,1)
#frac = RooRealVar("frac_{sig}","frac_{sig}",0.5724,0,1)
#sig = RooAddPdf("sig","DblCB + BreitWigner Sig Fcn",RooArgList(dblcb,bwig),RooArgList(frac))
sig = RooAddPdf("sig","Gauss + BifurGauss Sig Fcn",RooArgList(gauss,bifurG),RooArgList(frac))
GAUSS = RooArgSet(gauss)
BIFURG = RooArgSet(bifurG)
DBLCB = RooArgSet(dblcb)
##############################################################
bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,m0,C,A,B)

#pdf = RooAddPdf("pdf","nbkg*bkg", RooArgList(bkg),RooArgList(nbkg));
#pdf = RooAddPdf("pdf","nsig*sig", RooArgList(sig),RooArgList(nsig));
#pdf = RooExtendPdf("pdf","nsig*sig", sig, nsig);
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

pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.68, 0.99, 0.93))# Higher Parameter Box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.60, 0.95, 0.90))# Higher Parameter Box, signal MC

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.6, 0.96, 0.85))# Medium Parameter Box

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.65, 0.99, 0.63))# Lower Parameter Box
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.65, 0.99, 0.51))# Lower Few Parameter Box

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

fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs","RECREATE")
#fOutput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippcutsbcs","RECREATE")
ws.Write()
fOutput.Write()
fOutput.Close()
"""
