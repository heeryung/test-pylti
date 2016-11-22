from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
from IPython.display import display, Javascript
import os
from flask import Flask, render_template, jsonify, request 
from pylti.flask import lti
import geoip2.webservice
import geoip2.database
import pygeoip
from flask_mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix
import sys









javascript = """
<script type="text/Javascript">

function trigger_trigger () {
    console.log("booted")

    var callbacks = cell.get_callbacks()
    kernel.execute(ipgetter(), callbacks);
    console.log("executed")
}


</script>
"""










class testHandler (IPythonHandler):
    # 일단 플라스크를 불러냄 (플라스크, 그러니까 그 함수들. 다 들어있는 거)
    # 자바스크립트가 여기서 들어가는데, Jupyter.notebook.kernel.execute("", {"output": callback}) 이게 들어가고
    # 이게 
    # EB looks for an 'app' callable by default.
    application = Flask(__name__)
    app = application
    app.config.from_object('config')

    @app.route('/', methods = ['GET', 'POST'])
    def ipgetter() :

        user_info_lst = {}
        client = geoip2.database.Reader ('/Users/ChoiHeeryung/test-pylti/GeoLite2-City.mmdb')

        # Get user IP
        # ip_address = request.remote_addr
        ip_address = "72.229.28.185"
        # save user IP information
        response = client.city(ip_address)
        country = response.country.name
        specific = response.subdivisions.most_specific.name
        city_name = response.city.name
        post_code = response.postal.code
        latitude = response.location.latitude
        longitude = response.location.longitude

        # user_info_lst.setdefault(user_id, []).append(user_ip, country, specific, city_name, post_code, latitude, longitude)    
    
        return render_template('index.html', ip_address=ip_address, latitude=latitude, longitude=longitude)

    return latitude, longitude

    if __name__ == '__main__':
        app.run()
    
    
    
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="my_exten",
        # _also_ in the `nbextension/` namespace
        require="my_exten/index")]
        
    
def load_jupyter_server_extension(nb_app):
    nbapp.log.info("my module enabled!")