import socket
import serial
import time

# --- Config ---
ROT_HOST = "127.0.0.1"
ROT_PORT = 4533
SERIAL_PORT = "COM6"   # change to your Arduino's COM port
BAUD_RATE = 115200
POLL_INTERVAL = 0.5    # seconds between updates
# --------------

def connect_rotctld():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ROT_HOST, ROT_PORT))
    s.settimeout(2.0)
    return s

def get_position(sock):
    sock.sendall(b"p\n")
    response = sock.recv(64).decode().strip()
    lines = response.split("\n")
    az = float(lines[0])
    el = float(lines[1])
    return az, el

def main():
    print(f"Connecting to rotctld at {ROT_HOST}:{ROT_PORT}...")
    sock = connect_rotctld()
    print("Connected to rotctld")

    print(f"Opening serial port {SERIAL_PORT} at {BAUD_RATE} baud...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # wait for Arduino to reset after serial connect
    print("Serial port open\n")

    try:
        while True:
            az, el = get_position(sock)
            msg = f"AZ:{az:.1f} EL:{el:.1f}\n"
            ser.write(msg.encode())
            print(msg.strip())
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()
        sock.close()

if __name__ == "__main__":
    main()