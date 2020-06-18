import caproto
from caproto import ChannelType
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run


class RecordMockingIOC(PVGroup):
    state_enum_strings = ['STOPPED', 'STARTING', 'RUNNING', 'FAULT', 'STOPPING']

    STATE_RBV = pvproperty(value=0, enum_strings=state_enum_strings, dtype=ChannelType.ENUM) 
    
    ilk_ok_rbv_enum_strings = ['NOT OK', 'OK']

    ILK_OK_RBV = pvproperty(value=0, enum_strings=ilk_ok_rbv_enum_strings, dtype=ChannelType.ENUM)

    error_rbv_enum_strings = ['TRUE', 'FALSE']

    ERROR_RBV = pvproperty(value=0, enum_strings=error_rbv_enum_strings, dtype=ChannelType.ENUM)


if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='pipDemoPv:',
        desc='Run an IOC that mocks an enum pv.')

    # Instantiate the IOC, assigning a prefix for the PV names.
    ioc = RecordMockingIOC(**ioc_options)
    # Run IOC.
    run(ioc.pvdb, **run_options)
