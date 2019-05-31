#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZMM_CMSSW_10_5_0_hasPF_step2'
config.General.workArea = 'Crab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'
config.JobType.sendPythonFolder = True
config.JobType.maxMemoryMB = 10000 #step2 turn out to use a lot
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/ZMM/syuan-ZMM_step1_new-01b325d492eb745aa9f7609172ddfa01/USER'
config.Data.outLFNDirBase = '/store/user/syuan/ZMM_UPGRADE'  
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
#config.Data.lumiMask = ''

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality=True
#config.Site.whitelist = ["T3_US*"]

