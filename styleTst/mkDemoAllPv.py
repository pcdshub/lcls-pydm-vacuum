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

    #vgc
    enum_strings = ['OPEN', 'CLOSED', 'MOVING', 'INVALID']
    vgc_POS_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vgc:POS_STATE_RBV')

    enum_strings = ['Vented', 'At Vacuum', 'Differential Pressure', 'Lost Vacuum', 'Ext Fault']
    vgc_STATE_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM, 
        name = 'vgc:STATE_RBV')

    enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']
    vgc_OPN_OK_RBV = pvproperty(value=0, 
         enum_strings=enum_strings, 
         dtype=ChannelType.ENUM,
         name = 'vgc:OPN_OK_RBV') 

    #pip
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

    enum_strings = ['TRUE', 'FALSE']
    pip_ERROR_RBV = pvproperty(value=0, 
        enum_strings=enum_strings, 
        dtype=ChannelType.ENUM,
        name = 'pip:ERROR_RBV')


if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='test:',
        desc='Run an IOC that mocks enum pv.')

    # Instantiate the IOC, assigning a prefix for the PV names.
    ioc = RecordMockingIOC(**ioc_options)
    # Run IOC.
    run(ioc.pvdb, **run_options)
