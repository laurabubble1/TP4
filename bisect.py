import os

# Récupérer le hash du commit mauvais (HEAD)
badhash = os.popen("git rev-parse HEAD").read().strip()

goodhash = os.popen("git rev-list --max-parents=0 HEAD").read().strip()
os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")