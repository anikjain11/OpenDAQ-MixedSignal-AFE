import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the exported KiCad CSV
df = pd.read_csv('adc_digital_out.csv', sep=';')
df.columns = df.columns.str.strip()
df = df.apply(pd.to_numeric, errors='coerce')

# Convert time to microseconds
time = df.iloc[:, 0] * 1e6  

# 2. Set up a 4-row stacked layout
fig, axs = plt.subplots(4, 1, figsize=(10, 9), sharex=True)
fig.suptitle('OpenDAQ Mixed-Signal AFE: 3-Bit Flash ADC Transient Response', fontsize=14, fontweight='bold')

# 3. Plot BIT_2 (MSB)
axs[0].plot(time, df['V(/BIT_2)'], color='blue', linewidth=2)
axs[0].set_ylabel('BIT_2\n(5V Logic)')
axs[0].set_ylim(-0.5, 5.5)
axs[0].grid(True, linestyle='--', alpha=0.6)

# 4. Plot BIT_1
axs[1].plot(time, df['V(/BIT_1)'], color='green', linewidth=2)
axs[1].set_ylabel('BIT_1\n(5V Logic)')
axs[1].set_ylim(-0.5, 5.5)
axs[1].grid(True, linestyle='--', alpha=0.6)

# 5. Plot BIT_0 (LSB)
axs[2].plot(time, df['V(/BIT_0)'], color='red', linewidth=2)
axs[2].set_ylabel('BIT_0\n(5V Logic)')
axs[2].set_ylim(-0.5, 5.5)
axs[2].grid(True, linestyle='--', alpha=0.6)

# 6. Plot the Analog Input Pulse
axs[3].plot(time, df['V(/Shaped_Out)'], color='purple', linewidth=2)
axs[3].set_ylabel('Shaped Pulse\n(V)')
axs[3].set_xlabel('Time (µs)')
axs[3].grid(True, linestyle='--', alpha=0.6)

# Save the final high-res image
plt.tight_layout()
plt.savefig('adc_publication_plot.png', dpi=300)
print("Complete 4-panel publication plot successfully saved as adc_publication_plot.png!")