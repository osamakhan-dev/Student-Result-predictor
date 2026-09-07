# Student Result Predictor System

def predict_result(study_hours, attendance_percentage):
    print("\n--- Analyzing Student Data ---")
    
    # Basic prediction logic
    if study_hours >= 5 and attendance_percentage >= 75:
        status = "Passed with Distinction"
        estimated_marks = "85% - 95%"
    elif study_hours >= 3 and attendance_percentage >= 60:
        status = "Passed"
        estimated_marks = "60% - 84%"
    else:
        status = "At Risk / Needs Improvement"
        estimated_marks = "Below 60%"
        
    return status, estimated_marks

# Main Execution
print("=== Student Result Prediction System ===")
hours = float(input("Enter daily study hours (1-10): "))
attendance = float(input("Enter school attendance percentage (1-100): "))

status, marks = predict_result(hours, attendance)

print("\n--- Prediction Output ---")
print(f"Status: {status}")
print(f"Estimated Marks Range: {marks}")