import itertools
from collections import Counter
import random
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
                print(combined_set)
                if is_valid_selection(combined_set):
                    valid_combinations.append(combined_set)
    
    return valid_combinations

def find_all_possible_combinations(n_samples, num_times, counts):
    all_combinations = []
    total_combinations = generate_combinations(set_A, set_B, n_samples, counts)
    
    while len(all_combinations) < num_times:
        all_combinations.extend(random.sample(total_combinations, min(num_times - len(all_combinations), len(total_combinations))))
    
    return all_combinations

def validate_combination_frequency(combinations, required_frequency):
    frequency_count = Counter(sample for comb in combinations for sample in comb)
    return all(freq == required_frequency for freq in frequency_count.values())

# Counts
sample_counts_6 = [(5, 1), (4, 2)]  # 6 samples: 5 from A and 1 from B or 4 from A and 2 from B
sample_counts_7 = [(6, 1)]  # 7 samples: 6 from A and 1 from B

# Generate combinations
start = time.time()
combinations_6 = find_all_possible_combinations(6, 4, sample_counts_6)
combinations_7 = find_all_possible_combinations(7, 18, sample_counts_7)

# Combine all generated combinations
all_combinations = combinations_6 + combinations_7

# Validate if the frequency of each sample is 5
valid = validate_combination_frequency(all_combinations, 5)

if valid:
    print("All samples appear exactly 5 times in the 150 selections.")
else:
    print("The frequency requirement is not met.")

print("Total combinations:", len(all_combinations))

print(time.time() - start, ' seconds')