from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root","READ")
t = f.Get("pi0tree")
#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#t = f.Get("dsprecontree")

gmthetacms = RooRealVar("gmthetacms","gmthetacms",0,3.14)
nBins=100
lb = gmthetacms.getMin()
rb = gmthetacms.getMax()
frame = gmthetacms.frame()
frame2 = gmthetacms.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

OptimizeCut_LessThan(rb,lb,t,"gmthetacms","whomi","","From MC: #theta_{#gamma_{1}#gamma_{2}} in the Center of Mass Frame","#theta_{#gamma_{1}#gamma_{2}}",h1,h2,frame,frame2,0.4,"/home/tkimmel/Research/plots/nbpi0/gmthetacms","std")
#OptimizeCut_LessThan(rb,lb,t,"gmthetacms","whoru","","From MC: #theta_{#gamma_{1}#gamma_{2}} in the Center of Mass Frame","#theta_{#gamma_{1}#gamma_{2}}",h1,h2,frame,frame2,0.4,"/home/tkimmel/Research/plots/alldtokpi/gmthetacms_bestCut_test","std")
