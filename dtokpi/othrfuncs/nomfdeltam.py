from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nonbcutdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.139,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"deltam","","From MC: #DeltaM_{D^{*+}D^{+}} (D^{*+} -> D^{0} (-> K^{-} + #pi^{+}) + #pi^{+})","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,"/home/taylor/Research/plots/dtokpi/nomfdeltam")
