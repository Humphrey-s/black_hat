#!/usr/bin/env python3
import struct
import socket
from ctypes import *

class IP(Structure):

    _fields_ = [
            ("ihl", c_ubyte, 4),
            ("version", c_ubyte, 4),
            ("tos", c_ubyte, 8),
            ("len", c_ushort, 16),
            ("id", c_ushort, 16),
            ("offset", c_ushort, 16),
            ("ttl", c_ubyte, 8),
            ("protocol_num", c_ubyte, 8),
            ("sum", c_ushort, 16),
            ("src", c_uint32, 32),
            ("dst", c_uint32, 32)
            ]

    def __new__(cls, socket_buffer=None):

        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:

            print("%s No protocol for %s".format(e, self.protocol_num))
