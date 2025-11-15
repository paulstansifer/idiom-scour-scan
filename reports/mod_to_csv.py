import re
import csv

def extract_numbers(line):
    # Extract initial number (removing commas)
    first_num = line.split()[0].replace(',', '')
    
    # Extract percentages
    percentages = re.findall(r'(\d+\.\d+)%', line)
    
    # Extract final number after the dash
    final_num = line.strip().split('-')[-1].strip()
    
    return [first_num] + percentages + [final_num]

def process_file(input_filename, output_filename, sample_size=400):
    with open(input_filename, 'r') as f:
        lines = f.readlines()
    
    # Filter out empty lines
    lines = [line for line in lines if line.strip()]
    
    # Calculate step size for even sampling
    step = max(1, len(lines) // sample_size)
    
    # Sample evenly
    sampled_lines = lines[::step][:sample_size]
    
    # Process each line to extract numbers
    processed_data = [extract_numbers(line) for line in sampled_lines]
    
    # Write to CSV
    headers = ['Initial_Number', 'Percentage1', 'Percentage2', 'Percentage3', 'Final_Number']
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(processed_data)

if __name__ == '__main__':
    input_file = '/tmp/hof-mod'  # The input file in the reports directory
    output_file = 'sampled_output.csv'  # The output will be created in the reports directory
    process_file(input_file, output_file)