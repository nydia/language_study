"""
opencv-python 工具去除水印
"""

import cv2

class WaterMark:
    def __init__(self) -> None:
        pass
    def remove_watermark(self, image_path, mask_path, output_path):
        print(">>> 开始去除水印 remove_watermark_with_inpaint <<<")
        # 读取原始图像和遮罩图像
        src = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # 使用 inpaint 函数去除水印
        dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)

        # 保存结果图像
        cv2.imwrite(output_path, dst)
 
watermark_util = WaterMark()
