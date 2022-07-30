import mysql.connector as connection
mydb = connection.connect(host= "localhost", user = "root", passwd = "ritesh123")
print (mydb)
cursor = mydb.cursor()
#cursor.execute("create database task240722")
#cursor.execute("show databases")

"""1. Create a table for Attribute Dataset and Dress Dataset"""
#q1 = "create table task240722.DressDataset (Dress_ID int(30), Dress_Style varchar(30), Dress_Price varchar(30), Dress_Rating FLOAT(10,5), Dress_Size varchar(10), Dress_Season varchar(30), Dress_NeckLine varchar(30), Dress_SleeveLength varchar(30), Dress_waiseline varchar(30), Dress_Material varchar(30), Dress_FabricType varchar(30), Dress_Decoration varchar(30), Dress_Pattern_Type varchar(30), Dress_Recommendation int(10))"

#q2  = "create table task240722.DressSales (Dress_ID int(30),29_08_2013 int(10),31_08_2013 int(10),09_02_2013 int(10),09_04_2013 int(10),09_06_2013 int(10),09_08_2013 int(10),09_10_2013 int(10),09_12_2013 int(10),14_09_2013 int(10),16_09_2013 int(10),18_09_2013 int(10),20_09_2013 int(10),22_09_2013 int(10),24_09_2013 int(10),26_09_2013 int(10),28_09_2013 int(10),30_09_2013 int(10),10_02_2013 int(10),10_04_2013 int(10),10_06_2013 int(10),10_08_2010 int(10),10_10_2013 int(10),10_12_2013 int(10))"

#cursor.execute(q2)
#print(cursor.fetchall())

#"""Write a SQL query to find out how many unique dress that we have based on dress id"""
#q3 = cursor.execute("select count(distinct(Dress_ID)) from task240722.dressdataset")
#for i in q3:


