from nydia_tools import settings

# 随机字符串
def get_base_dir(): 
    base_path = settings.BASE_DIR.__str__()
    return base_path
def get_img_dir(): 
    base_path = settings.BASE_DIR.__str__()
    img_path = [base_path, '/files/file_path/']
    return ''.join(img_path)