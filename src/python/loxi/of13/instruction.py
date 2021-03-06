# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
import const
import common
import action
import instruction
import oxm
import action_id
import instruction_id
import meter_band
import bsn_tlv
import util
import loxi.generic_util

class instruction(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = instruction.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = instruction()
        obj.type = reader.read("!H")[0]
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("instruction {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class apply_actions(instruction):
    type = 4

    def __init__(self, actions=None):
        if actions != None:
            self.actions = actions
        else:
            self.actions = []
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append(loxi.generic_util.pack_list(self.actions))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = apply_actions()
        _type = reader.read("!H")[0]
        assert(_type == 4)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        reader.skip(4)
        obj.actions = loxi.generic_util.unpack_list(reader, action.action.unpack)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.actions != other.actions: return False
        return True

    def pretty_print(self, q):
        q.text("apply_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("actions = ");
                q.pp(self.actions)
            q.breakable()
        q.text('}')

instruction.subtypes[4] = apply_actions

class experimenter(instruction):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None, data=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if data != None:
            self.data = data
        else:
            self.data = ''
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(self.data)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        obj.experimenter = reader.read("!L")[0]
        obj.data = str(reader.read_all())
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.data != other.data: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("data = ");
                q.pp(self.data)
            q.breakable()
        q.text('}')

instruction.subtypes[65535] = experimenter

class bsn(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 6035143

    def __init__(self, subtype=None):
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 8)
        subclass = bsn.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = bsn()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        obj.subtype = reader.read("!L")[0]
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.subtype != other.subtype: return False
        return True

    def pretty_print(self, q):
        q.text("bsn {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[6035143] = bsn

class bsn_arp_offload(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 1

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_arp_offload()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 1)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_arp_offload {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[1] = bsn_arp_offload

class bsn_deny(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 5

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_deny()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 5)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_deny {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[5] = bsn_deny

class bsn_dhcp_offload(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 2

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_dhcp_offload()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 2)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_dhcp_offload {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[2] = bsn_dhcp_offload

class bsn_disable_split_horizon_check(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 3

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_disable_split_horizon_check()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 3)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_disable_split_horizon_check {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[3] = bsn_disable_split_horizon_check

class bsn_disable_src_mac_check(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 0

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_disable_src_mac_check()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 0)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_disable_src_mac_check {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[0] = bsn_disable_src_mac_check

class bsn_packet_of_death(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 6

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_packet_of_death()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 6)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_packet_of_death {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[6] = bsn_packet_of_death

class bsn_permit(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 4

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_permit()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 4)
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_permit {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[4] = bsn_permit

class clear_actions(instruction):
    type = 5

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = clear_actions()
        _type = reader.read("!H")[0]
        assert(_type == 5)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("clear_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

instruction.subtypes[5] = clear_actions

class goto_table(instruction):
    type = 1

    def __init__(self, table_id=None):
        if table_id != None:
            self.table_id = table_id
        else:
            self.table_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.table_id))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = goto_table()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        obj.table_id = reader.read("!B")[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.table_id != other.table_id: return False
        return True

    def pretty_print(self, q):
        q.text("goto_table {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("table_id = ");
                q.text("%#x" % self.table_id)
            q.breakable()
        q.text('}')

instruction.subtypes[1] = goto_table

class meter(instruction):
    type = 6

    def __init__(self, meter_id=None):
        if meter_id != None:
            self.meter_id = meter_id
        else:
            self.meter_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.meter_id))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = meter()
        _type = reader.read("!H")[0]
        assert(_type == 6)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        obj.meter_id = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.meter_id != other.meter_id: return False
        return True

    def pretty_print(self, q):
        q.text("meter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("meter_id = ");
                q.text("%#x" % self.meter_id)
            q.breakable()
        q.text('}')

instruction.subtypes[6] = meter

class write_actions(instruction):
    type = 3

    def __init__(self, actions=None):
        if actions != None:
            self.actions = actions
        else:
            self.actions = []
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append(loxi.generic_util.pack_list(self.actions))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = write_actions()
        _type = reader.read("!H")[0]
        assert(_type == 3)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        reader.skip(4)
        obj.actions = loxi.generic_util.unpack_list(reader, action.action.unpack)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.actions != other.actions: return False
        return True

    def pretty_print(self, q):
        q.text("write_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("actions = ");
                q.pp(self.actions)
            q.breakable()
        q.text('}')

instruction.subtypes[3] = write_actions

class write_metadata(instruction):
    type = 2

    def __init__(self, metadata=None, metadata_mask=None):
        if metadata != None:
            self.metadata = metadata
        else:
            self.metadata = 0
        if metadata_mask != None:
            self.metadata_mask = metadata_mask
        else:
            self.metadata_mask = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append(struct.pack("!Q", self.metadata))
        packed.append(struct.pack("!Q", self.metadata_mask))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = write_metadata()
        _type = reader.read("!H")[0]
        assert(_type == 2)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len - (2 + 2))
        reader.skip(4)
        obj.metadata = reader.read("!Q")[0]
        obj.metadata_mask = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.metadata != other.metadata: return False
        if self.metadata_mask != other.metadata_mask: return False
        return True

    def pretty_print(self, q):
        q.text("write_metadata {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("metadata = ");
                q.text("%#x" % self.metadata)
                q.text(","); q.breakable()
                q.text("metadata_mask = ");
                q.text("%#x" % self.metadata_mask)
            q.breakable()
        q.text('}')

instruction.subtypes[2] = write_metadata


