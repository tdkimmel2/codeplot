from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dspkstree")

coskspiz = RooRealVar("coskspiz","coskspiz",-1,1)
nBins = 100
lb = coskspiz.getMin()
rb = coskspiz.getMax()
frame = coskspiz.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable(t,"coskspiz","whoru==2","From MC: Truth Matched cos(#theta_{K^{0}_{S}#pi^{0}})","cos(#theta_{K^{0}_{S}#pi^{0}})",h1,frame,0.25,"/home/taylor/Research/plots/dspkstree/tmcoskspiz")
