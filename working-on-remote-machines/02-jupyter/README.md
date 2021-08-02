# jupyter lab and notebooks

To start a jupyter lab session on the local machine using a certain container and software installation directory use:

```console
PYTHONUSERBASE=/path/to/installation/dir singularity run -B /path/to/installation/dir /path/to/container.sif jupyter lab --no-browser --notebook-dir /path/to/working/dir
```
The command above can be used also to start a notebook in a remote machine. In this case the command must be sent through ssh, possibily tunnelling through a machine. See site specific instructions for more details.
