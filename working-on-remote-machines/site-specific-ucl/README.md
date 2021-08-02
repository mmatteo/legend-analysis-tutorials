# HEP cluster at UCL

# SSH 
SSH gateways are:

```
plus1.hep.ucl.ac.uk
plus2.hep.ucl.ac.uk
```

You can connect to them using: 
```console
ssh your-username@plus1.hep.ucl.ac.uk
```

After conneting to `plus1` or `plus2`, you can accesso to all UCL machines, including those in the batch farm. UCL LEGEND users are currently using as interactive machine `pc204`, which can be directly access from the gateways using:
```console
ssh pc204
```

Here is an example of `.ssh/config` file for linux:
```console
Host plus1
    HostName plus1.hep.ucl.ac.uk
    User your-user-name
    ForwardX11 yes
    ForwardX11Trusted yes
  Host plus2
    HostName plus2.hep.ucl.ac.uk
    User your-user-name
    ForwardX11 yes
    ForwardX11Trusted yes
  Host pc204
    HostName pc204
    User your-user-name
    ProxyCommand ssh plus1 -W %h:22
    ForwardX11 yes
    ForwardX11Trusted yes
```

## load software
The disk space allocated for LEGEND is located under `/unix/legend/`. Our software is developed and run through singularity containers. To load a specifc container and software version use:

```console
/unix/legend/software/load-v01.sh
```
To unload the software environment use `exit` or `CTRL-D`.

Info on the software versions available can be found in `/unix/legend/software/README`

## Jupyter Lab and Notebooks

###  If your local machine is a linux system
After setting the ssh config file above, you can open a notebook on pc204 using this command:

```console
ssh pc204 -L MYPORT:localhost:MYPORT  'PYTHONUSERBASE=/unix/legend/software/pygama-v01/local singularity run  -B /run/user/$(id -u) -B /unix /unix/legend/software/containers/this.sif jupyter lab --no-browser --notebook-dir /unix/legend --port MYPORT --port-retries 0'
```
where MYPORT is a number of 4 digits above 8800. 

###  If your local machine is a linux system (Version 10)
Open two powershells. In the first one run the command

```console
ssh -L PORT1:pc204:22 username@plus1.hep.ucl.ac.uk
```
to esablish an port forwarding of the ssh port of pc204 on your local host. Then run in the second powershell:

```console
ssh -p PORT1 username@localhost -L PORT2:localhost:PORT2 "PYTHONUSERBASE=/unix/legend/software/pygama-v01/local singularity run -B /unix /unix/legend/software/containers/this.sif jupyter lab --no-browser --notebook-dir /home/username --port PORT2 --port-retries 0"
```
In the commands above, you must replace PORT1 and PORT2 with two numbers of 4 digits above 8800 and username with your linux username on the UCL hep cluster.

### ERROR: the notebook server could not be started because port ???? is not available
If you see this error, it is because you have a Jupyter kernel runnig already. In this case, you can either connect to pc204 and kill it, or kill it through ssh using a command such as:

ssh -p PORT1 username@localhost -L PORT2:localhost:PORT2 "ssh -p PORT1 username@localhost -L PORT2:localhost:PORT2 "pkill -u username" 



