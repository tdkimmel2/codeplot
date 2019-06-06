from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsplrecontree")

pipp = RooRealVar("pipp","pipp",0,1)
nBins = 100
lb = pipp.getMin()
rb = pipp.getMax()
frame = pipp.frame()
frame2 = pipp.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_LessThan(rb,lb,t,"pipp","whomi","","From MC: #pi^{+} Momentum D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}","|p_{#pi^{+}}|",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/dtokpi/pippklcut","std")
