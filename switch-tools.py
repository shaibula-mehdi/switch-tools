import subprocess #use for net-snmp
import re
import telnetlib
from socket import error as socket_error

#cos different command syntax
DLINK_DES3526 = []
DLINK_C1 = []
DLINK_3010 = []
DLINK_A1B1 = []
DLINK_OTHER = []

CISCO_ME3XXX = []
EDGECORE = []

def get_vendor(host):
  """later, need net-snmp lib, www.net-snmp.org"""
  pass

def bulk(self, cmd, opt):
  pass

def selector(host, model):
  if model in DLINK_DES3526:
    pass
  elif model in DLINK_C1:
    pass
  elif model in DLINK_3010:
    pass
  elif model in DLINK_A1B1:
    pass
  elif model in DLINK_OTHER:
    pass
  elif model in CISCO_ME3XXX:
    pass
  elif model in EDGECORE:
    pass


def connection(host, opt_negotiation = False):
  try:
    session = telnetlib.Telnet()
    if opt_negotiation == True:
      session.set_option_negotiation(bulk)
  except socket_error as e:
    print(e)
    

def auth(connection):
  pass
  
  
def sender(connection):
  pass


