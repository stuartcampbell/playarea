import mantid
from mantid.simpleapi import StartLiveData
import os

# setup to spoof the live data service
mantid.kernel.ConfigService.setString('default.facility', 'TEST_LIVE')
mantid.kernel.ConfigService.setString('fileeventdatalistener.filename',
                                      '/SNS/PG3/IPTS-15653/0/28380/preNeXus/PG3_28380_neutron_event.dat')
mantid.kernel.ConfigService.setString('fileeventdatalistener.chunks', '200')

# various script files
script_dir = '/home/scu/code/mantidproject/scratch/live-testing'  # REPLACE WITH SCRIPT LOCATIONS
proc_script = os.path.join(script_dir, 'reduce_ADARA_LIVE_proc.py')
post_script = os.path.join(script_dir, 'reduce_ADARA_LIVE_postproc.py')

StartLiveData(FromNow=False,
              FromStartOfRun=True,
              UpdateEvery=1,  # in seconds
              Instrument='ADARA_FileReader',
              ProcessingScriptFilename=proc_script,
              PostProcessingScriptFilename=post_script,
              PreserveEvents=True,
              AccumulationMethod='Replace',
              AccumulationWorkspace='livedata_chunks',
              OutputWorkspace='livedata')

