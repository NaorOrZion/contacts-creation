# Contacts Creation Website

Author: Naor Or-Zion

## What is the _Contacts Creation Website_?

Greetings!
This tool has been wrriten in order to bulk add contacts by Excel file to any phone whose contacts book is synced with his google account.

## How does it work?

Your google account must be synced with your mobile device and it's contacts in order to use the "Google People" API.
When you open a project for "Google People API", it will automatically pair your synced contacts with the API, by so we can manipulate data by using the API. 

#### Sync device with Google Contacts

To sync your device with google contacts, please visit this link:
https://support.google.com/contacts/answer/2753077

#### How to open a Google People API project?

Open google with the google account you synced your contacts with, than:
1.  Visit: https://console.cloud.google.com/apis/dashboard
2.  Open a new project.
3.  In the left bar: click on "Library".
4.  Search for "google people api" and download the first package.
5.  In the left bar: click on "Credentials".
6.  Click on "Create credentials".
7.  Create an OAuth Id and pick a name for the project.
8.  When requested to fill the "Application type", pick Desktop App and pick a name.
9.  Now download the "Client JSON".
10.  Change it's name to "client_secret.json".
11.  Place this file in the github project in "website/resources".

## The files in this project

```sh
"main.py" - The main project file
"Dockerfile" - a docker file to run the program.
"README.txt" - Project explanation.
"requirments.txt" - Libraries required for the project to work.
"website" - The website folder.
	"init.py" - Init python file to initialize the flask library.
	"google_contacts.py" - The project's brain, here is where the API is managed and the Excel files are read.
	"resources" - The "client_secret.json" file will be stored in this directory.
	"static" - Css, js, images and fonts will be stored here.
	"templates" - HTML pages are wrriten here.
	"uploads" - The excel file a user uploads goes here.

```

## How to use and initialize the website?

#### Prerequities

-   Python 3

#### Installation

1. Clone the github project to a designated folder in your desktop.
```sh
git clone https://github.com/NaorOrZion/contacts-creation.git
```

2. Move to the cloned folder.
```sh
cd contacts-creation
```
    
3. Create a Virtual environment and activate it.
```sh
python -m venv venv
venv\Scripts\activate
```

4. Install the requirements.
```sh
pip install -r requirements.txt
```

5. Run the main file (Notice that it will run on 0.0.0.0:5000).
```sh
python main.py
```
