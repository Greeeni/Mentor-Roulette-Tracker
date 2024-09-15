import sqlite3
import json




def db_init():
    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()
    

    cursor.execute("CREATE TABLE IF NOT EXISTS dungeons (id integer, expansionId integer, contentTypeId integer, levelRequired integer, nameEn text, descriptionEn text)")
    conn.commit()
    conn.close()
    


def data_init():
    try:
        conn = sqlite3.connect('testdb.db')
        cursor = conn.cursor()
        with open("dungeons.json") as f:
            data = json.loads(f.read())
        for item in data['results']:
            cursor.execute("INSERT INTO dungeons (id, expansionId, contentTypeId, levelRequired, nameEn, descriptionEn) VALUES (?, ?, ?, ?, ?, ?)", (item["id"], item["expansionId"], item["contentTypeId"], item["levelRequired"], item["nameEn"], item["descriptionEn"]))
            conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"something happened erm... Error inserting {item}: {e}")

def json_test():
    with open("dungeons.json") as f:
        data = json.loads(f.read())
    # for item in data['results']:
    #     print(item["id"])

    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()
    with open("dungeons.json") as f:
        data = json.loads(f.read())
    print((data['results'][0]["id"], data['results'][0]["expansionId"], data['results'][0]["contentTypeId"], data['results'][0]["levelRequired"], data['results'][0]["nameEn"], data['results'][0]["descriptionEn"]))
    cursor.execute("INSERT INTO dungeons (id, expansionId, contentTypeId, levelRequired, nameEn, descriptionEn) VALUES (?, ?, ?, ?, ?, ?)", (data['results'][0]["id"], data['results'][0]["expansionId"], data['results'][0]["contentTypeId"], data['results'][0]["levelRequired"], data['results'][0]["nameEn"], data['results'][0]["descriptionEn"]))
    conn.commit()
    conn.close()
    

    



if __name__ == '__main__':
    print('Begin')
    db_init()
    data_init()
    # json_test()
    conn = sqlite3.connect('testdb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dungeons")
    items = cursor.fetchall()
    for item in items:
        print(item)
    # data = cursor.fetchall()
    # print(len(data))
    conn.close()
    



    # with open("dungeons.json") as f:
    #     data = json.loads(f.read())
    # # print(data['results'][0]['id'])
    # for item in data['results']:
    #     print(item)

    # for items in data:
    #     print(items['id'],items['expansionId'],items['contentTypeId'])