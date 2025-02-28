#! /bin/bash

# Setup the common directory env variables
if [ -e      /reg/g/pcds/pyps/config/common_dirs.sh ]; then
	source   /reg/g/pcds/pyps/config/common_dirs.sh
elif [ -e    /afs/slac/g/pcds/pyps/config/common_dirs.sh ]; then
	source   /afs/slac/g/pcds/pyps/config/common_dirs.sh
fi

# Use pcds-conda env 
source ${ENG_TOOLS_SCRIPTS}/pcds_conda

#export IOC_PV=IOC:TMO:TST
export BASE=LAMP:VCN:01

pushd /reg/g/pcds/epics-dev/screens/pydm/vacuumscreens/screens/TMO/VAT590
pydm -m "DEV=${BASE}" vat590.ui &
