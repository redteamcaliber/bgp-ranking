#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Blocklist.de parsers
    ~~~~~~~~~~~~~~~~~~~~

    Class used to parse the blocklists provided by blocklist.de
"""

from modules.abstract_module_default import AbstractModuleDefault

class BlocklistDeSsh(AbstractModuleDefault):

    def __init__(self, raw_dir):
        self.directory = 'blocklist_de/ssh/'
        AbstractModuleDefault.__init__(self)

class BlocklistDeMail(AbstractModuleDefault):

    def __init__(self, raw_dir):
        self.directory = 'blocklist_de/mail/'
        AbstractModuleDefault.__init__(self)

class BlocklistDeApache(AbstractModuleDefault):

    def __init__(self, raw_dir):
        self.directory = 'blocklist_de/apache/'
        AbstractModuleDefault.__init__(self)

class BlocklistDePop3(AbstractModuleDefault):

    def __init__(self, raw_dir):
        self.directory = 'blocklist_de/pop3/'
        AbstractModuleDefault.__init__(self)

class BlocklistDeFtp(AbstractModuleDefault):

    def __init__(self, raw_dir):
        self.directory = 'blocklist_de/ftp/'
        AbstractModuleDefault.__init__(self)
