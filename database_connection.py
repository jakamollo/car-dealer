#!python

# import postgresql database module
import psycopg2

# Establish database connection
conn = psycopg2.connect(database="car_dealer", user="postgres", password="ogolla", host="localhost", port="5432")
cur = conn.cursor()