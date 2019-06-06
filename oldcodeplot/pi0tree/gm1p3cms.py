from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

gm1p3cms = RooRealVar("gm1p3cms","gm1p3cms",0,1)
nBins = 100
lb = gm1p3cms.getMin()
rb = gm1p3cms.getMax()
frame = gm1e.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gm1p3cms","","From MC: #gamma_{1} Energy","E_{#gamma_{1}} (GeV)",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/gm1p3cms")
