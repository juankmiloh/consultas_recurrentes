## Back-end para el manejo de consultas recurrentes

# linux/MacOS
export FLASK_ENV=development

python -m venv venv

source venv/bin/activate

sudo pip install -r requirements.txt

flask run -p 5000

# Windows PowerShell
<!-- $env:FLASK_ENV = "production" -->
$env:FLASK_ENV = "development"

python -m venv .venv

.venv\scripts\activate

pip install -r requirements.txt

flask run -p 5000
