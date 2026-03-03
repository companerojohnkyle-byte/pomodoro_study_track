import time

total_sessions = 0

def timer(minutes, label):
    seconds = minutes * 60
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{label} Time: {mins}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n{label} ended!\n")

def study_session():
    global total_sessions
    total_sessions += 1

    print("\n • STUDY SESSION • ")
    minutes = input("Enter your study time (Default is 25 Mins): ")

    if minutes:
        minutes = int(minutes)

    print(f"Starting {minutes}-minute study session. Stay focused! ")
    timer(minutes, "Study")

    print("Great job! It's Time for a 5-minute break ")
    timer(5, "Use your break time wisely.")

def show_stats():
    print("\n • YOUR STUDY STATS • ")
    print(f"Total Sessions Progress: {total_sessions}")
    print("")

while True:
    print("|== • SIMPLE STUDY TIMER • ===|")
    print("| 1. Start Study Session      |")
    print("| 2. View Stats               |")
    print("| 3. Exit                     |")
    print("|_____________________________|")
    choice = input("Choose an option: ")

    if choice == "1":
        study_session()
    elif choice == "2":
        show_stats()
    elif choice == "3":
        print("Good luck with your studies! ")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.\n")