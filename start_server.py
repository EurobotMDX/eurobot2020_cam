from server import *

print("Starting web server")
app.run(HOST, PORT)
time.sleep(5)
print("Server should be running")