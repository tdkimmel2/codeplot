from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/expert.root","READ")
#f = TFile("/home/taylor/Research/root/expert.root","READ")
t = f.Get("experttree")

nn = RooRealVar("nn","nn",-1,1)
nBins = 100
lb = nn.getMin()
rb = nn.getMax()
frame = nn.frame()
frame2 = nn.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#OptimizeCut_GreaterThan(rb,lb,t,"nn","truth","","From MC: #pi^{0} Neurobayes Output","NB Output",h1,h2,frame,frame2,0.4,"/home/tkimmel/Research/plots/nbpi0/mfsig13vars","std")
OptimizeCut_GreaterThan(rb,lb,t,"nn","truth","","From MC: #pi^{0} Neurobayes Output","NB Output",h1,h2,frame,frame2,0.4,"/home/tkimmel/Research/plots/nbpi0/klsigMC/mfsig10vars","std")
#OptimizeCut_GreaterThan(rb,lb,t,"nn","truth","","From MC: #pi^{0} Neurobayes Output","NB Output",h1,h2,frame,frame2,0.4,"/home/taylor/Research/plots/nbpi0/nogmPcut","std")
