import psycopg2

# Main function to connect to the database and call the other functions
def main():
    connection = psycopg2.connect(
    user="postgres",
    database="ASSIGNMENT03"
    )
    cursor = connection.cursor()
    
    display_menu()

    while True:
        choice = input("Enter a number: ")
        if choice == "1":
            getAllStudents(cursor)
        elif choice == "2":
            getAllStudents(cursor)
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment date (YYYY-MM-DD): ")
            addStudent(cursor, first_name, last_name, email, enrollment_date)
        elif choice == "3":
            getAllStudents(cursor)
            student_id = input("Enter the student's ID: ")
            email = input("Enter the student's new email: ")
            updateStudentEmail(cursor, student_id, email)
        elif choice == "4":
            getAllStudents(cursor)
            student_id = input("Enter the student's ID: ")
            deleteStudent(cursor, student_id)
        elif choice == "5":
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")
        display_menu()
        connection.commit()
    cursor.close()
    connection.close()


# Function to get all students from the database
def getAllStudents(cursor):
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print(f'{"ID":<5}{"First Name":<15}{"Last Name":<15}{"Email":<30}{"Enrollment Date":<15}')
    print('-' * 80)

    for row in rows:
        id, first_name, last_name, email, enrollment_date = row
        formatted_date = enrollment_date.strftime('%Y-%m-%d')  # Format the date as a string
        print(f'{id:<5}{first_name:<15}{last_name:<15}{email:<30}{formatted_date:<15}')

    print()
    
# Function to add a student to the database
def addStudent(cursor, first_name, last_name, email, enrollment_date):
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    cursor.execute("SELECT * FROM students")

# Function to update a student's email
def updateStudentEmail(cursor, student_id, email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))

# Function to delete a student from the database
def deleteStudent(cursor, student_id):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

# Function to display the menu for user interaction
def display_menu():
    print("1. Get all students")
    print("2. Add a student")
    print("3. Update a student's email")
    print("4. Delete a student")
    print("5. Quit")
    print()

if __name__ == "__main__":
    main()