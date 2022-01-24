from info import *


# Logic Begins ---

rating = 0
for disk_free in range(40, 100) and ram_avail in range(2,5):
    rating = 1
for disk_free in range(100, 200) and ram_avail in range(2,5):
    rating = 2
for disk_free in range(250, disk_total) and ram_avail in range(6, ram_total):
    rating = 3
for disk_free in range(400, disk_total) and ram_avail in range(8, ram_total):
    rating = 4
for disk_free in range(500, disk_total) and ram_avail in range(8, ram_total):
    rating = 5


# print(rating)

# Logic Ends ---
