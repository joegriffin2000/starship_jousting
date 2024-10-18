from flask import Flask, render_template, url_for
from flask_talisman import Talisman


app = Flask(__name__)
# talisman = Talisman(app) 

# csp = {
#     'default-src': [
#         '\'self\'',
#         'https://code.jquery.com',
#         'https://cdn.jsdelivr.net'
#     ]
# }
# # HTTP Strict Transport Security (HSTS) Header
# hsts = {
#     'max-age': 31536000,
#     'includeSubDomains': True
# }
# # Enforce HTTPS and other headers
# talisman.force_https = True
# talisman.force_file_save = True
# talisman.x_xss_protection = True
# talisman.session_cookie_secure = True
# talisman.session_cookie_samesite = 'Lax'
# talisman.frame_options_allow_from = 'https://www.google.com'
 
# # Add the headers to Talisman
# talisman.content_security_policy = csp
# talisman.strict_transport_security = hsts

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=('../cert.pem', '../key.pem'))
