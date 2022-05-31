# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position,unused-import,unused-wildcard-import
"""stream pcap file extractor

:mod:`pcapkit` is an independent open source library, using only
`DictDumper`_ as its formatted output dumper.

.. _DictDumper: https://dictdumper.jarryshaw.me

    There is a project called |jspcapy|_ works on :mod:`pcapkit`,
    which is a command line tool for PCAP extraction.

Unlike popular PCAP file extractors, such as `Scapy`_,
`DPKT`_, `PyShark`_, and etc, :mod:`pcapkit` uses streaming
strategy to read input files. That is to read frame by
frame, decrease occupation on memory, as well as enhance
efficiency in some way.

.. _Scapy: https://scapy.net
.. _DPKT: https://dpkt.readthedocs.io
.. _PyShark: https://kiminewt.github.io/pyshark

In :mod:`pcapkit`, all files can be described as following eight
different components.

- Interface (:mod:`pcapkit.interface`)

  user interface for the :mod:`pcapkit` library, which
  standardise and simplify the usage of this library

- Foundation (:mod:`pcapkit.foundation`)

  synthesise file I/O and protocol analysis, coordinate
  information exchange in all network layers

- Reassembly (:mod:`pcapkit.reassembly`)

  base on algorithms described in :rfc:`815`,
  implement datagram reassembly of IP and TCP packets

- Protocols (:mod:`pcapkit.protocols`)

  collection of all protocol family, with detailed
  implementation and methods

- Utilities (:mod:`pcapkit.utilities`)

  collection of utility functions and classes

- CoreKit (:mod:`pcapkit.corekit`)

  core utilities for :mod:`pcapkit` implementation

- ToolKit (:mod:`pcapkit.toolkit`)

  utility tools for :mod:`pcapkit` implementation

- DumpKit (:mod:`pcapkit.dumpkit`)

  dump utilities for :mod:`pcapkit` implementation

"""
import os
import warnings

import tbtrim

from pcapkit.utilities.exceptions import BaseError
from pcapkit.utilities.logging import DEVMODE
from pcapkit.utilities.warnings import DevModeWarning

# set up sys.excepthook
if DEVMODE:
    warnings.showwarning('development mode enabled', DevModeWarning,
                         filename=__file__, lineno=0,
                         line=f"PCAPKIT_DEVMODE={os.environ['PCAPKIT_DEVMODE']}")
else:
    ROOT = os.path.dirname(os.path.realpath(__file__))
    tbtrim.set_trim_rule(lambda filename: ROOT in os.path.realpath(filename),
                         exception=BaseError, strict=False)

from pcapkit.foundation.registry import *
from pcapkit.interface import *
from pcapkit.protocols import *
from pcapkit.toolkit import *

__all__ = [
    'extract', 'reassemble', 'trace',                       # Interface Functions

    'TREE', 'JSON', 'PLIST', 'PCAP',                        # Format Macros
    'LINK', 'INET', 'TRANS', 'APP', 'RAW',                  # Layer Macros
    'DPKT', 'Scapy', 'PyShark', 'PCAPKit',                  # Engine Macros

    # Protocol Numbers
    'LINKTYPE', 'ETHERTYPE', 'TRANSTYPE',

    'NoPayload',                                            # No Payload
    'Raw',                                                  # Raw Packet

    'ARP', 'Ethernet', 'L2TP', 'OSPF', 'RARP', 'VLAN',      # Link Layer

    'AH', 'IP', 'IPsec', 'IPv4', 'IPv6', 'IPX',             # Internet Layer
    'HIP', 'HOPOPT', 'IPv6_Frag', 'IPv6_Opts', 'IPv6_Route', 'MH',
                                                            # IPv6 Extension Header

    'TCP', 'UDP',                                           # Transport Layer

    'FTP', 'HTTP',                                          # Application Layer
]
