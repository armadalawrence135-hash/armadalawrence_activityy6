
import requests

API_URL = "https://johannesaguilar-activity4.onrender.com/student"


def get_classmate_student():

    try:
        response = requests.get(API_URL, timeout=60)

        if response.status_code == 200:

            data = response.json()

            print("\n===== CLASSMATE API =====")
            print("API request successful!")

            print("Student ID:", data.get("student_id"))
            print("Name:", data.get("name"))
            print("Program:", data.get("program"))
            print("Year:", data.get("year"))
            print("Section:", data.get("section"))

            return data

        else:
            print("Request failed.")
            print("Status Code:", response.status_code)
            print("Response:", response.text)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)


if __name__ == "__main__":
    get_classmate_student()
