# ImageCaptioningApp 
**This is a guide to run demo app**

## Server

First, make sure your phone connect to your Django server. We suggest use **ngork** to do this. You can download from **[hear](https://ngrok.com/download)**. 

Ngrok is a cross-platform application that enables developers to expose a local development server to the Internet with minimal effort. The software makes your locally-hosted web server appear to be hosted on a subdomain of ngrok.com, meaning that no public IP or domain name on the local machine is needed.

From your ngrok directory run :

`ngrok http 8000`

You will see something like this :

![Alt text](https://github.com/huavanson/ImageCaptioningApp/blob/main/ngrok.png "Optional title")

Next, copy the link which ngrok create(in this case http://fa61dae7a148.ngrok.io) add into INSTALLED_APPS and ALLOWEDS_HOSTS at django/upload/settings.py. Then run :

`python manage.py runserver`

Your server will be ready !!!

## Client

First, copy the ngrok link then paste it into App.js so that the react app can request to your server. 

`npm start` or `yarn start` or `expo start`

When you run expo start (or npm start), Expo CLI starts Metro Bundler, which is an HTTP server that compiles the JavaScript code of our app using Babel and serves it to the Expo app. It also pops up Expo Dev Tools, a graphical interface for Expo CLI. Then you must turn on the **Tunnel** button. Under the tunnel setting, your computer will setup a tunnel to exp.direct, a domain using the ngrok tunnel service.

**Please make sure you installed Expo Platform and downloaded the ExpoGo from CH play** 

Check **[this site](https://expo.io/)** for more information

Opening the app on your phone/tablet, on your Android device, press "Scan QR Code" on the "Projects" tab of the Expo Go app and scan the QR code you see in the terminal or in Expo Dev Tools. You will see what we did on your device. Press the "Pick an image from camera roll" button to connect your device camera and take a picture. 
The image is posted to the django server for processing and returns the results immediately.
