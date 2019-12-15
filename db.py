import sqlite3 as sql
db = sql.connect("chinook\chinook.db")
cur = db.cursor()
def listele():
    sorgu = """SELECT MUS_ID,MUS_ADI,MUS_SOYADI FROM MUS_BILGI"""
    cur.execute(sorgu)
    liste = cur.fetchall()
    for id,adi,soyadi in liste:
        print("{}-{}-{}".format(id,adi,soyadi))
anahtar = 1
while anahtar:
    adi = input("Adınız:")
    soyadi = input("Soyadınız:")
    cinsiyet = input("Cinsiyet(0/1):")
    sorgu = """INSERT INTO MUS_BILGI (MUS_ADI,MUS_SOYADI,MUS_CINS)
    VALUES ('{}','{}',{})""".format(adi,soyadi,cinsiyet)
    cur.execute(sorgu)
    db.commit()
    listele()
else:
    db.close()

