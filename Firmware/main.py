"""
Hexadecipad V2 Firmware
Pure CircuitPython - reads matrix and encoders, sends data over USB serial
No keyboard framework needed - just raw I/O and protocol
"""

import board
import busio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
import usb_cdc

# I2C configuration - SDA on GPIO6 (D4), SCL on GPIO7 (D5)
i2c = busio.I2C(board.D5, board.D4)  # D5=SCL (GPIO7), D4=SDA (GPIO6)
mcp = MCP23017(i2c, address=0x20)    # A0, A1, A2 all grounded = 0x20

console = usb_cdc.console

def send_message(message):
    """Send message over USB serial"""
    try:
        console.write(message + "\n")
    except:
        pass

# ============================================================================
# MCP23017 PIN CONFIGURATION
# ============================================================================

# GPIOA pins (0-7)
GPA0 = mcp.get_pin(0)   # Column 4
GPA1 = mcp.get_pin(1)   # Column 3
GPA2 = mcp.get_pin(2)   # Column 2
GPA3 = mcp.get_pin(3)   # Unused
GPA4 = mcp.get_pin(4)   # Unused
GPA5 = mcp.get_pin(5)   # Unused
GPA6 = mcp.get_pin(6)   # Unused
GPA7 = mcp.get_pin(7)   # Unused

# GPIOB pins (8-15)
GPB0 = mcp.get_pin(8)   # Row 0
GPB1 = mcp.get_pin(9)   # Row 1
GPB2 = mcp.get_pin(10)  # Row 2
GPB3 = mcp.get_pin(11)  # Row 3
GPB4 = mcp.get_pin(12)  # Row 4
GPB5 = mcp.get_pin(13)  # Row 5
GPB6 = mcp.get_pin(14)  # Column 0
GPB7 = mcp.get_pin(15)  # Column 1

# Matrix layout
rows = [GPB0, GPB1, GPB2, GPB3, GPB4, GPB5]
cols = [GPB6, GPB7, GPA2, GPA1, GPA0]

# Configure pins as inputs/outputs
# Rows are outputs (driven low to select), Columns are inputs (pulled high)
for row in rows:
    row.switch_to_output(value=True)

for col in cols:
    col.switch_to_input(pull=board.Pull.UP)

# ============================================================================
# ENCODER PINS (RP2040 GPIO)
# ============================================================================

# Xiao RP2040 pin mapping: D0=GPIO26, D1=GPIO27, D2=GPIO28, D3=GPIO29, D7=GPIO1, D8=GPIO2, D9=GPIO4, D10=GPIO3
encoder_pins = [
    (board.D3, board.D2),    # Encoder 1: A=GPIO29/D3, B=GPIO28/D2
    (board.D1, board.D0),    # Encoder 2: A=GPIO27/D1, B=GPIO26/D0
    (board.D10, board.D9),   # Encoder 3: A=GPIO3/D10, B=GPIO4/D9
    (board.D8, board.D7),    # Encoder 4: A=GPIO2/D8, B=GPIO1/D7
]

# Initialize encoder pins as inputs
for pin_a, pin_b in encoder_pins:
    pin_a.switch_to_input()
    pin_b.switch_to_input()

# Track encoder states for detecting rotation
encoder_states = [None] * 4  # Previous state for each encoder
encoder_transitions = {
    # Clockwise transitions (Gray code)
    (0b11, 0b01): 'UP',
    (0b01, 0b00): 'UP',
    (0b00, 0b10): 'UP',
    (0b10, 0b11): 'UP',
    
    # Counter-clockwise transitions
    (0b11, 0b10): 'DOWN',
    (0b10, 0b00): 'DOWN',
    (0b00, 0b01): 'DOWN',
    (0b01, 0b11): 'DOWN',
}

# ============================================================================
# MATRIX SCANNING & KEY TRACKING
# ============================================================================

# Track which keys are currently pressed
key_states = {}  # (row, col) -> is_pressed

# Matrix layout: sparse layout with only certain keys in each row
# Row 0: 4 keys (cols 0-3)
# Row 1-4: 5 keys (cols 0-4)
# Row 5: 4 keys (cols 0-3)
VALID_KEYS = {
    0: [0, 1, 2, 3],           # Row 0: 4 keys
    1: [0, 1, 2, 3, 4],        # Row 1: 5 keys
    2: [0, 1, 2, 3, 4],        # Row 2: 5 keys
    3: [0, 1, 2, 3, 4],        # Row 3: 5 keys
    4: [0, 1, 2, 3, 4],        # Row 4: 5 keys
    5: [0, 1, 2, 3],           # Row 5: 4 keys
}

def scan_matrix():
    """Scan matrix and detect key presses/releases"""
    for row_idx, row_pin in enumerate(rows):
        # Drive this row low, all others high
        for i, r in enumerate(rows):
            r.value = (i != row_idx)
        
        time.sleep(0.001)  # Debounce delay
        
        # Read columns for this row
        for col_idx in VALID_KEYS[row_idx]:
            col_pin = cols[col_idx]
            is_pressed = not col_pin.value  # Column pulled low = key pressed
            
            key_id = (row_idx, col_idx)
            old_state = key_states.get(key_id, False)
            
            if is_pressed != old_state:
                key_states[key_id] = is_pressed
                
                if is_pressed:
                    send_message(f"KEY_R{row_idx}C{col_idx}_PRESSED")
                else:
                    send_message(f"KEY_R{row_idx}C{col_idx}_RELEASED")
        
        # Return all rows to high
        for r in rows:
            r.value = True

def read_encoders():
    """Read encoder rotations"""
    for enc_idx, (pin_a, pin_b) in enumerate(encoder_pins):
        # Read Gray code state: (A << 1) | B
        current_state = (pin_a.value << 1) | pin_b.value
        previous_state = encoder_states[enc_idx]
        
        # Update state
        encoder_states[enc_idx] = current_state
        
        # Detect transitions
        if previous_state is not None:
            transition = (previous_state, current_state)
            if transition in encoder_transitions:
                direction = encoder_transitions[transition]
                send_message(f"ENC{enc_idx+1}_{direction}")

# ============================================================================
# MAIN LOOP
# ============================================================================

# Send startup message
send_message("DEVICE_READY")

# Timing
last_encoder_check = time.monotonic()
encoder_check_interval = 0.005  # Check encoders every 5ms
last_matrix_scan = time.monotonic()
matrix_scan_interval = 0.010     # Scan matrix every 10ms

print("Hexadecipad V2 firmware running...")

while True:
    current_time = time.monotonic()
    
    # Matrix scanning
    if current_time - last_matrix_scan >= matrix_scan_interval:
        scan_matrix()
        last_matrix_scan = current_time
    
    # Encoder reading
    if current_time - last_encoder_check >= encoder_check_interval:
        read_encoders()
        last_encoder_check = current_time
    
    time.sleep(0.001)  # Small delay to prevent spinning

