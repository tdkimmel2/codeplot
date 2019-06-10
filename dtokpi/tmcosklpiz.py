from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsplrecontree")

coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
nBins = 75
lb = coskpiz.getMin()
rb = coskpiz.getMax()
frame = coskpiz.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Charm MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/tkimmel/Research/plots/dtokpigeneric/tmklcoskpiz")
plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Mixed MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/tkimmel/Research/plots/dtokpimixed/tmklcoskpiz")
plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Charged MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/tkimmel/Research/plots/dtokpicharged/tmklcoskpiz")
plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From UDS MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/tkimmel/Research/plots/dtokpiuds/tmklcoskpiz")
#plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==2","Tight TM","whomi>0 && mcflag==2","Loose TM","mcflag==2","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Charm MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/taylor/Research/plots/dtokpigeneric/tmklcoskpiz")
#plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==3","Tight TM","whomi>0 && mcflag==3","Loose TM","mcflag==3","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Mixed MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/taylor/Research/plots/dtokpimixed/tmklcoskpiz")
#plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==4","Tight TM","whomi>0 && mcflag==4","Loose TM","mcflag==4","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Charged MC","cos(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/taylor/Research/plots/dtokpicharged/tmklcoskpiz")
#plot_variable3histos(rb,lb,t,"coskpiz","whomi>3 && mcflag==5","Tight TM","whomi>0 && mcflag==5","Loose TM","mcflag==5","Total","Truth Matched cos(#theta_{K_{L}^{0}#pi^{0}})  D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From UDS MC","cos_{CM}(#theta_{K_{L}^{0}#pi^{0}})",h1,h2,h3,frame,0.2,0.6,"/home/taylor/Research/plots/dtokpiuds/tmklcoskpiz")
