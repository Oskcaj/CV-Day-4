from cv_models import CV, WorkExperience
import json
from datetime import date
from typing import List, Dict, Any

def validate_work_experience():
    try:
        with open("work_experience.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 驗證每個工作經驗
        for exp in data["work_experience"]:
            # 轉換日期字串為 date 對象
            exp["start_date"] = date.fromisoformat(exp["start_date"])
            if exp["end_date"]:
                exp["end_date"] = date.fromisoformat(exp["end_date"])
            
            # 使用 Pydantic 模型驗證
            WorkExperience(**exp)
        
        print("✅ work_experience.json 驗證通過")
        return True
    except Exception as e:
        print(f"❌ work_experience.json 驗證失敗: {str(e)}")
        return False

def validate_summary():
    try:
        with open("summary.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 驗證 summary 結構
        CV(**data)
        
        print("✅ summary.json 驗證通過")
        return True
    except Exception as e:
        print(f"❌ summary.json 驗證失敗: {str(e)}")
        return False

if __name__ == "__main__":
    print("開始驗證 JSON 文件...")
    work_exp_valid = validate_work_experience()
    summary_valid = validate_summary()
    
    if work_exp_valid and summary_valid:
        print("所有文件驗證通過！")
    else:
        print("部分文件驗證失敗，請檢查錯誤訊息。") 