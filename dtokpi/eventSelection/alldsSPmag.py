from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t = f.Get("dsrecontree")
#t = f.Get("dstree")

dsPmag = RooRealVar("dsPmag","dsPmag",0,7)

#magCut = 3.3
#dsPmag = RooRealVar("dsPmag","dsPmag",magCut,7)


nBins = 100
lb = dsPmag.getMin()
rb = dsPmag.getMax()
frame = dsPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)
h5 = TH1F("h5","h5",nBins,lb,rb)


#######################dsrecontree########################
plot_variable2histos(t,"dsPmag","mcflag==2 && abs(dsflag)==1","Charm","mcflag!=2 && mcflag !=5 && abs(dsflag)==1","B","D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|p_{D*}| (GeV/c)",h1,h2,frame,0.55,0.6,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_alldsSPmag_2Histos_TM")
#plot_variable(t,"dsPmag","mcflag==2 && abs(dsflag)==1 && dsPmag>%s"%(str(magCut)),"D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|p_{D*}| (GeV/c)",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/alldtokpi/ksRecon_alldsSPmag_%sCut"%(str(magCut)))

#######################dstree########################
#plot_variable2histos(t,"dsPmag","mcflag==2 && whomi==1","Charm","mcflag!=2 && mcflag !=5 && whomi==1","B","D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi+: From All Generic MC","|p_{D*}| (GeV/c)",h1,h2,frame,0.55,0.6,"/home/tkimmel/Research/plots/alldtokpi/ks_alldsSPmag_2Histos_TM")
#plot_variable(t,"dsPmag","mcflag==2 && whomi==1 && dsPmag>%s"%(str(magCut)),"D* 3-Momentum Magnitude D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi+: From All Generic MC","|p_{D*}| (GeV/c)",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/alldtokpi/ks_alldsSPmag_TM_%sCut"%(str(magCut)))
