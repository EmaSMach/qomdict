# import sqlite3

# from_conn = sqlite3.connect("words.db")
# to_conn = sqlite3.connect("db.sqlite3")

# from_cur = from_conn.cursor()
# to_cur = to_conn.cursor()

# print(from_conn.execute("select name from sqlite_master where type='table';").fetchall())
# words > 'dictionary_words
# print(to_conn.execute("select name from sqlite_master where type='table';").fetchall())
# from_words = from_cur.execute("select id, qom, dfs, syn, var, see from words").fetchall()
# from_words = [list(l).insert(0, None) for l in from_words]
# to_cur.executemany("insert into dictionary_word values (?, ?, ?, ?, ?, ?)", from_words)
# to_conn.commit()
# to_cur.close()
# to_conn.close()
# from_cur.close()
# from_conn.close()
# print(from_words, len(from_words))
