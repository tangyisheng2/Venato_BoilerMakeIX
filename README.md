# Venato_BoilerMakeIX

Hi there, this is the repo for Venato@BoilerMakeIX!😁

![img](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/804/612/datas/original.png)

## Inspiration
As the adage goes, "Well-begun is half done." However, getting started really can be the hard part. We wanted to create an application that allows users to keep track and get an unbiased analysis of their eating habits without requiring the user to exert unnecessary effort.

## What it does
Venato is an application that allows users to analyze and track their health habits by inputting their groceries and meals. Inputting groceries and meals is as easy as typing in your items and selecting them. With this information, our program will track and tabulate your calorie, protein, and caffeine intake. Additionally, using our Machine Learning Model, we can predict your obesity risk based on your grocery habits.

## How we built it
Frontend: Chakra, Redux
Backend: Google Cloud SQL, Flask, Flask-RESTful, Netlify (for deploying)
NN Model: Pytorch, Pandas, HuggingFace, Flask, Google Colab
Our dataset of nutritional values for foods is based on the FNDDS Nutrient Values dataset. It was modified to remove components that were not needed for the development of Venato.

The obesity model is limited only by the content of this dataset. It consists of countries and their average consumption in weight across diverse categories of food. We developed the neural network to decipher meaning from the data while not overfitting it. With state of the art neural network techniques accompanied by leading natural language processing transformers we made the most from the set to enable any user submission to translate to valuable data for the AI.

## Challenges we ran into
We ran into numerous challenges when developing Venato, the largest one was time. We were unable to complete the receipt analysis feature. However, we planned ahead and ensured that we don't let a setback faze us as we set milestones which allowed us to have an MVP that was attainable and then the ability to add extra features (such as receipt analysis and the obesity risk analyzer).

##Accomplishments that we're proud of
We're incredibly proud to have done the following:

- Create a working and stable MVP for Venato.
- Generate an accurate ML Model that can predict obesity risk.
- Integrating the FNDDS dataset to our app to provide precise nutritional information for thousands of produce.
- Creating a SQL backend that is strong and usable.
## What we learned
Creating Venato was a really insightful experience for all 4 of us. This was Michael and Eason's first rodeo with hackathons and they learned a lot about the nuances of hacking. As a collective, we learned about the ingenious methods of using machine learning to create an application that can be an effective and useful health tracker.

What's next for Venato
We've developed a robust structure for Venato which allows for dynamic scalability. This allows us to add a lot more awesome things in the future.

Receipt Support: We want to allow users to snap a picture of their receipt and get their analysis on the spot. Due to time constraints, we were unable to deploy this feature but we have our blueprint of an OCR system that can read the receipts and locate the information needed to find the nutritional values.
Native Mobile Experience: We have designed a conceptual mobile experience for Venato which has the same functionality as our operational web app. This Figma file and the attachment on the Devpost outlines that vision we have.
Smartwatch Companion: A smartwatch companion application for Venato will allow us to take this app to newer and greater heights.


## Play with the app

To play with the code, run
```shell
pip install -r requirements.txt
```
This code is tested in Linux, MySQL 5.6 and Python3.10 environment.
