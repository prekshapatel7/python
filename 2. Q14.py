''') Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:

Marks Range Grade

Absent NA

0 – 39 F

40 – 44 P

45 – 49 C

50 – 54 B

55 – 59 B+

60 – 69 A

70 – 79 A+

80 – 100 O'''
def get_grade(mark):
    if mark == "Absent":
        return "NA"
    mark = int(mark)
    if 0 <= mark <= 39:
        return "F"
    elif 40 <= mark <= 44:
        return "P"
    elif 45 <= mark <= 49:
        return "C"
    elif 50 <= mark <= 54:
        return "B"
    elif 55 <= mark <= 59:
        return "B+"
    elif 60 <= mark <= 69:
        return "A"
    elif 70 <= mark <= 79:
        return "A+"
    elif 80 <= mark <= 100:
        return "O"
    else:
        return "Invalid"

marks = []
grades = []
total = 0
fail = False

# Input marks for 3 subjects
for i in range(1, 4):
    mark = input(f"Enter marks for Subject {i} (or type 'Absent'): ")
    if mark == "Absent":
        grades.append("NA")
        fail = True  # Automatically fail if absent
    else:
        mark_int = int(mark)
        marks.append(mark_int)
        grades.append(get_grade(mark))
        total += mark_int
        if mark_int <= 39:
            fail = True

# Calculate average only for subjects with marks
average = total / len(marks) if marks else 0

# Print results
print("\n--- Result ---")
for i in range(3):
    print(f"Subject {i+1}: Grade = {grades[i]}")

print("Total Marks =", total)
print("Average Marks =", round(average, 2))

if fail:
    print("Status: Fail")
else:
    print("Status: Pass")
