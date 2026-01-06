-python code 
- fig 42
import matplotlib.pyplot as plt
import numpy as np

# Data
protocols = ['2PC (Baseline)', 'NoSQL (Audit)', '3PC (Resilient)', 'Blockchain (Secure)']
latency_values = [45.2, 55.0, 78.5, 198.4] # Added NoSQL at 55.0
colors = ['gray', 'teal', 'royalblue', 'purple'] # Teal for NoSQL

plt.figure(figsize=(10, 6))
bars = plt.bar(protocols, latency_values, color=colors, width=0.6)

plt.title('Average Transaction Latency Comparison (Including NoSQL)', fontsize=14, fontweight='bold')
plt.xlabel('Protocol Architecture', fontsize=12)
plt.ylabel('Latency (milliseconds)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add text labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 2,
             f'{height} ms', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig("Fig37_Latency_Chart_Updated.png", dpi=300)
plt.show()


--fig 43
import matplotlib.pyplot as plt

# Data
protocols_fail = ['2PC (Blocking)', '3PC (Non-Blocking)', 'Blockchain', 'NoSQL (Eventual)']
recovery_times = [15000, 200, 800, 10] # 2PC=15s, 3PC=0.2s, NoSQL~0 (used 10 for log scale visibility)

plt.figure(figsize=(10, 6))
# Using a line plot to match your previous style
plt.plot(protocols_fail, recovery_times, marker='o', color='red', linewidth=3, markersize=10)

plt.title('System Recovery Time (RTO) Under Failure', fontsize=14, fontweight='bold')
plt.ylabel('Recovery Time (ms) - Log Scale', fontsize=12)
plt.yscale('log') # Log scale is crucial here
plt.grid(True, which="both", ls="--", alpha=0.5)

# Add text labels
for i, txt in enumerate(recovery_times):
    label = f"{txt} ms"
    if txt == 15000: label = "15,000 ms (Timeout)"
    if txt == 10: label = "Instant (Non-Blocking)"
    plt.annotate(label, (protocols_fail[i], recovery_times[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig("Fig38_Recovery_Chart_Updated.png", dpi=300)
plt.show()

--fig 44
import matplotlib.pyplot as plt

# Data
protocols_store = ['2PC (SQL)', '3PC (SQL+Log)', 'NoSQL (BSON)', 'Blockchain (Hash)']
storage_gb = [1.2, 1.5, 1.8, 4.8] 
colors = ['green', 'green', 'orange', 'red'] # Orange for NoSQL warning

plt.figure(figsize=(10, 6))
bars_store = plt.bar(protocols_store, storage_gb, color=colors)

plt.title('Storage Overhead Comparison (Scalability)', fontsize=14, fontweight='bold')
plt.ylabel('Storage (GB) per 1 Million Rows', fontsize=12)

# Add text labels
for bar in bars_store:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 0.1,
             f'{height} GB', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig("Fig39_Storage_Chart_Updated.png", dpi=300)
plt.show()

