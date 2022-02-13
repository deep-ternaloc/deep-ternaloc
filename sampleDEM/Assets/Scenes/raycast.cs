using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
public class raycast : MonoBehaviour
{


    public float height=3000;
    RaycastHit hit;

    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25002;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    Vector3 receivedPos = Vector3.zero;
    public string height_ground;
    public string xposition_python;
    public string yposition_python;
    bool running;

    // Start is called before the first frame update


    // Update is called once per frame
    void Update()
    {
        Ray ray = new Ray(transform.position,-Vector3.up);

        Debug.DrawRay(transform.position, Vector3.down*height, Color.red);
    
    if (Physics.Raycast(ray, out hit))
        
        if (hit.collider.tag == "ground")
        {
            float height_above_ground = hit.distance -2.5f;
            float xposition = transform.position.x;
            float yposition = transform.position.z;
            
            height_ground = height_above_ground.ToString();
            xposition_python = xposition.ToString();
            yposition_python = yposition.ToString();   
            Debug.Log("height above ground: " + height_above_ground);
        }

    
    }

    private void Start()
    {
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();
    }


    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();

        client = listener.AcceptTcpClient();

        running = true;
        while (running)
        {
            SendAndReceiveData();
        }
        listener.Stop();
    }


    void SendAndReceiveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //---receiving Data from the Host----
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string

        if (dataReceived != null)
        {
            //---Using received data---
            //receivedPos = StringToVector3(dataReceived); //<-- assigning receivedPos value from Python
            print("received pos data, and moved the Cube!");

            //---Sending Data to Host----
            byte[] myWriteBuffer = Encoding.ASCII.GetBytes(xposition_python+","+yposition_python); //Converting string to byte data
            nwStream.Write(myWriteBuffer, 0, myWriteBuffer.Length); //Sending the data in Bytes to Python
        }
    }
}
