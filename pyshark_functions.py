import pyshark

def get_packets():
    capture = pyshark.LiveCapture()
    capture.sniff(timeout=5)
    return capture

if __name__ == "__main__":
    # This code will only be executed if the script is run directly
    capture = get_packets()
    print(capture[3])
