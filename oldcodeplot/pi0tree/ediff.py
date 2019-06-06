from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

ediff = RooRealVar("ediff","ediff",0,1)
nBins = 100
lb = ediff.getMin()
rb = ediff.getMax()
frame = ediff.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"ediff","","From MC: E_{#gamma_{1}} - E_{#gamma_{1}}","#DeltaE (GeV)",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/ediff")
