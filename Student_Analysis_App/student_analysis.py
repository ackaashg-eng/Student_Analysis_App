
import matplotlib.pyplot as plt


# 1. Collect marks from 10 students
def collect_marks():
    marks = []

    for i in range(10):
        while True:
            try:
                mark = float(input(f"Enter marks for student {i + 1}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Enter a mark between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return marks


# 2. Calculate mean
def calculate_mean(marks):
    return sum(marks) / len(marks)


# 3. Calculate median
def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_marks[middle - 1] +
                sorted_marks[middle]) / 2
    else:
        return sorted_marks[middle]


# 4. Calculate population variance
def calculate_variance(marks):
    mean = calculate_mean(marks)

    total = sum((mark - mean) ** 2 for mark in marks)

    return total / len(marks)


# 5. Calculate probabilities
def calculate_probability(marks):
    n = len(marks)
    pass_mark = 50

    passed = sum(1 for mark in marks if mark >= pass_mark)
    failed = sum(1 for mark in marks if mark < pass_mark)
    above_80 = sum(1 for mark in marks if mark > 80)

    probabilities = {
        "pass": passed / n,
        "fail": failed / n,
        "above_80": above_80 / n,
        "pass_percentage": (passed / n) * 100,
        "fail_percentage": (failed / n) * 100
    }

    return probabilities


# 6. Display statistical results
def display_statistics(marks):
    mean = calculate_mean(marks)
    median = calculate_median(marks)
    variance = calculate_variance(marks)
    probabilities = calculate_probability(marks)

    print("\n--- Statistical Analysis ---")
    print("Student marks:", marks)
    print("Mean:", mean)
    print("Median:", median)
    print("Maximum score:", max(marks))
    print("Minimum score:", min(marks))
    print("Variance:", variance)
    print("Pass percentage:",
          probabilities["pass_percentage"], "%")
    print("Fail percentage:",
          probabilities["fail_percentage"], "%")

    print("\n--- Probability Analysis ---")
    print("Probability of passing:",
          probabilities["pass"])
    print("Probability of scoring above 80:",
          probabilities["above_80"])
    print("Probability of failing:",
          probabilities["fail"])


# 7. Generate four graphs
def generate_graphs(marks):
    students = list(range(1, len(marks) + 1))

    plt.figure(figsize=(12, 8))

    # Bar chart
    plt.subplot(2, 2, 1)
    plt.bar(students, marks, color="skyblue",
            edgecolor="black")
    plt.title("Bar Chart - Student vs Marks")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    plt.xticks(students)
    plt.ylim(0, 100)

    # Line chart
    plt.subplot(2, 2, 2)
    plt.plot(students, marks, marker="o",
             color="green")
    plt.title("Line Chart - Marks Trend")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    plt.xticks(students)
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)

    # Histogram
    plt.subplot(2, 2, 3)
    plt.hist(marks,
             bins=[0, 20, 40, 60, 80, 100],
             color="orange",
             edgecolor="black")
    plt.title("Histogram - Score Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    # Scatter plot
    plt.subplot(2, 2, 4)
    plt.scatter(students, marks, color="red")
    plt.title("Scatter Plot - Student vs Marks")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    plt.xticks(students)
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


# 8. Main function
def main():
    marks = collect_marks()

    display_statistics(marks)

    generate_graphs(marks)


# Start the program
if __name__ == "__main__":
    main()
