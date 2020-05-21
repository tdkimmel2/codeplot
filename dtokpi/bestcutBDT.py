from ROOT import *
import sys
#sys.path.append('/home/taylor/Research/codeplot/functions/')
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/taylor/Research/root/allmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/pi0training_BDT.root","READ")
t = f.Get("pi0tree")

mfchi2 = RooRealVar("mfchi2","mfchi2",0,1)
nBins = 100
lb = mfchi2.getMin()
rb = mfchi2.getMax()
frame = mfchi2.frame()
frame2 = mfchi2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#OptimizeCut_GreaterThan(rb,lb,t,"mfchi2","truthflag","","From Generic Charm MC: Mass Fit #Chi^{2}","#Chi^{2}",h1,h2,frame,frame2,0.7,"/home/taylor/Research/plots/alldtokpi/bestcutmfchi2","std")
OptimizeCut_GreaterThan(rb,lb,t,"mfchi2","truthflag","","From Generic Charm MC: Mass Fit #Chi^{2}","#Chi^{2}",h1,h2,frame,frame2,0.7,"/home/tkimmel/Research/plots/fastBDT/bestcutmfchi2","std")
