student_scores = {
    'Dev': 89,
    'Ram': 70,
    'Shyam': 60,
    'Jaya': 95,
    'Savi': 75
}
    
print("Student scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")
    
highest_score_student = max(student_scores, key=student_scores.get)
print(f"\nStudent with the highest score: {highest_score_student} with a score of {student_scores[highest_score_student]}")
    
student_scores['Ram'] = 85
    
print("\nUpdated student scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

