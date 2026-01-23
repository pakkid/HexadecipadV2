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

 - **[Interactive BOM](PCB/HexadecipadV2/bom/ibom.html)**

## Design Files

- **Schematic:** [PCB/HexadecipadV2/HexadecipadV2.kicad_sch](PCB/HexadecipadV2/HexadecipadV2.kicad_sch)
- **PCB Layout:** [PCB/HexadecipadV2/HexadecipadV2.kicad_pcb](PCB/HexadecipadV2/HexadecipadV2.kicad_pcb)
- **PCB 3D Model:** [PCB/HexadecipadV2/HexadecipadV2.step](PCB/HexadecipadV2/HexadecipadV2.step)
- **Case Design:** [CAD/HexadecipadV2-assembled.step](CAD/HexadecipadV2-assembled.step)

### Firmware

Refer to the [Firmware](Firmware/) to see my stupid code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
