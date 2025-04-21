import streamlit as st
import json
from datetime import datetime
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="Professional CV",
    page_icon="🦸",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: #f0f8ff;
    }
    .header {
        font-size: 3rem;
        font-weight: 800;
        color: #0066CC;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        letter-spacing: -1px;
    }
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #0066CC;
        margin: 3rem 0 1.5rem 0;
        border-bottom: 4px solid #FF0000;
        padding-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        letter-spacing: -0.5px;
        display: inline-block;
    }
    .company-name {
        font-size: 1.6rem;
        font-weight: 700;
        color: #0066CC;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .position {
        font-size: 1.3rem;
        font-weight: 600;
        color: #FF0000;
        margin-bottom: 0.5rem;
        letter-spacing: -0.3px;
    }
    .date {
        font-size: 1rem;
        color: #666666;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    .achievement-item {
        margin-bottom: 0.8rem;
        padding: 0.8rem 1.2rem;
        border-left: 4px solid #FFD700;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .achievement-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .description {
        margin: 1.2rem 0;
        line-height: 1.8;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        font-size: 1.1rem;
    }
    .summary-text {
        font-size: 1.2rem;
        line-height: 1.8;
        margin: 1.5rem 0;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .qualification-item {
        margin: 0.8rem 0;
        padding: 1rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #FF0000;
        transition: transform 0.2s ease;
    }
    .qualification-item:hover {
        transform: translateX(5px);
    }
    .competency-item {
        display: inline-block;
        margin: 0.5rem;
        padding: 0.8rem 1.5rem;
        background-color: #0066CC;
        border-radius: 25px;
        color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        font-weight: 500;
    }
    .competency-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .contact-info {
        display: flex;
        flex-wrap: wrap;
        gap: 1.2rem;
        margin-bottom: 1.5rem;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        color: #0066CC;
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
        background-color: rgba(0, 102, 204, 0.1);
        border-radius: 6px;
        transition: transform 0.2s ease;
    }
    .contact-item:hover {
        transform: translateY(-2px);
    }
    .skill-item {
        margin: 0.8rem 0;
        padding: 1rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #FFD700;
        transition: transform 0.2s ease;
    }
    .skill-item:hover {
        transform: translateX(5px);
    }
    .project-item {
        margin: 1.5rem 0;
        padding: 1.5rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #0066CC;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .project-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .certification-item {
        margin: 0.8rem 0;
        padding: 1rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #FF0000;
        transition: transform 0.2s ease;
    }
    .certification-item:hover {
        transform: translateX(5px);
    }
    .language-item {
        display: inline-block;
        margin: 0.5rem;
        padding: 0.8rem 1.5rem;
        background-color: #FFD700;
        border-radius: 25px;
        color: #0066CC;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .language-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f2ff 100%);
    }
    .profile-container {
        display: flex;
        align-items: center;
        gap: 3rem;
        margin-bottom: 3rem;
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .profile-image {
        border-radius: 50%;
        border: 4px solid #FF0000;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    .profile-image:hover {
        transform: scale(1.05);
    }
    .profile-info {
        flex: 1;
    }
    .section-container {
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    with open('sample_cv.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Format date
def format_date(date_str):
    if not date_str:
        return "Present"
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%B %Y")

# Main app
def main():
    data = load_data()
    
    # Profile Section with Image
    st.markdown("<div class='profile-container'>", unsafe_allow_html=True)
    
    # Profile Image
    col1, col2 = st.columns([1, 2])
    with col1:
        image_path = 'images/superman_glasses.jpg'
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                st.image(image, width=200, use_column_width=False)
            except Exception as e:
                st.error(f"""
                ### 圖片載入失敗
                請確認圖片格式是否正確。
                錯誤信息：{str(e)}
                """)
        else:
            st.warning("""
            ### 請添加個人照片
            1. 在專案目錄下建立 `images` 資料夾
            2. 將您的照片命名為 `superman_glasses.jpg`
            3. 放入 `images` 資料夾中
            """)
    
    # Personal Info
    with col2:
        st.markdown(f"<div class='header'>{data['personal_info']['name']}</div>", unsafe_allow_html=True)
        st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
        st.markdown(f"<div class='contact-item'>📧 {data['personal_info']['email']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='contact-item'>📱 {data['personal_info']['phone']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='contact-item'>📍 {data['personal_info']['current_location']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Professional Summary Section
    st.markdown("<div class='section-title'>Professional Summary</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='summary-text'>
    Experienced reporter transitioning to cybersecurity engineer with extensive experience in real-time response and crisis management. 
    Excels at maintaining composure under pressure and solving complex problems in minimal time. 
    Possesses exceptional observation and analytical skills, enabling quick identification of potential threats.
    </div>
    """, unsafe_allow_html=True)
    
    # Career Objective
    st.markdown("<div class='section-title'>Career Objective</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='summary-text'>
    Transforming journalistic acumen and sense of justice into cybersecurity protection, safeguarding vulnerable groups in the digital world. 
    Committed to creating a safer online environment where everyone can use technology with peace of mind.
    </div>
    """, unsafe_allow_html=True)
    
    # Key Qualifications
    st.markdown("<div class='section-title'>Key Qualifications</div>", unsafe_allow_html=True)
    qualifications = [
        "Exceptional crisis management skills",
        "Rapid learning and adaptation to new technologies",
        "Outstanding problem-solving abilities",
        "Strong sense of responsibility and justice",
        "Excellent teamwork spirit"
    ]
    for qualification in qualifications:
        st.markdown(f"<div class='qualification-item'>• {qualification}</div>", unsafe_allow_html=True)
    
    # Core Competencies
    st.markdown("<div class='section-title'>Core Competencies</div>", unsafe_allow_html=True)
    competencies = [
        "Real-time response and decision-making",
        "Risk assessment and threat analysis",
        "System security protection",
        "Vulnerability detection and remediation",
        "Security awareness training"
    ]
    cols = st.columns(3)
    for i, competency in enumerate(competencies):
        with cols[i % 3]:
            st.markdown(f"<div class='competency-item'>{competency}</div>", unsafe_allow_html=True)
    
    # Industry Expertise
    st.markdown("<div class='section-title'>Industry Expertise</div>", unsafe_allow_html=True)
    expertise = [
        "Cybersecurity",
        "System Protection",
        "Data Encryption",
        "Security Monitoring",
        "Emergency Response"
    ]
    cols = st.columns(3)
    for i, item in enumerate(expertise):
        with cols[i % 3]:
            st.markdown(f"<div class='competency-item'>{item}</div>", unsafe_allow_html=True)
    
    # Work Experience
    st.markdown("<div class='section-title'>Work Experience</div>", unsafe_allow_html=True)
    for experience in data['work_experience']:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"<div class='company-name'>{experience['company']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='position'>{experience['position']}</div>", unsafe_allow_html=True)
            
        with col2:
            start_date = format_date(experience['start_date'])
            end_date = format_date(experience['end_date'])
            st.markdown(f"<div class='date'>{start_date} - {end_date}</div>", unsafe_allow_html=True)
        
        # Translate descriptions
        descriptions = {
            "Daily Planet": "As a senior reporter, responsible for real-time coverage of major news events. Known for remarkable speed and accuracy in reporting, often arriving at scenes before other reporters. Particularly skilled in disaster scene reporting, always completing interviews safely in the most dangerous situations.",
            "Smallville Gazette": "Started journalism career at a small local newspaper, covering community news and sports. Known for exceptional physical fitness and endurance, able to complete multiple reporting tasks in a short time. Particularly focused on vulnerable groups and social justice issues."
        }
        
        st.markdown(f"<div class='description'>{descriptions.get(experience['company'], experience['description'])}</div>", unsafe_allow_html=True)
        
        st.markdown("**Key Achievements:**")
        # Translate achievements
        achievements = {
            "Daily Planet": [
                "Received 'Reporter of the Year' award for three consecutive years",
                "Exclusive coverage of multiple major news events, including major disasters in Metropolis",
                "Established extensive news source network for quick access to first-hand information",
                "Maintained high-quality reporting under extreme weather conditions"
            ],
            "Smallville Gazette": [
                "Successfully exposed multiple local corruption cases",
                "Completed reporting tasks under extreme weather conditions",
                "Built community trust, becoming the most trusted reporter among local residents",
                "Protected colleagues' safety in multiple dangerous situations"
            ]
        }
        
        for achievement in achievements.get(experience['company'], experience['achievements']):
            st.markdown(f"<div class='achievement-item'>{achievement}</div>", unsafe_allow_html=True)
        
        st.markdown("---")
    
    # Education
    st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
    for education in data['education']:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"<div class='company-name'>{education['school']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='position'>{education['degree']} in {education['major']}</div>", unsafe_allow_html=True)
            
        with col2:
            start_date = format_date(education['start_date'])
            end_date = format_date(education['end_date'])
            st.markdown(f"<div class='date'>{start_date} - {end_date}</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='description'>
        Major in Journalism with a minor in Computer Science. Served as editor of the campus newspaper and participated in multiple campus news projects.
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"**GPA:** {education['gpa']}")
        st.markdown("---")
    
    # Skills
    st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
    for skill in data['skills']:
        st.markdown(f"<div class='skill-item'>{skill['name']} ({skill['level']}) - {skill['years_of_experience']} years experience</div>", unsafe_allow_html=True)
    
    # Projects
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
    for project in data['projects']:
        st.markdown(f"""
        <div class='project-item'>
            <div class='company-name'>{project['name']}</div>
            <div class='position'>{project['role']}</div>
            <div class='date'>{format_date(project['start_date'])} - {format_date(project['end_date'])}</div>
            <div class='description'>{project['description']}</div>
            <div style='margin-top: 1rem;'><strong>Technologies:</strong></div>
            <div class='contact-info' style='margin-top: 0.5rem;'>
                {''.join([f"<div class='contact-item'>{tech}</div>" for tech in project['technologies']])}
            </div>
            <div style='margin-top: 1rem;'><strong>Key Achievements:</strong></div>
            {''.join([f"<div class='achievement-item'>{achievement}</div>" for achievement in project['achievements']])}
        </div>
        """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)
    for cert in data['certifications']:
        st.markdown(f"""
        <div class='certification-item'>
            <div class='company-name'>{cert['name']}</div>
            <div class='description'>
                <strong>Issuer:</strong> {cert['issuer']}<br>
                <strong>Valid:</strong> {format_date(cert['issue_date'])} - {format_date(cert['expiry_date'])}<br>
                <strong>Credential ID:</strong> {cert['credential_id']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Languages
    st.markdown("<div class='section-title'>Languages</div>", unsafe_allow_html=True)
    for language in data['languages']:
        st.markdown(f"<div class='language-item'>{language['name']} ({language['proficiency']})</div>", unsafe_allow_html=True)
    
    # Professional Achievements
    st.markdown("<div class='section-title'>Professional Achievements</div>", unsafe_allow_html=True)
    achievements = [
        "Maintained system stability under extreme conditions",
        "Quickly identified and fixed security vulnerabilities",
        "Established effective security protection mechanisms",
        "Successfully prevented multiple potential cyber attacks"
    ]
    for achievement in achievements:
        st.markdown(f"<div class='achievement-item'>{achievement}</div>", unsafe_allow_html=True)
    
    # Career Highlights
    st.markdown("<div class='section-title'>Career Highlights</div>", unsafe_allow_html=True)
    highlights = [
        "Perfect transition from news reporting to cybersecurity",
        "Applied journalistic acumen to security protection",
        "Established rapid response security protection system",
        "Protected vulnerable groups in the digital world"
    ]
    for highlight in highlights:
        st.markdown(f"<div class='achievement-item'>{highlight}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 