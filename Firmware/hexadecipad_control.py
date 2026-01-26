"""
Hexadecipad V2 Control Application
Listens to custom USB serial protocol from RP2040 and controls audio/apps
Protocol format:
  - KEY_R#C#_PRESSED: Key press (Row/Column)
  - KEY_R#C#_RELEASED: Key release
  - ENC#_UP: Encoder rotation up
  - ENC#_DOWN: Encoder rotation down
  - ENC#_PRESSED: Encoder button press
  - ENC#_RELEASED: Encoder button release
"""

import serial
import serial.tools.list_ports
import time
import os
import subprocess
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import threading

class HexadecipadController:
    def __init__(self, port=None, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False
        
        # Action configuration - customize these per your needs
        self.action_map = {
            # Encoder 1: Spotify volume
            'ENC1_UP': lambda: self.change_app_volume('spotify', 0.02),
            'ENC1_DOWN': lambda: self.change_app_volume('spotify', -0.02),
            'ENC1_PRESSED': lambda: self.toggle_app_mute('spotify'),
            
            # Encoder 2: Discord volume
            'ENC2_UP': lambda: self.change_app_volume('discord', 0.02),
            'ENC2_DOWN': lambda: self.change_app_volume('discord', -0.02),
            'ENC2_PRESSED': lambda: self.toggle_app_mute('discord'),
            
            # Encoder 3: Game volume
            'ENC3_UP': lambda: self.change_app_volume('game', 0.02),
            'ENC3_DOWN': lambda: self.change_app_volume('game', -0.02),
            'ENC3_PRESSED': lambda: self.toggle_app_mute('game'),
            
            # Encoder 4: Master volume
            'ENC4_UP': lambda: self.change_master_volume(0.02),
            'ENC4_DOWN': lambda: self.change_master_volume(-0.02),
            'ENC4_PRESSED': lambda: self.toggle_master_mute(),
            
            # Customizable key actions
            'KEY_R0C0_PRESSED': lambda: print("Key R0C0 pressed"),
            'KEY_R0C1_PRESSED': lambda: print("Key R0C1 pressed"),
            'KEY_R0C2_PRESSED': lambda: print("Key R0C2 pressed"),
            'KEY_R0C3_PRESSED': lambda: print("Key R0C3 pressed"),
            
            'KEY_R5C0_PRESSED': lambda: self.launch_spotify(),
            'KEY_R5C1_PRESSED': lambda: print("Key R5C1 pressed"),
            'KEY_R5C2_PRESSED': lambda: print("Key R5C2 pressed"),
            'KEY_R5C3_PRESSED': lambda: print("Key R5C3 pressed"),
            
            # Row 1-4 keys
            'KEY_R1C0_PRESSED': lambda: print("Key R1C0 pressed"),
            'KEY_R1C1_PRESSED': lambda: print("Key R1C1 pressed"),
            'KEY_R1C2_PRESSED': lambda: print("Key R1C2 pressed"),
            'KEY_R1C3_PRESSED': lambda: print("Key R1C3 pressed"),
            'KEY_R1C4_PRESSED': lambda: print("Key R1C4 pressed"),
            # ... add more as needed
        }
        
        # App names for volume control
        self.app_names = {
            'spotify': ['spotify.exe'],
            'discord': ['discord.exe'],
            'game': ['java.exe', 'Valorant.exe', 'RustClient.exe', 'csgo.exe'],  # Add game executables
            'chrome': ['chrome.exe'],
            'firefox': ['firefox.exe'],
        }
    
    def find_device(self):
        """Auto-detect Hexadecipad serial port"""
        ports = serial.tools.list_ports.comports()
        for port in ports:
            # Look for RP2040 or CircuitPython devices
            if 'XIAO' in port.description or 'RP2040' in port.description or 'CircuitPython' in port.description:
                return port.device
        
        # Fallback: use first available COM port
        if ports:
            return ports[0].device
        return None
    
    def connect(self):
        """Connect to the Hexadecipad device"""
        if not self.port:
            self.port = self.find_device()
            if not self.port:
                print("Error: Could not find device. Specify port manually.")
                return False
        
        try:
            print(f"Connecting to {self.port}...")
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for connection to stabilize
            print(f"Connected to {self.port}")
            return True
        except Exception as e:
            print(f"Error connecting: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from device"""
        if self.ser:
            self.ser.close()
            print("Disconnected")
    
    def run(self):
        """Main loop - listen for messages and execute actions"""
        if not self.connect():
            return
        
        self.running = True
        print("Listening for commands... (Press Ctrl+C to exit)")
        print("Protocol format: ENC1_UP, ENC1_DOWN, KEY_R1C2_PRESSED, etc.")
        
        try:
            while self.running:
                if self.ser and self.ser.in_waiting:
                    try:
                        message = self.ser.readline().decode('utf-8').strip()
                        if message:
                            self.handle_message(message)
                    except Exception as e:
                        print(f"Error reading: {e}")
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("\nExiting...")
        finally:
            self.disconnect()
    
    def handle_message(self, message):
        """Process incoming message and execute corresponding action"""
        print(f"Received: {message}")
        
        if message in self.action_map:
            try:
                self.action_map[message]()
            except Exception as e:
                print(f"Error executing action: {e}")
        elif message == "DEVICE_READY":
            print("Device initialized")
        else:
            print(f"Unknown command: {message}")
    
    def get_app_volume(self, app_name):
        """Get audio session for specific app"""
        app_names = self.app_names.get(app_name.lower(), [app_name])
        sessions = AudioUtilities.GetAllSessions()
        
        for session in sessions:
            if session.Process:
                exe_name = os.path.basename(session.Process.name()).lower()
                if any(name.lower() in exe_name for name in app_names):
                    return session.SimpleAudioVolume
        return None
    
    def change_app_volume(self, app_name, delta):
        """Change volume for specific app"""
        volume = self.get_app_volume(app_name)
        if volume:
            try:
                current = volume.GetMasterVolume()
                new_volume = max(0.0, min(1.0, current + delta))
                volume.SetMasterVolume(new_volume, None)
                pct = int(new_volume * 100)
                print(f"{app_name}: {pct}%")
            except Exception as e:
                print(f"Error changing volume: {e}")
        else:
            print(f"{app_name}: Not running")
    
    def toggle_app_mute(self, app_name):
        """Toggle mute for specific app"""
        volume = self.get_app_volume(app_name)
        if volume:
            try:
                current_mute = volume.GetMute()
                volume.SetMute(not current_mute, None)
                state = "unmuted" if current_mute else "muted"
                print(f"{app_name}: {state}")
            except Exception as e:
                print(f"Error toggling mute: {e}")
        else:
            print(f"{app_name}: Not running")
    
    def change_master_volume(self, delta):
        """Change system master volume"""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(ISimpleAudioVolume)
            
            current = volume.GetMasterVolume()
            new_volume = max(0.0, min(1.0, current + delta))
            volume.SetMasterVolume(new_volume, None)
            pct = int(new_volume * 100)
            print(f"Master: {pct}%")
        except Exception as e:
            print(f"Error changing master volume: {e}")
    
    def toggle_master_mute(self):
        """Toggle system master mute"""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(ISimpleAudioVolume)
            
            current_mute = volume.GetMute()
            volume.SetMute(not current_mute, None)
            state = "unmuted" if current_mute else "muted"
            print(f"Master: {state}")
        except Exception as e:
            print(f"Error toggling master mute: {e}")
    
    def launch_spotify(self):
        """Launch Spotify"""
        try:
            subprocess.Popen(['spotify'])
            print("Launching Spotify...")
        except Exception as e:
            print(f"Error launching Spotify: {e}")
    
    def configure_action(self, command, action):
        """Dynamically configure an action"""
        self.action_map[command] = action
        print(f"Configured: {command}")


if __name__ == '__main__':
    # Auto-detect device, or specify port manually
    controller = HexadecipadController()  # auto-detect
    # controller = HexadecipadController(port='COM3')  # manual port
    
    # Optional: Configure custom actions at runtime
    # controller.action_map['KEY_R1C0_PRESSED'] = lambda: print("Custom action!")
    
    controller.run()
