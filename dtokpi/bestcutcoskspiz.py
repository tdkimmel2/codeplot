from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/allmfrecon.root","READ")
t = f.Get("dsprecontree")

coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
nBins = 100
lb = coskpiz.getMin()
rb = coskpiz.getMax()
frame = coskpiz.frame()
frame2 = coskpiz.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"coskpiz","whomi","mcflag==1","From MC: cos(#theta_{K_{S}^{0}#pi^{0}}) D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","cos(#theta_{K_{S}^{0}#pi^{0}})",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/alldtokpi/coskspizcut","std")
