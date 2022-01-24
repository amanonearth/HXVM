from info import *


# Logic Begins ---

rating = 0

for disk_free in range(90, 200):
    if ram_avail <= 4:
        rating = 1
    if ram_avail <= 6:
        rating = 2
    if ram_avail > 6 and ram_avail <= 8:
        rating = 3
    if ram_avail > 8 and ram_avail <= 12:
        rating = 4
    if ram_avail > 12 and ram_avail <= 16:
        rating = 5

ratingstr = str(rating)

# Logic Ends ---
