from ROOT import *
#from ROOT import gInterpreter, gSystem
#from ROOT import RooFit
import math, os

#gInterpreter.ProcessLine('#include "RooCruijff.h"')
gInterpreter.ProcessLine('.L RooVoigtian.cxx++')
#gSystem.Load('RooCruijff.cxx++')


f1 = "/home/tkimmel/Research/root/klsignalmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_k0sigtrain10vars.root"
#f1 = "/home/tkimmel/Research/root/allmfdtokpi.root"
#f1 = "/home/taylor/Research/root/allmfrecon.root"
#f1 = "/home/taylor/Research/root/signalmfrecon.root"
#f1 = "/home/taylor/Research/root/allmfdtokpi.root"
#f1 = "/home/taylor/Research/root/inclusivemfreconnb.root"
tree = "dsplrecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

deltam = RooRealVar("deltam", "deltam", 0.138, 0.18)
nb = RooRealVar("nb", "nb", -1, 1)
nbgm1 = RooRealVar("nbgm1", "nbgm1", -1, 1)
nbgm2 = RooRealVar("nbgm2", "nbgm2", -1, 1)
coskpiz = RooRealVar("coskpiz", "coskpiz", -1, 1)
coskpizcm = RooRealVar("coskpizcm", "coskpizcm", -1, 1)
cosdpipcm = RooRealVar("cosdpipcm", "cosdpipcm", -1, 1)
pipp = RooRealVar("pipp", "pipp", 0, 1)
dspPmag = RooRealVar("dspPmag", "dspPmag", 0, 5)
#dnb = RooRealVar("dnb", "dnb", -1, 1)

lb = deltam.getMin()
rb = deltam.getMax()
nBins = 42
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag)
#vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,dnb)


#data = RooDataSet("data", "raw data", t, vars) #No cuts
data = RooDataSet("data", "raw data", t, vars, "nb > 0.690")# mfsig pi0training 10 variables
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

##################################################################################
##################################################################################
##################################################################################

## All MC
##Gaussian
#gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.1453,0.145,0.146)
#gaussigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0009,0.0001,0.001)
#
##DstD0BG
#dm0 = RooRealVar("dm0", "dm0", 0.137, 0.136, 0.140)
#a = RooRealVar("a", "a", -30, -10)
#b = RooRealVar("b", "b", -10, 10)
#d = RooRealVar("d", "d", 0.006, 0, 10)

# Signal MC
#Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.1453,0.145,0.146)
#gausmean.setConstant()
gaussigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.001,0.0005,0.01)# Signal MC

#DstD0BG
dm0 = RooRealVar("dm0", "dm0", 0.137, 0.136, 0.140)
a = RooRealVar("a", "a", -30, -10)
b = RooRealVar("b", "b", -1, 1)
d = RooRealVar("d", "d", 0.485, 0, 1)

##################################################################################
##################################################################################
##################################################################################

#nsig = RooRealVar("N_{Signal}","nsig",0,10000)# All MC
nsig = RooRealVar("N_{Signal}","nsig",0,100000)# Signal MC
nbkg = RooRealVar("N_{Bkg}","nbkg",0,100000)

#cheby = RooChebychev("Chebychev","Chebychev",deltam,RooArgList(c0,c1,c2))
#bkg = RooAddPdf("bkg","bkg",RooArgList(cheby,dstd0),RooArgList(frac))
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
#dstd0 = RooDstD0BG("DstD0BG","DstD0BG",deltam,dm0,d,a,b)

sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal
bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,dm0,d,a,b)
frac = RooRealVar("frac","frac",0,1)

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

#Figure of Merit
#deltam.setRange("FullRange",0.138,0.18)
#deltam.setRange("ThreeSigma",0.1436,0.1474) #Ks Three Sigma Window
#deltam.setRange("ThreeSigma",0.1428,0.1481) #Kl Three Sigma Window
deltam.setRange("ThreeSigma",gausmean.getVal() - 3*gaussigma.getVal(),gausmean.getVal() + 3*gaussigma.getVal())
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

#frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From MC")) 
frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC"))
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

#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.93))# Higher parameter box
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.57, 0.96, 0.50))# Lower parameter box
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

canvas.Print("/home/tkimmel/Research/plots/klSignalMC/mfsig69010varsL.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/k0sig85410varsL.png")
#canvas.Print("/home/tkimmel/Research/plots/nullL.png")
#canvas.Print("/home/taylor/Research/plots/nullL.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.pdf")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.eps")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippdspPmagcuts.pdf")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippcutsbcs.pdf")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippcutsbcs.eps")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfkl54pinbcoskpizcosdpipcmpippcutsbcs.png")

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
