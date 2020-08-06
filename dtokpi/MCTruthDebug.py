from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/taylor/Research/root/k0signalmfrecon.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#D*+: 413
#D0: 421
#nb: 0.854

plot_variable(t,"deltam","pizmtrID!=421 && pizgmaID!=413","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC Grandmother of #pi^{0} is Not a D^{*+} and Mother of #pi^{0} is Not a D^{0}","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/MCDebug/piznotfromd0ordsp")
