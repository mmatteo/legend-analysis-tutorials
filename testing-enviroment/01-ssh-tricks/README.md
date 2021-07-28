# SSH Tutorial

## LINUX

### Basics

The first thing to do is to 'ssh' to the hep cluster and then to pc204 where
we shall be working.

The simplest way to do this is to use 

`ssh your-username@plus1.hep.ucl.ac.uk`

and then 

`ssh pc204`.

You can logout by simply typing `logout`.

### Generating keys

To make this process easier and to stop you having to enter your password
every time you log in we can generate a set of keys. From your home directory
(when not using ssh) execute:

`ssh-keygen -t ed25519 -C your-email-address@something.com`

you can simply save this to the default address and leave the password blank
or short for ease of use.
To copy the public key onto the cluster use

`ssh-copy-id -i ~/.ssh/id_ed25519.pub plus1`

### Even quicker method

After adding your keys the process can be sped up further by adding the
following block into your .ssh/config. (Simply cd to the .ssh/ directory and
then open the config file with your prefered editor).

```
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

plus1 and plus2 are visible from the web and the settings are just related to X
forwarding. pc204 is not visible from the web and an extra option is needed to
do a ssh tunnel through plus1. Change the username field.

## Through VCODE

If you're using windows it is probably easiest to work through VS code. 
A walkthrough of how to set up ssh for this is found here:
https://code.visualstudio.com/docs/remote/ssh-tutorial
Ignore the parts about Azure and setting up hosts. 
Also https://code.visualstudio.com/docs/datascience/jupyter-notebooks may be useful. 

## Adding keys to github

One final step is needed which is to add your keys to github. You can do this 
for both your home computer and the cluster. To generate a key on the cluster
simply follow the instructions above while 'ssh'ed. Then follow the
instructions here:
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh


