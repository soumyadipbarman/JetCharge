#!/usr/bin/env python
#import FWCore.ParameterSet.Config as cms  # for local only
import os, sys
#import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
#from PhysicsTools.NanoAODTools.postprocessing.examples.skimmer import jetskimmer                        #local
from PhysicsTools.NanoAODTools.postprocessing.examples.skimmer import *                                  #crab
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

name= 'JetCharge_skimmer'

#UL2017_Custom_NanoAOD_JetHT
files=["root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017B-09Aug2019_UL2017-v1_PFNanoAOD/200716_075309/0000/nano106X_on_mini106X_2017_data_NANO_372.root"]
#files=["root://cms-xrd-global.cern.ch//store/user/algomez/PFNano/106x_v01/JetHT/Run2017D-09Aug2019_UL2017-v1_PFNanoAOD/200716_075602/0000/nano106X_on_mini106X_2017_data_NANO_163.root"]
#files=["root://cms-xrd-global.cern.ch//store/user/mmorris/PFNano/106x_v01/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/RunIISummer19UL17PFNanoAOD-106X_mc2017_realistic_v6_ext2-v2/200720_195938/0000/nano106X_on_mini106X_2017_mc_NANO_2.root"]
#local run
#p=PostProcessor(".",files, modules=[jetskimmer()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_DATA.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis())

p=PostProcessor(".",files, "Jet_pt>30","keep_and_drop.txt",modules=[jetskimmer()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_DATA.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis())
#p=PostProcessor(".",files,"Jet_pt>400","keep_and_drop.txt", modules=[jmeCorrections2018C_DATA_AK4CHS(), jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",files,"Jet_pt>30", modules=[jmeCorrections2018_MC_AK4CHS(), MCeventselectionTest()],)

#crab
#p=PostProcessor(".",inputFiles(),"Jet_pt>30","keep_and_drop.txt", modules=[jetskimmer()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_DATA.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis())

#p=PostProcessor(".",inputFiles(),"Jet_pt>30","keep_and_drop.txt", modules=[jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
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
#os.system("ls -lR")       # not needed for local run
