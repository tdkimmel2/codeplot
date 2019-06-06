from ROOT import *

fInput = TFile("Workspace_deltamksfit.root")
ws = fInput.Get("ws")

ws.Print()

#ws.var("#mu_{sig}").setConstant(1)

model = RooStats.ModelConfig()
model.SetWorkspace(ws)
model.SetPdf("pdf")

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
