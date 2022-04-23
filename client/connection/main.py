import msgpack
import ssl
from requests import get, post

class Server:
	def __init__(self, host:str = "localhost", port:int = 8443):
		self.host = host
		self.port = port
	
	def getAgents(self):
		try:
			with get(f"http://{self.host}:{self.port}/agent/list") as resp:
				self.data = resp.content
				print(self.data)
		
		except Exception as err:
			print(f"Coun\'t get agents, error: {err}")