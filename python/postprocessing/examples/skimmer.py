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

class Jetcharge_skimNANO(Module):
        #def __init__(self, jetSelection): #, jetSelection):       #crab                                       
        def __init__(self,EventLimit=-1):                          #local
                #self.jetSel = jetSelection  
		self.writeHistFile=True
                self.hltBranchName= "HLT"
		print "Running Jetcharge_skimNANO Module......"
                #pass

		#event counters
        	self.EventCounter = 0  
		self.EventLimit = EventLimit     #max events to be processed
		
		### Kinematics Cuts ###
        	self.minJetPt = 30.
        	self.maxJetEta = 2.4

		self.totalWeight = 1

        def beginJob(self, histFile, histDirName):
		Module.beginJob(self, histFile, histDirName)
		
		#ROOT.gSystem.Load("libPhysicsToolsNanoAODJMARTools.so")
	
		self.histotype = ['h_']
		
		for ihist, hist in enumerate(self.histotype):
		    self.addObject( ROOT.TH1F(hist + 'ngoodrecojet',            hist + 'ngoodrecojet',        8, 2, 10 ))
		    self.addObject( ROOT.TH1F(hist + 'goodrecojetpt',           hist + 'goodrecojetpt',        160, 400, 2000 ) )
		    self.addObject( ROOT.TH1F(hist + 'goodrecojeteta',          hist + 'goodrecojeteta',        100, -1.5, 1.5 ) )
		    self.addObject( ROOT.TH1F(hist + 'goodrecojetphi',          hist + 'goodrecojetphi',        100, -3.0, 3.0 ) )
		    
		    self.addObject( ROOT.TH1F(hist + 'goodrecojetpt1',           hist + 'goodrecojetpt1',        160, 400, 2000 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojeteta1',          hist + 'goodrecojeteta1',        100, -2.5, 2.5 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojetphi1',          hist + 'goodrecojetphi1',        100, -3.0, 3.0 ) )

                    self.addObject( ROOT.TH1F(hist + 'goodrecojetpt2',           hist + 'goodrecojetpt2',        160, 400, 2000 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojeteta2',          hist + 'goodrecojeteta2',        100, -2.5, 2.5 ) )
                    self.addObject( ROOT.TH1F(hist + 'goodrecojetphi2',          hist + 'goodrecojetphi2',        100, -3.0, 3.0 ) )
		   
		    self.addObject( ROOT.TH1F(hist + 'nrecoChgCands',            hist + 'nrecoChgCands',        199, 1, 200) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgpt',           hist + 'jetchgpt',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgeta',          hist + 'jetchgeta',        100, -1.5, 1.5 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgphi',          hist + 'jetchgphi',        100, -3.0, 3.0 ) )

		    self.addObject( ROOT.TH1F(hist + 'nrecoChgCands1',            hist + 'nrecoChgCands1',        199, 1, 200) )
		    self.addObject( ROOT.TH1F(hist + 'jetchgpt1',           hist + 'jetchgpt1',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgeta1',          hist + 'jetchgeta1',        100, -1.5, 1.5 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgphi1',          hist + 'jetchgphi1',        100, -3.0, 3.0 ) )

		    self.addObject( ROOT.TH1F(hist + 'nrecoChgCands2',            hist + 'nrecoChgCands2',        199, 1, 200) )
            	    self.addObject( ROOT.TH1F(hist + 'jetchgpt2',           hist + 'jetchgpt2',        200, 20, 2020 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgeta2',          hist + 'jetchgeta2',        100, -1.5, 1.5 ) )
                    self.addObject( ROOT.TH1F(hist + 'jetchgphi2',          hist + 'jetchgphi2',        100, -3.0, 3.0 ) )

		    self.addObject( ROOT.TH1F(hist + 'nrecoCands1',            hist + 'nrecoCands1',        199, 1, 200) )
		    self.addObject( ROOT.TH1F(hist + 'nrecoCands2',            hist + 'nrecoCands2',        199, 1, 200) )

                    self.addObject( ROOT.TH1F(hist + 'jetcharge1',           hist + 'jetcharge1',        20, -1.0, 1.0 ) )
		    self.addObject( ROOT.TH1F(hist + 'jetcharge2',           hist + 'jetcharge2',        20, -1.0, 1.0 ) )

		    self.addObject( ROOT.TH2F(hist + 'mult_leadjet1',           hist + 'mult_leadjet1',        160,400,2000,50,10,60 ) )
		    self.addObject( ROOT.TH2F(hist + 'mult_leadjet2',           hist + 'mult_leadjet2',        160,400,2000,50,10,60 ) )

	
		#self.h_recopt=ROOT.TH1F('recopt',   'recopt',   100, 0, 1000)
        	#self.addObject(self.h_recopt)
                  
        def endJob(self):
		Module.endJob(self)
                pass
        def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                self.out = wrappedOutputTree
		self.out.branch("nrecojet", "I")
		self.out.branch("rawjetpt", "F")
		self.out.branch("rawjeteta", "F")
		self.out.branch("rawjetphi", "F")  
		#self.out.branch()  
		pass
        def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
                pass      
	def analyze(self, event):
		"""process event, return True (go to next module) or False (fail, go to next event)"""
	        #Event counters, max events to be processed for local running of jobs
		current_time = datetime.datetime.now()
                self.EventCounter +=1

		print'Number of Events processed :', self.EventCounter, 'at', current_time, 'CEST'
     		
		if self.EventCounter > self.EventLimit > -1:
                	return False
		
		###### Get list of reco jets #######
        	# List of reco jets:
        	allrecojets = list(Collection(event, "Jet"))
        	allrecoparts = list(Collection(event, "JetPFCands"))
		#wtft = list(Collection(event, "genWeight"))

		hlt = Object(event, self.hltBranchName)
	
		#trigobj = ["hlt.PFJet40", "hlt.PFJet60", "hlt.PFJet80", "hlt.PFJet140", "hlt.PFJet200", "hlt.PFJet260", "hlt.PFJet320", "hlt.PFJet400","hlt.PFJet450", "hlt.PFJet500", "hlt.PFJet550"]	

		#recojets = []	
		recojet_count = []
		recoChgCands_count = []
		recoChgCands1_count = []
		recoChgCands2_count = []
		
		recoCands1_count = []
		recoCands2_count = []

		Q1 = 0.0
		jet1pt = 0.0
		jetcharge1 = 0.0
		
		Q2 = 0.0
                jet2pt = 0.0
                jetcharge2 = 0.0

		multiplicity1 = 0
		mult1 = 0
		leadjet1 = 0.0

		multiplicity2 = 0
                mult2 = 0
                leadjet2 = 0.0

		# All the charged particles within jets		
		pfcharged = [x for x in allrecoparts] # if (x.charge != 0)]
		
		# For constituents inside jets
		pfCandsVec = ROOT.vector("TLorentzVector")()
		pfCandsChg = []
		for p in pfcharged :
                	pfCandsVec.push_back( ROOT.TLorentzVector( p.p4().Px(), p.p4().Py(), p.p4().Pz(), p.p4().E()) )
			#pfCandsChg.push_back(p)
			pfCandsChg.append(p)

		### applying basic selection to jets
                recojets = [ x for x in allrecojets if x.p4().Perp() > self.minJetPt and abs(x.p4().Eta()) < self.maxJetEta and x.jetId>=2 ]  # recheck JETID criteria
                recojets.sort(key=lambda x:x.p4().Perp(),reverse=True)

		#event selection
		# Trigger
	        if(hlt.PFJet40==1 or hlt.PFJet60==1 or hlt.PFJet80==1 or hlt.PFJet140==1 or hlt.PFJet200==1 or hlt.PFJet260==1 or hlt.PFJet320==1 or hlt.PFJet400==1 or hlt.PFJet450==1 or hlt.PFJet500==1 or hlt.PFJet550==1):
			# select events with at least 2 jets
			#if len(recojets) >= 2:
			if ((len(recojets) >= 2) and (recojets[0].p4().Perp() > 400 and abs(recojets[0].p4().Eta()) < 1.5)  and (recojets[1].p4().Perp() > 100 and abs(recojets[1].p4().Eta()) < 1.5)):
				#print "Dijet Event Selection..."
				for irecojet,recojet in enumerate(recojets):
					#print "Start Jet Loop..."
					recojet_count.append((irecojet,recojet))
					#recojetscands[irecojet] = {}
					# Cluster only the particles near the appropriate jet to save time
                    			#constituents = ROOT.vector("TLorentzVector")()
					constituents = []
					for ipfCandsVec,ipfCandsChg in zip(pfCandsVec,pfCandsChg) :
						#print "PF Loop..."
                				if abs(recojet.p4().DeltaR( ipfCandsVec )) < 0.4: # and x.charge:
							#print "Select Particles within cone 0.4..."
                    					#constituents.push_back( ROOT.TLorentzVector( x.p4().Px(), x.p4().Py(), x.p4().Pz(), x.p4().E()) )
							constituents.append(ipfCandsChg)
							#recocands4v = ROOT.TLorentzVector()
							#recocands4v = [ x for x in constituents ]
					#if (irecojet == 0):
							#print "First jet with only charged particles..."
					for irecocands,recocands in enumerate(constituents):
						if (recocands.p4().Perp() > 1):
							if (recocands.charge != 0):
								recoChgCands_count.append((irecocands,recocands))
								self.h_jetchgpt.Fill(recocands.p4().Perp(), self.totalWeight)
                                                                self.h_jetchgeta.Fill(recocands.p4().Eta(), self.totalWeight)
                                                                self.h_jetchgphi.Fill(recocands.p4().Phi(), self.totalWeight)
								if (irecojet == 0):
									recoChgCands1_count.append((irecocands,recocands))
									self.h_jetchgpt1.Fill(recocands.p4().Perp(), self.totalWeight)
                                                                	self.h_jetchgeta1.Fill(recocands.p4().Eta(), self.totalWeight)
                                                                	self.h_jetchgphi1.Fill(recocands.p4().Phi(), self.totalWeight)
									irecocands += 1
									#mult1 += (multiplicity1)
									#leadjet1 += (recocands.p4().Perp())#, self.totalWeight)
									self.h_mult_leadjet1.Fill(recojet.p4().Perp(), irecocands, self.totalWeight)
								if (irecojet == 1):
                                                                        recoChgCands2_count.append((irecocands,recocands))
                                                                        self.h_jetchgpt2.Fill(recocands.p4().Perp(), self.totalWeight)
                                                                        self.h_jetchgeta2.Fill(recocands.p4().Eta(), self.totalWeight)
                                                                        self.h_jetchgphi2.Fill(recocands.p4().Phi(), self.totalWeight)
								        irecocands += 1
                                                                        #mult2 += (multiplicity2)
                                                                        #leadjet2 += (recocands.p4().Perp())#, self.totalWeight)
                                                                        self.h_mult_leadjet2.Fill(recojet.p4().Perp(), irecocands, self.totalWeight)
							if (irecojet == 0):
								recoCands1_count.append((irecocands,recocands))
								Q1 += (1.0)*(recocands.charge)*(pow((recocands.p4().Perp()),1.0))
                                                        	jet1pt += pow(recojet.p4().Perp(),1.0)                                                                        
								jetcharge1 += (1.0)*(Q1/jet1pt)
								self.h_jetcharge1.Fill(jetcharge1, self.totalWeight)
							if (irecojet == 1):
                                                                recoCands2_count.append((irecocands,recocands))
                                                                Q2 += (1.0)*(recocands.charge)*(pow((recocands.p4().Perp()),1.0))
                                                                jet2pt += pow(recojet.p4().Perp(),1.0)
                                                                jetcharge2 += (1.0)*(Q2/jet2pt)
                                                                self.h_jetcharge2.Fill(jetcharge2, self.totalWeight)
								#print "Basic Distibutions using charged particles inside first Jet..."

					self.out.fillBranch("rawjetpt", recojet.p4().Perp())
	                		self.out.fillBranch("rawjeteta", recojet.p4().Eta())
        	        		self.out.fillBranch("rawjetphi", recojet.p4().Phi())
					self.h_goodrecojetpt.Fill(recojet.p4().Perp(), self.totalWeight)
	                		self.h_goodrecojeteta.Fill(recojet.p4().Eta(), self.totalWeight)
                			self.h_goodrecojetphi.Fill(recojet.p4().Phi(), self.totalWeight)
					if (irecojet == 0):
						self.h_goodrecojetpt1.Fill(recojet.p4().Perp(), self.totalWeight)
				                self.h_goodrecojeteta1.Fill(recojet.p4().Eta(), self.totalWeight)
                				self.h_goodrecojetphi1.Fill(recojet.p4().Phi(), self.totalWeight)
					if (irecojet == 1):
						self.h_goodrecojetpt2.Fill(recojet.p4().Perp(), self.totalWeight)
                                                self.h_goodrecojeteta2.Fill(recojet.p4().Eta(), self.totalWeight)
                                                self.h_goodrecojetphi2.Fill(recojet.p4().Phi(), self.totalWeight)

							
		jet_sel = len(recojet_count)
		recoChgCands_sel = len(recoChgCands_count)
		recoChgCands1_sel = len(recoChgCands1_count)
		recoChgCands2_sel = len(recoChgCands2_count)
	        recoCands1_sel = len(recoCands1_count)
		recoCands2_sel = len(recoCands2_count)

		self.out.fillBranch("nrecojet",jet_sel)
		self.h_ngoodrecojet.Fill(jet_sel, self.totalWeight)
		self.h_nrecoChgCands.Fill(recoChgCands_sel, self.totalWeight)
		self.h_nrecoChgCands1.Fill(recoChgCands1_sel, self.totalWeight)
		self.h_nrecoChgCands2.Fill(recoChgCands2_sel, self.totalWeight)
		self.h_nrecoCands1.Fill(recoCands1_sel, self.totalWeight)
                self.h_nrecoCands2.Fill(recoCands2_sel, self.totalWeight)

				
		#print "Return True"
		return True


	#print "Number of jets :" + str(xyz)
#print "Ok Done :"(jetsel)
#printer = Jetcharge_skimNANO()
#print printer.__init()__
#printer = Jetcharge_skimNANO()
#printer.analyze()

	#def printer(self):
		#return self.jetsel
#epson = Jetcharge_skimNANO()
#epson.printer()

#if __name__ == "__main__":
#	if analyze():
#		print "ElectronID_presel:", jetsel

#print(Module.event)

"""
preselection="Jet_pt[0] > 400"
files=["root://cmsxrootd.fnal.gov//store/data/Run2017B/JetHT/NANOAOD/Nano25Oct2019-v1/40000/F444480C-9D10-4041-9F8E-A67CF1D98368.root"]
p=PostProcessor(".",files,cut=preselection,branchsel=None,modules=[Jetcharge_skimNANO()],noOut=True,histFileName="histOut.root",histDirName="jets13")
p.run()
"""

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

#jetskimmer = lambda : Jetcharge_skimNANO(jetSelection= lambda j : j.pt > 30)
jetskimmer = lambda : Jetcharge_skimNANO()


