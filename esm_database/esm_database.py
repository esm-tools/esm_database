#!/usr/bin/env python3

import os, sys
import sqlite3
import datetime

class sqlite3_database:
    def __init__(self, filename, tablename, sample):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.tablename = tablename
        self.sample = sample

        if not os.path.isfile(filename):
            self.create_new_table()
        elif not self.table_exists():
            self.create_new_table()


    def create_new_table(self):
        print (creating_new_message)
        self.cursor.execute("CREATE TABLE " + self.tablename + self.layout_nocase())

    def table_exists(self):
        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self.tablename + "'") 
        if self.cursor.fetchone()[0] == 0:
            return False
        return True

    def display_whole_database(self):
        sql = "SELECT * FROM " + self.tablename
        self.cursor.execute(sql)
        print (self.cursor.fetchall())

    def submit_query(self, query):
        rows = self.cursor.execute(query)
        if "INSERT" in query:
            self.conn.commit()
        return rows

    def all_info(self):
        rows = self.cursor.execute("SELECT * FROM " + self.tablename)
        return rows

    def layout(self):
        sep = ""
        layout = "("
        for entry in list(self.sample.types):
            layout += sep + entry + " " + self.sample.types[entry]
            sep = ", "
        layout += ")"
        return layout

    def layout_nocase(self):
        sep = ""
        layout = "("
        for entry in list(self.sample.types):
            layout += sep + entry + " " + self.sample.types[entry] + " COLLATE NOCASE"
            sep = ", "
        layout += ")"
        return layout

    def values(self, entry):
        sep = ""
        values = " VALUES ('"
        for listentry in list(entry.values):
            values = values + sep + entry.values[listentry]
            sep = "', '"
        values = values + "')"
        return values

    def new_entry(self, entry):
        query = "INSERT INTO " + self.tablename + self.values(entry)
        return query

    def last_entry(self, searchfor, searchwhere, searchlike):
        query = self.search_query(searchfor, searchwhere, searchlike)
        entries = self.submit_query(query)
        if type(entries) == list:
            return entries[-1]
        return ""

    def search_query(self, searchfor, searchwhere, searchlike):
        query = "SELECT " + searchfor + " FROM " +  self.tablename + " WHERE " + searchwhere + " LIKE '%" + searchlike + "%'"
        return query

    def timestamp(self):
        this_datetime = datetime.datetime.now()
        date = this_datetime.strftime("%Y-%m-%d")
        time = this_datetime.strftime("%H:%M")
        return date, time





##########################################################################################



#class database(sqlite3_database):
#    pass



