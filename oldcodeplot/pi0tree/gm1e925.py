from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

gm1e925 = RooRealVar("gm1e925","gm1e925",0,1)
nBins = 100
lb = gm1e925.getMin()
rb = gm1e925.getMax()
frame = gm1e925.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gm1e925","","From MC: E_{9}/E_{25} of #gamma_{1}","E_{9}/E_{25}",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/gm1e925")
