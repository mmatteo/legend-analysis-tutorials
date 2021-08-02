# Processing the Data for dev branch (2021/08/02)

The conversion of fcio daq files into raw is currently done by the pygama
function `process_flashcam` which is defined in:

https://github.com/legend-exp/pygama/blob/dev/pygama/io/daq_to_raw.py

The conversion of daq into dsp files is done by the pygama function `raw_to_dsp`
that is defined in:

https://github.com/legend-exp/pygama/blob/dev/pygama/io/raw_to_dsp.py

The config file parsed to `raw_to_dsp` is described in the `build_dsp` tutorial.

For convenience, an python script providing an interface to these two functions
is attached to this tutorial.  
