from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfrecon.root","READ")
t = f.Get("kltree")

flayer = RooRealVar("flayer","flayer",0,30)
layers = RooRealVar("layers","layers",0,16)
nBins = 100
#lb = flayer.getMin()
#rb = flayer.getMax()
lb = layers.getMin()
rb = layers.getMax()
#frame = flayer.frame()
frame = layers.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"layers","whoru==1","Signal","whoru==0","Background","","Total","From MC:Truth Matched K^{0}_{L} Number of Layers Hit in KLM","Layers Hit",h1,h2,h3,frame,0.7,0.5,"/home/taylor/Research/plots/kltree/tmlayers")
