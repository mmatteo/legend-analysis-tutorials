# legend-analysis-tutorials
Collection of tutorials and code snippets for analyzing the LEGEND data.

### working-on-remote-machines

This tutorial covers tools and tricks on how to work on remote machines,
including site-specific instructions on how to load the LEGEND software.

### tier-data

This tutorial provides an introduction on how to access to LEGEND data and
retrieve objects such as waveforms or DSP parameters. It also shows how to plot
these objects.

### processing-data

This tutorial shows how to manually process the `daq` files into `raw` and then `dsp`. 
Instruction on how to use the automatic tools for data production can be found
under: [legend-exp/legend-prodenv](https://github.com/legend-exp/legend-prodenv) and
[legend-exp/legend-prodenv](https://github.com/legend-exp/legend-dataflow-hades)

### build-dsp

This tutorial focuses on the digital signal processing, i.e. the creation of the
`dsp` tier. It provides an introduction to the configuration of the processing
chain, i.e. the chains of `pygama` processors that run over the waveforms. It
also shows how to implement new processors.
