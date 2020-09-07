from ROOT import *
#from ROOT import gInterpreter, gSystem
import math, os

gInterpreter.ProcessLine('.L MyDblCB.cxx++')

#f1 = "/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root"
f1 = "/home/tkimmel/Research/root/charmmfrecon_reducedpi0fittingsample.root"
tree = "pi0tree"
f = TFile(f1,"READ")
t = f.Get(tree)

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.035,0.235)# Wider window
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.085,0.185)# Wide window
pi0mass = RooRealVar("pi0mass", "pi0mass",0.09,0.18)
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.1071,0.1606)# 5 sigma window
lb = pi0mass.getMin()
rb = pi0mass.getMax()
nBins = 60
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


vars = RooArgSet(pi0mass)


data = RooDataSet("data", "raw data", t, vars)

#Function Variables

#Double Sided Crystal Ball
crymu = RooRealVar("#mu","Mean of Crystal Ball",0.1345,0.13,0.14)
crysigma = RooRealVar("#sigma","#sigma",0.00545,0.003,0.01)
cryalpha1 = RooRealVar("#alpha_{1}","#alpha_{1}",1.25491,0,2)
cryn1 = RooRealVar("n_{1}","n_{1}",1.0288,0,5)
cryalpha2 = RooRealVar("#alpha_{2}","#alpha_{2}",1.77619,0,2)
cryn2 = RooRealVar("n_{2}","n_{2}",1.7362,0,5)
#cryn1.setConstant()
#cryn2.setConstant()
cryalpha1.setConstant()
cryalpha2.setConstant()

#Chebychev
c0 = RooRealVar("c0","c0",-1,1)
c1 = RooRealVar("c1","c1",-2,1)
c2 = RooRealVar("c2","c2",-1,1)

nsig = RooRealVar("N_{Signal}","nsig",145000,0,1000000)
nbkg = RooRealVar("N_{Background}","nbkg",2000000,0,5000000)

sig = MyDblCB("sig","Crystal Ball Signal Function",pi0mass,crymu,crysigma,cryalpha1,cryn1,cryalpha2,cryn2) #Use for signal Crystal Ball

bkg = RooChebychev("poly","Chebychev Bkg Fcn",pi0mass,RooArgList(c0,c1))
#bkg = RooChebychev("poly","Chebychev Bkg Fcn",pi0mass,RooArgList(c0,c1,c2))

SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))


#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(4), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE))
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(4), RooFit.Strategy(2), RooFit.Minos(kTRUE))

ff = TFile("DSCBCheby_fitres.root","RECREATE")
fitRes.Write("fitRes")
pdf.Write("pdf")
BKG.Write("BKG")
SIG.Write("SIG")
bkg.Write("bkg")
sig.Write("sig")
ff.Close()

#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# PLOTTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

# Create a new canvas
canvas = TCanvas("canvas", "canvas", 800, 800)
histPad = TPad("histPad", "Histogram Pad", 0.0, .35, 1.0, 1.0)
residPad = TPad("residPad", "Residual Pad",0.0, 0.0, 1.0, .35)
histPad.SetLeftMargin(0.15)
histPad.SetTopMargin(0.1)
histPad.SetBottomMargin(0.02)
#histPad.SetGrid()
residPad.SetLeftMargin(0.15)
residPad.SetTopMargin(0.04)
residPad.SetBottomMargin(0.35)
#residPad.SetGrid()
histPad.Draw()
residPad.Draw()
histPad.cd()

fitRes.Print()
# Sanity Check
h1 = TH1F("h1","h1",nBins,lb,rb)

#frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title("From MC: #pi^{0} Mass"))
frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title("#pi^{0} Mass: From Charm MC"))
pullFrame = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title(""))
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
#pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed)) #Uncomment for background dashed line
#pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.Components(BKG),RooFit.LineColor(kRed),RooFit.LineStyle(kDashed))
pdf.plotOn(frame1, RooFit.Components(SIG),RooFit.LineColor(kBlue))
pdf.plotOn(frame1, RooFit.LineColor(kBlack))
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.65, 1, 0.95))
frame1.Draw()

#histPad.BuildLegend()
leg = TLegend(0.2,0.6,0.4,0.8)
leg.AddEntry(data,"Data","lep")
leg.AddEntry(frame1.findObject("sig"),"Signal","l")
leg.AddEntry(frame1.findObject("bkg"),"Background","l")
leg.Draw("same")

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
pullFrame.GetXaxis().SetTitle("#pi^{0} Mass (GeV/c^{2})")
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


#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon.png")


canvas.Print("/home/tkimmel/Research/plots/nbpi0/noteFit_reducedCharmMC.png")
#canvas.SaveAs("noteFit.C")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/noteFit_reducedCharmMC.C")
#canvas.Print("/home/tkimmel/Research/codeplot/nbpi0/fitting/noteFit_reducedCharmMC.root")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedCharmMC_constantAlphas.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedCharmMC_constantAlphas_paramOff.png")


#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon_5sigmaWindow.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon_widerwindow.png")

