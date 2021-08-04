# Introduction to the Processing Chain

Here is an example processing chain for raw to dsp. 

```json
{
  "outputs": [
    "bl_mean", "bl_sig", "trapEmax"
  ],
  "processors":{
        "wf_blsub":{
            "function": "bl_subtract",
            "module": "pygama.dsp.processors",
            "args": ["waveform", "baseline", "wf_blsub"],
            "prereqs": ["waveform", "baseline"],
            "unit": "ADC"
         },

        "bl_mean , bl_std, bl_slope, bl_intercept":{
            "function": "linear_slope_fit",
            "module": "pygama.dsp.processors",
            "args" : ["wf_blsub[0: 1650]", "bl_mean","bl_std", "bl_slope","bl_intercept"],
            "prereqs": ["wf_blsub"],
            "unit": ["ADC","ADC","ADC","ADC"]
          },
        "wf_pz": {
            "function": "pole_zero",
            "module": "pygama.dsp.processors",
            "args": ["wf_blsub", "db.pz.tau", "wf_pz"],
            "prereqs": ["wf_blsub"],
            "unit": "ADC",
            "defaults": { "db.pz.tau":"260*us" }
          },
        "wf_trap": {
            "function": "trap_norm",
            "module": "pygama.dsp.processors",
            "args": ["wf_pz", "8*us", "2*us", "wf_trap"],
            "prereqs": ["wf_pz"],
            "unit": "ADC"
          },
        "trapEmax": {
            "function": "amax",
            "module": "numpy",
            "args": ["wf_trap", 1, "trapEmax"],
            "kwargs": {"signature":"(n),()->()", "types":["fi->f"]},
            "unit": "ADC",
            "prereqs": ["wf_trap"]
          }
         }
}
```

At the top we first specify the final outputs of processing the data. In this case the mean and standard deviation of the baseline and the energy. Attributes from the raw file can be added here (e.g. 'baseline') if you want to copy them across into the dsp file or outputs from other processors. For example we could add "wf_trap" here to check the pole zero is being applied correctly. 

The next section are the processors themselves which are arranged in a chain. Each is defined by its outputs (the outputs at the top should each match one of these); the first processor outputs baseline subtracted version of the waveform. Inside the curly braces we then specify the function that will return these outputs in this case the "bl_subtract" function and where it is found "pygama.dsp.processors". This could be a pygama function but it could equally be a general function from numpy etc. such as in the last processor "trapEmax" where numpy.amax is used.

The args function is where the inputs and outputs are specified. As can be seen from the first processor it is also possible to take slices of the input to be processed. The units of the input can also be specified as in the "wf_trap".
The last  general fields is the prereqs which specify the inputs (without any slicing).



