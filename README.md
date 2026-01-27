# HexadecipadV2

A fully customizable macro pad with 24 mechanical switches and 4 rotary encoders, designed with KiCAD and featuring an little baby RP2040 microcontroller.

## Overview

HexadecipadV2 is hackpad designed for the blueprint/hackpad ysws. I spent about 6 hours pulling my hair out over case design before I knew what I was doing... ps. I still have no idea what I'm doing.

**Key Features:**
- 24 hot-swap MX-compatible mechanical switches (oops)
- 4 rotary encoders for volume control, scrolling, or custom functions (more oops)
- Seeed Studio XIAO RP2040 microcontroller
- MCP23017 I/O expander because XIAO RP2040 is little baby.
- Open-source KiCAD design because i broke.
- 3D-printed case 👍
- Too many inputs. checked with Blueprint Support, they said its fine as long as I pay.
- Too big pcb (100mmx130mm) also checked with Blueprint staff.
- Fully custom vibe coded garbage script that send serial to a python script on my pc so we can modify keys without having to use stupid kmk.

## Project Structure (just the READMEs for when you access on github.io)

```
HexadecipadV2/
├── CAD/                     # Case and mechanical design files
│   └── README.md            # CAD file documentation
├── Firmware/                # Source firmware code
│   └── README.md            # Firmware documentation
├── PCB/                     # KiCad PCB design files
│   └── HexadecipadV2/       # Main PCB project
│       └── README.md        # PCB documentation
├── Production/              # Manufacturing-ready files
│   ├── CAD/                 # STL files for 3D printing
│   │   └── README.md        # 3D printing guide
│   ├── Firmware/            # Production firmware
│   │   └── README.md        # Firmware installation guide
│   ├── PCB/                 # Gerber files for PCB fab
│   │   └── README.md        # PCB ordering guide
│   └── README.md            # Production overview
└── Other files/             # Supporting files
    ├── 3d models/           # Component STEP models
    │   └── README.md        # 3D models documentation
    ├── images/              # Documentation images
    │   └── README.md        # Images documentation
    └── README.md            # Other files overview
```

### Links and stuff
- **[CAD Files](CAD/)** - Case design and mechanical files
- **[Firmware](Firmware/)** - Source code and development files
- **[PCB Design](PCB/)** - KiCad project and design files
- **[Production Files](Production/)** - Ready-to-manufacture files
  - [3D Printable Case Files](Production/CAD/)
  - [Production Firmware](Production/Firmware/)
  - [PCB Manufacturing Files](Production/PCB/)
- **[Other Files](Other%20files/)** - Component models and documentation images
 
## Screenshots

### Hackpad

![Hackpad Overview](Other%20files/images/case%20with%20pcb.png)

### Schematic

![Schematic](Other%20files/images/schematic.png)

### PCB

**PCB Filled:**
![PCB Filled](Other%20files/images/pcb%20filled.png)

**PCB Unfilled:**
![PCB Unfilled](Other%20files/images/pcb%20unfilled.png)

### Case Assembly

![Case Assembly](Other%20files/images/case%20with%20pcb.png)

## Bill of Materials (BOM)

| # | References | Value | Footprint | Quantity |
|---|------------|-------|-----------|----------|
| 1 | R1, R2 | R | R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal | 2 |
| 2 | D1–D28 | D | D_DO-35_SOD27_P7.62mm_Horizontal | 28 |
| 3 | U1 | XIAO-RP2040-DIP | XIAO-RP2040-DIP | 1 |
| 4 | U2 | MCP23017_SP | DIP-28_W7.62mm | 1 |
| 5 | SW5–SW28 | SW_Push_45deg | MX-Hotswap-1U | 24 |
| 6 | SW1–SW4 | Encoder | RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm | 4 |
| 7 | N/A | M3x16mm screws | N/A | 4 |

 - **[Interactive BOM](https://hxdcpd.stuffandthings.cc/PCB/HexadecipadV2/bom/ibom.html)**

## Design Files

- **Schematic:** [PCB/HexadecipadV2/HexadecipadV2.kicad_sch](PCB/HexadecipadV2/HexadecipadV2.kicad_sch)
- **PCB Layout:** [PCB/HexadecipadV2/HexadecipadV2.kicad_pcb](PCB/HexadecipadV2/HexadecipadV2.kicad_pcb)
- **PCB 3D Model:** [PCB/HexadecipadV2/HexadecipadV2.step](PCB/HexadecipadV2/HexadecipadV2.step)
- **Case Design:** [CAD/HexadecipadV2-assembled.step](CAD/HexadecipadV2-assembled.step)

### Firmware

Have a look at [Firmware](Firmware/) to see my stupid code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributing will probably end up with me being fried because of my terrible everything in this project.