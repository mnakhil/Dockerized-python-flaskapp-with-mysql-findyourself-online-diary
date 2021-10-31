create database diarydb;
use diarydb;
create table User(id int unsigned auto_increment, email varchar(150) unique, firstName char(150), 
lastName char(150),password varchar(150), secQuestion varchar(30),answer varchar(30), primary key(id));
create table diary(id int unsigned auto_increment, data varchar(10000), date datetime,name char(150),privacy varchar(10), user_id int unsigned,
FOREIGN KEY (user_id) REFERENCES User(id),primary key(id));