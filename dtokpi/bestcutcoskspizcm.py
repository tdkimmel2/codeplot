from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsprecontree")

coskpizcm = RooRealVar("coskpizcm","coskpizcm",-1,1)
nBins = 100
lb = coskpizcm.getMin()
rb = coskpizcm.getMax()
frame = coskpizcm.frame()
frame2 = coskpizcm.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"coskpizcm","whomi","","From MC: cos_{CM}(#theta_{K_{S}^{0}#pi^{0}}) D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","cos_{CM}(#theta_{K_{S}^{0}#pi^{0}})",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/dtokpi/coskspizcmcut","std")
