# Production Directory

This directory contains production-ready files for manufacturing and assembly of the HexadecipadV2.

## Subdirectories

### CAD/
3D printable STL files for case manufacturing:
- **Case bottom.stl** - Bottom half of the case
- **Case top.stl** - Top half of the case
- **Plate.stl** - Switch mounting plate

### Firmware/
Production firmware ready for deployment:
- **adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.0.3.uf2** - CircuitPython bootloader/runtime for XIAO RP2040
- **CIRCUITPY/** - Directory structure to be copied to the device
  - `main.py` - Production firmware main file
  - `lib/` - Required CircuitPython libraries

### PCB/
Manufacturing files for PCB fabrication:
- **Hexadecipad_V2_TDSOTM_Edition.zip** - Complete Gerber files and manufacturing package for PCB production
- **netlist.ipc** - IPC-356 netlist for PCB testing and verification

## Manufacturing Instructions

### PCB
1. Send `Hexadecipad_V2_TDSOTM_Edition.zip` to your PCB manufacturer
2. Recommended specs: Check the PCB.md file in /PCB/HexadecipadV2/

### Case
1. 3D print the STL files in the CAD/ directory
2. Recommended settings: 0.2mm layer height, 20% infill or higher
3. Material: PLA, ABS, or really whatever you want

### Firmware Installation
1. Flash `adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-10.0.3.uf2` to the XIAO RP2040 by entering bootloader mode
2. Copy contents of `CIRCUITPY/` to the mounted CIRCUITPY drive
3. Device will automatically restart with the firmware
