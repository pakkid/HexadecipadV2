# CAD Directory

This directory contains all Computer-Aided Design (CAD) files for the HexadecipadV2 case and mechanical design.

## Files

### Case Design Files

- **Case-Production.shapr** - Shapr3D native file format for the case design (editable source file)
- **Case.step** - STEP format export of the case design for universal CAD compatibility
- **Case.x_t** - Parasolid format export of the case design
- **HexadecipadV2-assembled.step** - Complete assembled model in STEP format showing the full device assembly
- **platecutout.dxf** - DXF file for the switch plate cutout pattern, used for laser cutting or CNC machining

## File Formats

- `.shapr` - Shapr3D native format (requires Shapr3D software)
- `.step` / `.stp` - Industry-standard 3D CAD format, compatible with most CAD software
- `.x_t` - Parasolid format, widely supported in professional CAD applications
- `.dxf` - 2D drawing exchange format for manufacturing processes

## Usage

The production-ready files for manufacturing are:
- `platecutout.dxf` for the switch plate
- `Case.step` or `Case.x_t` for the case (depending on your manufacturer's preference)
