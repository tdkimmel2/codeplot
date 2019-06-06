from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dsprecontree")

deltam2 = RooRealVar("deltam2","deltam2",0.2,0.8)
nBins = 100
lb = deltam2.getMin()
rb = deltam2.getMax()
frame = deltam2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"deltam2","","From MC: #DeltaM^{2}_{D^{*+}D^{0}} No Cuts","#DeltaM^{2}_{D^{*+}D^{0}} (GeV^{2}/c^{4})",h1,frame,0.15,"/home/taylor/Research/plots/dsprecontree/deltam2nocuts")
