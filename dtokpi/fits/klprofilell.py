from ROOT import *

fInput = TFile("Workspace_allmfks54pinbcoskpizcosdpipcmpippdspPmagcutsbcs")
#fInput = TFile("Workspace_deltamklfit.root")
ws = fInput.Get("ws")

ws.Print()

ws.var("#mu_{sig}").setConstant(1)
ws.var("dm0").setConstant(1)
ws.var("a").setConstant(1)
ws.var("b").setConstant(1)
ws.var("d").setConstant(1)


#Setup ModelConfig to Obtain the PDF
model = RooStats.ModelConfig()
model.SetWorkspace(ws)
model.SetPdf("pdf")
pdf = model.GetPdf()

#Create Plain Likelihood
nll = pdf.createNLL(ws.data("data"),RooFit.NumCPU(2))
#Minimize likelihood w.r.t all parameters before plotting
RooMinuit(nll).migrad()
#Plot likelihood scan nsig or frac
nsig = ws.var("N_{Signal}")
frac = ws.var("frac")
frame1 = nsig.frame(RooFit.Bins(10),RooFit.Range(0.01,0.95),RooFit.Title("LL and ProfileLL in N_{Signal}"))
#frame1 = frac.frame(RooFit.Bins(50),RooFit.Range(0.01,0.95),RooFit.Title("LL and ProfileLL in #frac{S}{B}"))
#frame1 = nsig.frame(Bins(10),Range(0.01,0.95),Title(""))
nll.plotOn(frame1,RooFit.ShiftToZero())
#Plot likelihood in scan of Gaussian Sigma
sigma = ws.var("#sigma_{sig}")
frame2 = sigma.frame(RooFit.Bins(50),RooFit.Range(0.01,0.95),RooFit.Title("LL and ProfileLL in #sigma_{sig}"))
nll.plotOn(frame2,RooFit.ShiftToZero())

#Construct Profile Likelihood in nsig or frac
pll_nsig = nll.createProfile(RooArgSet(nsig))
#pll_frac = nll.createProfile(RooArgSet(frac))
#Plot the profile likelihood in nsig
pll_nsig.plotOn(frame1,RooFit.LineColor(kRed))
#pll_frac.plotOn(frame1,RooFit.LineColor(kRed))

#Adjust frame min and max to view better
frame1.SetMinimum(0)
frame1.SetMaximum(1)

#Construct Profile Likelihood in signal sigma
pll_sigma = nll.createProfile(RooArgSet(sigma))
#Plot the profile likelihood in nsig
pll_sigma.plotOn(frame2,RooFit.LineColor(kRed))

#Adjust frame min and max to view better
frame2.SetMinimum(0)
frame2.SetMaximum(1)

#Make canvas and draw RooPlots
c = TCanvas("profilell","profilell",1600,800)
c.Divide(2)
c.cd(1)
gPad.SetLeftMargin(0.15)
#frame1.GetYaxis().SetTitleOffset(2)
#frame1.GetXaxis().SetRange(0,3)
frame1.GetXaxis().SetLimits(0,0.06)
frame1.Draw()
c.cd(2)
gPad.SetLeftMargin(0.15)
#frame2.GetYaxis().SetTitleOffset(2)
#frame2.GetXaxis().SetRange(0,3)
frame2.GetXaxis().SetLimits(-0.01,0.015)
frame2.Draw()
c.Print("/home/tkimmel/Research/plots/profiletest.pdf")
c.Print("/home/tkimmel/Research/plots/profiletest.eps")
c.Print("/home/tkimmel/Research/plots/profiletest.png")
#c.Print("/home/taylor/Research/plots/fracklprofilelikelihood1var.pdf")
#c.Print("/home/taylor/Research/plots/fracklprofilelikelihood1var.eps")
#c.Print("/home/taylor/Research/plots/fracklprofilelikelihood1var.png")

del pll_nsig
#del pll_frac
del pll_sigma
del nll

#pll_frac.plotOn(frame1,LineColor(kRed)

"""
nsig = ws.var("N_{Signal}")
poi = RooArgSet(nsig)
nullParams = poi.snapshot()
nullParams.setRealValue("N_{Signal}",0.)

plc = RooStats.ProfileLikelihoodCalculator()

plc.SetData(ws.data("data"))
plc.SetModel(model)
plc.SetParameters(poi)
plc.SetNullParameters(nullParams)

htr = plc.GetHypoTest()

print "The p-value for the null is ", htr.NullPValue()
print "Corresponding to a significance of ", htr.Significance()

del plc
"""
