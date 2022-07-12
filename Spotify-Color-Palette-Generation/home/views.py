from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from numpy import gradient
import color_extractor

# THESE ARE FOR THE COLOR EXTRACTOR SCRIPT

# class BaseView(TemplateView):
#     template_name = "base/home.html"

# Change image paths to see effects
img_path = "home/popevil.jpg"
img_path_full = "home/static/" + img_path

def home(request):
    # Color extractor returns 4 dominant colors
    rgb_list = color_extractor.return_color_palette(img_path_full)

    # Sorts color values summing up RGB values
    # Brighter color = total RGB value is higher
    # Dimmer color = total RGB value is lower
    rgb_list.sort()

    # Collect brightest color for card, highest one is the brightest one 
    card_color = str(rgb_list[-1])
    card_color = "rgb" + card_color
    # Collect second brightest one for light gradient, dark gradient is default black
    gradient_light = str(rgb_list[-2])
    gradient_light = "rgb" + gradient_light
    print(card_color)
    print(gradient_light)
    return render(request, 'home/home.html', {'img_path': img_path, 'card_color':card_color, 'gradient_light':gradient_light})

# This is a test function
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