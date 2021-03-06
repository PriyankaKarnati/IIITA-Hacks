from flask import Flask, render_template, request
import socket
import sys
import threading

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/receive", methods=['GET', 'POST'])               #Recieves the IP from where file is to be received
def connect():
	#print("hello")
	if request.method == 'POST':
		#print("hello")
		ip_addr = request.form['ip_addr']
		file_name = request.form['file_name']
		#print(request.form['ip_addr'])
		#Sending request on IP
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_port = 6790
		sock_host = ip_addr
		sock.connect((sock_host, sock_port))
		fp = open(file_name, "wb")
		byte = sock.recv(1024)
		while (byte):
			fp.write(byte)
			byte = sock.recv(1024)
		fp.close()
		sock.close()
		return "Received succesfully"


if __name__ == '__main__':
	if (len(sys.argv) == 1):
		port = 4998
	else:
		port = int(sys.argv[1])
	app.run(debug=True, port=port)


