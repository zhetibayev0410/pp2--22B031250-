import re

def find_lower_case_sequences(input_str):
    pattern = r'\b[a-z]+_[a-z]+\b'
    match_list = re.findall(pattern, input_str)
    return match_list

input_str = "The_quick_brown_fox_jumps_over_the_lazy_dog."
matches = find_lower_case_sequences(input_str)
print(matches)
