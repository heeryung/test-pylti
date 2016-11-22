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
application = Flask(__name__)
app = application
app.config.from_object('config')


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

@app.route('/', methods = ['GET', 'POST'])
def ipgetter() :
    if requext.method == "POST":



        user_info_lst = {}
        client = geoip2.database.Reader ('/Users/ChoiHeeryung/test-pylti/GeoLite2-City.mmdb')

        # Get user IP
        ip_address = request.remote_addr
        # ip_address = "72.229.28.185"
        # save user IP information
        response = client.city(ip_address)
        country = response.country.name
        specific = response.subdivisions.most_specific.name
        city_name = response.city.name
        post_code = response.postal.code
        latitude = response.location.latitude
        longitude = response.location.longitude

        # user_info_lst.setdefault(user_id, []).append(user_ip, country, specific, city_name, post_code, latitude, longitude)
    
        return ip_adress + " " + laltitude + " " + longitude
        # return render_template('index.html', ip_address=ip_address, latitude=latitude, longitude=longitude)

return latitude, longitude

if __name__ == '__main__':
    app.run()