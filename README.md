# MyFridgeAPI

MyFridge is a simple rest API implemented with Django REST Framework and MongoDB thought for those people who never know what to cook, like me :) 


## Users are able to: 

* Sign up
* Sign in
* Access and update their user detail
* Complete their profile
* Upload their fridge ingredients
* Create, read, update and delete ingredients
* Create, read, update and delete recipes
* And, the main thing, is that **they can consult the recipes that they can make with their fridge's ingredients.**


## Running Locally

1. Must have Python 3 & [MongoDB (Community Server)][1] installed and running. If you don´t here is the [MongoDB Install Guide][2], to install mongo locally.
1. Clone this repository and access it through the command line.
1. Create a virtual environment: `python -m venv venv`
1. Go into your virtual environment: `source venv/bin/activate` (or `venv/Scripts/activate` in Windows)
1. Install dependencies: `pip install -r requirements.txt`
1. Setup Database (in the mongo shell)
    1. Create the database: `use my-fridge;`
    1. Create DB user with privilages on all dbs:
			db.createUser(
			{	user: "my-fridge-admin",
			pwd: "password",
			roles:[{role: "userAdminAnyDatabase" , db:"admin"}]})

1. Run migrations: `python manage.py migrate`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`
1. Run the app: `python manage.py runserver`
1. You can access the admin interface at `localhost:8000/admin`


## Schema

* User
  * email
  * username
  * is_active
  * is_admin
  * password

* Profile
  * user (OneToOne)
  * picture
  * first_name
  * last_name
  * biography

* Fridge
  * owner (User OneToOne)
  * ingredients (ManyToMany)
  
* Ingredient
  * name
  * slug_name
  * created_by (User FoeringKey)
  * picture
  * description
  * is_veggie
  * is_vegan
  
* Recipe
  * name
  * slug_name
  * created_by (User FoeringKey)
  * picture
  * description
  * instructions
  * ingredients (ManyToMany)
  * is_veggie
  * is_vegan
  

## API Endpoints

**/users/signup/**

* post

**/users/login/**

* post

**/users/:username/**

* get (User Detail is also the way to check user's profile and fridge content)
* put
* patch

**/users/:username/profile/**

* put
* patch

**/users/:username/fridge/**

* patch

*example get User Detail response:*

```json
{
    "id": 47,
    "email": "nsterro@gmail.com",
    "username": "nsterroni",
    "is_admin": false,
    "is_verified": false,
    "is_active": true,
    "profile": {
        "picture": null,
        "first_name": "Nicolas",
        "last_name": "Terroni",
        "biography": "Thanks for visiting!"
    },
    "fridge": {
        "ingredients": [
            41,
            40
        ]
    }
}
```

**/ingredients/**

* post
* get

**/ingredients/:slug_name/**

* get
* put
* patch
* delete

**/recipes/**

* post
* get

**/recipes/:slug_name/**

* get
* put
* patch
* delete

**recipes/possible_recipes/**

* get (List recipes that contain user's fridge ingredients.)

**recipes/my_recipes/**

* get (List recipes created by the requesting user.)


[1]: https://www.mongodb.com/try/download/community "MongoDB"
[2]: https://docs.mongodb.com/guides/server/install/ "MongoDB Install Guide"