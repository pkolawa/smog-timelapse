from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class DrawText:

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((1164, 742),"13:55",(255,255,255),font=font_light_160)
    draw.text((1649,760),"23°C",(255,255,255),font=font_light_40)
    draw.text((1649,812),"40%",(255,255,255),font=font_light_40)
    draw.text((1649,861),"1014 hPa",(255,255,255),font=font_light_40)

    draw.text((213,859),"normy",(255,255,255),font=font_bold_25)
    draw.text((445,859),"normy",(255,255,255),font=font_bold_25)
    draw.text((705,859),"normy",(255,255,255),font=font_bold_25)
    draw.text((960,859),"normy",(255,255,255),font=font_bold_25)

    draw.text((213,809),"58%",(255,255,255),font=font_bold_50)
    draw.text((445,809),"211%",(255,255,255),font=font_bold_50)
    draw.text((705,809),"23%",(255,255,255),font=font_bold_50)
    draw.text((960,809),"18%",(255,255,255),font=font_bold_50)

    draw.text((213,752),"PM10",(255,255,255),font=font_regular_35)
    draw.text((445,752),"PM2,5",(255,255,255),font=font_regular_35)
    draw.text((705,752),"NO2",(255,255,255),font=font_regular_35)
    draw.text((960,752),"SO2",(255,255,255),font=font_regular_35)

    draw.text((213,895),"4,78",(255,255,255),font=font_light_37)
    draw.text((445,895),"124,83",(255,255,255),font=font_light_37)
    draw.text((705,895),"1,78",(255,255,255),font=font_light_37)
    draw.text((960,895),"15,78",(255,255,255),font=font_light_37)

    draw.text((213,935),"μg/m3",(255,255,255),font=font_bold_25)
    draw.text((445,935),"μg/m3",(255,255,255),font=font_bold_25)
    draw.text((705,935),"μg/m3",(255,255,255),font=font_bold_25)
    draw.text((960,935),"μg/m3",(255,255,255),font=font_bold_25)

    def __init__(self):
        img = Image.open("2.jpg")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font_light_160 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Light.ttf", 160)
        font_light_40 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Light.ttf", 40)
        font_light_37 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Light.ttf", 37)
        font_bold_50 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf", 50)
        font_bold_25 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf", 25)
        font_regular_35 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Regular.ttf", 35)

    def drawAndShow(self, xpos, ypos, text, redColor, greenColor, blueColor, fontType):
        self.draw.text((xpos, ypos), text, (redColor, greenColor, blueColor), font=fontType)
        self.img.show()

    def drawAndSave(self, xpos, ypos, text, redColor, greenColor, blueColor, fontType):
        self.draw.text((xpos,ypos),text,(redColor,greenColor,blueColor),font=fontType)
        self.img.save('sample-out.jpg')

# img.show()
