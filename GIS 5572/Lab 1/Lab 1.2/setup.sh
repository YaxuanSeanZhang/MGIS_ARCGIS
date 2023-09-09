#Install PostGIS and psycopg2 on the VM:
sudo apt-get update
sudo apt-get install postgis
pip install psycopg2-binary
pip install Flask

#This will start the Flask app and allow anyone to retrieve the polygon as GeoJSON by visiting the URL http://your_vm_external_ip:5000/get_polygon in a web browser or by sending a GET request to this URL using a programmatic HTTP client.



#Find out which process is using the port: You can use the lsof command to find out which process is using the port. Run the following command:
#sudo lsof -i :5000
#Stop the process using the port: Once you have the PID of the process using the port, you can use the kill command to stop the process. Run the following command:
#sudo kill PID


#Replace your_vm_external_ip with the external IP address of your VM.
export FLASK_APP=app.py
flask run --host=0.0.0.0
