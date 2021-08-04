# Introduction to the Processing Chain

Here is an example definition of processing chain for `raw` to `dsp` in JSON
format. This structure is an input to pygama's `io.raw_to_dsp` function, as
described in the [run-production
tutorial](https://github.com/mmatteo/legend-analysis-tutorials/tree/main/run-production).

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

At the top we first specify the final outputs of processing the data. In this
case we have the mean and standard deviation of the baseline and the energy.
Outputs from other processors or data fields from the `raw` file can be added
here (e.g. `baseline`), if you want to forward them to the `dsp` tier. For
example we could add `"wf_trap"` here to check if the pole zero is being
applied correctly.

The next JSON block `"processors"` defines the processors themselves, arranged
in a chain.  Each processor name is defined by the outputs (fields in
`"outputs"` at the top should match these). As instance, the `"wf_blsub"`
processor outputs a baseline-subtracted version of the waveform. Inside the
curly braces we then specify the `"function"` that will return these outputs
(in this case the `bl_subtract` function) and the `"module"` it is defined in
(`pygama.dsp.processors`). This could be a pygama function but it could equally
be a general function from NumPy etc. such as in the last processor
`"trapEmax"` where `numpy.amax` is used.  The `"args"` field is where inputs
and outputs of the function are specified.  As it can be seen in the first
processor it is also possible to take slices of the input to be processed. The
units of the input can also be specified as in the `"wf_trap"`.  The last field
is `"prereqs"` which defines the inputs the processor depends on (without any
slicing).
