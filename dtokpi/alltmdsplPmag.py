from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsplrecontree")

dspPmag = RooRealVar("dspPmag","dspPmag",0,5)
nBins = 100
lb = dspPmag.getMin()
rb = dspPmag.getMax()
frame = dspPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)

plot_variable4histos(rb,lb,t,"dspPmag","mcflag==2 && whomi > 3","Charm MC","mcflag==3 && whomi > 3","Mixed MC","mcflag==4 && whomi > 3","Charged MC","mcflag==5 && whomi > 3","UDS MC","Truth-Matched Reconstructed D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,frame,0.65,0.6,"/home/tkimmel/Research/plots/alldtokpi/alltmdsplPmag")
#plot_variable4histos(rb,lb,t,"dspPmag","mcflag==2 && whomi > 3","Charm MC","mcflag==3 && whomi > 3","Mixed MC","mcflag==4 && whomi > 3","Charged MC","mcflag==5 && whomi > 3","UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,frame,0.65,0.6,"/home/taylor/Research/plots/alldtokpi/alltmdsplPmag")
