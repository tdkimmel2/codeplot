from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/nbvars.root","READ")
t = f.Get("pi0tree")

gmthetacms = RooRealVar("gmthetacms","gmthetacms",0,3.14)

nBins = 100
lb = gmthetacms.getMin()
rb = gmthetacms.getMax()
frame = gmthetacms.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"gmthetacms","whomi==1","Signal","whomi!=1","Background","From All Generic MC: Angle Between Photons in the CMS Frame","#theta_{#gamma_{1}#gamma_{2}}^{CMS}",h1,h2,frame,0.59,0.66,"/home/tkimmel/Research/plots/nbpi0/nbvars/gmthetacms")
