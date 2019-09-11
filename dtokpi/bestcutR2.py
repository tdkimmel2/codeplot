from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/allmfrecon.root","READ")
#t = f.Get("dsprecontree")
t = f.Get("dsplrecontree")

R2 = RooRealVar("R2","R2",0,1)
nBins = 100
lb = R2.getMin()
rb = R2.getMax()
frame = R2.frame()
frame2 = R2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"R2","mcflag","","From MC: R2 D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","R2",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/alldtokpi/bestcutR2","std")
