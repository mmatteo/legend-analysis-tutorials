## Raw Waveform

In a new notebook we can start having a look at LEGEND data. Let's start by plotting a
waveform, the code for doing this is given below:

```py
import matplotlib.pyplot as plt
import pygama.lh5 as lh5
import numpy as np

f_raw = f'tier1.lh5'

sto = lh5.Store()

wfs_all = sto.read_object('/raw/waveform/values', f_raw, 30)[0].nda
wf0 = wfs_all[0, :]
ts = np.arange(0, wf0.shape[0], 1)
plt.plot(ts[:], wf0[:])
plt.show()
```

The `f_raw` line specifies the file we want to work on. To start with let's change it to
`f'/unix/legend/testenv-v02/ref-prod/master/data/prod/raw/V04199A/tier1/th_HS2_lat_psa/th_HS2_lat_psa/char_data-V04199A-th_HS2_lat_psa-run0001-200825T140003_tier1.lh5'`,
although any file in that folder will work.  Then run the code with `Shift+Enter` to plot
your first waveform! You can look at other waveforms by changing the 0 in the `wf0` line
to other numbers. 2 and 3 give a nice example of pileup events.

This method works but is a bit clunky. A better way of viewing waveforms using pygama's
waveform browser can be found
[here](https://github.com/legend-exp/pygama/blob/master/tutorials/WaveformBrowserTutorial.ipynb)

## Looking at DSP data

The data at LEGEND is processed in tiers. The waveform we just plotted was in the `raw` tier
while the next tier up is `dsp`. Here various parameters have been extracted from the data.
To start with we shall plot one of them which is the mean of the baseline. In the notebook
we can do:

```py
import matplotlib.pyplot as plt
import pygama.lh5 as lh5
import numpy as np

f_dsp = f'/unix/legend/testenv-v02/ref-prod/master/data/prod/dsp/V04199A/tier1/th_HS2_lat_psa/th_HS2_lat_psa/char_data-V04199A-th_HS2_lat_psa-run0001-200825T140003_tier1.lh5'

bl = lh5.load_nda(f_dsp, ['bl'], "/raw")['bl']

plt.figure()
plt.hist(bl, bins=1000, density=True, histtype='step')
plt.xlabel("baseline mean")
plt.ylabel("Frequency")
plt.yscale("log")
plt.show()
```

This should return a histogram of the baseline mean.  Here a different method of loading
the data is used. This is the `lh5.load_nda` function which is less versatile and will only work
for data tables, this is fine for the `dsp` data but you would run into problems if you use
the same function to try to load the `raw` waveforms.
There are many other parameters we can plot in this data set. Two others are the standard
deviation of the baseline and the energy. To do this change `'bl_mean'` to either
`'bl_sig'` or `'trapEmax'`, alternatively the `lh5.load_nda` function can also load lists of
parameters and will return the array of their values as a dictionary. You will also have
to change the bins for the histogram in the `bins` line. For the energy try start and end
points of 0 and 60000 and for the standard deviation 0 and 12500.
