# CV Database Structure

This project provides a comprehensive and flexible data structure for managing Curriculum Vitae (CV) information using Pydantic v2. The structure is designed to handle detailed professional profiles with support for various types of information typically found in CVs.

## Features

- **Flexible Data Structure**: All fields are optional, allowing for partial data entry
- **Type Safety**: Built on Pydantic v2 for robust data validation
- **Comprehensive Models**: Covers all aspects of a professional CV
- **Extensible Design**: Easy to extend with additional fields as needed

## Data Models

### 1. Personal Information (`PersonalInfo`)
- Basic contact details
- Social media profiles
- Emergency contact information
- Visa and work permit status

### 2. Professional Summary (`Summary`)
- Professional summary
- Career objectives
- Key qualifications
- Core competencies
- Industry expertise
- Professional achievements
- Career highlights
- Personal attributes (leadership style, work style, etc.)

### 3. Education (`Education`)
- School information
- Degree and major
- Dates and GPA
- Honors and awards
- Relevant courses
- Thesis information
- Extracurricular activities

### 4. Work Experience (`WorkExperience`)
- Company details
- Position and responsibilities
- Employment period
- Achievements
- Department and supervisor
- Technologies used
- Salary information
- Reason for leaving

### 5. Skills (`Skill`)
- Skill categories
- Proficiency levels
- Years of experience
- Last used date
- Related certifications
- Project applications

### 6. Projects (`Project`)
- Project details
- Role and responsibilities
- Timeline
- Technologies used
- Team information
- Budget and deliverables
- Challenges and results

### 7. Certifications (`Certification`)
- Certification details
- Issuing organization
- Validity period
- Verification information
- Related skills
- Status tracking

### 8. Languages (`Language`)
- Language proficiency
- Certification details
- Years of experience
- Last used date
- Level assessment

### 9. Main CV Structure (`CV`)
- Integration of all above models
- Version control
- Status tracking
- Metadata support
- Creation and update timestamps

## Requirements

- Python 3.8+
- Pydantic v2.0.0 or higher
- python-dateutil 2.8.2 or higher
- typing-extensions 4.5.0 or higher

## Installation

```bash
pip install -r requirements.txt
```

## Usage Example

```python
from cv_models import CV, PersonalInfo, Education

# Create a new CV instance
cv = CV(
    personal_info=PersonalInfo(
        name="John Doe",
        email="john.doe@example.com",
        phone="+1234567890"
    ),
    education=[
        Education(
            school="University of Example",
            degree="Bachelor of Science",
            major="Computer Science",
            gpa=3.8
        )
    ]
)
```

## Markdown CV Example

```markdown
# John Doe
## Personal Information
- 📧 Email: john.doe@example.com
- 📱 Phone: +1234567890
- 🌍 Location: Taipei, Taiwan
- 🔗 LinkedIn: [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)
- 💻 GitHub: [github.com/johndoe](https://github.com/johndoe)

## Professional Summary
Experienced software engineer with 5+ years of experience in full-stack development. 
Specialized in Python, JavaScript, and cloud technologies.

## Education
### University of Example
**Bachelor of Science in Computer Science** | 2018 - 2022
- GPA: 3.8/4.0
- Relevant Coursework: Data Structures, Algorithms, Database Systems
- Honors: Dean's List (2019-2022)

## Work Experience
### Senior Software Engineer | Tech Company Inc.
**2020 - Present**
- Led development of microservices architecture
- Implemented CI/CD pipelines
- Mentored junior developers
- Technologies: Python, Django, React, AWS

## Skills
### Programming Languages
- Python (Expert)
- JavaScript (Advanced)
- Java (Intermediate)

### Tools & Technologies
- Docker
- Kubernetes
- AWS
- Git

## Projects
### E-commerce Platform
- Role: Lead Developer
- Technologies: Python, Django, React, PostgreSQL
- Achievements:
  - Reduced page load time by 40%
  - Implemented real-time inventory tracking

## Certifications
- AWS Certified Solutions Architect
- Google Cloud Professional Developer

## Languages
- English (Fluent)
- Mandarin (Native)
```

## Contributing

Feel free to contribute to this project by:
1. Reporting bugs
2. Suggesting improvements
3. Adding new features
4. Improving documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.
