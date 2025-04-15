cd CM4025_CW
sudo python3 -m venv ./
source ./bin/activate
sudo chown -R $USER ~/CM4025_CW
pip install -r requirements.txt
python manage.py runserver