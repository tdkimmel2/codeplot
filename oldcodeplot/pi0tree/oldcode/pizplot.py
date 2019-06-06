from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dspsmallset.root","READ")
t = f.Get("pi0tree")

pi0mass = RooRealVar("pi0mass","pi0mass",0.035,0.235)
nBins = 100
lb = pi0mass.getMin()
rb = pi0mass.getMax()
frame = pi0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"pi0mass","","From MC: #pi^{0} Mass","M_{#pi^{0}} (GeV/c^{2})",h1,frame,0.2,"/home/taylor/Research/plots/pi0tree/pi0mass")
