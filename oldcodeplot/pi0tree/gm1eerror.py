from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

gm1eerror = RooRealVar("gm1eerror","gm1eerror",0,0.0001)
nBins = 100
lb = gm1eerror.getMin()
rb = gm1eerror.getMax()
frame = gm1eerror.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gm1eerror","","From MC: #gamma_{1} Energy Error","Error (GeV)",h1,frame,0.65,"/home/taylor/Research/plots/pi0tree/gm1eerror")
