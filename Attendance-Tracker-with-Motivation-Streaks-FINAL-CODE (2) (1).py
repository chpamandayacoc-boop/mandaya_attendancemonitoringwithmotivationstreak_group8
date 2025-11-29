import datetime

# Dictionary to store students and their attendance records
attendance_records = {}

# Dictionary to track current streaks
streaks = {}

def add_student():
    name = input("Enter student's name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in attendance_records:
        print(f"{name} is already in the system.")
    else:
        attendance_records[name] = []
        streaks[name] = 0  # Initialize streak to 0
        print(f"{name} has been added.")

def mark_attendance():
    if not attendance_records:
        print("No students in the system. Add students first.")
        return
    
    date = datetime.date.today().strftime("%Y-%m-%d")
    print(f"\nMarking attendance for {date}:")
    for student in attendance_records:
        # Prevent double-marking for the same date
        if attendance_records[student] and attendance_records[student][-1][0] == date:
            print(f"⚠️  {student} already marked for {date}: {attendance_records[student][-1][1]}")
            continue

        while True:
            status = input(f"Mark {student} (P/A): ").strip().upper()
            if status == 'P':
                attendance_records[student].append((date, "Present"))
                streaks[student] = streaks.get(student, 0) + 1  # Increment streak
                print(f"✅ {student} is present! (Streak: {streaks[student]} days)")
                # Fun encouragement messages
                if streaks[student] == 3:
                    print(f"🔥 {student} is on a 3-day streak! Keep it up!")
                elif streaks[student] == 5:
                    print(f"🏅 {student} reached a 5-day streak! Great consistency!")
                elif streaks[student] >= 10:
                    print(f"✨ {student} reached a 10-day streak! Your consistency is inspiring — keep showing up and giving your best every day!")
                elif streaks[student] >= 15:
                    print(f"🌟 {student} reached a 15-day streak! Your hard work is paying off — stay focused and continue pushing forward!")
                elif streaks[student] >= 20:
                    print(f"👑 {student} reached a 20-day streak! You've built a powerful habit — keep leading by example and aiming higher!")
                break
            elif status == 'A':
                prev_streak = streaks.get(student, 0)
                # Decrease streak by 1 but never below 0
                new_streak = max(prev_streak - 1, 0)
                attendance_records[student].append((date, "Absent"))
                streaks[student] = new_streak
                if prev_streak > new_streak:
                    print(f"❌ {student}'s streak decreased from {prev_streak} to {new_streak}.")
                else:
                    print(f"❌ {student} is absent. (Streak remains {new_streak} days)")
                break
            else:
                print("Invalid input! Please enter 'P' or 'A'.")

def view_attendance():
    if not attendance_records:
        print("No attendance records to show.")
        return

    print("\nAttendance Records:")
    for student, records in attendance_records.items():
        print(f"\n{student}: (Current Streak: {streaks.get(student, 0)} days🔥)")
        if not records:
            print("  No records yet.")
        else:
            for record in records:
                print(f"  Date: {record[0]} - {record[1]}")

def main():
    while True:
        print("\n🔥 Attendance Monitoring System (with Streaks)")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Records")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            view_attendance()
        elif choice == '4':
            print("Exiting the system... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
