import matplotlib.pyplot as plt
import pygama.lh5 as lh5
import numpy as np

f_raw = f'tier1.lh5'

sto = lh5.Store()
tb_data, n_rows = sto.read_object('/raw', f_raw, 30)

wfs_all = tb_data['waveform']['values'].nda
wf0 = wfs_all[0, :]
ts = np.arange(0, wf0.shape[0], 1)
plt.plot(ts[:], wf0[:])
plt.show()
