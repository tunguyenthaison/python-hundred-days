# grading program
"""
DO NOT write any print statements.
This is the scoring criteria:
    Scores 91 - 100: Grade = "Outstanding"
    Scores 81 - 90: Grade = "Exceeds Expectations"
    Scores 71 - 80: Grade = "Acceptable"
    Scores 70 or lower: Grade = "Fail"
Expected output:
'{
    'Harry': 'Exceeds Expectations',
    'Ron': 'Acceptable',
    'Hermione': 'Outstanding',
    'Draco': 'Acceptable',
    'Neville': 'Fail'
}'
"""


def grading() -> None:
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
        }
    student_grades = {}
    for student in student_scores.keys():
        score = student_scores[student]
        if (91 <= score and score <= 100):
            student_grades[student] = "Outstanding"
        elif (81 <= score and score <= 90):
            student_grades[student] = "Outstanding"
        elif (71 <= score and score <= 80):
            student_grades[student] = "Exceeds Expectation"
        elif (score <= 70):
            student_grades[student] = "Fail"
    print(student_grades)


if __name__ == "__main__":
    grading()
