from ROOT import *
import ROOT
import array

#f = TFile("/home/taylor/Research/codeplot/tmvapi0/test.root","READ")
f = TFile("/home/taylor/Research/codeplot/tmvapi0/PyMVAOutput.root","READ")
t = f.Get("dataset").Get("TestTree")
#t = f.Get("dataset").Get("TrainTree")

"""
reader = ROOT.TMVA.Reader()

var1 = array.array('f',[0]) ; reader.AddVariable("pi0p3",var1)
var2 = array.array('f',[0]) ; reader.AddVariable("pi0p3cms",var2)
var3 = array.array('f',[0]) ; reader.AddVariable("gm1e",var3)
var4 = array.array('f',[0]) ; reader.AddVariable("gm2e",var4)
var5 = array.array('f',[0]) ; reader.AddVariable("gm1e925",var5)
var6 = array.array('f',[0]) ; reader.AddVariable("gm2e925",var6)
var7 = array.array('f',[0]) ; reader.AddVariable("ediff",var7)
var8 = array.array('f',[0]) ; reader.AddVariable("gm1eerror",var8)
var9 = array.array('f',[0]) ; reader.AddVariable("gm2eerror",var9)
var10 = array.array('f',[0]) ; reader.AddVariable("gm1p3cms",var10)
var11 = array.array('f',[0]) ; reader.AddVariable("gm2p3cms",var11)
var12 = array.array('f',[0]) ; reader.AddVariable("gmthetacms",var12)
var13 = array.array('f',[0]) ; reader.AddVariable("mfchi2",var13)

reader.BookMVA("BDT","weights/TMVAClassification_BDT.weights.xml")

# create a new 2D histogram with fine binning
histo2 = ROOT.TH2F("histo2","",200,-5,5,200,-5,5)

gcSaver = []
# loop over the bins of a 2D histogram
for i in range(1,histo2.GetNbinsX() + 1):
    for j in range(1,histo2.GetNbinsY() + 1):

        # find the bin center coordinates
        var1[0] = histo2.GetXaxis().GetBinCenter(i)
        var2[0] = histo2.GetYaxis().GetBinCenter(j)

        # calculate the value of the classifier
        # function at the given coordinate
        bdtOutput = reader.EvaluateMVA("BDT")

        # set the bin content equal to the classifier output
        histo2.SetBinContent(i,j,bdtOutput)

gcSaver.append(ROOT.TCanvas())
histo2.Draw("colz")

# draw sigma contours around means
for mean, color in (
    ((1,1), ROOT.kRed), # signal
    ((-1,-1), ROOT.kBlue), # background
    ):

    # draw contours at 1 and 2 sigmas
    for numSigmas in (1,2):
        circle = ROOT.TEllipse(mean[0], mean[1], numSigmas)
        circle.SetFillStyle(0)
        circle.SetLineColor(color)
        circle.SetLineWidth(2)
        circle.Draw()
        gcSaver.append(circle)

ROOT.gPad.Modified()

# Prevent Canvases from closing
print("Close the ROOT window via File -> Close!")
ROOT.gApplication.Run()
"""

# fill histograms for signal and background from the test sample tree
t.Draw("PyKeras>>hSig(22,-0,1)","classID == 0","goff")  # signal
t.Draw("PyKeras>>hBg(22,-0,1)","classID == 1", "goff")  # background
t.Draw("GTB>>hSig2(22,-0,1)","classID == 0","goff")  # signal
t.Draw("GTB>>hBg2(22,-0,1)","classID == 1", "goff")  # background

ROOT.hSig.SetLineColor(ROOT.kBlue); ROOT.hSig.SetLineWidth(2)  # signal histogram
ROOT.hBg.SetLineColor(ROOT.kRed); ROOT.hBg.SetLineWidth(2)   # background histogram
ROOT.hSig2.SetLineColor(ROOT.kCyan); ROOT.hSig2.SetLineWidth(2)  # signal histogram
ROOT.hBg2.SetLineColor(ROOT.kOrange); ROOT.hBg2.SetLineWidth(2)   # background histogram

# use a THStack to show both histograms
hs = ROOT.THStack("hs","")
hs.Add(ROOT.hSig)
hs.Add(ROOT.hBg)
hs.Add(ROOT.hSig2)
hs.Add(ROOT.hBg2)

# show the histograms
gcSaver = []
gcSaver.append(ROOT.TCanvas())
hs.Draw()

# Prevent Canvases from closing
print("Close the ROOT window via File -> Close!")
ROOT.gApplication.Run()
