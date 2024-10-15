def calculate_parity_bit(data):
    """Calculate the parity bit for the given binary data."""
    count_ones = data.count('1')
    # Even parity: if count of 1's is odd, parity bit is 1, else 0
    return '1' if count_ones % 2 != 0 else '0'

def check_parity(data_with_parity):
    """Check if the received data has the correct parity."""
    data = data_with_parity[:-1]  # Exclude parity bit
    received_parity = data_with_parity[-1]
    calculated_parity = calculate_parity_bit(data)
    return received_parity == calculated_parity

# Example usage
data = '1101001'  # Original data
parity_bit = calculate_parity_bit(data)
data_with_parity = data + parity_bit
print("Data with parity bit:", data_with_parity)

# Simulating received data (correct and incorrect)
print("Is received data valid?", check_parity(data_with_parity))  # Should be True
print("Is received data valid?", check_parity(data_with_parity[:-1] + '1'))  # Should be False