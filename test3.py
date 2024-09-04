import itertools
from collections import Counter
import time

# Define the sets
all_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
set_A = {2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 18, 19, 20, 23, 24, 25, 26, 27, 30}
set_B = {1, 7, 8, 14, 15, 17, 21, 22, 28, 29}

def is_valid_selection(samples):
    """Check if the selection meets the condition of differences greater than 2."""
    return all(abs(a - b) > 2 for a in samples for b in samples if a != b)

def generate_combinations(set_A, set_B, n_samples, counts):
    valid_combinations = []
    
    set_A_list = sorted(set_A)
    set_B_list = sorted(set_B)
    
    for count_A, count_B in counts:
        if count_A + count_B != n_samples:
            continue
        
        for a_combination in itertools.combinations(set_A_list, count_A):
            for b_combination in itertools.combinations(set_B_list, count_B):
                combined_set = list(a_combination) + list(b_combination)
                
                if is_valid_selection(combined_set):
                    valid_combinations.append(combined_set)
    
    return valid_combinations

def find_combinations_for_frequency(valid_combinations, required_frequency, total_combinations_needed):
    """Find combinations such that each sample appears exactly `required_frequency` times."""
    for combination_set in itertools.combinations(valid_combinations, total_combinations_needed):
        # Flatten the list of combinations and count frequencies
        all_samples = [sample for combo in combination_set for sample in combo]
        freq_count = Counter(all_samples)
        
        # Check if all frequencies match the required frequency
        if all(freq == required_frequency for freq in freq_count.values()):
            return combination_set
    
    return None

# Generate all possible combinations
sample_counts_6 = [(5, 1), (4, 2)]  # 6 samples: 5 from A and 1 from B or 4 from A and 2 from B
sample_counts_7 = [(6, 1)]  # 7 samples: 6 from A and 1 from B


start = time.time()
combinations_6 = generate_combinations(set_A, set_B, 6, sample_counts_6)
combinations_7 = generate_combinations(set_A, set_B, 7, sample_counts_7)

# Find valid combination sets
required_frequency = 5
total_combinations_needed = 22
all_valid_combinations = combinations_6 + combinations_7
print('find valid combinations', len(all_valid_combinations))

import math

# Define the size of the set
n = len(all_valid_combinations) 
k = total_combinations_needed

# Calculate the number of combinations
num_combinations = math.comb(n, k)
consuming_year = num_combinations * 1e-8 * 1/3.154e7
print(f"The number of combinations of selecting 22 elements from a set of 29375 is: {num_combinations}")
print(f"Time consuming: {consuming_year} year")

# result_combinations = find_combinations_for_frequency(all_valid_combinations, required_frequency, total_combinations_needed)
# print(len(result_combinations))
# # Print results
# if result_combinations:
#     print("Found valid combination sets:")
#     for combo in result_combinations:
#         print(combo)
# else:
#     print("No valid combination sets found.")

print(time.time() - start, ' seconds')