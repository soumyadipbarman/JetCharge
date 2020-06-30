#!/usr/bin/env python
import FWCore.ParameterSet.Config as cms
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
#from Analysis.JetCharge.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
#from PhysicsTools.NanoAODTools.postprocessing.examples.skimmer import jetskimmer                        #local
#from PhysicsTools.NanoAODTools.postprocessing.examples.skimmer import *                                  #crab
from Analysis.JetCharge.postprocessing.examples.skimmer import jetskimmer
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *


#files=["root://cms-xrd-global.cern.ch//store/data/Run2018B/EGamma/NANOAOD/Nano25Oct2019-v1/60000/C61D3EFD-DC56-7F41-B028-39F3FA070B13.root"]
files=["root://cmsxrootd.fnal.gov//store/data/Run2017B/JetHT/NANOAOD/Nano25Oct2019-v1/40000/F444480C-9D10-4041-9F8E-A67CF1D98368.root"]

#local run
p=PostProcessor(".",files,"Jet_pt>30", modules=[jetskimmer()])
#p=PostProcessor(".",files,"Jet_pt>400","keep_and_drop.txt", modules=[jmeCorrections2018C_DATA_AK4CHS(), jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",files,"Jet_pt>30", modules=[jmeCorrections2018_MC_AK4CHS(), MCeventselectionTest()],)

#crab
#p=PostProcessor(".",inputFiles(),"Jet_pt>30","keep_and_drop.txt", modules=[jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",inputFiles(),"Jet_pt>30", modules=[jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",inputFiles(),"Jet_pt>30","keep_and_drop.txt", modules=[jmeCorrections2018A_DATA_AK4CHS(), jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())

"""
p = PostProcessor(
    '.', (inputFiles() if not args.iFile else [args.iFile]),
    cut=cuts,
    modules=listOfModules,
    provenance=True,
    haddFileName = "nano_postprocessed.root",
    histFileName = "histograms.root",
    histDirName = 'tthbb13',
    jsonInput=runsAndLumis(),
    prefetch=True,
    longTermCache=True,
)
"""
p.run()
print "Done"
os.system("ls -lR")       # not needed for local run
