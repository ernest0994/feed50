from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from auth import login_required
from db import get_db

from feedparser import parse

import ast

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
            title = feed['feed'].title
            try:
                db.execute(
                    "INSERT INTO feeds (user_id, title, url) VALUES (?, ?, ?)",
                    (session['user_id'], title, url),
                )
                db.commit()
            except db.IntegrityError:
                errors.append(f"Feed {title} is already registered.")
            else:
                flash(f"{title} Feed has been added successfully!!!")
                return redirect('/')

        for error in errors:
            flash(error, 'error')

    return render_template('add_feed.html')


@bp.route('/view')
@login_required
def view():
    db = get_db()
    rows = db.execute(
        'SELECT id, title, url FROM feeds WHERE user_id = ?', (session['user_id'],)
    )

    if not rows:
        return render_template("feeds.html")

    feeds = []

    for row in rows:
        feed = {'id': row['id'],
                'title': row['title'],
                'url': row['url']
                }
        feeds.append(feed)

    return render_template("feeds.html", feeds=feeds)


@bp.route('/delete')
@login_required
def delete():
    db = get_db()
    errors = []
    feed = request.args.get('feed')

    if not feed:
        errors.append('Not a valid selection')

    res = ast.literal_eval(feed)

    db.execute('DELETE FROM feeds WHERE id = ?', (res['id'],))
    db.commit()

    for error in errors:
        flash(error, 'error')

    flash('Feed deleted successfully')
    return redirect(url_for('feed.view'))
