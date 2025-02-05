#******************** MY SQL CODE ****************************************************************


# create database employee;
# use employee;
# create table emp(name char(20), gender char(10), email varchar(20), designation char(20));
# #-- Create Operation
# insert into emp values ("Dan Morris", "Male", "morris.dan@gmail.com", "Manager");
# insert into emp values ("Jude Cruise", "Male", "cruisej@gmail.com", "Developer");
# insert into emp values ("Sam", "Female", "sam@gmail.com", "HR");
# insert into emp values ("Smriti", "Female", "smriti128@gmail.com", "Data Scientist");
# #-- Read Operation
# select * from emp;
# create table empDetails as select distinct * from emp;
# select * from empDetails;
# #-- Update Operation
# ALTER TABLE empDetails ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;
# update empDetails set designation="Data Analyst" where id=1;
# #-- Delete Operation
# delete from empDetails where id=2;