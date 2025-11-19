import time
from datetime import datetime
# print(time.time())
# print(time.time() * 1000)

# print(time.time_ns())

# print(datetime.now())


# print(datetime.now().timestamp())
# ts = datetime.now().timestamp()
# print(ts * 1000000)
# print(int(ts * 1000000))
# rd_ts = int(ts * 1000000)

# rd_ts_m100 = int(rd_ts/100)

# rnd = rd_ts - (rd_ts_m100 * 100)

cnt = 0
while cnt < 6:
	ts = datetime.now().timestamp()
	rd_ts = int(ts * 1000000)
	rd_ts_m100 = int(rd_ts/100)
	rnd = rd_ts - (rd_ts_m100 * 100)
	if rnd > 49:
		number = rnd - 49
	else:
		number = rnd
	print(number)
	cnt += 1
