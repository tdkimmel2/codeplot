from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("d0tree")

d0mass = RooRealVar("d0mass","d0mass",1.76,1.96)
nBins = 100
lb = d0mass.getMin()
rb = d0mass.getMax()
frame = d0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variableandtrue(t,"d0mass","","Total","whoru","From MC: D^{0} Mass","M_{D^{0}} (GeV/c^{2})",h1,h2,frame,0.65,"/home/taylor/Research/plots/d0tree/trued0mass")
