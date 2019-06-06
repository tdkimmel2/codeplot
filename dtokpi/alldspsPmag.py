from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsprecontree")

dspPmag = RooRealVar("dspPmag","dspPmag",0,5)
nBins = 100
lb = dspPmag.getMin()
rb = dspPmag.getMax()
frame = dspPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable3histos(rb,lb,t,"dspPmag","mcflag==1","Inclusive MC","mcflag==2","Generic MC","mcflag==3","Mixed MC","Reconstructed D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,frame,0.65,0.6,"/home/taylor/Research/plots/alldspsPmag")
