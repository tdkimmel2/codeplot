from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dspkstree")

deltam2 = RooRealVar("deltam2","deltam2",0.2,0.8)
nBins = 100
lb = deltam2.getMin()
rb = deltam2.getMax()
frame = deltam2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variableandtrue(t,"deltam2","","Total","whoru","From MC: Truth Matched #DeltaM^{2}_{D^{*+}D^{0}}","#DeltaM^{2}_{D^{*+}D^{0}} (GeV^{2}/c^{4})",h1,h2,frame,0.65,"/home/taylor/Research/plots/dspkstree/tmdeltam2")
