# LH5

## File

### Raw

This file is a mix of data types. stat contains various info about the processing e.g cputime etc.
```
.
├── stat    
└── raw
     ├── baseline
     ├── channel
     ├── energy
     ├── ievt
     ├── numtraces
     ├── packet_id
     ├── timestamp
     ├── tracelist
     ├── waveform
     │   ├── dt
     │   ├── t0
     │   └── values
     ├── wf_max
     └── wf_std
     
```

### DSP

This file is generally a table as each waveform has only one value. This will change if you output parameters with other datatypes such as the 'wf_trap'. dsp_info contains various info about the processing e.g pygama version etc. An example is shown below
```
.
├── dsp_info    
└── raw
     ├──  bl
     ├──  bl_sig
     └──  trapEmax
```

### Navigation 

For ease of use `sto=lh5.Store()`.

`sto.ls(self, lh5_file, group_path='')`  This works like the ls command in unix. It can be used to find what is in the file. For example on the raw file we can run `sto.ls(your_file, 'raw/waveform')` to output the parameters within waveform: dt,t0 and values.

`lh5.Store.read_n_rows(self, name, lh5_file)` this will return the number of waveforms in the file. Name is the path e.g. raw.

`lh5.get_lh5_datatype_name(obj)` This tells us the format of the lh5 object. You will have to run the read_object command first and then pass the result to this to get the type. For example if we run 
```
sto.read_object(dsp_file)[0]
lh5.get_lh5_datatype_name(tb)
```
It will tell us that this data is stored in a table. 

### Getting Data

`sto.read_object(self, name, lh5_file, start_row=0, n_rows=None, obj_buf=None)` This is the most basic command that return a tuple of all the elements within the path specified and the number of waveforms. It will be slow, especially on the raw data, if you do not specify a complete path as it will grab all the data within the path. lh5-file is the file you want to extract the data from. Name is the path to the data you want. You can specify the number of row you want also. for example `sto.read('raw/waveform/values',file, 30)` will return a tuple of the waveform values and the number processed i.e. 30. 


These two commands can be grouped together:
`lh5.load_dfs(f_list, par_list, tb_in)`

`lh5.load_nda(f_list, par_list, tb_in)` 

These will take a file list which may include wildcards for example `th_HS2_lat_psa/th_HS2_lat_psa/*.lh5`. They will return all the values in all the files for the parameters specified either as an array or as a dataframe.

`lh5.Table.get_dataframe(get_dataframe(self, *cols, copy=False))` Useful for dsp data where the format will generally be a table. 



