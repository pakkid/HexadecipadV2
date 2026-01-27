# Production Firmware

This directory contains production-ready firmware files for the HexadecipadV2.

## Files

- **adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.0.3.uf2** - CircuitPython 10.0.3 firmware for the Seeed Studio XIAO RP2040

### CIRCUITPY/
Directory structure to be copied to the device after CircuitPython installation:
- **main.py** - Main firmware application
- **lib/** - Required CircuitPython libraries and dependencies

## Installation Instructions

### Step 1: Install CircuitPython Bootloader
1. Connect your XIAO RP2040 to your computer via USB
2. Press the RESET button twice quickly to enter bootloader mode
3. A drive named "RPI-RP2" should appear
4. Copy `adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.0.3.uf2` to the RPI-RP2 drive
5. The device will automatically reboot and appear as "CIRCUITPY"

### Step 2: Install Firmware
1. Copy the entire contents of the `CIRCUITPY/` folder to the CIRCUITPY drive
2. Ensure `main.py` is in the root of the CIRCUITPY drive
3. Copy the `lib/` folder and its contents to the CIRCUITPY drive
4. The device will automatically restart and run the firmware

## Troubleshooting

- If the device doesn't appear as CIRCUITPY after step 1, try pressing RESET twice again
- If there are errors, check the `serial console` for error messages
- Ensure all required libraries are present in the `lib/` folder
