DROP DATABASE [IF EXISTS] cb1;
CREATE DATABASE cb1;
CREATE USER cb1user WITH PASSWORD 'cb1';
grant all privileges on databse cb1 to cb1user;