# PCB Directory

This directory contains the printed circuit board (PCB) design files for HexadecipadV2.

## Subdirectories

### HexadecipadV2/
Main PCB design directory containing all KiCad project files:

#### Project Files
- **HexadecipadV2.kicad_pro** - KiCad project file
- **HexadecipadV2.kicad_sch** - KiCad schematic file
- **HexadecipadV2.kicad_pcb** - KiCad PCB layout file
- **HexadecipadV2.kicad_prl** - KiCad project local settings
- **HexadecipadV2.step** - 3D model export of the PCB

#### Configuration Files
- **fp-lib-table** - Footprint library table
- **sym-lib-table** - Symbol library table
- **fp-info-cache** - Footprint information cache

#### Subdirectories
- **3d models/** - Component 3D models for PCB visualization
- **bom/** - Bill of Materials files (includes `ibom.html` - Interactive HTML BOM)
- **libraries/** - Custom KiCad libraries including footprints and symbols
  - `Hackpad/` - Custom Hackpad symbols and footprints
  - `kicad-keyboard-parts.pretty-master/` - Keyboard-specific footprints
  - `MX_V2-main/` - MX switch footprint library
  - `OPL_Kicad_Library-master/` - Open Parts Library
  - `RotaryEncoder/` - Rotary encoder components
- **HexadecipadV2-backups/** - Automatic KiCad backup files

## Software Requirements

- KiCad 7.0 or later (recommended for full compatibility)

## Usage

1. Open `HexadecipadV2.kicad_pro` in KiCad to view and edit the design
2. Use `ibom.html` in the `bom/` folder for assembly reference
3. For manufacturing files, see the `/Production/PCB/` directory
