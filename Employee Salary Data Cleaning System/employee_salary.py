import numpy as np

# 1. CREATE THE EMPLOYEE DATASET

employee_ids = np.array([101, 102, 103, 104, 105, 106])

ages = np.array([25, 30, 28, 35, 40, 26])

departments = np.array([
    "IT", "HR", "IT", "Finance", "HR", "IT"
])

salaries = np.array([
    50000, 60000, -1000, 75000, 45000, 55000
], dtype=float)

experience = np.array([2, 5, 3, 10, 12, 1])

performance_scores = np.array([85, 95, 92, 88, 78, 96])

print("ORIGINAL EMPLOYEE DATA")

for i in range(len(employee_ids)):
    print(
        employee_ids[i],
        ages[i],
        departments[i],
        salaries[i],
        experience[i],
        performance_scores[i]
    )


# 2. CLEAN NEGATIVE SALARIES

# Replace negative salaries with zero
cleaned_salaries = np.where(salaries < 0, 0, salaries)

print("\nCLEANED SALARIES:")
print(cleaned_salaries)


# 3. INCREASE SALARIES BY 10%

# Broadcasting: multiply every salary by 1.10
increased_salaries = cleaned_salaries * 1.10

print("\nSALARIES AFTER 10% INCREASE:")
print(increased_salaries)


# 4. FILTER PERFORMANCE SCORES ABOVE 90

high_performance_mask = performance_scores > 90

high_performance_ids = employee_ids[high_performance_mask]

print("\nEMPLOYEES WITH PERFORMANCE ABOVE 90:")
print(high_performance_ids)

print("Their performance scores:")
print(performance_scores[high_performance_mask])


# 5. FIND SALARIES ABOVE AVERAGE

average_salary = np.mean(increased_salaries)

above_average_mask = increased_salaries > average_salary

print("\nAVERAGE SALARY:")
print(average_salary)

print("\nEMPLOYEES EARNING ABOVE AVERAGE:")
print(employee_ids[above_average_mask])

print("Their salaries:")
print(increased_salaries[above_average_mask])


# 6. RESHAPE THE SALARY ARRAY

# Convert 6 salary values into 2 rows and 3 columns
reshaped_salaries = increased_salaries.reshape(2, 3)

print("\nRESHAPED SALARIES (2 x 3):")
print(reshaped_salaries)


# 7. FLATTEN THE SALARY ARRAY

# Convert the 2D array back into a 1D array
flattened_salaries = reshaped_salaries.flatten()

print("\nFLATTENED SALARIES:")
print(flattened_salaries)


# 8. TRANSPOSE THE DATASET

# Combine numeric columns into a 2D array
numeric_dataset = np.column_stack((
    employee_ids,
    ages,
    increased_salaries,
    experience,
    performance_scores
))

print("\nNUMERIC DATASET (EMPLOYEES AS ROWS):")
print(numeric_dataset)

# Exchange rows and columns
transposed_dataset = numeric_dataset.transpose()

print("\nTRANSPOSED DATASET (FEATURES AS ROWS):")
print(transposed_dataset)


# 9. GENERATE THE CLEANED DATASET

cleaned_dataset = np.column_stack((
    employee_ids,
    ages,
    increased_salaries,
    experience,
    performance_scores
))

print("\nFINAL CLEANED DATASET")
print("-" * 60)
print("ID | Age | Salary | Experience | Performance")

for i in range(len(employee_ids)):
    print(
        f"{int(cleaned_dataset[i, 0])} | "
        f"{int(cleaned_dataset[i, 1])} | "
        f"{cleaned_dataset[i, 2]:.2f} | "
        f"{int(cleaned_dataset[i, 3])} | "
        f"{int(cleaned_dataset[i, 4])}"
    )

print("\nDataset cleaning completed!")


