from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

pi0p3cms = RooRealVar("pi0p3cms","pi0p3cms",0,1)
nBins = 100
lb = pi0p3cms.getMin()
rb = pi0p3cms.getMax()
frame = gm1e.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"pi0p3cms","","From MC: #gamma_{1} Energy","E_{#gamma_{1}} (GeV)",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/pi0p3cms")
