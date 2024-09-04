import itertools
import time

date_constrain_map = {}
weekday_map = set()
holiday_map = {17}
sun = 1
sat = 7
month_days = 30

for i in range(1, month_days+1):

    if i == sun and i <= month_days:
        holiday_map.add(i)
        sun += 7
    elif i == sat and i <= month_days:
        holiday_map.add(i)
        sat += 7
    elif i not in holiday_map:
        weekday_map.add(i)
    
    no_day = {i, i+1, i+2}
    date_constrain_map[i] = no_day



def is_valid_selection(samples):
    """Check if the selection meets the condition of differences greater than 2."""
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            if abs(samples[i] - samples[j]) <= 2:
                return False
    return True

def count_valid_combinations(set_A, set_B, num_samples, sample_counts):
    valid_combinations = 0

    # Convert sets to sorted lists for consistent ordering
    set_A_list = sorted(set_A)
    set_B_list = sorted(set_B)

    for count_A, count_B in sample_counts:
        if count_A + count_B != num_samples:
            continue
        
        for a_combination in itertools.combinations(set_A_list, count_A):
            for b_combination in itertools.combinations(set_B_list, count_B):
                # Create a combined set of samples
                combined_set = list(a_combination) + list(b_combination)
                
                # Check if combined set meets the condition
                if is_valid_selection(combined_set):
                    valid_combinations += 1

    return valid_combinations

# Define the sets
set_A = {2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 18, 19, 20, 23, 24, 25, 26, 27, 30}
set_B = {1, 7, 8, 14, 15, 17, 21, 22, 28, 29}

# Counts
sample_counts_6 = [(5, 1), (4, 2)]  # 6 samples: 5 from A and 1 from B or 4 from A and 2 from B
sample_counts_7 = [(6, 1)]  # 7 samples: 6 from A and 1 from B

start = time.time()

# Count valid combinations
total_valid_combinations_6 = count_valid_combinations(set_A, set_B, 6, sample_counts_6)
total_valid_combinations_7 = count_valid_combinations(set_A, set_B, 7, sample_counts_7)

# Assuming you want to count combinations for 4 times and 18 times respectively
total_combinations = (total_valid_combinations_6 * 4) + (total_valid_combinations_7 * 18)

print("Total valid combinations for 6 samples (4 times):", total_valid_combinations_6)
print("Total valid combinations for 7 samples (18 times):", total_valid_combinations_7)
print("Overall total combinations:", total_combinations)
print(time.time() - start, ' seconds')


