# Quality-Appraisal

#### The application is a review platform for startup accelerators, 7/12/2020.
#### By Felista Kiriinya

## Description

Quality-Appraisal is a review platform for startup accelerators in Kenya. By gathering feedback shared by startups, Quality informs 
the decisions of others and helps ensure that future startups partner up with a company that best suits their needs. In addition 
to inviting written reviews, Quality-Appraisal incorporates a five-star rating system, which can be used to rate companies with regards to 
mentorship, hiring, community, fundraising, and corporate development.

Each startup accelerator has its own company page, containing a company bio and other necessary information. This page also provides 
access to the latest reviews for the company, while displaying the company's average score in each of the five aforementioned 
categories, as well as its overall score based on all user feedback provided. In addition to posting reviews, users can update and 
remove reviews. The creation of company accounts, and any subsequent updates to said accounts, are limited to the administrator.

## Features

- Login/registration: By registering and logging into a secure account, users are able to provide feedback on listed startup accelerators.
- CRUD functionality: Registered users are able to create, read, update and delete reviews. The same functionality is available to site 
administrators with regards to company accounts.
- Review form with rating system: Before submitting a review, users are asked to rate the company out of five with regards to 
mentorship, hiring, community, fundraising, and corporate development.
- Dynamic five-star display: The ratings provided are then used to calculate the overall rating accompanying the individual review. They are 
also added to the database to contribute to the company's average score in each category, and its average score overall. These scores are 
displayed on the startup accelerator's company page via a dynamic five-star display, written using inline python.

## Technologies used

- Python: The underlying code, including views, models, forms, routes, and the majority of functionality, was written using Python.
- Django: This project was written using the Django web framework. Django authentication was used to create a secure registration and 
login feature.
- Bootstrap: The Bootstrap front-end web framework was used to help structure the website.
- Javascript/jQuery: Javascript and jQuery logic have been used to develop certain pieces of dynamic functionality, specifically the 
customisation of radio buttons in the review form to create a responsive five-star rating system. 
- HTML: HTML was used to help structure the website.
- CSS: The appearance of the website was enhanced using CSS. The stylesheet is available in the static folder.
- SQL: All data inputted into the website by administrators and users is saved to a Postgresql database.

## Live link
Visit the application on .

## Figma Link
This is the [figma]() link to my design.

## Support and contact details

Should you be unable to access the website, have any recommendations and/or questions, feel free to email me:[felkiriinya@gmail.com](mailto:felkiriinya@gmail.com)

## [License](https://github.com/felkiriinya/Quality-Appraisal/blob/main/LICENSE)

Copyright (c) 2020 [Felista Kiriinya](https://github.com/felkiriinya)
