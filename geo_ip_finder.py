import os
from flask import Flask, render_template, jsonify, request 
from pylti.flask import lti
import geoip2.webservice
import geoip2.database
import pygeoip
from flask_mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix
import sys



VERSION = '0.0.1'


# EB looks for an 'app' callable by default.

db = MongoEngine ()
application = Flask(__name__)
app = application
app.config.from_object('config')
db.init_app(app)


# class User (db.Document) :
#     email = db.String()




def error(exception):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')





# @app.route('/', methods = ['GET', 'POST'])
# @lti(request='any', error=error, app=app)
# def redirect_to(lti=lti) :
#
#     return render_template('index.html', lti=lti)
#
#
# # def db_store():
# #     online_user = mongo.db.users()

@app.route('/')
def ipgetter() :

    user_info_lst = {}

    client = geoip2.database.Reader ('/Users/ChoiHeeryung/test-pylti/GeoLite2-City.mmdb')
    # gi = pygeoip.GeoIP ('GeoIP.dat')
    # geo_data = gi.record_by_addr (request.remote_addr)

    # Get user IP
    user_ip = request.remote_addr

    # save user IP information
    response = client.city(user_ip)
    user_ip = response.ip_address
    country = response.country.name
    specific = response.subdivisions.most_specific.name
    city_name = response.response.city.name
    post_code = response.postal.code
    latitude = response.location.latitude
    longitude = response.location.longitude

    user_info_lst.setdefault(user_id, []).append(user_ip, country, specific, city_name, post_code, latitude, longitude)

    return jsonify (geo_data)

x = 12+6
print x


if __name__ == '__main__':
    app.run()