# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from io import BytesIO
import requests

def image_gen(titulo, subtitulo_1, text, empresa, empresa_blurb, url_base = '/content/'):
    
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/mockmedium.jpg"

    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # Open the image file
    #image = Image.open(url_base+"mockmedium.jpg")
    
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/titulo.otf"
    response = requests.get(url)
    # response.content
    titulo_font = ImageFont.truetype(BytesIO(response.content), 36)
    # Choose a font and font size
    #titulo_font = ImageFont.truetype(url_base+'titulo.otf', 36)
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/subtitulo.ttf"
    response = requests.get(url)
    subtitulo_1_font = ImageFont.truetype(BytesIO(response.content), 30)
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/subtitulo.ttf"
    response = requests.get(url)
    subtitulo_2_font = ImageFont.truetype(BytesIO(response.content), 25)
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/texto.ttf"
    response = requests.get(url)
    text_font = ImageFont.truetype(BytesIO(response.content), 25)
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/empresa.otf"
    response = requests.get(url)
    empresa_font = ImageFont.truetype(BytesIO(response.content), 22)
    url = "https://raw.githubusercontent.com/diegotorpoco/blog_boost/master/empresa.otf"
    response = requests.get(url)
    empresa_blurb_font = ImageFont.truetype(BytesIO(response.content), 20)
    #subtitulo_1_font = ImageFont.truetype(url_base+'subtitulo.ttf', 30)
    #subtitulo_2_font = ImageFont.truetype(url_base+'subtitulo.ttf', 25)
    #text_font = ImageFont.truetype(url_base+'texto.ttf', 25)
    #empresa_font = ImageFont.truetype(url_base+'empresa.otf', 22)
    #empresa_blurb_font = ImageFont.truetype(url_base+'empresa.otf', 20)

    subtitulo_1 = "The importance of validating data" #Resultado de prompt: Subtitle for X
    
    width_1 = 75
    wraped_text = textwrap.fill(text, width=width_1) #Pasa de un string lineal a un parrafo con X longitud de caracteres/distancia
    text = wraped_text

    width_2 = 40
    wraped_empresa = textwrap.fill(empresa_blurb, width=width_2) #Pasa de un string lineal a un parrafo con X longitud de caracteres/distancia
    empresa_blurb = wraped_empresa

    wraped_titulo = textwrap.fill(titulo, width=width_1) #Pasa de un string lineal a un parrafo con X longitud de caracteres/distancia
    titulo = wraped_titulo

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)
    subtitulo_2 = "Introduccion"
    # Add the text to the image
    draw.text((130, 30), empresa, font=empresa_font, fill=(0, 0, 0))
    draw.text((50, 140), titulo, font=titulo_font, fill=(0, 0, 0))
    draw.text((50, 210), subtitulo_1 , font=subtitulo_1_font, fill=(0, 0, 0))
    draw.text((50, 275), subtitulo_2, font=subtitulo_2_font, fill=(0, 0, 0))
    draw.text((50, 355), text, font=text_font, fill=(0, 0, 0))


    draw.text((1080, 165), empresa, font=empresa_font, fill=(0, 0, 0))
    draw.text((1080, 240), empresa_blurb, font=empresa_blurb_font, fill=(117, 117, 117))


    # Save the edited image
    # image.save(url_base+"edited_mockup.jpg")

    # mockup = url_base+"edited_mockup.jpg"
    return image

#titulo = "Using SHAP with Cross-Validation in Python" #Literalmente el tipo de blog que quiere la persona
#subtitulo_1 = "The importance of validating data" #Resultado de prompt: Subtitle for X
#subtitulo_2 = "Introduction" #Solo introducción
#Core prompt
#text = "In many situations, machine learning models are preferred over traditional linear models because of their superior predictive performance and their ability to handle complex nonlinear data. However, a common criticism of machine learning models is their lack of interpretability. For example, ensemble methods such as XGBoost and Random Forest, combine the results of many individual learners to generate their results. Although this often leads to superior performance, it makes it hard to know the contribution of each feature in the dataset to the output. In many situations, machine learning models are preferred over traditional linear models because of their superior predictive performance and their ability to handle complex nonlinear data. However, a common criticism of machine learning models is their lack of interpretability. For example, ensemble methods such as XGBoost and Random Forest, combine the results of many individual learners to generate their results. Although this often leads to superior performance, it makes it hard to know the contribution of each feature in the dataset to the output." 
#empresa = "Dan Kirk" #El nombre de la empresa
#empresa_blurb = "Researcher at Wageningen University Research, MSc Nutrition Health and BSc Biochemistry, practicing data science and lifetime natural bodybuilder." #La minidescripción de la persona

#link = image_gen(titulo, subtitulo_1, text, empresa, empresa_blurb, url_base='C:/Users/bruno/Desktop/Drive/Bruno/SEO/')
#prueba = Image.open(link)
#prueba.show()

