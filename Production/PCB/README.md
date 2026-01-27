# Production PCB Files

This directory contains manufacturing files for PCB fabrication.

## Files

- **Hexadecipad_V2_TDSOTM_Edition.zip** - Gerbers and drill files

- **netlist.ipc** - IPC-356 netlist file for electrical testing and verification of the manufactured PCB

## Ordering PCBs

### Upload Files
1. Upload `Hexadecipad_V2_TDSOTM_Edition.zip` to your PCB manufacturer (JLCPCB, PCBWay, OSH Park, etc.)

### Recommended Specifications
- Check the main PCB.md file in `/PCB/HexadecipadV2/` for detailed specifications
- Common settings:
  - **Layers:** 2
  - **PCB Thickness:** 1.6mm (standard)
  - **Surface Finish:** HASL or ENIG
  - **Copper Weight:** 1oz (35μm)

### Assembly
- For hand assembly, use the interactive BOM in `/PCB/HexadecipadV2/bom/ibom.html`
- For automated assembly, the pick-and-place files are included in the ZIP

## Quality Control

The `netlist.ipc` file can be used by the manufacturer or for in-house testing to verify:
- All connections are correct
- No short circuits exist
- All nets are properly connected
