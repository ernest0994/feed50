DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE feeds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT,
    url TEXT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
)
