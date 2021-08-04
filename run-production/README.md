# Processing the data with the `dev` branch [`5e261e6`](https://github.com/legend-exp/pygama/tree/5e261e69eec1610431fe2eda42d994ba58d299ea)

The conversion of FlashCam DAQ files (`daq`) into `raw` is currently done by
the pygama function `io.process_flashcam` which is part of [pygama's `io`
module](https://github.com/legend-exp/pygama/blob/dev/pygama/io) and is defined
in
[`io/fcdaq.py`](https://github.com/legend-exp/pygama/blob/dev/pygama/io/fcdaq.py)

The conversion of `raw` into `dsp` files is done by the pygama function
[`io.raw_to_dsp`](https://github.com/legend-exp/pygama/blob/dev/pygama/io/raw_to_dsp.py)
that is also part of the `io` module. The config file parsed by `io.raw_to_dsp`
is described in the `build-dsp` tutorial.

For convenience, a simple python script providing an interface to these two functions
is attached to this tutorial.
