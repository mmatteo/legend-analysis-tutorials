# Introduction to Processors

A processor is an algorithm that runs on a waveform and computes observables of interest.

## Making a Processor

Now that we have a new production cycle we can start customizing how it processes its
data.  All the processors are found in the pygama repository below
`software/src/python/pygama/pygama/dsp/_processors`.

You can simply add a new processor into this folder. For demonstration, let's implement a
new way of calculating the mean and standard deviation of the baseline.

```py
import numpy as np
from numba import guvectorize
from math import sqrt

@guvectorize(["void(float32[:], float32[:], float32[:])",
              "void(float64[:], float64[:], float64[:])"],
             "(n)->(),()", nopython=True, cache=True)
def mean_stdev(w_in, mean, stdev):
    """
    Calculate the mean and standard deviation of a vector using simple numpy operations
    """
    mean = np.mean(wf)
    stdev = np.stdev(wf)
 ```

All the processors in pygama must be written as these `void` functions.  Now we need to
let pygama know where to find this new processor.  The first place that needs to be
changed is the `processors.py` in the `dsp` directory. The line:

```py
from ._processors.my_new_process import new_function
```

will be needed. Next, navigate all the way back up to your production cycle root directory
and then to `data/meta/dsp`. You will find a `processor_list.json` file. As the name
implies, it contains a list of all the processors that will be used for data processing.
For this simple example we can just change the first block. Only the `function` line needs
changing to our new processor e.g.

```json
"function": "new_mean_stdev",
```

We are now ready to process the data with the new processor using the same process as
shown [here](https://github.com/mmatteo/legend-analysis-tutorials/tree/main/run-production).
