import caproto
from caproto import ChannelType
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run


class RecordMockingIOC(PVGroup):
    '''
    set up test:* pvs
    Use format:

    enum_strings = []
    <widget>_<PV suffix> = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = '<widget>:<PV suffix>')
    '''

################################
#Valves and Shutters
################################
# ApperatureValve - vgc
    '''
    _interlock_suffix = ":OPN_OK_RBV"
    _error_suffix = ":STATE_RBV"
    _state_suffix = ":POS_STATE_RBV"
    '''
    enum_strings = ['OPEN', 'CLOSED', 'MOVING', 'INVALID', 'OPEN_F']
    vgc_POS_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vgc:POS_STATE_RBV')

    enum_strings = ['Vented', 'At Vacuum', 'Lost Vacuum', 'Ext Fault']
    vgc_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vgc:STATE_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vgc_OPN_OK_RBV = pvproperty(value=0, 
         enum_strings=enum_strings, 
         dtype=ChannelType.ENUM,
         name = 'vgc:OPN_OK_RBV') 

# PnumaticValve - vrc, vgc (use vrc)
    '''
    _interlock_suffix = ":OPN_OK_RBV"
    _error_suffix = ":STATE_RBV"
    _state_suffix = ":POS_STATE_RBV"
    '''
    enum_strings = ['OPEN', 'CLOSED', 'MOVING', 'INVALID', 'OPEN_F']
    vrc_POS_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vrc:POS_STATE_RBV')

    enum_strings = ['Vented', 'At Vacuum', 'Lost Vacuum', 'Ext Fault']
    vrc_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vrc:STATE_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vrc_OPN_OK_RBV = pvproperty(value=0, 
         enum_strings=enum_strings, 
         dtype=ChannelType.ENUM,
         name = 'vrc:OPN_OK_RBV') 

# Fast Shutter - vfs
    '''
    _interlock_suffix = ":VAC_FAULT_OK_RBV"
    _error_suffix = ":STATE_RBV"
    _state_suffix = ":POS_STATE_RBV"
    '''
    enum_strings = ['OPEN', 'CLOSED', 'MOVING', 'INVALID']
    vfs_POS_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vfs:POS_STATE_RBV')

    enum_strings = ['At Vacuum', 'AT Vacuum', 'Triggered', 'Vacuum Fault',
                    'Close Timeout','Open Timeout', 'Ext Fault']
    vfs_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vfs:STATE_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vfs_VAC_FAULT_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'vfs:VAC_FAULT_OK_RBV') 


# Control Only Valve Normally Closed - vvcNC
    '''
    _interlock_suffix = ":OPN_OK_RBV"
    _state_suffix = ':OPN_DO_RBV'
    '''
    enum_strings = ['One', 'Zero', 'Open', 'Closed']
    vvcNC_OPN_DO_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vvcNC:OPN_DO_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vvcNC_OPN_OK_RBV = pvproperty(value=0, 
         enum_strings=enum_strings, 
         dtype=ChannelType.ENUM,
         name = 'vvcNC:OPN_OK_RBV') 

# Control Only Valve Normally Open - vvcNO
    '''
    _interlock_suffix = ":CLS_OK_RBV"
    _state_suffix = ':CLS_DO_RBV'
    ''' 
    enum_strings = ['One', 'Zero', 'Open', 'Closed']
    vvcNO_CLS_DO_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vvcNO:CLS_DO_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vvcNO_CLS_OK_RBV = pvproperty(value=0, 
         enum_strings=enum_strings, 
         dtype=ChannelType.ENUM,
         name = 'vvcNO:CLS_OK_RBV') 


# Needle Valve - vcn
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _state_suffix = ":STATE_RBV"
    '''
    enum_strings = ['Close', 'Open', 'PressureControl', 'ManualControl']
    vcn_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vcn:STATE_RBV')

    enum_strings = ['NOT OK', 'OK']
    vcn_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'vcn:ILK_OK_RBV')

################################
#Pumps  
################################
# Turbo Pump - ptm
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _error_suffix = ":FAULT_RBV"
    _state_suffix = ":STATE_RBV"
    '''
    enum_strings = ['STOPPED', 'STARTING', 'RUNNING', 'FAULT', 'STOPPING']
    ptm_STATE_RBV = pvproperty(value=0,
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'ptm:STATE_RBV') 
    
    enum_strings = ['ILK ACTIVE', 'ILK OK']
    ptm_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'ptm:ILK_OK_RBV')

    enum_strings = ['FALSE', 'TRUE']
    ptm_FAULT_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'ptm:FAULT_RBV')

# Scroll Pump - pro 
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _error_suffix = ":ERROR_RBV"
    _state_suffix = ":STATE_RBV"
    '''

    enum_strings = ['STOPPED', 'STARTING', 'RUNNING', 'FAULT', 'STOPPING']
    pro_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pro:STATE_RBV') 
    
    enum_strings = ['ILK ACTIVE', 'ILK OK']
    pro_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pro:ILK_OK_RBV')

    enum_strings = ['FALSE', 'TRUE']
    pro_ERROR_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pro:ERROR_RBV')


#Ion Pump - pip
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _error_suffix = ":ERROR_RBV"
    _state_suffix = ":STATE_RBV"
    _readback_suffix = ":PRESS_RBV"
    '''
    enum_strings = ['STOPPED', 'STARTING', 'RUNNING', 'FAULT', 'STOPPING']
    pip_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pip:STATE_RBV') 
    
    enum_strings = ['NOT OK', 'OK']
    pip_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pip:ILK_OK_RBV')

    enum_strings = ['FALSE', 'TRUE']
    pip_ERROR_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pip:ERROR_RBV')

    pip_PRESS_RBV = pvproperty(value=5E-25, 
        record = 'ai',
        name = 'pip:PRESS_RBV')

################################
#Gauges  
################################

#Rough Gauge - GPI
    '''
    _state_suffix = ":STATE_RBV"
    _readback_suffix = ":PRESS_RBV"
    '''
    enum_strings = ['PressInvalid', 'GaugeDisconnected', 'OoR', 'Off', 
        'Valid', 'ValidHi', 'ValidLo' ]
    gpi_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'gpi:STATE_RBV')  

    gpi_PRESS_RBV = pvproperty(value=5E-25, 
        record = 'ai',
        name = 'gpi:PRESS_RBV')


#Cold Cathode - GCC
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _state_suffix = ":STATE_RBV"
    _readback_suffix = ":PRESS_RBV"
    '''

    enum_strings = ['NOT OK', 'OK']
    gcc_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'gcc:ILK_OK_RBV')

    enum_strings = ['PressInvalid', 'GaugeDisconnected', 'OoR', 'Off', 
        'Starting', 'Valid', 'ValidHi', 'ValidLo' ]
    gcc_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'gcc:STATE_RBV')  

    gcc_PRESS_RBV = pvproperty(value=5E-25, 
        record = 'ai',
        name = 'gcc:PRESS_RBV')



#Hot Cathode - GHC
    '''
    _interlock_suffix = ":ILK_OK_RBV"
    _state_suffix = ":STATE_RBV"
    _readback_suffix = ":PRESS_RBV"
    '''

    enum_strings = ['NOT OK', 'OK']
    ghc_ILK_OK_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'ghc:ILK_OK_RBV')

    enum_strings = ['PressInvalid', 'GaugeDisconnected', 'OoR', 'Off', 
        'Starting', 'Valid', 'ValidHi', 'ValidLo' ]
    ghc_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'ghc:STATE_RBV')  

    ghc_PRESS_RBV = pvproperty(value=5E-25, 
        record = 'ai',
        name = 'ghc:PRESS_RBV')


if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='test:',
        desc='Run an IOC that mocks enum pv.')

    # Instantiate the IOC, assigning a prefix for the PV names.
    ioc = RecordMockingIOC(**ioc_options)
    # Run IOC.
    run(ioc.pvdb, **run_options)
