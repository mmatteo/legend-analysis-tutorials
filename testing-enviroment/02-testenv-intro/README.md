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

To exit this and return to the normal shell simply type:
`deactivate`.

## Raw Waveform

Now in the virtual environment we can work on the data. To do this simply enter:
`ipython`
to start an ipython instance. This has the same functionality as a jupyter notebook where we can
enter a block of code and then run using shift + enter. This can be exited using `exit()`.

But for now let's instead start by plotting a waveform, the code for doing this is given below:

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
Then run the code with shift+enter to make your first waveform! You can look at other waveforms by changing the 0 in the `wf0` line to other numbers. 2 and 3 give a nice example of pileup events.

## Looking at dsp data

The data at LEGEND is processed in tiers. The waveform we just plotted was in the raw tier while the next tier up is dsp. Here various parameters have been extracted from the data. To start with we shall plot one of them which is the mean of the baseline. The do this follow the same steps as above to enter an ipython ennvironment then run the code below:

```
import matplotlib.pyplot as plt
import pygama.io.lh5 as lh5
import numpy as np

f_dsp = f'/unix/legend/testenv-v02/ref-prod/master/data/prod/dsp/V04199A/tier1/th_HS2_lat_psa/th_HS2_lat_psa/char_data-V04199A-th_HS2_lat_psa-run0001-200825T140003_tier1.lh5'

sto = lh5.Store()
tb_data = sto.read_object("/raw",f_dsp)

bl_all = tb_data[0]['bl'].nda
bins = np.linspace(10000, 20000, 10001)
 
plt.figure()
plt.hist(bl_all, bins=bins, density=True, histtype='step')
plt.xlabel("baseline mean")
plt.ylabel("Frequency")
plt.yscale("log")
plt.show()
```
This should return a histogram of the baseline mean. There are 2 other parameters we can plot in this data set these are the standard deviation of the baseline and the Energy. To do this change the `'bl'` in the `bl_all` line to either `'bl_sig'` or `'trapEmax'`. You will also have to change the bins for the histogram in the `bins` line. For the energy try start and end points of 0 and 60000 and for the standard deviation 0 and 12500.
