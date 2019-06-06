from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dsprecontree")

dspmass = RooRealVar("dspmass","dspmass",1.9,2.1)
nBins = 100
lb = dspmass.getMin()
rb = dspmass.getMax()
frame = dspmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h2",nBins,lb,rb)

#Plot dspmass with a 5 sigma mass cut on d0mass
plot_variable3histos(t,"dspmass","cosd0pip>0.6","cos(#theta_{D^{0}#pi^{+}} > 0.6)","cosd0pip>0.8","cos(#theta_{D^{0}#pi^{+}} > 0.8)","","No Cut","From MC: D^{*+} Mass with cos(#theta_{D^{0}#pi^{+}}) > 0.6","M_{D^{*+}} (GeV/c^{2})",h1,h2,h3,frame,0.25,"/home/taylor/Research/plots/dsprecontree/cosd0pipcutdspmass")
