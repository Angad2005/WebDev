import sqlite3

def view_feedback():
    conn = sqlite3.connect('feedback.db')  # Connect to the feedback database
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM feedback")
    feedback_data = cursor.fetchall()
    conn.close()
    
    if feedback_data:
        print("\nFeedback Submissions:")
        print("=" * 50)
        for feedback in feedback_data:
            print(f"ID: {feedback[0]}")
            print(f"Email: {feedback[1]}")
            print(f"Message: {feedback[2]}")
            print("-" * 50)
    else:
        print("No feedback found in the database.")

if __name__ == "__main__":
    view_feedback()
