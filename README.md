# Top-5-Favorites


Using the steps we learned today, create a basic Flask web application that lists your top 5 favorite artists, sports figures, historical figues, etc. (It can be 5 favorite anything, have some fun with it!)
Steps:
-- Setup:
- Create project folder
- Create virtual environment: 
      - Windows: python -m venv {name_of_environment}
      - Mac/Linux: python3 -m venv {name_of_environment}
- Activate virtual environment: 
     - Windows: {name_of_environment}\Scripts\activate
     - Mac/Linux: source {name_of_environment}/bin/activate
- Install python module (make sure your venv is activated): pip install flask


-- App Features
- Create instance of Flask class
- Create two routes using @app.route 

(feel free to use Bootstrap for styling and components)
    - A Home/index route - Can be generic, nothing fancy but feel free to make it look however you'd like
    - A "Favorite 5" route - Pass through your list of five favorites
