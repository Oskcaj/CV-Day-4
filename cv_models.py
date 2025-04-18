from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr

class Education(BaseModel):
    school: Optional[str] = None
    degree: Optional[str] = None
    major: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    description: Optional[str] = None
    location: Optional[str] = None
    honors: Optional[List[str]] = None
    relevant_courses: Optional[List[str]] = None
    thesis: Optional[str] = None
    activities: Optional[List[str]] = None

class WorkExperience(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    location: Optional[str] = None
    department: Optional[str] = None
    supervisor: Optional[str] = None
    employment_type: Optional[str] = None
    technologies: Optional[List[str]] = None
    responsibilities: Optional[List[str]] = None
    projects: Optional[List[str]] = None
    salary: Optional[float] = None
    reason_for_leaving: Optional[str] = None

class Skill(BaseModel):
    category: Optional[str] = None
    name: Optional[str] = None
    level: Optional[str] = None
    years_of_experience: Optional[float] = None
    last_used: Optional[date] = None
    proficiency: Optional[str] = None
    certifications: Optional[List[str]] = None
    projects: Optional[List[str]] = None
    description: Optional[str] = None

class Project(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    technologies: Optional[List[str]] = None
    achievements: Optional[List[str]] = None
    team_size: Optional[int] = None
    client: Optional[str] = None
    budget: Optional[float] = None
    deliverables: Optional[List[str]] = None
    challenges: Optional[List[str]] = None
    results: Optional[List[str]] = None

class Certification(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    credential_id: Optional[str] = None
    verification_url: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[List[str]] = None
    level: Optional[str] = None
    status: Optional[str] = None

class Language(BaseModel):
    name: Optional[str] = None
    proficiency: Optional[str] = None
    certificate: Optional[str] = None
    years_of_experience: Optional[float] = None
    last_used: Optional[date] = None
    description: Optional[str] = None
    level: Optional[str] = None

class PersonalInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    nationality: Optional[str] = None
    current_location: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    social_media: Optional[Dict[str, str]] = None
    emergency_contact: Optional[Dict[str, str]] = None
    visa_status: Optional[str] = None
    work_permit: Optional[str] = None

class Summary(BaseModel):
    professional_summary: Optional[str] = None
    career_objective: Optional[str] = None
    key_qualifications: Optional[List[str]] = None
    core_competencies: Optional[List[str]] = None
    industry_expertise: Optional[List[str]] = None
    professional_achievements: Optional[List[str]] = None
    career_highlights: Optional[List[str]] = None
    unique_selling_points: Optional[List[str]] = None
    career_goals: Optional[List[str]] = None
    professional_values: Optional[List[str]] = None
    leadership_style: Optional[str] = None
    management_approach: Optional[str] = None
    problem_solving_approach: Optional[str] = None
    communication_style: Optional[str] = None
    work_style: Optional[str] = None

class CV(BaseModel):
    personal_info: Optional[PersonalInfo] = None
    summary: Optional[Summary] = None
    work_experience: Optional[List[WorkExperience]] = None
    education: Optional[List[Education]] = None
    skills: Optional[List[Skill]] = None
    projects: Optional[List[Project]] = None
    certifications: Optional[List[Certification]] = None
    languages: Optional[List[Language]] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    version: Optional[str] = None
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
