#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZMM_CMSSW_10_5_0_hasPF_step123test'
config.General.workArea = '.'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['step2.py','step3.py','step2.pkl','step3.pkl']
config.JobType.psetName = 'step1.py' #For job splitting, will be renamed as PSet.py
config.JobType.scriptExe = 'runtest.sh'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['log_step0.txt','log_step2.txt','log_step3.txt','step2.root','step3.root']
config.JobType.sendPythonFolder = True
config.JobType.maxMemoryMB = 10000 #step2 turn out to use a lot
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10 #number of events per jobs
config.Data.totalUnits = 20 #number of event
config.Data.outLFNDirBase = '/store/user/syuan/ZMM_UPGRADE'  
config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName
config.Data.outputPrimaryDataset = 'ZMM'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality=True
#config.Site.whitelist = ["T3_US_Baylor","T2_US_Nebraska"] #sites where the PU samples are stored for efficiency

