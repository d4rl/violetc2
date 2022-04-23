"""
listening_ip = Agent listening ip for receive commands/tasks
listening_pt = Agent listening port for receive commands/tasks

session_id 	 = Agent id for identify
name 		 = Agent name 
"""

import sqlite3
from websocket import create_connection

def check(ip:str, port:int):
    with create_connection(f"ws://{ip}:{pt}") as ws -> tuple:
    	try:
	        # Send check for check if is an valid websocket server
	        ws.send("Check")

	        # Get output and check
	        resp = ws.recv()

	        if "ok" in resp:
	        	ws.close()
	        	
	        	return (0, "sucess")

	        else:
	        	ws.close()

	        	return (1, "cant connect to agent")
	    
	    except Exception as err:
	    	return (1, err)

class Agents:

	def __init__(self):
		self.agents_conn = sqlite3.connect('data/agents.db', check_same_thread=False)
		self.agents_cursor = self.agents_conn.cursor()	


	# Basic stuffs
	def createAgentsDatabase(self) -> tuple:
		"""
			Create agents databse
			Returns 0 if sucess
		"""

		try:
			self.agents_cursor.execute("""
				CREATE TABLE IF NOT EXISTS agents (
					session_id INTEGER PRIMARY KEY AUTOINCREMENT, 
					name text, 
					listening_ip text,
					listening_pt text)
			""")
			# Return sucess
			return (0, "sucess")

		except Exception as err:
			# Return error 
			return (1, err)

	def loadAgents(self) -> dict:
		"""
			Returns the agent list
			Returns 0 if sucess
		"""

		try:
			agent_list = []	

			for agent in self.agents_cursor.execute("SELECT * FROM agents ORDER BY session_id"):
				agent_list.append(agent)
			
			# Returns sucess
			return (0, agent_list)

		except Exception as err:
			# Returns error
			return (1, err)


	# Data (Inserting)
	def addAgent(self, listening_ip:str, listening_pt:str, name:str = None) -> tuple:
		"""
			Add an agent to database
			Returns 0 if sucess
		"""
		try:
			agent_check = check(listening_ip, listening_pt)

			if agent_check != 0:
				return (1, agent_check[1])

			else:
				self.agents_cursor.execute("""
					INSERT INTO agents (name, listening_ip, listening_pt) VALUES (?, ?, ?)
				""", name, listening_ip, listening_pt)
				
				# Return sucess 
				return (0, "sucess")
		
		except Exception as err:
			# Return error 	
			return (1, err)

	# Data (Updating)

	# Data (Deleting)
