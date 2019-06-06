from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbpi0/recon.root","READ")
t = f.Get("pi0tree")

phi = RooRealVar("phi","phi",0,3.15)
nBins = 100
lb = phi.getMin()
rb = phi.getMax()
frame = phi.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"phi","whoru==1","Signal","whoru==0","Background","","Total","From MC:Truth Matched K^{0}_{L} #phi","#phi (Rad)",h1,h2,h3,frame,0.7,"/home/taylor/Research/plots/kltree/tmphi")
