import os

# Récupérer le hash du commit mauvais (HEAD)
badhash = os.popen("git rev-parse HEAD").read().strip()
# Récupérer le hash du commit bon (HEAD~10)
goodhash = os.popen("git rev-parse HEAD~10").read().strip()
os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")