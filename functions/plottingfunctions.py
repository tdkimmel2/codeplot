from ROOT import *
import math

def plot_variable(Tree,Variable,Option,Title,XTitle,Histogram,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",1100,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram.SetLineColor(kBlack)
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
    Frame.GetYaxis().SetTitleOffset(1.3)

    nentries = Tree.Draw(Variable+">>h1",Option,"goff")
    nentriesstr = str(nentries)
    Tree.Draw(Variable+">>h1",Option)
    Frame.addTH1(Histogram)

    legendwidth = 0.2
    legendheight = 0.2
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),"Entries "+nentriesstr,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    #gPad.SetLogy() #For logarithmic scale
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


#def plot_variable2histos(rb,lb,Tree,Variable,Option1,Option1Legend,Option2,Option2Legend,Title,XTitle,Histogram1,Histogram2,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
def plot_variable2histos(Tree,Variable,Option1,Option1Legend,Option2,Option2Legend,Title,XTitle,Histogram1,Histogram2,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",800,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram1.SetLineColor(kBlue)
    #Histogram1.SetFillColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kBlack)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

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

    nentries1 = Tree.Draw(Variable+">>h1",Option1,"goff")
    nentriesstr1 = str(nentries1)
    nentries2 = Tree.Draw(Variable+">>h2",Option2,"goff")
    nentriesstr2 = str(nentries2)
    Tree.Draw(Variable+">>h1",Option1)
    Tree.Draw(Variable+">>h2",Option2)

    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    #if norm1 != 0:
    #    h1.Scale(1/norm1)
    #if norm2 != 0:
    #    h2.Scale(1/norm2)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)

    legendwidth = 0.2
    legendheight = 0.2
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),Option1Legend+" "+nentriesstr1,"l")
    leg.AddEntry(Frame.findObject("h2"),Option2Legend+" "+nentriesstr2,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    #gPad.SetLogy() #For logarithmic scale
    Frame.Draw()
    #c1.SetLogy(1)
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


def plot_variablewith2cuts(Tree,Variable,Cut1,Cut2,Title,XTitle,Histogram,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",800,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram.SetLineColor(kBlack)
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

    nentries = Tree.Draw(Variable+">>h1",Cut1,Cut2)
    nentriesstr = str(nentries)
    Tree.Draw(Variable+">>h1",Cut1,Cut2)
    Frame.addTH1(Histogram)

    legendwidth = 0.2
    legendheight = 0.2
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),"Entries "+nentriesstr,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


def plot_variable3histos(rb,lb,Tree,Variable,Option1,Leg1,Option2,Leg2,Option3,Leg3,Title,XTitle,Histogram1,Histogram2,Histogram3,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",1100,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram1.SetLineColor(kBlue)
    #Histogram1.SetFillColor(kBlue)
    Histogram1.SetLineWidth(3)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    Histogram2.SetLineWidth(3)
    Histogram2.SetMinimum(1)

    Histogram3.SetLineColor(kBlack)
    Histogram3.SetLineWidth(3)
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

    nentries1 = Tree.Draw(Variable+">>h1",Option1)
    nentriesstr1 = str(nentries1)
    nentries2 = Tree.Draw(Variable+">>h2",Option2)
    nentriesstr2 = str(nentries2)
    nentries3 = Tree.Draw(Variable+">>h3",Option3)
    nentriesstr3 = str(nentries3)
    Tree.Draw(Variable+">>h1",Option1)
    Tree.Draw(Variable+">>h2",Option2)
    Tree.Draw(Variable+">>h3",Option3)

    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    norm3 = h3.GetEntries()
    if norm1 != 0:
        h1.Scale(1/norm1)
    if norm2 != 0:
        h2.Scale(1/norm2)
    if norm3 != 0:
        h3.Scale(1/norm3)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    Frame.addTH1(Histogram3)

    legendwidth = 0.15
    legendheight = 0.15
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),Leg1+" "+nentriesstr1,"l")
    leg.AddEntry(Frame.findObject("h2"),Leg2+" "+nentriesstr2,"l")
    leg.AddEntry(Frame.findObject("h3"),Leg3+" "+nentriesstr3,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")



def plot_variable4histos(rb,lb,Tree,Variable,Option1,Leg1,Option2,Leg2,Option3,Leg3,Option4,Leg4,Title,XTitle,Histogram1,Histogram2,Histogram3,Histogram4,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",1100,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram1.SetLineColor(kBlue)
    #Histogram1.SetFillColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

    Histogram3.SetLineColor(kBlack)
    Histogram3.SetLineWidth(2)
    Histogram3.SetMinimum(1)

    Histogram4.SetLineColor(kGreen)
    Histogram4.SetLineWidth(2)
    Histogram4.SetMinimum(1)

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

    nentries1 = Tree.Draw(Variable+">>h1",Option1)
    nentriesstr1 = str(nentries1)
    nentries2 = Tree.Draw(Variable+">>h2",Option2)
    nentriesstr2 = str(nentries2)
    nentries3 = Tree.Draw(Variable+">>h3",Option3)
    nentriesstr3 = str(nentries3)
    nentries4 = Tree.Draw(Variable+">>h4",Option4)
    nentriesstr4 = str(nentries4)
    Tree.Draw(Variable+">>h1",Option1)
    Tree.Draw(Variable+">>h2",Option2)
    Tree.Draw(Variable+">>h3",Option3)
    Tree.Draw(Variable+">>h4",Option4)

    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    norm3 = h3.GetEntries()
    norm4 = h4.GetEntries()
    if norm1 != 0:
        h1.Scale(1/norm1)
    if norm2 != 0:
        h2.Scale(1/norm2)
    if norm3 != 0:
        h3.Scale(1/norm3)
    if norm4 != 0:
        h4.Scale(1/norm4)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    Frame.addTH1(Histogram3)
    Frame.addTH1(Histogram4)

    legendwidth = 0.15
    legendheight = 0.15
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),Leg1+" "+nentriesstr1,"l")
    leg.AddEntry(Frame.findObject("h2"),Leg2+" "+nentriesstr2,"l")
    leg.AddEntry(Frame.findObject("h3"),Leg3+" "+nentriesstr3,"l")
    leg.AddEntry(Frame.findObject("h4"),Leg4+" "+nentriesstr4,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


def plot_variable5histos(rb,lb,Tree,Variable,Option1,Leg1,Option2,Leg2,Option3,Leg3,Option4,Leg4,Option5,Leg5,Title,XTitle,Histogram1,Histogram2,Histogram3,Histogram4,Histogram5,Frame,LegendLeftEdge,LegendBottomEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",1100,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    Histogram1.SetLineColor(kBlue)
    #Histogram1.SetFillColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

    Histogram3.SetLineColor(kBlack)
    Histogram3.SetLineWidth(2)
    Histogram3.SetMinimum(1)

    Histogram4.SetLineColor(kGreen)
    Histogram4.SetLineWidth(2)
    Histogram4.SetMinimum(1)

    Histogram4.SetLineColor(kCyan)
    Histogram4.SetLineWidth(2)
    Histogram4.SetMinimum(1)

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

    nentries1 = Tree.Draw(Variable+">>h1",Option1)
    nentriesstr1 = str(nentries1)
    nentries2 = Tree.Draw(Variable+">>h2",Option2)
    nentriesstr2 = str(nentries2)
    nentries3 = Tree.Draw(Variable+">>h3",Option3)
    nentriesstr3 = str(nentries3)
    nentries4 = Tree.Draw(Variable+">>h4",Option4)
    nentriesstr4 = str(nentries4)
    nentries5 = Tree.Draw(Variable+">>h5",Option5)
    nentriesstr5 = str(nentries5)
    Tree.Draw(Variable+">>h1",Option1)
    Tree.Draw(Variable+">>h2",Option2)
    Tree.Draw(Variable+">>h3",Option3)
    Tree.Draw(Variable+">>h4",Option4)
    Tree.Draw(Variable+">>h5",Option5)

    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    norm3 = h3.GetEntries()
    norm4 = h4.GetEntries()
    norm5 = h5.GetEntries()
    if norm1 != 0:
        h1.Scale(1/norm1)
    if norm2 != 0:
        h2.Scale(1/norm2)
    if norm3 != 0:
        h3.Scale(1/norm3)
    if norm4 != 0:
        h4.Scale(1/norm4)
    if norm5 != 0:
        h5.Scale(1/norm5)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    Frame.addTH1(Histogram3)
    Frame.addTH1(Histogram4)
    Frame.addTH1(Histogram5)

    legendwidth = 0.15
    legendheight = 0.15
    leg = TLegend(LegendLeftEdge,LegendBottomEdge,LegendLeftEdge+legendwidth,LegendBottomEdge+legendheight)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),Leg1+" "+nentriesstr1,"l")
    leg.AddEntry(Frame.findObject("h2"),Leg2+" "+nentriesstr2,"l")
    leg.AddEntry(Frame.findObject("h3"),Leg3+" "+nentriesstr3,"l")
    leg.AddEntry(Frame.findObject("h4"),Leg4+" "+nentriesstr4,"l")
    leg.AddEntry(Frame.findObject("h5"),Leg5+" "+nentriesstr5,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    c1.Update()
    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


def OptimizeCut_GreaterThan(rb,lb,Tree,Variable,TruthVariable,CutString,Title,XTitle,Histogram1,Histogram2,Frame,Frame2,LegendLeftEdge,OutputFilename,FoM):
    #FoM needs to be set to "std" for S/sqrt(S+B) or "punz" for punzi FoM
    #print(FOM)
    c1 = TCanvas("c1","",800,500)
    histPad = TPad("histPad","",0.0,0.32,1.0,1.0)
    fomPad = TPad("fromPad","",0.0,0.0,1.0,0.32)
    histPad.SetLeftMargin(0.15)
    histPad.SetTopMargin(0.1)
    histPad.SetBottomMargin(0.02)
    histPad.SetGrid()
    fomPad.SetLeftMargin(0.15)
    fomPad.SetTopMargin(0.04)
    fomPad.SetBottomMargin(0.45)
    fomPad.SetGrid()
    histPad.Draw()
    fomPad.Draw()
    histPad.cd()

    Histogram1.SetLineColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    #Histogram2.SetLineStyle(kDashed)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

    #Signal Weight to Potentially Weight Signal More - Set to 1 for just S/sqrt(S+B)
    sigweight = 1
    nBins = 100
    binWidth = (rb-lb)/nBins
    signalvar = 1 #Default, true=1 and false=0
    if TruthVariable == "mcflag":
        signalvar = 2 #Use for mcflag
    if TruthVariable == "whomi":
        signalvar = 4 #Use for whomi
    signalvarstr = str(signalvar)
    #print signalvarstr

    #nSigTotal = Tree.Draw(Variable+">>h1","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+">="+signalvarstr,"goff")
    #nBkgTotal = Tree.Draw(Variable+">>h2","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+"<"+signalvarstr,"goff")
    #print Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr,"goff"
    if CutString != "":
        if TruthVariable == "whomi" or "truth":
            nSigTotal = Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr,"goff")
            nBkgTotal = Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr,"goff")
        if TruthVariable == "mcflag":
            nSigTotal = Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr,"goff")
            nBkgTotal = Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr,"goff")
    else:
        if TruthVariable == "whomi" or "truth":
            nSigTotal = Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr,"goff")
            nBkgTotal = Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr,"goff")
        if TruthVariable == "mcflag":
            nSigTotal = Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr,"goff")
            nBkgTotal = Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr,"goff")

    nSigRetained = []
    nBkgRetained = []
    FOM = []

    for i in range(0,nBins):
        CUT = lb + i*binWidth
        #nSigRetained.append(Tree.Draw(Variable+">>h1","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        #nBkgRetained.append(Tree.Draw(Variable+">>h2","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        if CutString != "":
            if TruthVariable == "whomi" or "truth":
                nSigRetained.append(Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
                nBkgRetained.append(Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            if TruthVariable == "mcflag":
                nSigRetained.append(Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
                nBkgRetained.append(Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        else:
            if TruthVariable == "whomi" or "truth":
                nSigRetained.append(Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
                nBkgRetained.append(Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            if TruthVariable == "mcflag":
                nSigRetained.append(Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
                nBkgRetained.append(Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        #print math.sqrt((sigweight*nSigRetained[i])+nBkgRetained[i])
        #print nBkgRetained[i]
        if FoM=="std":
            denominator = (sigweight*nSigRetained[i])+nBkgRetained[i]
        if FoM=="punz":
            denominator = 5/2 + math.sqrt(nBkgRetained[i]) #Punzi Denominator
        # print(CUT)
        # print(nSigRetained)
        # print(nBkgRetained)
        # print(denominator)
        print(i)
        if denominator == 0:
            FOM.append(0)
        else:
            if FoM=="std":
                FOM.append((sigweight*nSigRetained[i])/(float(denominator)))
            if FoM=="punz":
                FOM.append((sigweight*nSigRetained[i])/(nSigTotal*float(denominator))) #Punzi FOM
        #print FOM[i]
        #print nSigRetained[i], nBkgRetained[i], denominator, FOM[i]

    print("The maximal figure of merit is %.3f"%max(FOM))
    optimalIteration = FOM.index(max(FOM))
    optimalCut = lb+optimalIteration*binWidth
    print "This is attained for a cut of "+Variable+" > %.3f"%optimalCut
    effiRetainSIG = 0
    effiRejectBKG = 0
    if nSigTotal != 0:
        effiRetainSIG = float(nSigRetained[optimalIteration])/nSigTotal
    if nBkgTotal != 0:
        effiRejectBKG = float(nBkgTotal - nBkgRetained[optimalIteration])/nBkgTotal
    print("Effi_rejectBKG = %.3f"%effiRejectBKG)
    print("Effi_retainSIG = %.3f"%effiRetainSIG)

    bottomBound = min(FOM)
    topBound = max(FOM)
    topBound+=int(float(topBound-bottomBound)/6+0.9)
    bottomBound-=int(float(topBound-bottomBound)/6+0.5)

    RESULT = "#splitline{Optimal Cut:}{%s > %.3f}"%(XTitle,optimalCut)
    tex1 = TLatex(0.72,0.15,RESULT)
    tex1.SetTextSize(0.1)
    tex1.SetNDC()

    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.02)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle("")
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.5)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.02)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.4)
    Frame.SetMinimum(1)

    #Tree.Draw(Variable+">>h1","deltam<0.1476 && deltam>0.1434 && "+TruthVariable+">="+signalvarstr)
    #Tree.Draw(Variable+">>h2","deltam<0.1476 && deltam>0.1434 && "+TruthVariable+"<"+signalvarstr)
    if CutString != "":
        if TruthVariable == "whomi" or "truth":
            Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr)
            Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr)
        if TruthVariable == "mcflag":
            Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr)
            Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr)
    else:
        if TruthVariable == "whomi" or "truth":
            Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr)
            Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr)
        if TruthVariable == "mcflag":
            Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr)
            Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr)

    #Normalize histograms
    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    #print(norm1)
    #print(norm2)
    if norm1 != 0:
        h1.Scale(1/norm1)
    if norm2 != 0:
        h2.Scale(1/norm2)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    maxY = [Histogram1.GetMaximum(), Histogram2.GetMaximum()]
    minY = [Histogram1.GetMinimum(), Histogram2.GetMinimum()]
    topArrow = max(maxY)
    bottomArrow = min(minY)
    topArrow = int(2*float(topArrow)/10+0.5)
    bottomArrow += int(float(topArrow-bottomArrow)/10+0.5)
    a = TArrow(optimalCut,bottomArrow,optimalCut,topArrow,0.02,"<|")
    a.SetLineWidth(3)
    a.SetLineColor(kBlack)
    a.SetLineStyle(7)
    l = TLine(optimalCut, bottomBound, optimalCut, topBound)
    l.SetLineWidth(2)
    l.SetLineColor(kBlack)
    l.SetLineStyle(7)
    Frame.addObject(a)

    Histogram1.Draw()
    Histogram2.Draw()

    legendwidth = 0.25
    leg = TLegend(LegendLeftEdge,0.74,LegendLeftEdge+legendwidth,0.89)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),"Normalized Signal","l")
    leg.AddEntry(Frame.findObject("h2"),"Normalized Background","l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    #c1.SetLogy(1)
    histPad.cd()
    histPad.Draw()
    histPad.Draw()
    c1.Update()

    fomPad.cd()
    hFOM = TH1F("hFOM","hFOM",nBins,lb,rb)
    hFOM.SetLineColor(kBlack)
    for k in range(nBins):
        hFOM.SetBinContent(k+1,FOM[k])
    hFOM.Draw()

    Frame2.SetTitle("")
    Frame2.GetXaxis().CenterTitle(True)
    Frame2.GetXaxis().SetLabelOffset(0.03)
    Frame2.GetXaxis().SetLabelSize(0.07)
    Frame2.GetXaxis().SetTitle(XTitle)
    Frame2.GetXaxis().SetTitleSize(0.1)
    Frame2.GetXaxis().SetTitleOffset(1.7)
    Frame2.GetYaxis().CenterTitle(True)
    Frame2.GetYaxis().SetLabelOffset(0.01)
    Frame2.GetYaxis().SetLabelSize(0.05)
    if FoM=="std":
        Frame2.GetYaxis().SetTitle("#frac{S}{#sqrt{S+B}}")
    if FoM=="punz":
        Frame2.GetYaxis().SetTitle("#frac{S}{#frac{5}{2}+B}")
    Frame2.GetYaxis().SetTitleSize(0.1)
    Frame2.GetYaxis().SetTitleOffset(0.55)
    Frame2.SetMinimum(1)

    Frame2.addTH1(hFOM)
    Frame2.addObject(l)
    Frame2.addObject(tex1)
    Frame2.SetAxisRange(bottomBound,topBound,"Y")

    fomPad.SetTickx()
    fomPad.SetTicky()
    Frame2.SetStats(0)
    Frame2.Draw()
    fomPad.Draw()
    histPad.cd()

    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")



def OptimizeCut_LessThan(rb,lb,Tree,Variable,TruthVariable,CutString,Title,XTitle,Histogram1,Histogram2,Frame,Frame2,LegendLeftEdge,OutputFilename,FoM):
    #FoM needs to be set to "std" for S/sqrt(S+B) or "punz" for punzi FoM
    #print(FOM)
    c1 = TCanvas("c1","",800,500)
    histPad = TPad("histPad","",0.0,0.32,1.0,1.0)
    fomPad = TPad("fromPad","",0.0,0.0,1.0,0.32)
    histPad.SetLeftMargin(0.15)
    histPad.SetTopMargin(0.1)
    histPad.SetBottomMargin(0.02)
    histPad.SetGrid()
    fomPad.SetLeftMargin(0.15)
    fomPad.SetTopMargin(0.04)
    fomPad.SetBottomMargin(0.45)
    fomPad.SetGrid()
    histPad.Draw()
    fomPad.Draw()
    histPad.cd()

    Histogram1.SetLineColor(kBlue)
    Histogram1.SetLineWidth(2)
    Histogram1.SetMinimum(1)

    Histogram2.SetLineColor(kRed)
    #Histogram2.SetLineStyle(kDashed)
    Histogram2.SetLineWidth(2)
    Histogram2.SetMinimum(1)

    #Signal Weight to Potentially Weight Signal More - Set to 1 for just S/sqrt(S+B)
    sigweight = 1
    nBins = 100
    binWidth = (rb-lb)/nBins
    signalvar = 4
    signalvarstr = str(signalvar)

    #nSigTotal = Tree.Draw(Variable+">>h1","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+">="+signalvarstr,"goff")
    #nBkgTotal = Tree.Draw(Variable+">>h2","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+"<"+signalvarstr,"goff")
    #nSigTotal = Tree.Draw(Variable+">>h1",CutString+TruthVariable+">="+signalvarstr,"goff")
    #nBkgTotal = Tree.Draw(Variable+">>h2",CutString+TruthVariable+"<"+signalvarstr,"goff")
    if CutString != "":
        #nSigTotal = Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr,"goff")
        #nBkgTotal = Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr,"goff")
        nSigTotal = Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr,"goff")
        nBkgTotal = Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr,"goff")
    else:
        #nSigTotal = Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr,"goff")
        #nBkgTotal = Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr,"goff")
        nSigTotal = Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr,"goff")
        nBkgTotal = Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr,"goff")

    nSigRetained = []
    nBkgRetained = []
    FOM = []

    for i in range(0,nBins):
        CUT = rb - i*binWidth
        #nSigRetained.append(Tree.Draw(Variable+">>h1","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        #nBkgRetained.append(Tree.Draw(Variable+">>h2","deltam < 0.1476 && deltam > 0.1434 && "+TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        if CutString != "":
            #nSigRetained.append(Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            #nBkgRetained.append(Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            nSigRetained.append(Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            nBkgRetained.append(Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        else:
            #nSigRetained.append(Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            #nBkgRetained.append(Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            nSigRetained.append(Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
            nBkgRetained.append(Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        #print math.sqrt((sigweight*nSigRetained[i])+nBkgRetained[i])
        #print nBkgRetained[i]
        #nSigRetained.append(Tree.Draw(Variable+">>h1",CutString+TruthVariable+">="+signalvarstr+" && "+Variable+"<%f"%CUT,"goff"))
        #nBkgRetained.append(Tree.Draw(Variable+">>h2",CutString+TruthVariable+"<"+signalvarstr+" && "+Variable+"<%f"%CUT,"goff"))
        if FoM=="std":
            denominator = math.sqrt((sigweight*nSigRetained[i])+nBkgRetained[i])
        if FoM=="punz":
            denominator = 5/2 + math.sqrt(nBkgRetained[i]) #Punzi Denominator
        # print(CUT)
        # print(nSigRetained)
        # print(nBkgRetained)
        # print(denominator)
        print(i)
        if denominator == 0:
            FOM.append(0)
        else:
            if FoM=="std":
                FOM.append((sigweight*nSigRetained[i])/(float(denominator)))
            if FoM=="punz":
                FOM.append((sigweight*nSigRetained[i])/(nSigTotal*float(denominator))) #Punzi FOM

    print("The maximal figure of merit is %.3f"%max(FOM))
    optimalIteration = FOM.index(max(FOM))
    optimalCut = rb-optimalIteration*binWidth
    print "This is attained for a cut of "+Variable+" < %.3f"%optimalCut
    effiRetainSIG = float(nSigRetained[optimalIteration])/nSigTotal
    effiRejectBKG = float(nBkgTotal - nBkgRetained[optimalIteration])/nBkgTotal
    print("Effi_rejectBKG = %.3f"%effiRejectBKG)
    print("Effi_retainSIG = %.3f"%effiRetainSIG)

    bottomBound = min(FOM)
    topBound = max(FOM)
    topBound+=int(float(topBound-bottomBound)/6+0.9)
    bottomBound-=int(float(topBound-bottomBound)/6+0.5)

    RESULT = "#splitline{Optimal Cut:}{%s < %.3f}"%(XTitle,optimalCut)
    tex1 = TLatex(0.72,0.15,RESULT)
    tex1.SetTextSize(0.1)
    tex1.SetNDC()

    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.02)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle("")
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.5)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.02)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.4)
    Frame.SetMinimum(1)

    #Tree.Draw(Variable+">>h1","deltam<0.1476 && deltam>0.1434 && "+TruthVariable+">="+signalvarstr)
    #Tree.Draw(Variable+">>h2","deltam<0.1476 && deltam>0.1434 && "+TruthVariable+"<"+signalvarstr)
    #Tree.Draw(Variable+">>h1",CutString+TruthVariable+">="+signalvarstr)
    #Tree.Draw(Variable+">>h2",CutString+TruthVariable+"<"+signalvarstr)
    if CutString != "":
        #Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+">="+signalvarstr)
        #Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+"<"+signalvarstr)
        Tree.Draw(Variable+">>h1",CutString+" && "+TruthVariable+"<="+signalvarstr)
        Tree.Draw(Variable+">>h2",CutString+" && "+TruthVariable+">"+signalvarstr)
    else:
        #Tree.Draw(Variable+">>h1",TruthVariable+">="+signalvarstr)
        #Tree.Draw(Variable+">>h2",TruthVariable+"<"+signalvarstr)
        Tree.Draw(Variable+">>h1",TruthVariable+"<="+signalvarstr)
        Tree.Draw(Variable+">>h2",TruthVariable+">"+signalvarstr)
    #Normalize histograms
    norm1 = h1.GetEntries()
    norm2 = h2.GetEntries()
    #print(norm1)
    #print(norm2)
    if norm1 != 0:
        h1.Scale(1/norm1)
    if norm2 != 0:
        h2.Scale(1/norm2)

    Frame.addTH1(Histogram1)
    Frame.addTH1(Histogram2)
    maxY = [Histogram1.GetMaximum(), Histogram2.GetMaximum()]
    minY = [Histogram1.GetMinimum(), Histogram2.GetMinimum()]
    topArrow = max(maxY)
    bottomArrow = min(minY)
    topArrow = int(2*float(topArrow)/10+0.5)
    bottomArrow += int(float(topArrow-bottomArrow)/10+0.5)
    a = TArrow(optimalCut,bottomArrow,optimalCut,topArrow,0.02,"<|")
    a.SetLineWidth(3)
    a.SetLineColor(kBlack)
    a.SetLineStyle(7)
    l = TLine(optimalCut, bottomBound, optimalCut, topBound)
    l.SetLineWidth(2)
    l.SetLineColor(kBlack)
    l.SetLineStyle(7)
    Frame.addObject(a)

    Histogram1.Draw()
    Histogram2.Draw()

    legendwidth = 0.25
    leg = TLegend(LegendLeftEdge,0.74,LegendLeftEdge+legendwidth,0.89)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    leg.AddEntry(Frame.findObject("h1"),"Normalized Signal","l")
    leg.AddEntry(Frame.findObject("h2"),"Normalized Background","l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    Frame.Draw()
    #c1.SetLogy(1)
    histPad.cd()
    histPad.Draw()
    #histPad.Draw()
    c1.Update()

    fomPad.cd()
    hFOM = TH1F("hFOM","hFOM",nBins,lb,rb)
    hFOM.SetLineColor(kBlack)
    for k in range(nBins):
        hFOM.SetBinContent(k+1,FOM[k])
    hFOM.Draw()

    Frame2.SetTitle("")
    Frame2.GetXaxis().CenterTitle(True)
    Frame2.GetXaxis().SetLabelOffset(0.03)
    Frame2.GetXaxis().SetLabelSize(0.07)
    Frame2.GetXaxis().SetTitle(XTitle)
    Frame2.GetXaxis().SetTitleSize(0.1)
    Frame2.GetXaxis().SetTitleOffset(1.7)
    Frame2.GetYaxis().CenterTitle(True)
    Frame2.GetYaxis().SetLabelOffset(0.01)
    Frame2.GetYaxis().SetLabelSize(0.05)
    if FoM=="std":
        Frame2.GetYaxis().SetTitle("#frac{S}{#sqrt{S+B}}")
    if FoM=="punz":
        Frame2.GetYaxis().SetTitle("#frac{S}{#frac{5}{2}+B}")
    Frame2.GetYaxis().SetTitleSize(0.1)
    Frame2.GetYaxis().SetTitleOffset(0.55)
    Frame2.SetMinimum(1)

    Frame2.addTH1(hFOM)
    Frame2.addObject(l)
    Frame2.addObject(tex1)
    Frame2.SetAxisRange(bottomBound,topBound,"Y")

    fomPad.SetTickx()
    fomPad.SetTicky()
    Frame2.SetStats(0)
    Frame2.Draw()
    fomPad.Draw()
    #histPad.cd()

    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")


def plot_roc(rb,lb,Tree,Variable,TruthVariable,CutString,Title,Frame,LegendLeftEdge,OutputFilename):
    c1 = TCanvas("c1","",1100,500)
    gPad.SetRightMargin(0.2)
    gPad.SetLeftMargin(0.15)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)

    sigweight = 1
    nBins = 100
    binWidth = (rb-lb)/nBins
    signalvar = 1
    signalvarstr = str(signalvar)

    nSigTotal = Tree.Draw(Variable+">>h1",CutString+TruthVariable+">="+signalvarstr,"goff")
    nBkgTotal = Tree.Draw(Variable+">>h2",CutString+TruthVariable+"<"+signalvarstr,"goff")

    nSigRetained = []
    nBkgRetained = []
    FOM = []

    sigeff = []
    sigeffvec = TVectorF(nBins)
    bkgdiff = []
    bkgdiffvec = TVectorF(nBins)

    for i in range(0,nBins):
        CUT = lb + i*binWidth
        #print(Tree.Draw(Variable,CutString+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))
        sigeff.append(float(Tree.Draw(Variable,CutString+TruthVariable+">="+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))/float(nSigTotal))
        #print(sigeff[i])
        bkgdeff = float(Tree.Draw(Variable,CutString+TruthVariable+"<"+signalvarstr+" && "+Variable+">%f"%CUT,"goff"))/float(nBkgTotal)
        bkgdiff.append(1 - bkgdeff)
        print("%s,%s"%(sigeff[i],bkgdiff[i]))

        sigeffvec[i] = sigeff[i]
        bkgdiffvec[i] = bkgdiff[i]


    Frame.SetTitle(Title)
    Frame.GetXaxis().CenterTitle(True)
    Frame.GetXaxis().SetLabelOffset(0.01)
    Frame.GetXaxis().SetLabelSize(0.05)
    Frame.GetXaxis().SetTitle("#epsilon_{S}")
    Frame.GetXaxis().SetTitleSize(0.05)
    Frame.GetXaxis().SetTitleOffset(1.2)
    Frame.GetYaxis().CenterTitle(True)
    Frame.GetYaxis().SetLabelOffset(0.01)
    Frame.GetYaxis().SetLabelSize(0.05)
    Frame.GetYaxis().SetTitle("1 - #epsilon_{B}")
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.2)
    Frame.SetAxisRange(0,1,"X")
    Frame.SetAxisRange(0,1.1,"Y")

    graph = TGraph(sigeffvec,bkgdiffvec)
    Frame.addObject(graph)

    graph.Draw()

    Frame.Draw()

    c1.Print(OutputFilename+".pdf")
    c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")

def plot_2d(Tree,Variable1,Variable2,Option1,Option2,Title,XTitle,YTitle,Histogram,Frame,LegendLeftEdge,OutputFilename):
    nBins = 100
    c1 = TCanvas("c1","",900,900)
    gPad.SetRightMargin(0.4)
    gPad.SetLeftMargin(0.2)
    gPad.SetRightMargin(0.05)
    gPad.SetBottomMargin(0.2)
    gStyle.SetTitleW(0.99)
    gStyle.SetOptStat(0)

    #Histogram.SetLineColor(kBlack)
    #Histogram.SetLineWidth(2)
    #Histogram.SetMinimum(1)

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
    Frame.GetYaxis().SetTitle(YTitle)
    Frame.GetYaxis().SetTitleSize(0.05)
    Frame.GetYaxis().SetTitleOffset(1.3)

    #nentries = Tree.Draw(Variable+">>h1",Option)
    #nentriesstr = str(nentries)
    #Draw(y:x)
    Tree.Draw(Variable2+":"+Variable1+">>h2",Option1,Option2)
    Frame.addObject(Histogram)

    cor = h2.GetCorrelationFactor()
    print("The Correlation Factor for %s and %s is %.5f"%(Variable2,Variable1,cor))

    legendwidth = 0.2
    leg = TLegend(LegendLeftEdge,0.74,LegendLeftEdge+legendwidth,0.89)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(kWhite)
    leg.SetTextSize(0.04)
    #leg.AddEntry(Frame.findObject("h1"),"Entries "+nentriesstr,"l")
    Frame.addObject(leg)

    #gStyle.SetOptStat("e");
    #gPad.SetLogy()
    #Frame.Draw()
    c1.Update()
    #c1.Print(OutputFilename+".pdf")
    #c1.Print(OutputFilename+".eps")
    c1.Print(OutputFilename+".png")

