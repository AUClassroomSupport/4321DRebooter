from mojo import context
from svsitcpsender import SVSiTCPSend
import datetime

context.log.info('4321DRebooter Script Running on CoEdNx<NUMBER>!')

# Device List: list of 4321D IPs to reboot
deviceList = []
deviceList.append("IP")

# minTick - called every minute
# see https://docs.python.org/3.6/library/datetime.html#strftime-strptime-behavior
def minTick(e):
    if datetime.datetime.now().strftime("%w") == "0": # if day is Sunday (0)
        if datetime.datetime.now().strftime("%H%M") == "0100": # If Time is 1AM
            context.log.info("Its Sunday at 1am, rebooting 4321Ds on CoEdNx<NUMBER>")
            for ip in deviceList:
                if SVSiTCPSend(ip, "setSettings:reboot:reboot"):
                    context.log.info('Success!')

# Timer Setup
rebootTimer = context.services.get("timeline")
rebootTimer.start([60000],True,-1) # Runs until killed
rebootTimer.expired.listen(minTick)

# leave this as the last line in the Python script
context.run(globals())