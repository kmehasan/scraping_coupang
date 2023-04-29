#!/usr/bin/python
import MySQLdb
class MyDB:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                            user="root",         # your username
                            passwd="",  # your password
                            db="test")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        self.cur = self.db.cursor()

    def getUrl(self,name):
        # Use all the SQL you like
        name = name.split('.')[0]
        q = f"SELECT guid FROM `wp_posts` WHERE `post_title` LIKE \"%{name}%\""
        # print(q)
        self.cur.execute(q)
        res = self.cur.fetchone()
        print(res)
        if(res == None):
            return ""
        return res[0]
        
    def getUrlList(self,list_data):
        if len(list_data) == 0:
            return []
        list_data = [i.split('.')[0] for i in list_data]
        q = f"SELECT guid FROM `wp_posts` WHERE `post_title` LIKE \"%{list_data[0]}%\""
        for i in list_data[1:]:
            q += f" OR `post_title` LIKE \"%{i}%\""
        # print(q)
        self.cur.execute(q)
        res = self.cur.fetchall()
        return res    
        
    def close(self):
        self.db.close()
if __name__ == "__main__":
    mydb = MyDB()
    print(mydb.getUrl("jhgkjhsblrgnjldnrg"))
    mydb.close()