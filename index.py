from mojo import context
from svsitcpsender import SVSiTCPSend
context.log.info('Resetting 4321D')

if SVSiTCPSend("192.168.0.40", "setSettings:reboot:reboot"):
    context.log.info('Success!')

# leave this as the last line in the Python script
context.run(globals())
