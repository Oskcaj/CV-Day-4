from datetime import date
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr

class Education(BaseModel):
    """Education model representing academic background."""
    school: Optional[str] = Field(None, description="學校名稱")
    degree: Optional[str] = Field(None, description="學位")
    major: Optional[str] = Field(None, description="主修")
    start_date: Optional[date] = Field(None, description="開始日期")
    end_date: Optional[date] = Field(None, description="結束日期")
    gpa: Optional[float] = Field(None, description="GPA")
    description: Optional[str] = Field(None, description="額外描述")
    location: Optional[str] = Field(None, description="學校地點")
    honors: Optional[List[str]] = Field(default_factory=list, description="榮譽獎項")
    relevant_courses: Optional[List[str]] = Field(default_factory=list, description="相關課程")
    thesis: Optional[str] = Field(None, description="論文題目")
    activities: Optional[List[str]] = Field(default_factory=list, description="課外活動")

class WorkExperience(BaseModel):
    """Work experience model representing professional history."""
    company: Optional[str] = Field(None, description="公司名稱")
    position: Optional[str] = Field(None, description="職位")
    start_date: Optional[date] = Field(None, description="開始日期")
    end_date: Optional[date] = Field(None, description="結束日期")
    description: Optional[str] = Field(None, description="工作描述")
    achievements: Optional[List[str]] = Field(default_factory=list, description="主要成就")
    location: Optional[str] = Field(None, description="工作地點")
    department: Optional[str] = Field(None, description="部門")
    supervisor: Optional[str] = Field(None, description="主管")
    employment_type: Optional[str] = Field(None, description="僱用類型")
    technologies: Optional[List[str]] = Field(default_factory=list, description="使用技術")
    responsibilities: Optional[List[str]] = Field(default_factory=list, description="工作職責")
    projects: Optional[List[str]] = Field(default_factory=list, description="相關專案")
    salary: Optional[float] = Field(None, description="薪資")
    reason_for_leaving: Optional[str] = Field(None, description="離職原因")

class Skill(BaseModel):
    """Skill model representing professional competencies."""
    category: Optional[str] = Field(None, description="技能類別")
    name: Optional[str] = Field(None, description="技能名稱")
    level: Optional[str] = Field(None, description="熟練程度")
    years_of_experience: Optional[float] = Field(None, description="使用年資")
    last_used: Optional[date] = Field(None, description="最後使用日期")
    proficiency: Optional[str] = Field(None, description="精通程度")
    certifications: Optional[List[str]] = Field(default_factory=list, description="相關證照")
    projects: Optional[List[str]] = Field(default_factory=list, description="應用專案")
    description: Optional[str] = Field(None, description="技能描述")

class Project(BaseModel):
    """Project model representing professional projects."""
    name: Optional[str] = Field(None, description="專案名稱")
    role: Optional[str] = Field(None, description="擔任角色")
    start_date: Optional[date] = Field(None, description="開始日期")
    end_date: Optional[date] = Field(None, description="結束日期")
    description: Optional[str] = Field(None, description="專案描述")
    technologies: Optional[List[str]] = Field(default_factory=list, description="使用技術")
    achievements: Optional[List[str]] = Field(default_factory=list, description="專案成就")
    team_size: Optional[int] = Field(None, description="團隊規模")
    client: Optional[str] = Field(None, description="客戶")
    budget: Optional[float] = Field(None, description="預算")
    deliverables: Optional[List[str]] = Field(default_factory=list, description="交付項目")
    challenges: Optional[List[str]] = Field(default_factory=list, description="挑戰")
    results: Optional[List[str]] = Field(default_factory=list, description="成果")

class Certification(BaseModel):
    """Certification model representing professional certifications."""
    name: Optional[str] = Field(None, description="證照名稱")
    issuer: Optional[str] = Field(None, description="發證機構")
    issue_date: Optional[date] = Field(None, description="發證日期")
    expiry_date: Optional[date] = Field(None, description="到期日期")
    credential_id: Optional[str] = Field(None, description="證照編號")
    verification_url: Optional[str] = Field(None, description="驗證網址")
    description: Optional[str] = Field(None, description="證照描述")
    skills: Optional[List[str]] = Field(default_factory=list, description="相關技能")
    level: Optional[str] = Field(None, description="等級")
    status: Optional[str] = Field(None, description="狀態")

class Language(BaseModel):
    """Language model representing language proficiencies."""
    name: Optional[str] = Field(None, description="語言名稱")
    proficiency: Optional[str] = Field(None, description="熟練程度")
    certificate: Optional[str] = Field(None, description="相關證書")
    years_of_experience: Optional[float] = Field(None, description="使用年資")
    last_used: Optional[date] = Field(None, description="最後使用日期")
    description: Optional[str] = Field(None, description="語言描述")
    level: Optional[str] = Field(None, description="等級")

class PersonalInfo(BaseModel):
    """Personal information model representing basic contact details."""
    name: Optional[str] = Field(None, description="姓名")
    email: Optional[EmailStr] = Field(None, description="電子郵件")
    phone: Optional[str] = Field(None, description="電話")
    address: Optional[str] = Field(None, description="地址")
    nationality: Optional[str] = Field(None, description="國籍")
    current_location: Optional[str] = Field(None, description="目前位置")
    date_of_birth: Optional[date] = Field(None, description="出生日期")
    gender: Optional[str] = Field(None, description="性別")
    marital_status: Optional[str] = Field(None, description="婚姻狀況")
    website: Optional[str] = Field(None, description="個人網站")
    linkedin: Optional[str] = Field(None, description="LinkedIn")
    github: Optional[str] = Field(None, description="GitHub")
    portfolio: Optional[str] = Field(None, description="作品集")
    social_media: Optional[Dict[str, str]] = Field(default_factory=dict, description="社群媒體")
    emergency_contact: Optional[Dict[str, str]] = Field(default_factory=dict, description="緊急聯絡人")
    visa_status: Optional[str] = Field(None, description="簽證狀態")
    work_permit: Optional[str] = Field(None, description="工作許可")

class Summary(BaseModel):
    """Summary model representing professional overview."""
    professional_summary: Optional[str] = Field(None, description="專業概述")
    career_objective: Optional[str] = Field(None, description="職業目標")
    key_qualifications: Optional[List[str]] = Field(default_factory=list, description="主要資格")
    core_competencies: Optional[List[str]] = Field(default_factory=list, description="核心競爭力")
    industry_expertise: Optional[List[str]] = Field(default_factory=list, description="行業專長")
    professional_achievements: Optional[List[str]] = Field(default_factory=list, description="專業成就")
    career_highlights: Optional[List[str]] = Field(default_factory=list, description="職業亮點")
    unique_selling_points: Optional[List[str]] = Field(default_factory=list, description="獨特賣點")
    career_goals: Optional[List[str]] = Field(default_factory=list, description="職業目標")
    professional_values: Optional[List[str]] = Field(default_factory=list, description="專業價值觀")
    leadership_style: Optional[str] = Field(None, description="領導風格")
    management_approach: Optional[str] = Field(None, description="管理方法")
    problem_solving_approach: Optional[str] = Field(None, description="解決問題方法")
    communication_style: Optional[str] = Field(None, description="溝通風格")
    work_style: Optional[str] = Field(None, description="工作風格")

class CV(BaseModel):
    """Main CV model integrating all components."""
    personal_info: Optional[PersonalInfo] = Field(None, description="個人資訊")
    summary: Optional[Summary] = Field(None, description="專業概述")
    work_experience: Optional[List[WorkExperience]] = Field(default_factory=list, description="工作經驗")
    education: Optional[List[Education]] = Field(default_factory=list, description="教育背景")
    skills: Optional[List[Skill]] = Field(default_factory=list, description="技能列表")
    projects: Optional[List[Project]] = Field(default_factory=list, description="專案經驗")
    certifications: Optional[List[Certification]] = Field(default_factory=list, description="證照")
    languages: Optional[List[Language]] = Field(default_factory=list, description="語言能力")
    created_at: Optional[date] = Field(default_factory=date.today, description="建立日期")
    updated_at: Optional[date] = Field(default_factory=date.today, description="更新日期")
    version: Optional[str] = Field(None, description="版本")
    status: Optional[str] = Field(None, description="狀態")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="元數據")
