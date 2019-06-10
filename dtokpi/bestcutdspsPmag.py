from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsprecontree")

dspPmag = RooRealVar("dspPmag","dspPmag",0,5)
nBins = 100
lb = dspPmag.getMin()
rb = dspPmag.getMax()
frame = dspPmag.frame()
frame2 = dspPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"dspPmag","mcflag","whomi>3","From All MC: Reconstructed D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,frame2,0.7,"/home/tkimmel/Research/plots/alldtokpi/bestdspsPmagcut","std")
#OptimizeCut_GreaterThan(rb,lb,t,"dspPmag","mcflag"," whomi>3","From All MC: Reconstructed D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/alldtokpi/bestdspsPmagcut","std")
