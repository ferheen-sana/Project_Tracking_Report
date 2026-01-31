# Project Tracker - Updated Version (v2)

This version adds:
- Aircraft dropdown per project row.
- On-change endpoint that auto-updates No.Meetings, IOM/TM, No.Sorties according to aircraft selected.
- Larger Brief textarea on add/edit form.
- Bootstrap header/footer with ADA logo.

Instructions:
1. Unzip and cd into the folder.
2. Create & activate virtualenv.
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Create superuser (optional):
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver
7. Open http://127.0.0.1:8000/

