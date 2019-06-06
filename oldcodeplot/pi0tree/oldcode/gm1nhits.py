from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dspsmallset.root","READ")
t = f.Get("pi0tree")

gamma1nhits = RooRealVar("gamma1nhits","gamma1nhits",0,25)
nBins = 100
lb = gamma1nhits.getMin()
rb = gamma1nhits.getMax()
frame = gamma1nhits.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gamma1nhits","","From MC: #gamma_{1} Number of Hits","Number of Hits",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/gm1nhits")
