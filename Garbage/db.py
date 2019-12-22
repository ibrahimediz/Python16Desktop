import sqlite3 as sql
db = sql.connect("chinook\chinook.db")
cur = db.cursor()
def listele(param):
    sorgu = f"""select alb.Title,art.Name,tra.Name from albums as alb
                INNER JOIN artists as art on alb.ArtistId = art.ArtistId
                INNER JOIN tracks as tra on tra.AlbumId = alb.AlbumId
                where art.ArtistId = {param}
                """
    cur.execute(sorgu)
    liste = cur.fetchall()
    for album,artist,parca in liste:
        print("{}-{}-{}".format(album,artist,parca))
# anahtar = 1
# while anahtar:
#     adi = input("Adınız:")
#     soyadi = input("Soyadınız:")
#     cinsiyet = input("Cinsiyet(0/1):")
#     sorgu = """INSERT INTO MUS_BILGI (MUS_ADI,MUS_SOYADI,MUS_CINS)
#     VALUES ('{}','{}',{})""".format(adi,soyadi,cinsiyet)
#     cur.execute(sorgu)
#     db.commit()
listele(input("ARtist Id Gir"))
# else:
#     db.close()

