<h2 align="center">Violet C2</h2>
<p>This is an c2 made with friends. Currently it's in some basic c2 server but we will implement more stuffs like metasploit support and more.</p>

# Explaining
<p>The purpose of this project is an basic c2 thats bypass AV's like windows default because PowerShell-Empire bypass isn't good.</p>
<p>So i decided to create my own c2 i'm my prefered language. First the C2 Server starts an HTTP server to receive c2 connections, and then starts websocket server for contact the agents, when agents hit's /agent/add the server add it to a database to store it and check the connection. The user can send commands, run modules and etc.</p>

# Features
* WebSocket Support 
* Easyly extension implementation

# Todo:
- [ ] Encrypt connection with ssl
- [ ] Add agent
- [ ] Add metasploit support
- [ ] Add Cobalt Strike support
