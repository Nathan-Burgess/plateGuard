/*******************************************************************************
* Desc: Establish connection to server and transmit packets using UDP
*******************************************************************************/

#include <cstdlib>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "Transmit.h"
#include "error.h"
using namespace std;

Transmit::Transmit()
{
  // Server port number
  port = 6676;
  // Set up socket
  conn_fd = socket(AF_INET, SOCK_STREAM, 0);

  serv_len = sizeof(servaddr);

  // Check if connection socket was successful
  if(conn_fd < 0)
  {
    error("Error opening socket", 1);
  }

  // Get address from hostname

  // Set up server connection
  memset((char*)&servaddr, 0, sizeof(servaddr));
  servaddr.sin_family = AF_INET;
  servaddr.sin_port = htons(port);
  if(inet_aton("127.0.0.1", &servaddr.sin_addr) == 0)
  {
    fprintf(stderr, "inet_aton() failed\n");
    exit(1);
  }
}

Transmit::~Transmit()
{
  shutdown(conn_fd, SHUT_RDWR);
  close(conn_fd);
}

void Transmit::sendFrame(Mat frame)
{
  char message[5];
  // Encode message before sending
  int frameSize = frame.total() * frame.elemSize();

  // cout << frame << endl;

  connect(conn_fd, (struct sockaddr *) &servaddr, sizeof(servaddr));

  if(send(conn_fd, frame.data, frameSize, 0) < 0)
  {
    error("Error: Unable to send", 1);
  }

  cout << message << endl;
}
