# Intoduction to the Test Environment

## Setting Up

First log in to the server

`ssh pc204`

then navigate to the test env

`cd /unix/legend/testenv-v02`

You will then need to source the config file using:

`source setup.sh`

Navigate to a production cycle:

`cd ref-prod/master`

Finally make a shell within the virtual environment and load all the software using:

`testenv-bash.sh config.json`

(venv) should appear at the start of your command line.

## Working on the data 

Now in the virtual environment we can work on the data. To do this simply enter:
`ipython`
to start an ipython instance. This has the same functionality as a jupyter notebook where we can
enter a block of code and then run using shift + enter.  

Let's start by plotting a waveform, the code for doing this is given below:

```
import matplotlib.pyplot as plt
import pygama.io.lh5 as lh5
import numpy as np

f_raw = f'tier1.lh5'

sto = lh5.Store()
tb_data, n_rows = sto.read_object('/raw', f_raw,30)

wfs_all = tb_data['waveform']['values'].nda
wf0 = wfs_all[0, :]
ts = np.arange(0, wf0.shape[0], 1)
plt.plot(ts[:], wf0[:])
plt.show()
```
The `f_raw` line specifies the file we want to work on. To start with let's change it to 
`f'/unix/legend/testenv-v02/ref-prod/master/data/prod/raw/V04199A/tier1/th_HS2_lat_psa/th_HS2_lat_psa/char_data-V04199A-th_HS2_lat_psa-run0001-200825T140003_tier1.lh5' `
although any file in that folder will work.
Then run the code with shift+enter to make your first waveform!
