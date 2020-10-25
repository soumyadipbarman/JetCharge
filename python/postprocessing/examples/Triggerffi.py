#!/usr/bin/env python

#import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from importlib import import_module
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.tools import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer

import math as m
import array
import numpy as np
import random
import copy
import datetime


class TriggerAnalysis(Module):
    def __init__(self,EventLimit=-1):
        """ Initialization for the module 
        """
	
	#event counters
        self.EventCounter = 0
        self.EventLimit = EventLimit     #max events to be processed

        self.writeHistFile = True
        self.trigTurnonList = {
            'HLT_PFJet40':'HLT_PFJet60',
            'HLT_PFJet60':'HLT_PFJet80',
            'HLT_PFJet80':'HLT_PFJet140',
            'HLT_PFJet140':'HLT_PFJet200',            
            'HLT_PFJet200':'HLT_PFJet260',
            'HLT_PFJet260':'HLT_PFJet320',
            'HLT_PFJet320':'HLT_PFJet400',
            'HLT_PFJet400':'HLT_PFJet450',
            'HLT_PFJet450':'HLT_PFJet500',      
            'HLT_PFJet500':'HLT_PFJet550',
            }

	self.triggerpaths = [HLT_PFJet40,
            		     HLT_PFJet60,
            		     HLT_PFJet80,
            		     HLT_PFJet140,
                             HLT_PFJet200,
			     HLT_PFJet260,
                             HLT_PFJet320,
			     HLT_PFJet400,
                             HLT_PFJet450,
			     HLT_PFJet500,
                             HLT_PFJet550]


	self.triggerprescale = [237260,123000,237300,2400,600,148,59,21,12,1,1]
        
    def beginJob(self, histFile, histDirName):
        """Book control histograms and the predictions for the background.
        The background is data-driven and estimated by weighting the 1-tag region
        by the mistag rate to extrapolate to the 2-tag region. 
        """
        Module.beginJob(self, histFile, histDirName)
        for itrig,jtrig in zip(self.triggerpaths,self.triggerprescale):
            self.addObject (ROOT.TH1F('h_ak4pt_' + itrig,                     'h_ak4pt_' + itrig,   5, 0, 1000) )
            self.addObject (ROOT.TH1F('h_ak4pt_' + itrig + '_eff_' + jtrig,   'h_ak4pt_' + jtrig,   5, 0, 1000) )
            
    def endJob(self):
        Module.endJob(self)
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """Perform either the anti-tag and probe (mistag estimate) or double tag (signal region) selection.
        """

	#Event counters, max events to be processed for local running of jobs
        current_time = datetime.datetime.now()
        self.EventCounter +=1

        print'Number of Events processed :', self.EventCounter, 'at', current_time, 'CEST'

        if self.EventCounter > self.EventLimit > -1:
        	return False

        #weight = 1.0
        # Select the jets that satisfy jet ID and mass requirements. 
        ak4_pt = [ event.Jet_pt[i] for i in xrange(event.nJet) if (event.Jet_pt[i] > 30) and event.Jet_jetId[i]>=2 and abs(event.Jet_eta[i]) < 2.4 ]
        if len(ak4_pt) < 2 :
            return False

        # Calculate HT. Get it from the event if it is there, otherwise calculate on the fly. 
        lead_pt = 0.0
        if hasattr( event, "Jet_pt"):
            lead_pt = event.Jet_pt[0]
        #else :
        #    for i in xrange( event.nJet ) :
        #        lead_pt = event.Jet_pt[0]

        # Calculate the trigger turnons. 
        #for itrig,jtrig in self.trigTurnonList.iteritems():
        #    if getattr( event, itrig ) == 1: 
        #        getattr(self, 'h_ak4pt_'+itrig).Fill( lead_pt, weight )
        #        if getattr( event, jtrig ) == 1: 
        #            getattr(self, 'h_ak4pt_'+ itrig + '_eff_' + jtrig).Fill( lead_pt, weight )

	for itrig,jtrig in zip(self.triggerpaths,self.triggerprescale):
		if (itrig == 1):
			Fill(lead_pt, jtrig)
		Fil(lead_pt, weight)
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

Jettrigger = lambda : TriggerAnalysis() 
