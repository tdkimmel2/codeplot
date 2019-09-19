from ROOT import *
#from ROOT import gInterpreter, gSystem
#from ROOT import RooFit
import math, os

#gInterpreter.ProcessLine('#include "RooCruijff.h"')
gInterpreter.ProcessLine('.L RooVoigtian.cxx++')
#gSystem.Load('RooCruijff.cxx++')


#f1 = "/home/tkimmel/Research/root/allmfrecon.root"
#f1 = "/home/tkimmel/Research/root/allmfdtokpi.root"
#f1 = "/home/taylor/Research/root/allmfdtokpi.root"
f1 = "/home/taylor/Research/root/allmfrecon.root"
#f1 = "/home/taylor/Research/root/inclusivemfreconnb.root"
tree = "dsprecontree"
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
R2 = RooRealVar("R2", "R2", 0, 1)
dnb = RooRealVar("dnb", "dnb", -1, 1)

lb = deltam.getMin()
rb = deltam.getMax()
#nBins = 42
nBins = 50
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(deltam,nb,nbgm1,nbgm2,coskpiz,coskpizcm,cosdpipcm,pipp,dspPmag)
vars = RooArgSet(deltam,nb,coskpiz,cosdpipcm,pipp,dspPmag,dnb)


#data = RooDataSet("data", "raw data", t, vars) #No cuts
#data = RooDataSet("data", "raw data", t, vars, "dnb > 0.52 && nb > 0.54") #Low statistics nb
data = RooDataSet("data", "raw data", t, vars, "dnb > 0.62 && nb > 0.54")
#data = RooDataSet("data", "raw data", t, vars, "R2>0.41") #R2 Cut
#data = RooDataSet("data", "raw data", t, vars, "nb>0.54 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38")
#data = RooDataSet("data", "raw data", t, vars, "coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38") #pinbcut>0.54 cut applied during the reconstruction
#data = RooDataSet("data", "raw data", t, vars, "coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38 && dspPmag>3.2") #pinbcut>0.54 cut applied during the reconstruction
#data = RooDataSet("data", "raw data", t, vars, "nb>0.54 && coskpiz>0.24 && cosdpipcm>0.985 && pipp<0.38 && dspPmag>3.2")
#data = RooDataSet("data", "raw data", t, vars, "nb>0.68 && coskpizcm>0.64")
#data = RooDataSet("data", "raw data", t, vars, "nb>0.54 && nbgm1>-0.28 && nbgm2>-0.28 && coskpiz>0.12")

#Function Variables

#Chebyshev
c0 = RooRealVar("c_{0}","c_{0}",-1,1)
c1 = RooRealVar("c_{1}","c_{1}",-1,1)
c2 = RooRealVar("c_{2}","c_{2}",-1,1)

#Voigtian
voigmean = RooRealVar("<>_{signal}", "<>_{signal}", 0.145, 0, 0.5)
voigwidth = RooRealVar("width_{signal}", "#width_{signal}", 0.0005, 0, 0.1)
voigsigma = RooRealVar("#sigma_{signal}", "#sigma_{signal}", 0.0005, 0, 0.1)

#Breit Wigner
bwmean = RooRealVar("#mu_{sig}", "#mu_{sig}", 0.145, 0, 0.2)
bwwidth = RooRealVar("#Gamma_{sig}", "#Gamma_{sig}", 0.0009, 0, 0.1)

#Gaussian
gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.145465,0.144,0.146)
#gausmean = RooRealVar("#mu_{sig}","#mu_{sig}",0.1455,0,0.2)
#gausmean.setConstant()
gaussigma = RooRealVar("#sigma_{sig}","#sigma_{sig}",0.0006,0,0.0007)

#DstD0BG
dm0 = RooRealVar("dm0", "dm0", 0.137, 0.136, 0.140);
d = RooRealVar("d", "d", 0.006, 0, 10);
#d = RooRealVar("d", "d", -10, 10);
#a = RooRealVar("a", "a", 0, 20);
#a = RooRealVar("a", "a", -0.1, 0.1); #coskpizcm+pinb
a = RooRealVar("a", "a", -20, 0); #coskpiz+cosdpipcm+pinb
#b = RooRealVar("b", "b", 0, 20);
#b = RooRealVar("b", "b", -0.1, 0.1); #coskpizcm+pinb
b = RooRealVar("b", "b", -10, 20); #coskpiz+cosdpipcm+pinb

nsig = RooRealVar("N_{Signal}","nsig",0,10000)
nbkg = RooRealVar("N_{Bkg}","nbkg",0,100000)

cheby = RooChebychev("Chebychev","Chebychev",deltam,RooArgList(c0,c1,c2))
dstd0 = RooDstD0BG("DstD0BG","DstD0BG",deltam,dm0,d,a,b)
frac = RooRealVar("frac","frac",0,1)
#bkg = RooAddPdf("bkg","bkg",RooArgList(cheby,dstd0),RooArgList(frac))
bkg = RooDstD0BG("bkg","DstD0BG Bkg Fcn",deltam,dm0,d,a,b)
#sig = RooVoigtian("sig","Voigtian Signal Fcn",deltam,voigmean,voigwidth,voigsigma) #Use for Voigtian Signal
#sig = RooBreitWigner("sig","Breit Wigner Signal Fcn", deltam,bwmean,bwwidth) #Use for Breit Wigner Signal
sig = RooGaussian("sig","Gaussian Signal Fcn", deltam,gausmean,gaussigma) #Use for Gaussian Signal
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

#frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From MC")) 
#frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC"))
frame1 = deltam.frame(RooFit.Bins(nBins),RooFit.Title("D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC"))
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

#canvas.Print("/home/tkimmel/Research/plots/test.png")
#canvas.Print("/home/taylor/Research/plots/test50bins.png")
#canvas.Print("/home/taylor/Research/plots/r2cutfit.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.pdf")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.eps")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcuts.pdf")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcuts.eps")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippdspPmagcuts.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.pdf")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.eps")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.png")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.pdf")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.eps")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allmfks54pinbcoskpizcosdpipcmpippcutsbcs.png")
#canvas.Print("/home/taylor/Research/plots/dtokpibmc/bmcmfks54pinbcoskpizcosdpipcmpippcutsbcs.pdf")
#canvas.Print("/home/taylor/Research/plots/dtokpibmc/bmcmfks54pinbcoskpizcosdpipcmpippcutsbcs.eps")
#canvas.Print("/home/taylor/Research/plots/dtokpibmc/bmcmfks54pinbcoskpizcosdpipcmpippcutsbcs.png")
#canvas.Print("/home/taylor/Research/plots/genericdtokpi/genericmfks54pinbcutsbcs.pdf")
#canvas.Print("/home/taylor/Research/plots/genericdtokpi/genericmfks54pinbcutsbcs.eps")
#canvas.Print("/home/taylor/Research/plots/genericdtokpi/genericmfks54pinbcutsbcs.png")
#canvas.Print("/home/taylor/Research/plots/alldtokpi/allcuts.png")
canvas.Print("/home/taylor/Research/plots/alldtokpi/nbdnbcutsmorestats62.png")
#canvas.Print("/home/taylor/Research/plots/dtokpipi0nb/mfks54cuts.pdf")
#canvas.Print("/home/taylor/Research/plots/dtokpipi0nb/mfks54cuts.eps")
#canvas.Print("/home/taylor/Research/plots/dtokpipi0nb/mfks54cuts.png")
#canvas.Print("/home/taylor/Research/plots/tests")

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
