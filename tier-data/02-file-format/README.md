# LH5 – the LEGEND custom HDF5 data format

In the previous section we looked at loading data and used two functions:
`lh5.read_object` and `lh5.load_nda`. We need to use these functions as all
data in LEGEND is stored in the [LH5 (LGDO)
format](https://legend-exp.github.io/legend-data-format-specs), based on
[HDF5](https://www.hdfgroup.org/solutions/hdf5/). This allows us to store large
amounts of data in single files and access just the data we want without having
to load all of it (This is especially handy for raw data where 1000 of
waveforms are in the file but we might only want to see a few without having to
load all of them in memory). This section goes into more depth on the functions
we can use to look at LH5 data.

### Raw LH5 files

This type of file containers a mix of data types. `stat` contains various info
about the processing e.g cputime etc. `raw` contains the data for each waveform.
All the parameters are shown below:

```console
raw.lh5
├── stat
└── raw
     ├── baseline    # FPGA-estimated baseline
     ├── channel     # right now, index of the trigger (trace)
     ├── energy      # FPGA-estimated energy
     ├── ievt        # index of event
     ├── numtraces   # number of triggered FADC channels
     ├── packet_id   # packet index in file
     ├── timestamp   # time since beginning of file
     ├── tracelist   # list of triggered FADC channels
     ├── waveform    # digitizer data
     │   ├── dt      # sampling period (ns) - 16
     │   ├── t0
     │   └── values  # array holding the waveform samples FADC units
     ├── wf_max      # ultra-simple np.max energy estimation
     └── wf_std      # ultra-simple np.std noise estimation

```

### DSP LH5 files

This file is generally a table as each waveform has only one value. This will
change if you output parameters with other datatypes such as the `'wf_trap'`.
`dsp_info` contains various info about the processing e.g pygama version etc.
An example is shown below:

```console
dps.lh5
├── dsp_info
└── raw
     ├──  bl
     ├──  bl_sig
     └──  trapEmax
```

## Interacting with LH5 files

The pygama module that implements dedicated routines to work with LH5 files is
`pygama.lh5`. For ease of use initialise the store class with `sto =
lh5.Store()`.

```py
import pygama.lh5 as lh5
sto = lh5.Store()
```

### Browsing, getting info

The most important utility functions are:

- `lh5.Store.ls(lh5_file, lh5_group_path='')` works like the UNIX `ls`
  command. It can be used to find what is in the file. For example on the raw
  file we can run `sto.ls(your_file, 'raw/waveform/')` to output the parameters
  within waveform: `dt`,`t0` and `values`.

- `lh5.Store.read_n_rows(lh5_group_path, lh5_file)` will return the number
  of waveforms in the file.

- `lh5.get_lh5_element_type(obj)` tells us the format of the LH5 object.
  You will have to run the `lh5.read_object` command first (see next section)
  and then pass the result to this to get the type. For example if we run
  ```py
  obj = sto.read_object('/raw', dsp_file)[0]
  lh5.get_lh5_element_type(obj)
  ```
  It will tell us that this data is stored in a table.

### Reading data

`lh5.Store.read_object(lh5_group_path, lh5_file, start_row=0, n_rows=None,
obj_buf=None)` is the most basic command that returns a tuple of all the
elements within the path specified and the number of waveforms. Scalars and
arrays are encoded in pygamas LH5 custom data types. The command will be slow,
especially on the raw data, if you do not specify a precise path as it will
grab all the data within the file. `lh5_file` is the file you want to extract
the data from. `lh5_group_path` is the path to the data you want. You can
specify the number of rows you want to read too. for example
`sto.read_object('raw/waveform/values', lh5_file, n_rows=30)` will return a
tuple of the waveform values and the number processed i.e. 30.

Two commands are available in the `lh5` scope to load data in
[NumPy](https://numpy.org/doc/stable/user/basics.html) and
[Pandas](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe) data
structures:
```py
lh5.load_nda(file_list, par_list, lh5_group_path)
lh5.load_dfs(file_list, par_list, lh5_group_path)
```
These will take a file list which may include wildcards (e.g.
`th_HS2_lat_psa/th_HS2_lat_psa/*.lh5`). They will return all the values in all
the files for the parameters specified either as a dictionary of NumPy arrays
or as a Pandas dataframe. the `par_list` argument must be used to specify which
columns to read from the table on disk. For example:
```py
lh5.load_nda(f_raw, ('baseline', 'channel', 'waveform/values'), '/raw')
```

`lh5.Table.get_dataframe(get_dataframe(*cols, copy=False))` is useful for `dsp`
data where the format will generally be a table.
