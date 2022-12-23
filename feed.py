from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from db import get_db

from feedparser import parse

bp = Blueprint('feed', __name__, '/feed')


@bp.route('/fetch')
@login_required
def fetch():
    d = parse('https://moxie.foxnews.com/google-publisher/latest.xml')
    test = d['feed']['title']
    return render_template("index.html")
