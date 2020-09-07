from ROOT import *

gInterpreter.ProcessLine('.L MyDblCB.cxx++')

name = "/home/tkimmel/Research/codeplot/nbpi0/fitting/DSCBCheby_fitres.root"
ff = TFile(name,"READ")
fitRes = gDirectory.Get("fitRes")
pdf = gDirectory.Get("pdf")
SIG = gDirectory.Get("SIG")
BKG = gDirectory.Get("BKG")
#sig = gDirectory.Get("sig")
#bkg = gDirectory.Get("bkg")

f1 = "/home/tkimmel/Research/root/charmmfrecon_reducedpi0fittingsample.root"
tree = "pi0tree"
f = TFile(f1,"READ")
t = f.Get(tree)

pi0mass = RooRealVar("pi0mass", "pi0mass",0.09,0.18)

lb = pi0mass.getMin()
rb = pi0mass.getMax()
nBins = 60
binWidth = (rb-lb)/nBins
binWidthMEV = binWidth*1000

vars = RooArgSet(pi0mass)
data = RooDataSet("data", "raw data", t, vars)

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

#fitRes.Print()

# Sanity Check IDK why this is here
#h1 = TH1F("h1","h1",nBins,lb,rb)

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
sig = RooFit.Components(SIG)
bkg = RooFit.Components(BKG)

#histPad.BuildLegend()
sigLine = TAttLine(kBlue, kSolid, 4)
bkgLine = TAttLine(kRed, kDashed, 4)
leg = TLegend(0.2,0.6,0.4,0.8)
leg.AddEntry(data,"Data","lp")
leg.AddEntry(sigLine,"Signal","l")
leg.AddEntry(bkgLine,"Background","l")
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


canvas.Print("/home/tkimmel/Research/plots/nbpi0/noteFit_reducedCharmMC_plottingCode.png")
