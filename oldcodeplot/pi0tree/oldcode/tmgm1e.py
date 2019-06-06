from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallset.root","READ")
t = f.Get("pi0tree")

gm1e = RooRealVar("gm1e","gm1e",0,1.5)
nBins = 100
lb = gm1e.getMin()
rb = gm1e.getMax()
frame = gm1e.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(t,"gm1e","whoru==1","Signal","whoru!=1","Background","","Total","From MC: #gamma_{1} Energy","E_{#gamma_{1}} (GeV)",h1,h2,h3,frame,0.65,"/home/taylor/Research/plots/pi0tree/tmgm1e")
