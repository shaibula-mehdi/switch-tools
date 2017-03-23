import subprocess #use for net-snmp
import re
import telnetlib
from socket import error as socket_error

class SwitchTolls():
  """docs, add later"""
  def __init__(self, arg)
    pass

def get_vendor(host):
  """later, need net-snmp lib, www.net-snmp.org"""
  pass

def bulk(self, cmd, opt):
  pass

class DLink():
  """docs, add later"""
  def __init(self):
    self.session = telnetlib.Telnet()
    self.session.set_option_negotiation(bulk) #for fast opertaion, this disable func WILL, DO, WONT etc
    #self.session.set_debuglevel(0)
    self.connect_state = False
    self.auth_state = False
  
  def connect():
    pass
  
  def auth():
    pass
  
  def disconnect():
    pass
  
  def send():
    pass
