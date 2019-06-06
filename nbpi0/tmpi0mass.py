from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbpi0/nomfreconnb.root","READ")
t = f.Get("pi0tree")

pi0mass = RooRealVar("pi0mass","pi0mass",0.1158433,0.152761)
nBins = 100
lb = pi0mass.getMin()
rb = pi0mass.getMax()
frame = pi0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"pi0mass","whomi==1","Signal","whomi==0","Background","","Total","From MC:Truth Matched #pi^{0} Mass","#pi^{0} Mass (GeV/c^{2})",h1,h2,h3,frame,0.7,"/home/taylor/Research/plots/nbpi0/tmpi0mass")
