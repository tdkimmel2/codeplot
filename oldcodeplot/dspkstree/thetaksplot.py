from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dspkstree")

thetaks = RooRealVar("thetaks","thetaks",0,3.1415)
nBins = 100
lb = thetaks.getMin()
rb = thetaks.getMax()
frame = thetaks.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"thetaks","","From MC: #theta_{K^{0}_{S}}","#theta_{K^{0}_{S}}",h1,frame,0.65,"/home/taylor/Research/plots/dspkstree/thetaks")
