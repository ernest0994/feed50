from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from auth import login_required
from db import get_db

from feedparser import parse

bp = Blueprint('feed', __name__, '/feed')


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        db = get_db()
        errors = []
        url = request.form['feed']
        feed = parse(url)

        if not url:
            errors.append('Please provide a RSS Feed')
        elif len(feed.entries) == 0:
            errors.append('No entries for URL. Did you typed the correct URL?')

        if not errors:
            try:
                db.execute(
                    "INSERT INTO feeds (user_id, url) VALUES (?, ?)",
                    (session['user_id'], url),
                )
                db.commit()
            except db.IntegrityError:
                errors.append(f"Error adding URL.")
            else:
                flash(f"URL has been added successfully!!!")
                return redirect('/')

        for error in errors:
            flash(error, 'error')

    return render_template('add_feed.html')


@bp.route('/fetch')
@login_required
def fetch():
    d = parse('https://moxie.foxnews.com/google-publisher/latest.xml')
    test = d['feed']['title']
    return render_template("index.html")
