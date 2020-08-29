import os
cmd = "docker pull fjukstad/trimmomatic"
os.system(cmd)
cmd = "docker pull mcfonsecalab/qcat"
os.system(cmd)
cmd = "docker pull nanozoo/nanoplot:1.32.0--1ae6f5d"
os.system(cmd)
cmd = "docker pull nanozoo/fastqc"
os.system(cmd)
cmd = "docker pull mcfonsecalab/nanofilt"
os.system(cmd)
cmd = "docker pull flowcraft/kraken:1.0-0.1"
os.system(cmd)
cmd = "docker pull nanozoo/unicycler:0.4.7-0--c0404e6"
os.system(cmd)
cmd = "docker pull replikation/abricate"
os.system(cmd)