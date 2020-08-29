# FullForcePlasmidAssembler

#Make sure any version of python3 is running on your system.


##### SETTING UP A NEW UNBUNTO BASED CLOUD SERVER #############
-Create ubuntu instance with plenty of space and mem.
#Python3 installed already
-install docker
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ sudo usermod -a -G docker $USER
#Close terminal and reopen.

#Git clone
$ sudo usermod -a -G docker $USER
#run images.py
$ python3 images.py

#Once docker has been succesfully installed, pull following images:
Docker images:
fjukstad/trimmomatic
mcfonsecalab/qcat
nanozoo/nanoplot:1.32.0--1ae6f5d
nanozoo/fastqc
mcfonsecalab/nanofilt
flowcraft/kraken:1.0-0.1
nanozoo/unicycler:0.4.7-0--c0404e6
replikation/abricate

