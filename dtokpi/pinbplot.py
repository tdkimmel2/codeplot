from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpiworking.root","READ")
t = f.Get("dsplrecontree")

nb = RooRealVar("nb","nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
frame = nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"nb","","From MC: #pi^{0} NeuroBayes Output","#pi^{0} NB",h1,frame,0.2,"/home/taylor/Research/plots/dtokpi/klpinbplot")
