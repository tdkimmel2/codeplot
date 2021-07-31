from ROOT import *
#from ROOT import gInterpreter, gSystem
import math, os

gInterpreter.ProcessLine('.L MyDblCB.cxx')

f1 = "/home/tkimmel/Research/root/systematics/pi0Systematics.root"
title="#pi^{0} Mass: From #pi^{0} Systematics MC"
dataType = "MC"

"""
f1 = "/home/tkimmel/Research/root/systematics/pi0SystematicsData.root"
title="#pi^{0} Mass: From #pi^{0} Systematics Data"
dataType = "Data"
"""

#outname = "/home/tkimmel/Research/plots/nbpi0/Systematics/"
#outname = "/home/tkimmel/Research/plots/nbpi0/Systematics/MomentumBins/"

#title+=" [|#vec{p}_{#pi^{0}}| < 1.0 GeV/c]"
#momcut = " && pizP>=0 && pizP<1"
#momcutname = "00pizPBin"

#title+=" [|#vec{p}_{#pi^{0}}| < 1.25 GeV/c]"
#momcut = " && pizP>=0 && pizP<1.25"
#momcutname = "0pizPBin"

#title+=" [0.5 GeV/c #leq |#vec{p}_{#pi^{0}}| < 1.25 GeV/c]"
#momcut = " && pizP>=0.5 && pizP<1.25"
#momcutname = "0_5pizPBin"

#title+=" [0.75 GeV/c #leq |#vec{p}_{#pi^{0}}| < 1.25 GeV/c]"
#momcut = " && pizP>=0.75 && pizP<1.25"
#momcutname = "0_75pizPBin"

#title+=" [1.0 GeV/c #leq |#vec{p}_{#pi^{0}}| < 1.25 GeV/c]"
#momcut = " && pizP>=1.0 && pizP<1.25"
#momcutname = "1pizPBin"

#title+=" [1.25 GeV/c #leq |#vec{p}_{#pi^{0}}| < 1.625 GeV/c]"
#momcut = " && pizP>=1.25 && pizP<1.625"
#momcutname = "2pizPBin"

title+=" [1.625 GeV/c #leq |#vec{p}_{#pi^{0}}| < 2.0 GeV/c]"
momcut = " && pizP>=1.625 && pizP<2.0"
momcutname = "3pizPBin"

#title+=" [2.0 GeV/c #leq |#vec{p}_{#pi^{0}}| < 2.375 GeV/c]"
#momcut = " && pizP>=2.0 && pizP<2.375"
#momcutname = "4pizPBin"

#title+=" [2.375 GeV/c #leq |#vec{p}_{#pi^{0}}| < 2.75 GeV/c]"
#momcut = " && pizP>=2.375 && pizP<2.75"
#momcutname = "5pizPBin"

#title+=" [2.75 GeV/c #leq |#vec{p}_{#pi^{0}}| < 3.125 GeV/c]"
#momcut = " && pizP>=2.75 && pizP<3.125"
#momcutname = "6pizPBin"

#title+=" [3.125 GeV/c #leq |#vec{p}_{#pi^{0}}| < 3.5 GeV/c]"
#momcut = " && pizP>=3.125 && pizP<3.5"
#momcutname = "7pizPBin"

#title+=" [|#vec{p}_{#pi^{0}}| #geq 3.5 GeV/c ]"
#momcut = " && pizP>=3.5"
#momcutname = "8pizPBin"

#f1 = "/home/tkimmel/Research/root/allmfrecon_pi0.root"
#title="#pi^{0} Mass: From All Generic MC"
#f1 = "/home/tkimmel/Research/root/massFit/allmfrecon_reducedpi0fittingsample.root"
#f1 = "/home/tkimmel/Research/root/massFit/charmmfrecon_reducedpi0fittingsample.root"
#title="#pi^{0} Mass: From Subset of Charm MC"
#outname = "/home/tkimmel/Research/plots/nbpi0/"
outname = "/home/tkimmel/Research/plots/nbpi0/Systematics/null"

tree = "pi0tree"
f = TFile(f1,"READ")
t = f.Get(tree)

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.08,0.180)# Wide window
pi0mass = RooRealVar("pi0mass", "pi0mass",0.085,0.185)
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.1,0.17)# Narrow window
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.12,0.15)# Narrower window

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.11,0.16)
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.1,0.17)
#pi0mass = RooRealVar("pi0mass", "pi0mass",0.095,0.175)

#pi0mass = RooRealVar("pi0mass", "pi0mass",0.1071,0.1606)# 5 sgma window
pizP = RooRealVar("pizP","pizP",0,5)
nb = RooRealVar("nb","nb",-1,1)
bcsflag = RooRealVar("bcsflag","bcsflag",0,1)
run = RooRealVar("run","run",0,240)
exp = RooRealVar("exp","exp",31,55)
lb = pi0mass.getMin()
rb = pi0mass.getMax()
nBins = 60
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000


#vars = RooArgSet(pi0mass)
vars = RooArgSet(pi0mass,nb,bcsflag,exp,run,pizP)


#data = RooDataSet("data", "raw data", t, vars)
data = RooDataSet("data", "raw data", t, vars, "nb>0.832 && bcsflag==1"+momcut)
dataoutname="withCuts"
#data = RooDataSet("data", "raw data", t, vars, "nb>0.832 && bcsflag==1 && ((exp==55 && run<24) || (exp==31 && run<235))")
#data = RooDataSet("data", "raw data", t, vars, "(exp==55 && run<24) || (exp==31 && run<235)")

#Function Variables

#Double Sided Crystal Ball
crymu = RooRealVar("#mu","Mean of Crystal Ball",0.13,0.14)
crysigma = RooRealVar("#sigma","#sigma",0.004,0.008)
cryalpha1 = RooRealVar("#alpha_{1}","#alpha_{1}",0,2)
cryalpha2 = RooRealVar("#alpha_{2}","#alpha_{2}",0,2)
#cryn1 = RooRealVar("n_{1}","n_{1}",0,50)
#cryn2 = RooRealVar("n_{2}","n_{2}",0,50)
#outname += dataoutname+"_"+dataType+"_"+momcutname

# Fixed n's
# Reduced Charm
#cryn1 = RooRealVar("n_{1}","n_{1}",1.123)
#cryn2 = RooRealVar("n_{2}","n_{2}",1.891)
#outname += "fixedNs_Minuit2"
#outname += "fixedNs"

# From withCuts_3pizPBin
cryn1 = RooRealVar("n_{1}","n_{1}",3.94)
cryn2 = RooRealVar("n_{2}","n_{2}",45)
#outname += "Fixed_Ns/"+dataoutname+"_"+dataType+"_"+momcutname+"_fixedNs"
#outname += "Fixed_Ns/narrowWindow_"+dataoutname+"_"+dataType+"_"+momcutname+"_fixedNs"

#cryn1 = RooRealVar("n_{1}","n_{1}",4.37)
#cryn2 = RooRealVar("n_{2}","n_{2}",66)
#outname += "PlusSigma/"+dataoutname+"_"+dataType+"_"+momcutname+"_fixedNsPlusSigma"
#cryn1 = RooRealVar("n_{1}","n_{1}",3.51)
#cryn2 = RooRealVar("n_{2}","n_{2}",24)
#outname += "MinusSigma/"+dataoutname+"_"+dataType+"_"+momcutname+"_fixedNsMinusSigma"


#Chebychev
c0 = RooRealVar("c0","c0",-3,3)
c1 = RooRealVar("c1","c1",-3,3)
c2 = RooRealVar("c2","c2",-1,1)
# No Cuts
"""
c0 = RooRealVar("c0","c0",-2,2)
c1 = RooRealVar("c1","c1",-5,0)
c2 = RooRealVar("c2","c2",-10,10)
"""

nsig = RooRealVar("N_{Signal}","nsig",38000,50000)
nbkg = RooRealVar("N_{Background}","nbkg",0,10000)# with cuts
#nsig = RooRealVar("N_{Signal}","nsig",144000,0,200000)
#nbkg = RooRealVar("N_{Background}","nbkg",1381439,0,1500000)

sig = MyDblCB("sig","sig",pi0mass,crymu,crysigma,cryalpha1,cryn1,cryalpha2,cryn2) #Use for signal Crystal Ball

bkg = RooChebychev("bkg","bkg",pi0mass,RooArgList(c0,c1))
#bkg = RooChebychev("poly","Chebychev Bkg Fcn",pi0mass,RooArgList(c0,c1,c2))

SIG = RooArgSet(sig)
BKG = RooArgSet(bkg)
pdf = RooAddPdf("pdf","sig+bkg",RooArgList(sig,bkg),RooArgList(nsig,nbkg))


#----------------------------------------------------------------------- 
#----------------------------------------------------------------------- 
# FITTING
#----------------------------------------------------------------------- 
#-----------------------------------------------------------------------

fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Range("Full"), RooFit.Extended(kTRUE));
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minimizer("Minuit2", "minimize"), RooFit.Minos(kTRUE))
#fitRes = pdf.fitTo(data, RooFit.Save(kTRUE), RooFit.Extended(kTRUE), RooFit.NumCPU(2), RooFit.Strategy(2), RooFit.Minos(kTRUE))

"""
ff = TFile("DSCBCheby_fitres.root","RECREATE")
fitRes.Write("fitRes")
pdf.Write("pdf")
BKG.Write("BKG")
SIG.Write("SIG")
bkg.Write("bkg")
sig.Write("sig")
ff.Close()
"""

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
frame1 = pi0mass.frame(RooFit.Bins(nBins),RooFit.Title(title))
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
#pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.65, 1, 0.95))
pdf.paramOn(frame1,RooFit.Format("NEU", RooFit.AutoPrecision(2)), RooFit.Layout(0.6, 0.99, 0.92))
frame1.Draw()

"""
#histPad.BuildLegend()
leg = TLegend(0.2,0.6,0.4,0.8)
leg.AddEntry(data,"Data","lep")
#leg.AddEntry(frame1.findObject("sig"),"Signal","l")
#leg.AddEntry(frame1.findObject("bkg"),"Background","l")
leg.AddEntry(frame1.findObject("sig"),"Signal","l")
leg.AddEntry(frame1.findObject("bkg"),"Background","l")
leg.Draw("same")
"""

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


outname += ".png"
canvas.Print(outname)

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/noCuts_constantAlphas_MC_lessEvents.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/noCuts_constantAlphas_MC.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/widerWindow_withCuts_MC.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/withCuts_MC.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/wideWindow_withCuts_MC.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/narrowWindow_withCuts_MC.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/noCuts_constantAlphas_Data_lessEvents.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/withCuts_Data.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/narrowWindow_withCuts_Data.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/Systematics/lessEvents_wideWindow_withCuts_Data.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon.png")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/noteFit_reducedCharmMC.png")
#canvas.Print("/home/tkimmel/Research/plots/alldtokpi/pi0_fit.png")

#canvas.SaveAs("noteFit.C")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/noteFit_reducedCharmMC.C")
#canvas.Print("/home/tkimmel/Research/codeplot/nbpi0/fitting/noteFit_reducedCharmMC.root")

#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedCharmMC_constantAlphas.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedCharmMC_constantAlphas_paramOff.png")


#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon_5sigmaWindow.png")
#canvas.Print("/home/tkimmel/Research/plots/nbpi0/pi0mass_doublecrystalballcheby_fit_reducedallmfrecon_widerwindow.png")
