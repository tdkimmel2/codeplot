from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbpi0/nbrecon.root","READ")
t = f.Get("pi0tree")

nb = RooRealVar("nb","nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
frame = nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"nb","whoru==1","Truth Matched","whoru!=1","Background","From MC: #pi^{0} Neurobayes Output","NB Output",h1,h2,frame,0.5,"/home/taylor/Research/plots/nbpi0/nbtm")
