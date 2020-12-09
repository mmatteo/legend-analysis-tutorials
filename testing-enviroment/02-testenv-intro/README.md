# Intoduction to the Test Environment

##Setting Up

First log in to the server

`ssh pc204`

then navigate to the test env

`cd /unix/legend/testenv-v02`

You will then need to source the config file using:

`source setup.sh`

Finally make a shell within the virtual environment and load all the software using:

`testenv-bash.sh config.json`

(venv) should appear at the start of your command line.

##Working on the data 

Now in the virtual environment we can work on the data. To do this simply enter:
`ipython`
to start an ipython instance. This has the same functionality as a jupyter notebook where we can
enter a block of code and then run using shift + enter.  

