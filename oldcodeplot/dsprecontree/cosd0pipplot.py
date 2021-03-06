from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dsprecontree")

cosd0pip = RooRealVar("cosd0pip","cosd0pip",-1,1)
nBins = 100
lb = cosd0pip.getMin()
rb = cosd0pip.getMax()
frame = cosd0pip.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"cosd0pip","","From MC: cos(#theta_{D^{0}#pi^{+}})","cos(#theta_{D^{0}#pi^{+}})",h1,frame,0.25,"/home/taylor/Research/plots/dsprecontree/cosd0pip")
