class StudentProfile:
    def __init__(self, id, name,course,score,is_placed):
        self.student_id=id
        self.name=name
        self.course=course
        self.score=0.0
        self.is_placed=False

    def __str__(self):
        placement_status=(
            "placed" if self.is_placed else "not placed"
        )
        return(
            f"Student ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Course: {self.course} | "
            f"Score: {self.score:.1f} | "
            f"Placed: {placement_status}"
        )





student_one= StudentProfile(
    id=101,
    name="Asha",
    course="Python",
    score=85.0,
    is_placed=False

)

student_two=StudentProfile(
    id=102,
    name="Rahul",
    course="Java",
    score=0.0,
    is_placed=False
)

print(student_one)
print(student_two)