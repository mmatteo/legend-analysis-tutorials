# Jupyter lab and notebooks

To start a [jupyter lab](https://jupyter.org/) session on the local machine using a certain
container and software installation directory use:

```
PYTHONUSERBASE=/path/to/installation/dir \
  singularity run -B /path/to/installation/dir /path/to/container.sif \
  jupyter lab --no-browser --notebook-dir /path/to/working/dir
```
Then follow the instructions on the console. The command above can be used also to start
a jupyter server on a remote machine. In this case the command must be sent through ssh,
possibily tunnelling through a machine. The interactive notebook can then be accessed through
a web browser from your local machine. See site specific instructions for more details about
how to set this up.
