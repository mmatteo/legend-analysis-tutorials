# SSH connections

## for LINUX

### basic ssh connections

Direct connection to a remote machine with public IP is typically handled
through an ssh connection which is established through the command

```console
ssh your-username@remote-host-address
```

Useful options that can be specified are `-X` and `-Y` which allow to export
graphical session from the remote machine.

### ssh keys

ssh keys can be used to simplify the establishment of an ssh connection and
avoid entering your password at every log-in. To create an ssh key go into your
home directory (on your local machine) and execute:

```console
ssh-keygen -t ed25519 -C your-email-address
```

you can simply save this to the default address and leave the password blank
or short for ease of use.
To copy the public key onto the cluster use

```console
ssh-copy-id -i ~/.ssh/id_ed25519.pub your-username@remote-host-address
```

### .ssh/config

The ssh connection settings for each host and ssh tunneling through machines can
be specified in the \.ssh/config\ file. (Simply cd to the .ssh/ directory and
then open the config file with your prefered editor). This is an example of how
to config the username and graphic-export setting for a host called host1 and
how to use to tunnel to host2, a machine which does not have a public IP and is
reahable only through host1. This is a typical situation as computing clusters
provide access to their internal network through gateway machines.

```console
Host host1-name
    HostName host1-address
    User your-user-name
    ForwardX11 yes
    ForwardX11Trusted yes
Host host2-name
    HostName host2-address
    User your-user-name
    ProxyCommand ssh host1 -W %h:22
    ForwardX11 yes
    ForwardX11Trusted yes
```

## ssh and  github

ssh keys can also be used to work with github repositories. You can add your ssh
key to github for all computers you develop code with.
To generate a key on your local or cluster machines simply follow the instructions above and at this link:
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh

## VCODE

Visual studio can easily create a remote connection through ssh.
A walkthrough of how to set up ssh for this is found here:
https://code.visualstudio.com/docs/remote/ssh-tutorial

Ignore the parts about Azure and setting up hosts. 
Also https://code.visualstudio.com/docs/datascience/jupyter-notebooks may be useful. 
