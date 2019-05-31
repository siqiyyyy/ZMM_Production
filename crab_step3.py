#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZMM_CMSSW_10_5_0_hasPF_step3'
config.General.workArea = 'Crab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = False
config.JobType.psetName = 'step3.py'
config.JobType.sendPythonFolder = True
config.JobType.maxMemoryMB = 10000 #step2/3 turn out to use a lot
#config.JobType.maxJobRuntimeMin = 600 #Should not take too long
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.inputDBS = 'phys03'
#config.Data.inputDataset = '/ZMM/syuan-ZMM_CMSSW_10_5_0_step2-a42192373376869e7ab2e245b4ebe61d/USER'
#config.Data.outLFNDirBase = '/store/user/syuan/ZMM_UPGRADE'  
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
#config.Data.outputPrimaryDataset = 'ZMM'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality=True
#config.Site.whitelist = ["T3_US_FNALLPC"]

