# OpenDAQ Mixed-Signal Analog Front-End (AFE)

## Overview
This repository contains the design, simulation, and PCB layout for an ultra-low noise Analog Front-End (AFE) intended for high-energy physics data acquisition (OpenDAQ). 

The system is designed to detect a **1 pC fast current pulse** (simulating a particle strike on a 70 pF PIN photodiode), integrate the charge, shape it into a measurable semi-Gaussian pulse, and digitize the transient event using a custom-built 3-Bit Flash ADC.

## Project Status
* **Phase 1: Mixed-Signal Simulation** $\rightarrow$ **[COMPLETE]**
* **Phase 2: 4-Layer PCB Hardware Layout** $\rightarrow$ **[IN PROGRESS]**

## System Architecture

### 1. Charge-Sensitive Preamplifier (CSP)
* **Function:** Integrates the femtocoulomb-level particle strike into a measurable voltage step.
* **Key Specs:** Utilizes a JFET-input OPA656 for ultra-low bias current. Configured with a 1 pF feedback capacitor (yielding a -1V/pC step) and a 50 M$\Omega$ continuous discharge path ($\tau = 50\ \mu\text{s}$).

### 2. Active Pulse Shaper
* **Function:** Differentiates and filters the CSP output into a smooth, baseline-restored semi-Gaussian pulse for accurate peak detection.
* **Key Specs:** Produces a clean 720 mV peak spanning roughly 1 to 2 microseconds.

### 3. 3-Bit Flash ADC (Mixed-Signal)
* **Function:** Digitizes the fast transient analog pulse into binary data.
* **Key Specs:** 8-resistor reference ladder (0V to 800mV) driving parallel comparators.

## Engineering Highlights
During the simulation phase, critical hardware bandwidth bottlenecks were identified and resolved. Legacy architectures (like the LM741) were proven mathematically insufficient due to slew-rate limitations ($0.5\text{ V}/\mu\text{s}$) when digitizing sub-microsecond particle strikes. To validate the digital logic against the fast analog pulse, the vendor macro-models were bypassed using mathematical arbitrary behavioral modeling in Ngspice.

$\rightarrow$ **[Read the full Simulation & Slew Rate Analysis Here](simulations_spice/Simulation_README.md)**

---
*Designed in KiCad. Transient analysis verified with Ngspice and Python (Matplotlib).*
