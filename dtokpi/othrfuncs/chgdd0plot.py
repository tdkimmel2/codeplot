from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfrecon.root","READ")
t = f.Get("dsptree")

d0mass = RooRealVar("d0mass","d0mass",1.84,1.89)
nBins = 100
lb = d0mass.getMin()
rb = d0mass.getMax()
frame = d0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"d0mass","","From MC: D^{0} -> K^{-} #pi^{+} Mass","M_{D^{0}} (GeV/c^{2})",h1,frame,0.65,"/home/taylor/Research/plots/dtokpi/chrgdd0mass")
