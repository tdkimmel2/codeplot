from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsplrecontree")

cosdpipcm = RooRealVar("cosdpipcm","cosdpipcm",0.75,1)
nBins = 100
lb = cosdpipcm.getMin()
rb = cosdpipcm.getMax()
frame = cosdpipcm.frame()
frame2 = cosdpipcm.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_GreaterThan(rb,lb,t,"cosdpipcm","whomi","","From MC: cos_{CM}(#theta_{D^{0}#pi^{+}}) D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}","cos_{CM}(#theta_{D^{0}#pi^{+}})",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/dtokpi/cosdlpipcmcut","std")
