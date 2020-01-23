from ROOT import *

f1 = "/home/taylor/Research/root/mfpi0.root"
tree = "dsprecontree"
f = TFile(f1,"READ")
t = f.Get(tree)

whoru = RooRealVar("whoru", "whoru",0,1)
pi0p3 = RooRealVar("pi0p3", "pi0p3",0,3)
pi0p3cms = RooRealVar("pi0p3cms", "pi0p3cms",0,4)
gm1e = RooRealVar("gm1e", "gm1e",0,2)
gm2e = RooRealVar("gm2e", "gm2e",0,2)
gm1e925 = RooRealVar("gm1e925", "gm1e925",0,1)
gm2e925 = RooRealVar("gm2e925", "gm2e925",0,1)
ediff = RooRealVar("ediff", "ediff",0,1.5)
gm1eerror = RooRealVar("gm1eerror", "gm1eerror",0,0.002)
gm2eerror = RooRealVar("gm2eerror", "gm2eerror",0,0.002)
gm1p3 = RooRealVar("gm1p3", "gm1p3",0,2)
gm2p3 = RooRealVar("gm2p3", "gm2p3",0,2)
gm1p3cms = RooRealVar("gm1p3cms", "gm1p3cms",0,2.5)
gm2p3cms = RooRealVar("gm2p3cms", "gm2p3cms",0,2.5)
gmthetacms = RooRealVar("gmthetacms", "gmthetacms",0,3.14)
mfchi2 = RooRealVar("mfchi2", "mfchi2",0,50)

ROOT.TMVA.Tools.Instance()

# note that it seems to be mandatory to have an
# output file, just passing None to TMVA::Factory(..)
# does not work. Make sure you don't overwrite an
# existing file.
fout = ROOT.TFile("test.root","RECREATE")

factory = ROOT.TMVA.Factory("TMVAClassification", fout,
                            ":".join([
                                "!V",
                                "!Silent",
                                "Color",
                                "DrawProgressBar",
                                "Transformations=I;D;P;G,D",
                                "AnalysisType=Classification"]
                                     ))

factory.AddVariable("pi0p3","F")
factory.AddVariable("pi0p3cms","F")
factory.AddVariable("gm1e","F")
factory.AddVariable("gm2e","F")
factory.AddVariable("gm1e925","F")
factory.AddVariable("gm2e925","F")
factory.AddVariable("ediff","F")
factory.AddVariable("gm1eerror","F")
factory.AddVariable("gm2eerror","F")
factory.AddVariable("gm1p3","F")
factory.AddVariable("gm2p3","F")
factory.AddVariable("gm1p3cms","F")
factory.AddVariable("gm2p3cms","F")
factory.AddVariable("gmthetacms","F")
factory.AddVariable("mfchi2","F")

factory.AddSignalTree(t)
factory.AddBackgroundTree(t)

# cuts defining the signal and background sample
sigCut = ROOT.TCut("whoru==1")
bgCut = ROOT.TCut("whoru==0")

factory.PrepareTrainingAndTestTree(sigCut,   # signal events
                                   bgCut,    # background events
                                   ":".join([
                                        "nTrain_Signal=0",
                                        "nTrain_Background=0",
                                        "SplitMode=Random",
                                        "NormMode=NumEvents",
                                        "!V"
                                       ]))

method = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT",
                   ":".join([
                       "!H",
                       "!V",
                       "NTrees=850",
                       "nEventsMin=150",
                       "MaxDepth=3",
                       "BoostType=AdaBoost",
                       "AdaBoostBeta=0.5",
                       "SeparationType=GiniIndex",
                       "nCuts=20",
                       "PruneMethod=NoPruning",
                       ]))

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
