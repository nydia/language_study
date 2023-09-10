from PIL import Image, ImageDraw

# 生成基本的头像
# 上述代码使用Python的PIL库（Python Imaging Library）来生成头像。请注意，您需要确保安装了PIL库，您可以通过在命令行中运行pip install pillow来安装它。
class Avatar:
    def __init__(self, size=200, background_color=(255, 255, 255), border_color=(0, 0, 0)):
        self.size = size
        self.background_color = background_color
        self.border_color = border_color

    def generate(self, name, save_path=None):
        image = Image.new('RGB', (self.size, self.size), self.background_color)
        draw = ImageDraw.Draw(image)

        # Draw a border
        border_width = 10
        draw.rectangle([0, 0, self.size - 1, self.size - 1], outline=self.border_color, width=border_width)

        # Draw text (initials) in the center of the avatar
        font_size = self.size // 3
        font = ImageFont.truetype("arial.ttf", font_size)
        text = self.get_initials(name)
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (self.size - text_width) // 2
        text_y = (self.size - text_height) // 2
        draw.text((text_x, text_y), text, fill=self.border_color, font=font)

        if save_path:
            image.save(save_path)
        else:
            image.show()

    def get_initials(self, name):
        name = name.strip().upper()
        initials = ""
        if name:
            names = name.split()
            for n in names:
                initials += n[0]
        return initials

if __name__ == "__main__":
    avatar = Avatar()
    name = "John Doe"  # Replace this with the desired name
    avatar.generate(name, "avatar.png")
