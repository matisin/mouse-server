from bluetooth import *
command_base = "xdotool "

commmand_base = "xdotool mousemove_relative --"
command_click_izq = commmand_base + "click 1"
command_click_middle = commmand_base + "click 2"
command_click_right = commmand_base + "click 3"
import subprocess

#   process = subprocess.Popen(commmand_base.split(), stdout=subprocess.PIPE)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock,address = server_sock.accept()
print( "Accepted connection from ",address)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        coords = " %s" % str(data, "utf-8")
        coords = coords.split('*')
        commmand = commmand_base + coords[0]+ ' '+coords[1]
        subprocess.Popen(commmand.split(), stdout=subprocess.PIPE)

# raise an exception if there was any error
except IOError:
    pass


print("disconnected")

client_sock.close()
server_sock.close()