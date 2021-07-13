from ROOT import *
#from ROOT import gInterpreter, gSystem
import math, os

gInterpreter.ProcessLine('.x MyDblCB.cxx')

f1 = "/home/tkimmel/Research/root/systematics/pi0Systematics.root"
#f1 = "/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root"
#f1 = "/home/tkimmel/Research/root/charmmfrecon.root"
#momcut = " && pizP>=1.625 && pizP<2.0"
tree = "pi0tree"
f = TFile(f1,"READ")
t = f.Get(tree)

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.035,0.235)# Wide window
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.085,0.185)
pi0mass = RooRealVar("pi0mass", "pi0mass",0.1,0.17)# Narrow window
pizP = RooRealVar("pizP","pizP",0,5)
whomi = RooRealVar("whomi", "whomi",0,1)
nb = RooRealVar("nb","nb",0,1)
run = RooRealVar("run","run",0,239)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
lb = pi0mass.getMin()
rb = pi0mass.getMax()
nBins = 42
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(pi0mass, whomi)
#vars = RooArgSet(pi0mass,nb,bcsflag,whomi,run)
vars = RooArgSet(pi0mass,nb,bcsflag,whomi,run,pizP)


#data = RooDataSet("data", "raw data", t, vars, "whomi==1")
data = RooDataSet("data", "raw data", t, vars, "nb>0.832 && bcsflag==1 && whomi==1")
#data = RooDataSet("data", "raw data", t, vars, "nb>0.832 && bcsflag==1 && whomi==1 && pizP>=1.625 && pizP<2.0")
#data = RooDataSet("data", "raw data", t, vars, "nb>0.832 && bcsflag==1 && whomi==1 && (run==234 || run==17)")

#Function Variables

#Double Sided Crystal Ball
crymu = RooRealVar("#mu","Mean of Crystal Ball",0.13,0.14)
crysigma = RooRealVar("#sigma","#sigma",0.0008,0.006)
#crysigma = RooRealVar("#sigma","#sigma",0.001,0.007)
cryalpha1 = RooRealVar("#alpha_{1}","#alpha_{1}",0,2)
cryn1 = RooRealVar("n_{1}","n_{1}",0,15)
cryalpha2 = RooRealVar("#alpha_{2}","#alpha_{2}",0,2)
cryn2 = RooRealVar("n_{2}","n_{2}",0,30)

nsig = RooRealVar("N_{Signal}","nsig",0,500000)

sig = MyDblCB("sig","Crystal Ball Signal Function",pi0mass,crymu,crysigma,cryalpha1,cryn1,cryalpha2,cryn2)
SIG = RooArgSet(sig)
pdf = RooAddPdf("pdf","sig",RooArgList(sig),RooArgList(nsig))

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minos(kTRUE))

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
frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title("#pi^{0} Mass: From #pi^{0} Systematics MC"))
pullFrame = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title(""))
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
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
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
pullFrame.GetXaxis().CenterTitle(kTRUE)
pullFrame.GetXaxis().SetLabelOffset(0.03)
pullFrame.GetXaxis().SetLabelSize(0.09)
pullFrame.GetXaxis().SetTitle("#pi^{0} Mass (GeV/c^{2})")
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

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/narrowWindow_withCuts_TM_Minuit2.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/withCuts_TM_Minuit2.png")
canvas.Print("/home/tkimmel/Research/plots/nbpi0/narrowWindow_withCuts_TM_Minuit2.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/withCuts_3pizPBin_TM_Minuit2.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/wideWindow_TM.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/wideWindow_withCuts_TM.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/wideWindow_withCuts_TM_Minuit2.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/wideWindow_withCuts_TM_Minuit2_reduced.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalball_fit.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalball_fit_test.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalball_fit_5sigWindow.png")
