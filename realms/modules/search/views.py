from flask import abort, g, render_template, request, redirect, Blueprint, flash, url_for, current_app
from realms import search as search_engine
from flask.ext.login import login_required, current_user

blueprint = Blueprint('search', __name__)

@blueprint.route('/_search')
def search():
    if current_app.config.get('PRIVATE_WIKI') and current_user.is_anonymous():
        return current_app.login_manager.unauthorized()

    results = search_engine.wiki(request.args.get('q'))
    return render_template('search/search.html', results=results)

