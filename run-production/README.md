# Processing the Data

## Creating a new Production Cycle

Before you start this tutorial make sure your cluster ssh key is linked to your [github](https://github.com/mmatteo/legend-analysis-tutorials/tree/main/testing-enviroment/01-ssh-tricks#adding-keys-to-github).

Starting in the test environment.

First you will need to source the config file as before with:

```console 
source setup.sh
```

Now navigate to `user-prod` and create a new production cycle using:

```console
testenv-init.sh -o mmatteo -b master 'whoami'-test-v01
```

The apostrophe's on the whoami should be backwards quotation marks ``. 
This is a bash command that will give back your username. In the future you can change 'test' to whatever the goal of the production cycle will be. So the naming convention should be: `username-goalOfTheCycle-v01`.

Finally run `testenv-install.sh` to install all the nessary code.

You should now be able to find you new production cycle in the `user-prod`.

## Processing Data

Inide your new production cycle you can run the script:

```console
testenv-r2d.sh -m 100 config.json ../../ref-prod/master/data/meta/keylists/V04199A-th_HS2_lat_psa-all.txt
```

to process the data in the reference production.
The number in the command (100 here) controls the number of waveforms to be processed. Here we are only running on a small fraction of the number of waveforms in the file, in the future you will be working with many more. If you do not include `-m` and a number it will process all waveforms in the file.
The last part of the command is the path to a file containing the file paths of all the data to be processed. If you want to change how many files you want to work on you can create a custom file list and specifiy the path to it when running the above command. The file is of the form:
```console
my-dir/my-file-1.lh5
my-dir/my-file-2.lh5
my-dir/my-file-3.lh5
```.
