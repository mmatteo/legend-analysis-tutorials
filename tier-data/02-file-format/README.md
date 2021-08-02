# LH5

In the previous section we looked at loading data and used 2 functions: read_object and load_nda. We need to use these functions as all data in LEGEND is stored in the lh5(lgdo) format. This allows us to store large amounts of data in single files and access just the data we want without having to load all of it (This is especially handy for raw data where 1000s of waveforms are in the file but we might only want to see a few without having to load all of them in memory). 
This section goes into more depth on the functions we can use to look at lh5 data.

## File

### Raw

This file is a mix of data types. Stat contains various info about the processing e.g cputime etc. Raw contains the data for each waveform. All the parameters are shown below:
```console
.
├── stat    
└── raw
     ├── baseline        # fpga baseline
     ├── channel         # right now, index of the trigger (trace)
     ├── energy          # fpga energy
     ├── ievt            # index of event
     ├── numtraces       # number of triggered adc channels
     ├── packet_id       # packet index in file
     ├── timestamp       # time since beginning of file
     ├── tracelist       # list of triggered adc channels
     ├── waveform        # digitizer data
     │   ├── dt          # sampling period (ns) - 16
     │   ├── t0
     │   └── values      
     ├── wf_max          # ultra-simple np.max energy estimation
     └── wf_std          # ultra-simple np.std noise estimation
     
```

### DSP

This file is generally a table as each waveform has only one value. This will change if you output parameters with other datatypes such as the 'wf_trap'. dsp_info contains various info about the processing e.g pygama version etc. An example is shown below
```console
.
├── dsp_info    
└── raw
     ├──  bl
     ├──  bl_sig
     └──  trapEmax
```

## Commands

### Navigation 

For ease of use initialise the store class with `sto=lh5.Store()`.

`sto.ls(self, lh5_file, group_path='')`  This works like the ls command in unix. It can be used to find what is in the file. For example on the raw file we can run `sto.ls(your_file, 'raw/waveform/')` to output the parameters within waveform: dt,t0 and values.

`sto.read_n_rows(name, lh5_file)` this will return the number of waveforms in the file. Name is the path e.g. raw.

`lh5.get_lh5_datatype_name(obj)` This tells us the format of the lh5 object. You will have to run the read_object command first and then pass the result to this to get the type. For example if we run 
```py
sto.read_object(dsp_file)[0]
lh5.get_lh5_datatype_name(tb)
```
It will tell us that this data is stored in a table. 

### Getting Data

`sto.read_object(name, lh5_file, start_row=0, n_rows=None, obj_buf=None)` This is the most basic command that return a tuple of all the elements within the path specified and the number of waveforms. It will be slow, especially on the raw data, if you do not specify a complete path as it will grab all the data within the path. lh5-file is the file you want to extract the data from. Name is the path to the data you want. You can specify the number of rows you want also. for example `sto.read('raw/waveform/values',file, 30)` will return a tuple of the waveform values and the number processed i.e. 30. 


These two commands can be grouped together:
```py
lh5.load_dfs(f_list, par_list, tb_in)
lh5.load_nda(f_list, par_list, tb_in) 
```

These will take a file list which may include wildcards for example `th_HS2_lat_psa/th_HS2_lat_psa/*.lh5`. They will return all the values in all the files for the parameters specified either as a dictionary of arrays or as a dataframe.

```py
lh5.Table.get_dataframe(get_dataframe(*cols, copy=False))
```
Useful for dsp data where the format will generally be a table. 



