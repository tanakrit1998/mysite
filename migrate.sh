rm db.sqlite3
rm -rf wakerfarmer/migrations
python manage.py makemigrations
python manage.py makemigrations wakerfarmer
python manage.py migrate wakerfarmer
python manage.py migrate
