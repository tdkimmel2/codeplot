from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dsprecontree")

dspmass = RooRealVar("dspmass","dspmass",1.9,3.0)
nBins = 100
lb = dspmass.getMin()
rb = dspmass.getMax()
frame = dspmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"dspmass","","From MC: D^{*+} Mass","M_{D^{*+}} (GeV/c^{2})",h1,frame,0.65,"/home/taylor/Research/plots/dsprecontree/dspmassnocuts")
