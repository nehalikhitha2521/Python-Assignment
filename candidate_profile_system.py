class PersonalInfo:
    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def display_personal(self):
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Contact Number:", self.contact)
        print("Email:", self.email)


class Education(PersonalInfo):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa):
        super().__init__(name, dob, contact, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Year of Graduation:", self.year)
        print("CGPA:", self.cgpa)


class Experience(Education):
    def __init__(self, name, dob, contact, email, degree, university, year, cgpa,
                 company, role, years_exp, skills):
        super().__init__(name, dob, contact, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.years_exp = years_exp
        self.skills = skills

    def display_experience(self):
        print("Company Name:", self.company)
        print("Job Role:", self.role)
        print("Years of Experience:", self.years_exp)
        print("Skills:", self.skills)


class CandidateProfile(Experience):

    def display_profile(self):
        print("\n----- Candidate Profile -----")
        self.display_personal()

        print("\n--- Education Details ---")
        self.display_education()

        print("\n--- Work Experience ---")
        self.display_experience()

    def check_eligibility(self):
        if self.years_exp >= 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")


# Candidate 1
c1 = CandidateProfile(
    "Neha", "25-06-2010", "876556710", "neha@email.com",
    "B.Tech", "GITAM University", 2018, 9.5,
    "Infosys", "Software Engineer", 6, "Python, Java"
)

# Candidate 2
c2 = CandidateProfile(
    "Geetha", "20-02-2006", "9854327891", "geetha@email.com",
    "BSc Computer Science", "Andhra University", 2021, 9.0,
    "Amazon", "Junior Developer", 2, "Python"
)

c1.display_profile()
c1.check_eligibility()

c2.display_profile()
c2.check_eligibility()
