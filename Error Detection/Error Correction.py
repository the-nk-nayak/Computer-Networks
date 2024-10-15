def calculate_hamming_code(data):
    """Calculate Hamming code for 4-bit data."""
    # Data bits
    d1, d2, d3, d4 = data
    # Parity bits
    p1 = d1 ^ d2 ^ d4  # Parity bit for positions 1, 2, 4
    p2 = d1 ^ d3 ^ d4  # Parity bit for positions 1, 3, 4
    p3 = d2 ^ d3 ^ d4  # Parity bit for positions 2, 3, 4
    return f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"

def detect_and_correct_hamming(received):
    """Detect and correct errors in Hamming code."""
    # Extract bits
    p1, p2, d1, p3, d2, d3, d4 = [int(bit) for bit in received]
    # Calculate parity
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4
    error_position = s1 * 1 + s2 * 2 + s3 * 4  # Calculate error position
    if error_position:
        print(f"Error detected at position {error_position}.")
        # Correct the error
        received = list(received)
        received[error_position - 1] = '1' if received[error_position - 1] == '0' else '0'
        received = ''.join(received)
    else:
        print("No error detected.")
    return received

# Example usage
data = '1010'  # Original 4-bit data
hamming_code = calculate_hamming_code(data)
print("Hamming code:", hamming_code)

# Simulating received data with an error
received_data = hamming_code[:3] + '1' + hamming_code[4:]  # Introduce an error
corrected_data = detect_and_correct_hamming(received_data)
print("Corrected data:", corrected_data)