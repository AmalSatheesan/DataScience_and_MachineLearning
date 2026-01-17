import numpy as np
import time

# 1. Setup: A list of 1 million salaries
salaries = list(range(1000000))

# --- THE NORMAL PYTHON WAY (Slow) ---
start_time = time.time()
bonus_salaries_list = []
for s in salaries:
    bonus_salaries_list.append(s * 1.1)
print(f"Normal Python took: {time.time() - start_time:.4f} seconds")

# --- THE DATA SCIENCE WAY (Fast - Vectorization) ---
# We convert the list to a NumPy Array (a 'vector')
salaries_array = np.array(salaries)

start_time = time.time()
bonus_salaries_array = salaries_array * 1.1  # No loop! This is vectorization.
print(f"Data Science Python took: {time.time() - start_time:.4f} seconds")

# Interpretation: 
# Notice the syntax 'salaries_array * 1.1'. 
# Python understands you want to apply that math to EVERY element at once.