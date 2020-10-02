from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root","READ")
t = f.Get("pi0tree")

mfchi2 = RooRealVar("mfchi2","mfchi2",0,10)
nBins=100
lb = mfchi2.getMin()
rb = mfchi2.getMax()
frame = mfchi2.frame()
frame2 = mfchi2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_LessThan(rb,lb,t,"mfchi2","whomi","","From MC: #pi^{0} Mass Fit #Chi^{2}","#Chi^{2}",h1,h2,frame,frame2,0.4,"/home/tkimmel/Research/plots/nbpi0/mfchi2_10","std")
