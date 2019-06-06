from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dspsmallset.root","READ")
t = f.Get("pi0tree")

gamma1e925 = RooRealVar("gamma1e925","gamma1e925",0.7,1)
nBins = 100
lb = gamma1e925.getMin()
rb = gamma1e925.getMax()
frame = gamma1e925.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gamma1e925","","From MC: E_{9}/E_{25}","E_{9}/E_{25}",h1,frame,0.2,"/home/taylor/Research/plots/pi0tree/gm1e925")
