from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbkl/mfreconnb.root","READ")
t = f.Get("kltree")

nb = RooRealVar("nb","nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
frame = nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"nb","","From MC: K^{0}_{L} NeuroBayes Output","NB",h1,frame,0.65,"/home/taylor/Research/plots/kltree/NB")
