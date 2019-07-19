import sqlite3

app = Flask(__name__)
def create_table():
    print("Creating table ...")
    com = sqlite3.connect('example.db')
    c = com.cursor()
    c.execute("CREATE TABLE IF NOT EXITS todos(item text);")
    com.commit()

def get_todos_from_db():
    com = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos VALUES('" + item +"')")
    com.commit()
    
    
    
    
if __name__ == '__main__':