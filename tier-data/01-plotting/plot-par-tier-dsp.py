import matplotlib.pyplot as plt
import pygama.io.lh5 as lh5
import numpy as np

f_dsp = f'.lh5'

sto = lh5.Store()
tb_data = sto.read_object("/raw",f_dsp)

bl_all = tb_data[0]['bl'].nda
bins = np.linspace(10000, 20000, 10001)
 
plt.figure()
plt.hist(bl_all, bins=bins, density=True, histtype='step')
plt.xlabel("baseline mean")
plt.ylabel("event number")
plt.yscale("log")
plt.show()
