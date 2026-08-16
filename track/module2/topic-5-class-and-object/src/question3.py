class StudentProfile:

    def __init__(self,student_id, name, course, score, is_placed):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.score=score
        self.is_placed=is_placed


    def __str__(self):
        placement_status=(
            "placed" if self.is_placed else "not placed"
        )

        return(
            f"student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {placement_status}"

        )


print("STUDENT PROFILE")
student_id=int(input())
student_name=input().strip()
course_name=input().strip()
score=float(input())
is_placed=input().strip().lower()


student= StudentProfile(
student_id=student_id,
name=student_name,
course=course_name,
score=score,
is_placed=is_placed
)
print(student)

