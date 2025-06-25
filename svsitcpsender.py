
from socket import *
from mojo import context

def SVSiTCPSend(ip, str):
    context.log.info('SVSi TCP Send Activated! Sending {} to {}'.format(str, ip))

    try:
        with socket(AF_INET,SOCK_STREAM) as sock:
            sock.connect((ip, 50001))
            
            # convert command string into bytes and send
            sock.sendall(bytes(str, 'ascii'))

            # receive datapacket back from command and send to status parser
            data=sock.recv(2048)

    except ConnectionRefusedError:
        context.log.info('Device {} refused connection, Marking offline'.format(ip))
        return False
    
    except TimeoutError:
        context.log.info('Device {} connection timed out, Marking offline'.format(ip))
        return False
    
    except OSError as e:
        context.log.info('OS Error {} occurred while sending to Device {}, Marking offline'.format(e, ip))
        return False
    
    # If we got data back, send it to parser and return True
    return True