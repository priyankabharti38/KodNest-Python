class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="remote",
        status=True
    ):

        self.job_id=job_id
        self.company=company
        self.role=role
        self.location=location
        self.status=status

    def __str__(self):
        status_label=(
            "Active" if self.status else "closed"
        )

        return(
            f"Job ID: {self.job_id} | "
            f"Company: {self.company} | "
            f"Role: {self.role} | "
            f"Location: {self.location} | "
            f"Status: {status_label}"
        )

job_one=JobDescription(
    job_id=501,
    company="TechNova",
    role="Python Developer",
    location="Bengaluru",
    status=True
)

job_two=JobDescription(
    job_id=502,
    company="TechNova",
    role="Python Developer",
    location="Bengaluru",
    status=True

)

job_three=JobDescription(
    job_id=503,
    company="CodeWorks",
    role="JavaDeveloper",
    location="Hyderabad",
    status=False
)
    

job_descriptions=[job_one,job_two,job_three]

for job in job_descriptions:
    print(job)
