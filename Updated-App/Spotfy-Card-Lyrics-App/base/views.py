from turtle import color
from cv2 import sort
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ImageForm, UserForm
from .models import Image
from numpy import gradient
import color_extractor

# THESE ARE FOR THE COLOR EXTRACTOR SCRIPT

# class BaseView(TemplateView):
#     template_name = "base/home.html"
# img_path = "base/static/base/bmth.jpg"
img_path = "base/bostonmanor.jpg"
img_path_full = "base/static/" + img_path

def home(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()

    if(len(img) == 0):
        rgb_list = color_extractor.return_color_palette(img_path_full)
        rgb_list.sort()
        card_color = str(rgb_list[-1])
        card_color = "rgb" + card_color
        gradient_light = str(rgb_list[-2])
        gradient_light = "rgb" + gradient_light


        color_1 = str(rgb_list[0])
        color_1 = "rgb" + color_1

        color_2 = str(rgb_list[1])
        color_2 = "rgb" + color_2

        color_3 = str(rgb_list[2])
        color_3 = "rgb" + color_3

        color_4 = str(rgb_list[3])
        color_4 = "rgb" + color_4

        print(f"color 1: {color_1}")
        print(f"color 2: {color_2}")
        print(f"color 3: {color_3}")
        print(f"color 4: {color_4}")

        return render(request, 'base/home.html', 
                    {'img_path': img_path,
                    'default':True,
                    'card_color':card_color, 
                    'gradient_light':gradient_light,
                    'form':form,
                    'color_1':color_1,
                    'color_2':color_2,
                    'color_3':color_3,
                    'color_4':color_4
                    })


    photo_ids = []
    photo_urls = []
    for i in img:
        photo_urls.append(i.photo.url)
        photo_ids.append(i.id)

    last_id = photo_ids[-1]

    print(img_path_full)
    photo_url_path = photo_urls[-1]
    photo_url_path = photo_url_path[1:]
    print(photo_url_path)

    rgb_list = color_extractor.return_color_palette(photo_url_path)
    rgb_list.sort()
    card_color = str(rgb_list[-1])
    card_color = "rgb" + card_color
    gradient_light = str(rgb_list[-2])
    gradient_light = "rgb" + gradient_light
    
    color_1 = str(rgb_list[0])
    color_1 = "rgb" + color_1

    color_2 = str(rgb_list[1])
    color_2 = "rgb" + color_2

    color_3 = str(rgb_list[2])
    color_3 = "rgb" + color_3

    color_4 = str(rgb_list[3])
    color_4 = "rgb" + color_4

    print(f"color 1: {color_1}")
    print(f"color 2: {color_2}")
    print(f"color 3: {color_3}")
    print(f"color 4: {color_4}")

    return render(request, 'base/home.html', 
                {'img_path': img_path,
                'default':False,
                'img':img,
                'last_id':last_id, 
                'card_color':card_color, 
                'gradient_light':gradient_light,
                'form':form,
                'color_1':color_1,
                'color_2':color_2,
                'color_3':color_3,
                'color_4':color_4
                })


def debug(request):
    rgb_list = color_extractor.return_color_palette(img_path_full)
    print(len(rgb_list))
    rgb_list.sort()
    color_1 = str(rgb_list[0])
    color_1 = "rgb" + color_1

    color_2 = str(rgb_list[1])
    color_2 = "rgb" + color_2

    color_3 = str(rgb_list[2])
    color_3 = "rgb" + color_3

    color_4 = str(rgb_list[3])
    color_4 = "rgb" + color_4

    print(f"color 1: {color_1}")
    print(f"color 2: {color_2}")
    print(f"color 3: {color_3}")
    print(f"color 4: {color_4}")

    return render(request, 'base/debug.html', 
                {'color_1':color_1,
                'color_2':color_2,
                'color_3':color_3,
                'color_4':color_4
                }) 



def url(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("Form Valid")
            image_url = form.cleaned_data['user']
            print("Image Url: " + image_url)

            import requests

            img_data = requests.get(image_url).content
            with open('base/static/base/downloaded_image.jpg', 'wb') as handler:
                handler.write(img_data)


    form = UserForm()
    print("Form not valid")
    
    img_path = "base/downloaded_image.jpg"
    img_path_full = "base/static/" + img_path

    
    rgb_list = color_extractor.return_color_palette(img_path_full)
    rgb_list.sort()
    card_color = str(rgb_list[-1])
    card_color = "rgb" + card_color
    gradient_light = str(rgb_list[-2])
    gradient_light = "rgb" + gradient_light


    color_1 = str(rgb_list[0])
    color_1 = "rgb" + color_1

    color_2 = str(rgb_list[1])
    color_2 = "rgb" + color_2

    color_3 = str(rgb_list[2])
    color_3 = "rgb" + color_3

    color_4 = str(rgb_list[3])
    color_4 = "rgb" + color_4

    print(f"color 1: {color_1}")
    print(f"color 2: {color_2}")
    print(f"color 3: {color_3}")
    print(f"color 4: {color_4}")

    return render(request, 'base/url.html', 
                {'img_path': img_path,
                'default':True,
                'card_color':card_color, 
                'gradient_light':gradient_light,
                'form':form,
                'color_1':color_1,
                'color_2':color_2,
                'color_3':color_3,
                'color_4':color_4
                })



def simple_function(request):
    print('\nThis is a simple function\n')
    # exec(open('base/scripts/test_script.py').read())
    # INSTRUCTION: Swap image path for different renders
   
    rgb_list = color_extractor.return_color_palette(img_path_full)
    rgb_list.sort()
    print(rgb_list[-1])
    rgb = str(rgb_list[-1])
    print(rgb)
    

    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")