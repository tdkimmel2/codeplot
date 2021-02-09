from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfreconKstree.root","READ")
t = f.Get("kstree")

ksmass = RooRealVar("ksmass","ksmass",0.490,0.506)
nBins = 100
lb = ksmass.getMin()
rb = ksmass.getMax()
frame = ksmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)
h5 = TH1F("h5","h5",nBins,lb,rb)

plot_variable5histos(rb,lb,t,"ksmass","mcflag==1","Inclusive MC","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","M_{K_{S}^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All Generic MC","M_{K_{S}^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.6,0.6,"/home/tkimmel/Research/plots/kstree/allksmass")
#plot_variable5histos(rb,lb,t,"ksmass","mcflag==1 && whoru==1","Inclusive MC","mcflag==2 && whoru==1","Charm MC","mcflag==3 && whoru==1","Mixed MC","mcflag==4 && whoru==1","Charged MC","mcflag==5 && whoru==1","UDS MC","M_{K_{S}^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All Generic MC","M_{K_{S}^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.65,0.6,"/home/tkimmel/Research/plots/kstree/alltmksmass")
