Charge-Sensitive Preamplifier (CSP) Front-End

Objective: 
Design an ultra-low bias current analog front-end to integrate a 1 pC fast current pulse (simulating a particle strike on a 70 pF PIN photodiode) into a measurable voltage step.

Architecture & Math:
Op-Amp: OPA656 (JFET input for low current noise).
Gain Stage: Feedback capacitor $C_f = 1\text{ pF}$ designed to yield a step voltage of $-1\text{ V}$ for a $1\text{ pC}$ input charge.
Discharge Path: Feedback resistor $R_f = 50\text{ M}\Omega$ placed in parallel to prevent saturation, setting a continuous discharge time constant of $\tau = 50\ \mu\text{s}$.

Analysis: 
Transient analysis confirms the theoretical derivations. The initial charge injection drives the output to approximately -900 mV. At $t = 50\ \mu\text{s}$, the signal decays to -330 mV, perfectly aligning with the $e^{-1}$ theoretical discharge curve.