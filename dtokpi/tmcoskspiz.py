from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsprecontree")

coskpizcm = RooRealVar("coskpizcm","coskpizcm",-1,1)
nBins = 75
lb = coskpizcm.getMin()
rb = coskpizcm.getMax()
frame = coskpizcm.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"coskpizcm","whomi>3","Tight TM","whomi>0","Loose TM","","Total","Truth Matched cos_{CM}(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From MC","cos_{CM}(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/taylor/Research/plots/dtokpi/tmkscoskpizcm")
