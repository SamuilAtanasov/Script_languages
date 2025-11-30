import os

def read_file(filename):
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
def write_odd_lines(lines, output_filename):
    odd_lines = [line for i, line in enumerate(lines) if i % 2 == 0]
    
    with open(output_filename, "w", encoding = "utf-8",) as f:
        f.writelines(line if line.endswith("\n") else line + "\n" for line in odd_lines)



script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "input.txt")
output_file = os.path.join(script_dir, "output.txt")

print("Looking for:", input_file)

lines = read_file(input_file)
if lines:
    write_odd_lines(lines, output_file)
    print(f"Odd lines written to {output_file}")