
import requests

BASE_URL = "http://127.0.0.1:5000"


def get_all_students():
    try:
        response = requests.get(
            f"{BASE_URL}/api/students",
            timeout=15
        )

        response.raise_for_status()

        students = response.json()

        print("\n===== MY STUDENT RECORDS =====")

        if not students:
            print("No student records found.")
            return

        for student in students:
            print("-----------------------------")
            print("Database ID:", student.get("id"))
            print("Student ID:", student.get("student_id"))
            print("Name:", student.get("name"))
            print("Program:", student.get("program"))
            print("Year:", student.get("year"))
            print("Section:", student.get("section"))

    except requests.exceptions.RequestException as error:
        print("API connection failed:", error)


def get_student(student_id):
    try:
        response = requests.get(
            f"{BASE_URL}/api/students/{student_id}",
            timeout=15
        )

        response.raise_for_status()

        student = response.json()

        print("\n===== STUDENT DETAILS =====")

        for key, value in student.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as error:
        print("Unable to retrieve student:", error)


if __name__ == "__main__":
    get_all_students()

    # Example:
    # get_student(1)
