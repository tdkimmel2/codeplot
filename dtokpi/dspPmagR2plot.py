from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/allmfrecon.root","READ")
t = f.Get("dsprecontree")

R2 = RooRealVar("R2","R2",0,1)
dspPmag = RooRealVar("dspPmag","dspPmag",0,7)
nBins = 100
lb = R2.getMin()
rb = R2.getMax()
ub = dspPmag.getMax()
bb = dspPmag.getMin()
frame = R2.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

#plot_2d(t,"R2","dspPmag","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dspPmagR2")
#plot_2d(t,"R2","dspPmag","whomi>3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmdspPmagR2")
#plot_2d(t,"R2","dspPmag","mcflag>2","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/BudsdspPmagR2")
plot_2d(t,"R2","dspPmag","mcflag==3 || mcflag==4","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/BdspPmagR2")
#plot_2d(t,"R2","dspPmag","(mcflag==3 || mcflag==4) && whomi>3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmBdspPmagR2")
#plot_2d(t,"R2","dspPmag","mcflag>2 && whomi>3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmBudsdspPmagR2")
#plot_2d(t,"R2","dspPmag","mcflag<3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/charmdspPmagR2")
#plot_2d(t,"R2","dspPmag","mcflag<3 && whomi>3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmcharmdspPmagR2")
