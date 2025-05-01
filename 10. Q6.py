'''Write a program that merges lines alternatively from two files and writes
the results to new file. If one file has less number of lines than the other,
the remaining lines from the larger file should be simply copied into the target
file.'''
# File paths
file1 = "file1.txt"
file2 = "file2.txt"
merged_file = "merged.txt"

try:
    # Read lines from both files
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Determine the length of both
    len1 = len(lines1)
    len2 = len(lines2)
    max_len = max(len1, len2)

    # Merge lines alternately
    merged_lines = []
    for i in range(max_len):
        if i < len1:
            merged_lines.append(lines1[i])
        if i < len2:
            merged_lines.append(lines2[i])

    # Write to the merged file
    with open(merged_file, "w") as mf:
        mf.writelines(merged_lines)

    print(f"Lines merged into '{merged_file}' successfully.")

except FileNotFoundError as e:
    print("Error:", e)
except Exception as e:
    print("An error occurred:", e)
