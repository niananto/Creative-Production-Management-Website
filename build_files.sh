echo "SETTING VENV"
python -m pip install --upgrade pip
python -m pip install virtualenv
python -m virtualenv venv
source venv/bin/activate
echo "SETTING VENV END"

echo "BUILD START"
python -m pip install -r requirements.txt
cd creative_production_management
python manage.py collectstatic --noinput
echo "BUILD END"