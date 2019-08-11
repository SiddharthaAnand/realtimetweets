from flask import Flask
from flask import request, jsonify, render_template

app = Flask(__name__)

###########################################################
#         Request Handlers Section                        #
#                                                         #
###########################################################
@app.route('/tweets/')
def handle_request():
    # Sanitize request

    # Return jsonified response
    response_content = request.args.get('source')
    return response_content



############################################################
#          Error Handlers Section                          #
#                                                          #
############################################################
@app.errorhandler(400)
def page_not_found(error):
    return render_template('page_not_found.html'), 400

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('internal_server_error.html'), 500


if __name__ == '__main__':
    app.run()