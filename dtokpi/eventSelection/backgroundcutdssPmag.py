from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t = f.Get("dsrecontree")
#t = f.Get("dstree")

dsPmag = RooRealVar("dsPmag","dsPmag",0,7)
nBins = 100
lb = dsPmag.getMin()
rb = dsPmag.getMax()
frame = dsPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

##############TESTING###############
#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.55,"/home/tkimmel/Research/plots/test",0.90)

#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.6,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_noBackgroundCut_100Sensitivity",100)
#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.55,"/home/tkimmel/Research/plots/alldtokpi/ks_noBackgroundCut_100Sensitivity",100)

#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.6,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_noBackgroundCut_99Purity",0.99)
#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1 && deltam > 0.1422863 && deltam < 0.1490903","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.6,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_noBackgroundCut_deltamWindow1stPass_98Purity",0.98)
NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1 && deltam > 0.1423971 && deltam < 0.1489743","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|#vec{p_{D*}}| (GeV/c)",h1,h2,frame,0.6,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_noBackgroundCut_deltamWindow2ndPass_99Purity",0.99)

#NoBackgroundCut_GreaterThan(rb,lb,t,"dsPmag","mcflag","abs(dsflag)==1","From All Generic MC: Reconstructed D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi","|p_{D*}| (GeV/c)",h1,h2,frame,0.55,"/home/tkimmel/Research/plots/alldtokpi/ks_noBackgroundCut_98Purity",0.98)
