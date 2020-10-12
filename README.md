# ConvertGps2Wtw
## About
現在地座標を What3Words の3ワードに変換して、Googleマップのピンとして表示するアプリ  
This web app is converting your current location into What3Words's 3 words and pinning it to Google Maps.  
  
This app is deployed using Pythonanywhere.  
https://yt1n4.pythonanywhere.com/

## Application Image
![application_image](https://user-images.githubusercontent.com/20642652/95697420-a1cbdb80-0c79-11eb-9395-b745aa237b71.png)

## Environment
- python: 3.8
- Django: >=2.2

## Set up
1. Create file.  
    `ConvertGps2Wtw/local_settings.py`
1. Write the following.
    ```
    SECRET_KEY = '{YOUR_DJANGO_KEY}'
    GOOGLE_API_KEY = '{YOUR_GOOGLE_MAPS_JAVASCRIPT_API_KEY}'
    WHAT3WORDS_KEY = '{YOUR_WHAT3WORDS_API_KEY}'
    ```
1. Run command.
    ```
    $ python3 manage.py migrate
    $ python3 manage.py runserver
    ```
