from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfrecon.root","READ")
t = f.Get("kltree")

klz = RooRealVar("klz","klz",-1,1)
nBins = 100
lb = 0
rb = 180
frame = klz.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"acos(klz)*180/3.14159","","From MC: D^{*+} Mass","M_{D^{*+}} (GeV/c^{2})",h1,frame,0.65,"/home/taylor/Research/plots/dtokpi/acosnz")
