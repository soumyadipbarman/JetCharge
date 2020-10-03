from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config # getUsernameFromSiteDB

config = Configuration()

config.section_("General")
config.General.requestName = 'JetHT_Run_UL2017B-v4'
config.General.workArea = 'crab_GJets'
config.General.transferLogs=True
config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.outputFiles = ['JetCharge_skimmer-trees.root','JetCharge_skimmer-histOut_DATA.root']
config.JobType.scriptExe = 'run_modules.sh'
config.JobType.inputFiles = ['PSet.py','run_modules.sh','run_modules_test.py','haddnano.py','keep_and_drop.txt'] #hadd nano will not be needed once nano tools are in cmssw
config.JobType.sendPythonFolder	 = True
config.section_("Data")
config.Data.inputDBS = 'phys03'
#config.Data.inputDBS = 'global'
config.Data.ignoreLocality = True
config.Data.inputDataset = '/JetHT/algomez-Run2017B-09Aug2019_UL2017-v1_PFNanoAOD-711e27fd71aadb4a77ae7e6321a59353/USER'
#config.Data.inputDataset = '/JetHT/algomez-Run2017C-09Aug2019_UL2017-v1_PFNanoAOD-711e27fd71aadb4a77ae7e6321a59353/USER'
#config.Data.inputDataset = '/JetHT/algomez-Run2017D-09Aug2019_UL2017-v1_PFNanoAOD-711e27fd71aadb4a77ae7e6321a59353/USER'
#config.Data.inputDataset = '/JetHT/algomez-Run2017E-09Aug2019_UL2017-v1_PFNanoAOD-711e27fd71aadb4a77ae7e6321a59353/USER'
#config.Data.inputDataset = '/JetHT/algomez-Run2017F-09Aug2019_UL2017-v1_PFNanoAOD-711e27fd71aadb4a77ae7e6321a59353/USER'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1 #25
#config.Data.totalUnits = 10
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
#config.Data.outLFNDirBase = '/store/user/%s/GJets' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/sobarman/'
config.Data.publication = False
config.Data.outputDatasetTag = 'JetCharge_NanoAOD_skimmer_JetHT_Run_UL2017B_DATA'
config.section_("Site")
config.Site.blacklist = ['T2_CH_CERN_HLT']#'T2_KR_KISTI']
config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH','T2_US_*','T3_CH_*','T2_CH_*','T1_US_FNAL','T2_CH_CSCS']#,'T3_US_FNALLPC','T3_CH_PSI']
#config.Site.ignoreGlobalBlacklist = True
config.Site.storageSite = "T2_IN_TIFR"
