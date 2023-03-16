import datetime_truncate
from datetime import datetime


print(datetime_truncate.truncate(datetime(2012, 3, 1), 'week'))
print(datetime_truncate.truncate(datetime(2012, 3, 1, hour=12)))
print(datetime_truncate.truncate_week(datetime(2012, 3, 1)))