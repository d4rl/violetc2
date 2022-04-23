import json
import ssl, msgpack, flask
from flask import Flask, request, jsonify
from json import dumps, loads
from sys import exit
from handler.persist_data import Agents
from menus.utils import *

# Create database and flask instance
agentsDatabase = Agents()
app = Flask(__name__)

@app.route("/agent/list")
def agentList():
	agents = agentsDatabase.loadAgents()

	if agents[0] != 0:
		return jsonify(
			sucess=1,
			error="{agents[1]}" 
		)

	return jsonify({
		"sucess" : 0,
		"agents" : f"{agents[1]}"
	})

@app.route("/agent/add", methods = ["POST"])
def addAgent():
	
	listening_ip = request.args.post('listening_ip')
	listening_pt = request.args.post('listening_pt')
	name = request.args.post('name')	
	
	# Check for none params
	if listening_pt == None or listening_pt == None or name == None:	
		jsonify({
			"sucess"  : 1,
			"error"   : "Cannot add an empty agent."
		})

	# Create an instance for errors handling
	agent = agentsDatabase.addAgent(data["listening_ip", "listening_pt"], data["name"])

	# Check if error in database
	if agent[0] != 0:
		Print.bad(f"Can\'t add agent, error: {agent[1]}")
		
		return jsonify({
			"sucess"  : 1,
			"error"   : f"{agent[1]}"
		})

	return jsonify({
		"sucess"  : 0,
	})
	
def main():
	Print.good("Initializing the database")
	
	# Check for database errors
	if agentsDatabase.createAgentsDatabase()[0] != 0:
		Print.bad(f"Cant create the database, error: {agentsDatabase.createAgentsDatabase()[1]}")
		exit()

	# Start flask server
	app.run(debug=True, port=1337)


if __name__ == '__main__':
	main()
