from ROOT import *
import sys
#sys.path.append('/home/tkimmel/Research/codeplot/functions/')
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/tkimmel/Research/root/genericmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
f = TFile("/home/taylor/Research/root/allmfrecon.root","READ")
t = f.Get("dsplrecontree")

R2 = RooRealVar("R2","R2",0,1)
nBins = 75
lb = R2.getMin()
rb = R2.getMax()
frame = R2.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(rb,lb,t,"R2","mcflag<3","Inclusive/Charm: ","mcflag==3 || mcflag==4","B Events: ","Truth Matched R2 D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC (No Cuts)","R2",h1,h2,frame,0.6,0.7,"/home/taylor/Research/plots/alldtokpi/tmlR2")
