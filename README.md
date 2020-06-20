# LabelWise - Backend

LabelWise allows you to easily visualize nutrition and ingredient labels. Take a photo of any Canadian/US nutritional label to analyze the food's nutrient breakdown. Labelwise also allows you to gain insights into the ingredients of your food, highlighting any potentially harmful additives. An demo video of the app can be found [here](https://www.youtube.com/watch?v=nDCk7Qt6Tj0).

The backend is a Flask app with endpoints for both photo upload as well as analysis using parsed text. In the case of photo upload, images are sent to Google's Vision SDK for text parsing. This backend is hosted on Google Cloud using Google App Engine Standard.

The corresponding iOS app can be found [here](https://github.com/frankfka/LabelWise-iOS)
