from ROOT import *

def plot_particlemass(Tree,ParticleMass,Title,XTitle,Histogram,Frame,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",800,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)
    
    Histogram.SetLineColor(kBlue)
    Histogram.SetLineWidth(2)
    Histogram.SetMinimum(1)

    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.01)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle(XTitle)
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.2)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.01)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.2)

    Tree.Draw(ParticleMass+">>h1")
    Frame.addTH1(Histogram)
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    #c1->Print("particlemass.eps","eps")

def plot_trueparticlemass(Tree,ParticleMass,TruthVariable,Title,XTitle,Histogram,Frame,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",800,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram.SetLineColor(kBlue)
    Histogram.SetLineWidth(2)
    Histogram.SetMinimum(1)

    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.01)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle(XTitle)
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.2)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.01)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.2)

    Tree.Draw(ParticleMass+">>h1",truthvariable+"==2")
    Frame.addTH1(Histogram)
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    #c1->Print("particlemass.eps","eps")

def plot_trueparticlemasswithbackground(Tree,ParticleMass,TruthVariable,Title,XTitle,Histogram1,Histogram2,Histogram3,Frame,LegendLeftEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",800,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram1.SetLineColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

    Histogram3.SetLineColor(kBlack)
    Histogram3.SetLineWidth(2)
    Histogram3.SetMinimum(1)

    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.01)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle(XTitle)
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.2)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.01)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.2)

    Tree.Draw(ParticleMass+">>h1",TruthVariable+"==2")
    Tree.Draw(ParticleMass+">>h2",TruthVariable+"==1")
    Tree.Draw(ParticleMass+">>h3")
    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    Frame.addTH1(Histogram3)

    legendwidth = 0.15
    leg = TLegend(LegendLeftEdge,0.74,LegendLeftEdge+legendwidth,0.89)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),"Signal","f")
    leg.AddEntry(Frame.findObject("h2"),"Background","l")
    leg.AddEntry(Frame.findObject("h3"),"Total","l")

    Frame.addObject(leg)

    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    #c1->Print("particlemass.eps","eps")
