from PIL import Image, ImageDraw, ImageFont
import textwrap


# Open the image file
image = Image.open("mockmedium.jpg")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Choose a font and font size
titulo_font = ImageFont.truetype("titulo_sohne.otf", 36)
subtitulo_1_font = ImageFont.truetype("SourceSerifPro-SemiBold.ttf", 30)
subtitulo_2_font = ImageFont.truetype("SourceSerifPro-SemiBold.ttf", 25)
text_font = ImageFont.truetype("textoserif.ttf", 25)
empresa_font = ImageFont.truetype("biosohne.otf", 22)
empresa_blurb_font = ImageFont.truetype("biosohne.otf", 20)

titulo = "Using SHAP with Cross-Validation in Python"
subtitulo_1 = "The importance of validating data"
subtitulo_2 = "Introduction"
text = "In many situations, machine learning models are preferred over traditional linear models because of their superior predictive performance and their ability to handle complex nonlinear data. However, a common criticism of machine learning models is their lack of interpretability. For example, ensemble methods such as XGBoost and Random Forest, combine the results of many individual learners to generate their results. Although this often leads to superior performance, it makes it hard to know the contribution of each feature in the dataset to the output."
empresa = "Dan Kirk"
empresa_blurb = "Researcher at Wageningen University Research, MSc Nutrition Health and BSc Biochemistry, practicing data science and lifetime natural bodybuilder."


width_1 = 75
wraped_text = textwrap.fill(text, width=width_1)
text = wraped_text

width_2 = 40
wraped_empresa = textwrap.fill(empresa_blurb, width=width_2)
empresa_blurb = wraped_empresa


# Add the text to the image
draw.text((130, 30), empresa, font=empresa_font, fill=(0, 0, 0))
draw.text((50, 140), titulo, font=titulo_font, fill=(0, 0, 0))
draw.text((50, 210), subtitulo_1 , font=subtitulo_1_font, fill=(0, 0, 0))
draw.text((50, 275), subtitulo_2, font=subtitulo_2_font, fill=(0, 0, 0))
draw.text((50, 355), text, font=text_font, fill=(0, 0, 0))


draw.text((1080, 165), empresa, font=empresa_font, fill=(0, 0, 0))
draw.text((1080, 240), empresa_blurb, font=empresa_blurb_font, fill=(117, 117, 117))


# Save the edited image
image.save("edited_facebook_post_mockup.jpg")
img_path = "/content/edited_facebook_post_mockup.jpg"

image = Image.open('edited_facebook_post_mockup.jpg')