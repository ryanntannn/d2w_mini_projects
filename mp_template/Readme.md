# Agrifood Emissions Prediction Suite

This repository contains the code for the Agrifood Emissions Prediction Suite (AEPS) project. The project aims to help policymakers run scenrios to predict the emissions of the agrifood sector caused by urbanisation.

## Forms

`PredictorForm` is a form that allows the user to input the parameters for the prediction. The form is rendered in the `predictor.html` template.

## Models

`PredictionInput` is a model that stores the input parameters for the prediction. The model is used to store the input parameters in the database, for future reference.

## Routes

`/predictor` is a route that renders the `predictor.html` template, which contains the `PredictorForm`.

`/history` is a route that renders the `history.html` template, which contains a table of all the input parameters for the predictions.

`/history/<id>` is a route that renders the `history_detauk.html` template, which contains the input parameters for the prediction with the given id, and its corresponding prediction.

## Running the project

1. Initialize the db

```
flask db init
flask db migrate
flask db upgrade
```

2. Run the project

```
flask run
```
