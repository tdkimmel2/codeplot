from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

mfchi2 = RooRealVar("mfchi2","mfchi2",0,20)

nBins = 100
lb = mfchi2.getMin()
rb = mfchi2.getMax()
frame = mfchi2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"mfchi2","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Mass Fit #Chi^{2}","#Chi^{2}",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/mfchi2")
