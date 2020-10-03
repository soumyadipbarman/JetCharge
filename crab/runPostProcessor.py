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

#preselection = "((HLT_PFJet60==1 && Jet_pt[0] > 81 ) || (HLT_PFJet80==1 && Jet_pt[0] > 103) || (HLT_PFJet140==1 && Jet_pt[0] > 191 ) || (HLT_PFJet200==1 && Jet_pt[0] > 258) || (HLT_PFJet260==1 && Jet_pt[0] > 333 ) || (HLT_PFJet320==1 && Jet_pt[0] > 363) || (HLT_PFJet400==1 && Jet_pt[0] > 458 ) || (HLT_PFJet450==1 && Jet_pt[0] > 493) || (HLT_PFJet500==1 && Jet_pt[0] > 580))"# || (HLT_PFJet550==1))"


#p=PostProcessor(".",files,"Jet_pt>400","keep_and_drop.txt", modules=[jmeCorrections2018C_DATA_AK4CHS(), jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())
#p=PostProcessor(".",files,"Jet_pt>30", modules=[jmeCorrections2018_MC_AK4CHS(), MCeventselectionTest()],)
#p=PostProcessor(".",inputFiles(),"Jet_pt>30","keep_and_drop.txt", modules=[jmeCorrections2018A_DATA_AK4CHS(), jetskimmer()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis())

## DATA ##
p=PostProcessor(".",inputFiles(),"Jet_pt>0","keep_and_drop.txt", modules=[jetskimmer()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_DATA.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis(),outputbranchsel='output_tree.txt')

## MC ##
#p=PostProcessor(".",inputFiles(),"Jet_pt>0","keep_and_drop.txt", modules=[jetskimmer()],provenance=True,fwkJobReport=True,histFileName= name +'-histOut_MC.root',histDirName="JetCharge_2017",haddFileName = name +'-trees.root',jsonInput=runsAndLumis(),outputbranchsel='output_tree.txt')

p.run()
print "Done"
#os.system("ls -lR")       
