# echo "SETTING VENV"
# python3.9 -m pip install --upgrade pip
# python3.9 -m pip install virtualenv
# python3.9 -m virtualenv venv
# source venv/bin/activate
# echo "SETTING VENV END"

echo "BUILD START"
python3.9 -m pip install -r requirements.txt
# cd creative_production_management
# python3.9 manage.py collectstatic --noinput
echo "BUILD END"