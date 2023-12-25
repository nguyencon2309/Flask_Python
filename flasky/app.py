from flask import Flask,render_template,request,url_for,redirect,flash

from connect_mongodb import col_employee,col_dep


from bson import ObjectId

# import os


app = Flask(__name__)
app.secret_key = "chuoi-bi-mat"






@app.route("/")
def index():
    list_employee = list(col_employee.find())
    list_dep = list(col_dep.find())
    return render_template("index.html",Employees=list_employee, deps=list_dep)

@app.route("/insert",methods=["GET", "POST"])
def insert():
    id= request.form['id']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    department = request.form['emp_department']

    col_employee.insert_one({'id':id,'name':name,'phone':phone,'email':email,'department':department})

    flash("add new employee successfully")

    return redirect(url_for('index')) 


@app.route("/delete/<_id>")
def delete(_id):
    col_employee.delete_one({"_id":ObjectId(_id)})
    flash("delete employee successfully")
    return redirect(url_for('index')) 
    

@app.route("/update/<_id>",methods=["GET", "POST"]) 
def update(_id):
    if request.method=='POST':
        depart = request.form['department_emp']
        col_employee.update_one(
            {"_id":ObjectId(_id)},
            {
                "$set":{
                    
                    "name":request.form['name'],
                    "phone":request.form['phone'],
                    "email":request.form['email'],
                    "department":depart
                    
                }
            }
        )
    flash("update employee successfully")
    return redirect(url_for('index')) 


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/base")
def base():
    return render_template('base.html')
app.config['DEBUG'] = True
if __name__ == "__main__":
    app.run(debug=True)