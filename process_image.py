from PIL import Image
import numpy as np

# 創建一個簡單的黑白圖片
width = 400
height = 500
image = np.zeros((height, width), dtype=np.uint8)

# 添加一些基本形狀
image[100:400, 100:300] = 255  # 臉部區域
image[150:200, 150:250] = 200  # 眼鏡區域

# 轉換為 PIL Image
img = Image.fromarray(image)

# 保存圖片
img.save('images/superman_glasses.jpg') 