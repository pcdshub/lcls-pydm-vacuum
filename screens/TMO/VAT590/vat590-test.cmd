#! /bin/bash

# Setup the common directory env variables
if [ -e      /reg/g/pcds/pyps/config/common_dirs.sh ]; then
	source   /reg/g/pcds/pyps/config/common_dirs.sh
elif [ -e    /afs/slac/g/pcds/pyps/config/common_dirs.sh ]; then
	source   /afs/slac/g/pcds/pyps/config/common_dirs.sh
fi

# Setup edm environment
source /reg/g/pcds/pyps/conda/py36env.sh

#export IOC_PV=IOC:TMO:TST
export BASE=VCN:TEST:01

pushd /reg/g/pcds/epics-dev/janezg/vacuumScreens/vat590Screens
pydm -m "DEV=${BASE}" vat590.ui &

pushd /reg/g/pcds/epics-dev/janezg/vacuumScreens
pydm im540_test.ui &
