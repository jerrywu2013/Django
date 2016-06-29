##
```
( echo 'a,b,c' ; echo '1,2,3' ) > somedata.csv
```
##
```
sqlite3 database.sqlite3
.mode csv
.import somedata.csv sometable
```
##
```
SELECT * FROM sometable;
```
