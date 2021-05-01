# Install depenceny
python -m pip install -r requirements.txt


View current cron jobs
``` shell
crontab -l
```
add new current cron jobs
``` shell
crontab -e
```


# Run every day at 00.00
``` shell
0 0 * * * /opt/ADL/python 24-rm-file-pg-ncell.py
```
