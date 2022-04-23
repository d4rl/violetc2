from sys import exit
from connection.main import Server
from utils.utils import Print
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.completion import WordCompleter

# Words completation
words_completation = WordCompleter(["interact", "sessions", "run"])

# Create prompt and server instance 
session = PromptSession()
server  = Server("localhost", 1337)

def main():
	with patch_stdout():
		while True:
			prompt = session.prompt("(Violet) > ", completer = words_completation)

			match prompt:
				case "exit":
					Print.good("Closing listener...")
					exit()

				case "sessions":
					server.getAgents()
				
				case "interact":
					print("")

				case "run":
					print("")

if __name__ == '__main__':
	main()