from cv_models import CV
import json
from datetime import date

def load_cv_from_json():
    try:
        # 讀取主要 CV 數據
        with open("sample_cv.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 讀取 summary 數據
        with open("summary.json", "r", encoding="utf-8") as f:
            summary_data = json.load(f)
        
        # 更新 summary 部分
        data["summary"] = summary_data["summary"]
        
        # 創建 CV 實例
        cv = CV(**data)
        
        # 打印 CV 資訊
        print("\n=== CV 實例創建成功！===")
        
        print("\n=== 個人資訊 ===")
        print(f"姓名: {cv.personal_info['name']}")
        print(f"電子郵件: {cv.personal_info['email']}")
        print(f"電話: {cv.personal_info['phone']}")
        print(f"地址: {cv.personal_info['address']}")
        print(f"國籍: {cv.personal_info['nationality']}")
        print(f"目前位置: {cv.personal_info['current_location']}")
        
        print("\n=== 專業概述 ===")
        print(cv.summary['professional_summary'])
        
        print("\n=== 職業目標 ===")
        print(cv.summary['career_objective'])
        
        print("\n=== 核心能力 ===")
        print("主要資格:")
        for qual in cv.summary['key_qualifications']:
            print(f"- {qual}")
        
        print("\n核心競爭力:")
        for comp in cv.summary['core_competencies']:
            print(f"- {comp}")
        
        print("\n行業專長:")
        for exp in cv.summary['industry_expertise']:
            print(f"- {exp}")
        
        print("\n專業成就:")
        for ach in cv.summary['professional_achievements']:
            print(f"- {ach}")
        
        print("\n職業亮點:")
        for high in cv.summary['career_highlights']:
            print(f"- {high}")
        
        print("\n=== 工作經驗 ===")
        for exp in cv.work_experience:
            print(f"\n公司: {exp.company}")
            print(f"職位: {exp.position}")
            print(f"期間: {exp.start_date} 至 {exp.end_date or '現在'}")
            print(f"描述: {exp.description}")
            print("成就:")
            for achievement in exp.achievements:
                print(f"- {achievement}")
        
        print("\n=== 教育背景 ===")
        for edu in cv.education:
            print(f"\n學校: {edu.school}")
            print(f"學位: {edu.degree}")
            print(f"主修: {edu.major}")
            print(f"期間: {edu.start_date} 至 {edu.end_date}")
            print(f"GPA: {edu.gpa}")
            print(f"描述: {edu.description}")
        
        print("\n=== 技能 ===")
        for skill in cv.skills:
            print(f"\n類別: {skill.category}")
            print(f"技能: {skill.name}")
            print(f"程度: {skill.level}")
            print(f"年資: {skill.years_of_experience} 年")
        
        print("\n=== 專案經驗 ===")
        for project in cv.projects:
            print(f"\n專案名稱: {project.name}")
            print(f"角色: {project.role}")
            print(f"期間: {project.start_date} 至 {project.end_date}")
            print(f"描述: {project.description}")
            print("技術: " + ", ".join(project.technologies))
            print("成就:")
            for achievement in project.achievements:
                print(f"- {achievement}")
        
        print("\n=== 證照 ===")
        for cert in cv.certifications:
            print(f"\n證照名稱: {cert.name}")
            print(f"發證機構: {cert.issuer}")
            print(f"發證日期: {cert.issue_date}")
            print(f"到期日期: {cert.expiry_date}")
            print(f"證照編號: {cert.credential_id}")
        
        print("\n=== 語言能力 ===")
        for lang in cv.languages:
            print(f"\n語言: {lang.name}")
            print(f"熟練度: {lang.proficiency}")
            if lang.certificate:
                print(f"證書: {lang.certificate}")
        
        print("\n=== 其他資訊 ===")
        print(f"建立日期: {cv.created_at}")
        print(f"更新日期: {cv.updated_at}")
        
        return cv
    except Exception as e:
        print(f"創建 CV 實例時發生錯誤: {str(e)}")
        return None

if __name__ == "__main__":
    print("開始載入 CV 資料...")
    cv = load_cv_from_json()
    if cv:
        print("\n=== CV 實例已成功創建並驗證！===")
