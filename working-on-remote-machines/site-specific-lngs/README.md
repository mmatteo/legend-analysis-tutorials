# HEP cluster at UCL

# SSH
The LEGEND SSH gateways are:

`legend-login1@infn.lngs.infn.it`
`legend-login2@infn.lngs.infn.it`

You can also use the alias `legend-login` which assign you automatically to one of the two machines.


You can connect to them using: 
``console
ssh your-username@legend-login.lngs.infn.it
```

After conneting to our LEGEND login-in machines you can drectly access to the common softaware installation, the data and the batch farm. The log-in machines are intended for interactive usage, computationally intensitve jobs should be submitted to u-lite.

Here is an example of `.ssh/config` file:
```console
Host legend-login1
    HostName legend-login1.lngs.infn.it
    User your-user-name
    ForwardX11 yes
    ForwardX11Trusted yes
Host legend-login2
    HostName legend-login2.lngs.infn.it
    User your-user-name
    ForwardX11 yes
    ForwardX11Trusted yes
```

## Jupyter Notebooks

## u-lite

## load software
