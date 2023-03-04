import psycopg2
import random
import matplotlib.pyplot as plt
import numpy as np

conn = psycopg2.connect(dbname="test_count", user="postgres", password="", host="localhost", port="5432")
cur = conn.cursor()
time_1 = np.array([])
time_2 = np.array([])
time_3 = np.array([])
time_4 = np.array([])
time_5 = np.array([])
time_6 = np.array([])
time_7 = np.array([])
x = np.array([])
cur.execute("CREATE TABLE IF NOT EXISTS test_counts(\n"
            "    id     SERIAL PRIMARY KEY,\n"
            "    fni    INTEGER,\n"
            "    fwi    INTEGER,\n"
            "    fni_nn INTEGER NOT NULL,\n"
            "    fwi_nn INTEGER NOT NULL\n"
            ");")
cur.execute("CREATE INDEX fwi_idx ON test_counts (fwi);")
cur.execute("CREATE INDEX fwi_nn_idx ON test_counts (fwi_nn);")
for i in range(1000):
    for j in range(1000):
        id = i * 1000 + j + 1
        fni_nn = random.randint(1, 1000)
        fwi_nn = random.randint(1, 1000)
        if random.randint(1, 10) >= 8:
            fwi = 'NULL'
        else:
            fwi = random.randint(1, 1000)
        if random.randint(1, 10) >= 8:
            fni = 'NULL'
        else:
            fni = random.randint(1, 1000)
        insert = "INSERT INTO test_counts (id, fni, fwi, fni_nn, fwi_nn) VALUES ({}, {}, {}, {}, {});".format(id, fni,
                                                                                                              fwi,
                                                                                                              fni_nn,
                                                                                                              fwi_nn)
        cur.execute(insert)
        conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(*) FROM test_counts')
    time_1 = np.append(time_1, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(id) FROM test_counts')
    time_2 = np.append(time_2, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(1) FROM test_counts')
    time_3 = np.append(time_3, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(fni) FROM test_counts')
    time_4 = np.append(time_4, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(fwi) FROM test_counts')
    time_5 = np.append(time_5, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(DISTINCT fni) FROM test_counts')
    time_6 = np.append(time_6, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    cur.execute('EXPLAIN ANALYZE SELECT COUNT(DISTINCT fwi) FROM test_counts')
    time_7 = np.append(time_7, float(cur.fetchone()[0].split('actual time=')[1].split('..')[0]))
    conn.commit()
    step = (i + 1) * 1000
    x = np.append(x, step)
plt.plot(x, time_1)
plt.savefig('count.png')
plt.clf()
plt.plot(x, time_2)
plt.savefig('count1.png')
plt.clf()
plt.plot(x, time_3)
plt.savefig('count_id.png')
plt.clf()
plt.plot(x, time_4)
plt.savefig('count_fni.png')
plt.clf()
plt.plot(x, time_5)
plt.savefig('count_fwi.png')
plt.clf()
plt.plot(x, time_6)
plt.savefig('count_d_fni.png')
plt.clf()
plt.plot(x, time_7)
plt.savefig('count_d_fwi.png')
plt.clf()