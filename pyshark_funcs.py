import pyshark

def get_packets(interface="en0", timeout=20):
    """
    Gets packets to explore.
    """
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(timeout=timeout)

    
    for packet in capture:
        print(f"Source:  {packet.ip.src} , Destination: {packet.ip.dst}")