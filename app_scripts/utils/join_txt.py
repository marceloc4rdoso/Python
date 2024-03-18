import os

# Specify the directory containing your TXT files
directory = "I:\\IVALIX\\TXT\\andresromano\\dados\\ZOLD\\all-files-andres-romano"

# Specify the name of the merged file
output_file = "I:\\IVALIX\\TXT\\andresromano\\dados\\ZOLD\\all-files-andres-romano\\merged.txt"

# Get a list of all TXT files in the directory
txt_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

# Sort the files if needed
# txt_files.sort()

# Open the output file for writing
with open(output_file, "w", encoding="utf-8") as merged_file:
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        with open(file_path, "r", encoding="utf-8") as input_file:
            # Read each line from the input file and write it to the merged file
            for line in input_file:
                merged_file.write(line)

print(f"Merged {len(txt_files)} files into {output_file}")
