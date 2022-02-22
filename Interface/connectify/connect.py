import socket


class UnityConnection():
    def __init__(self):
        self.host, self.port = "127.0.0.1", 25002
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    
    def establish_connection(self):
        self.sock.connect((self.host,self.port))

    

    def receive_data(self):
            
        self.sock.sendall("posString".encode("UTF-8")) #Converting string to Byte, and sending it to C#
        receivedData = self.sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
        
        #print(receivedData)
        return receivedData
            
