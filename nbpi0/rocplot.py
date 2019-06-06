from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nonbcutdtokpi.root","READ")
t = f.Get("dsprecontree")

nb = RooRealVar("nb","nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
frame = nb.frame()
frame2 = nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_roc(rb,lb,t,"nb","whomi","deltam<0.149 && deltam>0.142 && ","From MC: ROC",frame,0.5,"/home/taylor/Research/plots/nbpi0/nomfrocplot")
