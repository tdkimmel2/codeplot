from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

gm1theta = RooRealVar("gm1theta","gm1theta",0,1)
nBins = 100
lb = gm1theta.getMin()
rb = gm1theta.getMax()
frame = gm1theta.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(t,"gm1theta","whoru==1","Signal","whoru!=1","Background","","Total","From MC: #gamma_{1} Energy","E_{#gamma_{1}} (GeV)",h1,h2,h3,frame,0.65,"/home/taylor/Research/plots/pi0tree/tmgm1theta")
