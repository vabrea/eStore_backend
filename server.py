##from crypt import methods
import json
##from turtle import home
from flask import Flask, request, abort
from config import db
from flask_cors import CORS

app = Flask ('server')
CORS(app)

@app.route("/")
def root():
    return "welcome to the estore"

@app.route("/home")
def home():
    return "Hello There!"

####################################################
############# API CATALOG ##########################
####################################################

@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    all_products = []

    for prod in cursor:
        prod["_id"] = str(prod ["_id"])
        all_products.append(prod)

    return json.dumps(all_products)

@app.route("/api/catalog", methods=["POST"])
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    if not "title" in product or len(product["title"]) < 5:
        return abort (400, "Title must be at least 5 characters")

    if type(product["title"]) != str:
        return abort (400, "Please enter a valid title")

    if product["price"] <= 0:
       return abort (400, "a price is required")

    if type(product["price"]) != float and type(product["price"]) != int:
        return abort (400, "price must be greater than zero")

    if not "image" in product or len(product["image"]) < 1:
        return abort (400, "Please provide an image file")

    if not "category" in product or len(product["category"]) < 1:
        return abort (400, "Please provide a category")

    print ("saved")
    print (product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)


####################################################
############# API CATALOG ##########################
####################################################

@app.route("/api/couponCodes", methods=["post"])
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    if not "couponCode" in coupon or len(coupon["couponCode"]) < 5:
        return abort(400, "Code is required and must contain at least 5 characters.")


    if not "discount" in coupon:
        return abort(400, "Discount is required")

    if type(coupon["discount"]) != int and type(coupon["discount"]) != float:
        return abort(400, "Please enter a valid number")

    if coupon["discount"] > 35 or coupon["discount"] < 0:
        return abort(400, "Discount must be between 1-35%")


    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)

@app.route("/api/couponCodes")
def get_coupon():
    cursor = db.coupons.find({})
    all_coupons = []

    for coupon in cursor:
        coupon["_id"] = str(coupon["_id"])
        all_coupons.append(coupon)

    return json.dumps(all_coupons)

app.run(debug=True)