from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/inclusivemfreconnb.root","READ")
t = f.Get("dsprecontree")

dnb = RooRealVar("dnb","dnb",-1,1)
nBins = 100
lb = dnb.getMin()
rb = dnb.getMax()
frame = dnb.frame()
frame2 = dnb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"dnb","whomi","","From MC: D^{*+} NeuroBayes Output D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","dnb",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/bestcutdnb","std")
