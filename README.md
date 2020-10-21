# Library for importing kaggle data into colab and run vscode on the folder
_This is already implemented by ML Genius Abhishek Thakur, just a litte bit refinement and I have added methods for importing kaggle data straight into your_ _Drive folder and the vscode will open in your kaggle folder_

## Installation:
_pip install kagcolabserver_

# Basics optional params for the Code:

## Primary params

* -- port : for hosting the code server locally and tunnel using the ngrok
* -- drive : for mouting the drive
* -- folder_tree : Folder structure which will be created in the drive Ex: titanic/ or kaggle/titanic etc...
* -- kaggle : for working with kaggle user api and data api

## Secondary params

**Note :**  _On clicking API key in your profile, a file named kaggle.json with username and api key will be downloaded, kindly use them for below params_

* -- username : Your Kaggle username
* -- kag_api_key : API key found in your profile
* -- kag_data_api : On each kaggle competition, a data api will be given should pass that one!

 
# How to Use the library?

## For just starting the code server from google colab

```
* from kagcolabserver import kagColabServer
* kagColabServer(port=7000, drive=True, kaggle=False)
```

## For starting vscode in particular foler

```
* from kagcolabserver import kagColabServer
* kagColabServer(port=7000, drive=True, kaggle=False, folder_tree="kaggle")
```

## For importing Kaggle as well as starting the code-server in the folder location

```
* from kagcolabserver import kagColabServe
* kagColabServer(port=4000, drive=True)
* kolab = kagColabServer(port=4000,drive=True, kaggle=True)
* kolab.import_kaggle_data(username='XXXX', kag_api_key='XXXXX', kag_data_api='kaggle competitions download -c titanic', folder_tree='titanic/')
```