from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("my_pets")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", pet_data = { 'pets_list': pets })

@app.route("/add_pet", methods=["POST"])
def add_pet_to_db():
    print(request.form)
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
    
    query = "INSERT INTO pets (name, type) VALUES (%(name)s, %(type)s);"
    data = {
        "name": request.form["pname"],
        "type": request.form["ptype"]
    }
    mysql = connectToMySQL("my_pets")
    mysql.query_db(query, data)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)