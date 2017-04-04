#file path will be:
#outLFNDirBase/outputPrimaryDataset/outputDatasetTag/time_tag/...
#if no outputPrimaryDataset specify, will use "CRAB_PrivateMC" instead
#if no outputDatasetTag specify, will use requestName instead
from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True
config.General.requestName = 'Gen_20151124'
config.General.workArea = 'crab_projects'
config.JobType.psetName = 'testPythia8D0kpi_onlyDstar_py_GEN_SIM_PU.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['testPythia8D0kpi_onlyDstar_py_GEN_SIM_PU.root']
#config.Data.inputDataset = ''
config.Data.totalUnits = 10
config.Data.unitsPerJob = 10
config.Data.splitting = 'EventBased'
config.Data.outLFNDirBase = '/store/user/twang/testSpace/20151124_test1'
config.Data.outputPrimaryDataset = 'Pythia8_5020GeV_DstarD0kpi_755patch3_GEN_SIM_PU_20151120'
config.Data.publication = True
#config.Data.outputDatasetTag = 'someTag'
config.Site.storageSite = 'T2_US_MIT'
config.Site.whitelist = ['T2_US_MIT']
