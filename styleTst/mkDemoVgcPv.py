import caproto
from caproto import ChannelType
from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run


class RecordMockingIOC(PVGroup):
    pos_state_enum_strings = ['OPEN', 'CLOSED', 'MOVING', 'INVALID']

    POS_STATE_RBV = pvproperty(value=0, enum_strings=pos_state_enum_strings, dtype=ChannelType.ENUM)

    state_enum_strings = ['Vented', 'At Vacuum', 'Differential Pressure', 'Lost Vacuum', 'Ext Fault']

    STATE_RBV = pvproperty(value=0, enum_strings=state_enum_strings, dtype=ChannelType.ENUM)

    opn_ok_rbv_enum_strings = ['OPN ILK NOT OK', 'OPN ILK OK']

    OPN_OK_RBV = pvproperty(value=0, enum_strings=opn_ok_rbv_enum_strings, dtype=ChannelType.ENUM)

if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix='vgcDemoPv:',
        desc='Run an IOC that mocks an enum pv.')

    # Instantiate the IOC, assigning a prefix for the PV names.
    ioc = RecordMockingIOC(**ioc_options)
    # Run IOC.
    run(ioc.pvdb, **run_options)
