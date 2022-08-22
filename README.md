
# Spotify Color Palette Generation

Spotify displays song lyrics on a card during playing a song and the color of the card and the gradient background of the window changes acoording to the colors of the album art/cover. I wanted to replicate this feature on a basic application. I have built a simple web app for automatically generating Spotify like color palette from album arts. 
The application is built using Django python backend development framework. A color extractor script is used for extracting dominant colors using K means clustering from a given image. Later the extracted colors are sent to the CSS for generating desired styles for the background and the lyric card of the window.

## Screenshot
![](screenshot.png)

## Setup & Run
To run the application, first you need to clone the entire repository and then install the dependencies from the requirements.txt file.
The application itself is a django project and only contains one django app named 'home'.

The app uses only one HTML page which is the home page located in "/home/templates/home/home.html". 

The CSS file along with some sample album arts are located in "/home/static/home/styles.css".

Running "python manage.py runserver" in the root directory will start a local server on 'http://127.0.0.1:8000/'.

Then in the views.py file of the home directory, change the 'img_path' variable's value and refresh the website to see the results.

Currently there are 6 album arts in the static folder and the value of img_path can be:

"home/popevil.jpg"

"home/arcane.jpg"

"home/linkinpark.jpg" 

"home/bmth.jpg" 

"home/bostonmanor.jpg" 

"home/monuments.jpg" 



## Overview
In the views.py file of the home app, home() sends an image path into the color extractor and then renders home.html page upon receiving the results.
The color extractor script opens the image using the path and runs K means clustering for 20 epochs based on 4 clusters. This returns 4 dominant colors from the album art in RGB values in a list.
The list of RGB values are then sorted keeping the idea in mind that the higher the summation value of R,G and B the brighter the color is in the palette.
Later the brightest color is selected as the card color and the 2nd brightest is selected as the light gradient color of the background. These values are then passed into the template as template variables. Finally the template sends these template variable's values into the CSS file which styles the window according to the selected colors it received.

## Update
Some incremental updates were made on the app to provide more options to select an image. Inside the 'Updated-App' folder there is a similar app which has slightly different features and functionalities compared to the original one. On 'http://127.0.0.1:8000/' the updated app provides an option to upload any image from the computer. Then the uploaded image is stored in the database of the app and then displayed on the web page. The image file is stored in the 'media' folder of the app. The app now simply returns the last uploaded image from the database and then generates the web page.
Also there is another new feature at 'http://127.0.0.1:8000/url'. On this page you can put any image link on the form and submit to generate the web page for the desired image. This time the app simply downloads the image from the weblink and replaces a certain image to generate a new web page. 
Also the dominant colors are now displayed on the web pages for debugging purpose.
