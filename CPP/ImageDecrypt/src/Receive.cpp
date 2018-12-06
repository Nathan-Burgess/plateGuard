/*******************************************************************************
* Function definitions for Receive class
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
#include "Receive.h"
#include "error.h"
using namespace std;
using namespace cv;

Receive::Receive()
{
  // Server port number
  port = 1234;
  // Set up socket
  conn_fd = socket(AF_INET, SOCK_DGRAM, 0);

  if(conn_fd < 0)
  {
    error("Error opening sockets", 1);
  }

  memset((char*) &servaddr, 0, sizeof(servaddr));

  servaddr.sin_family = AF_INET;
  servaddr.sin_port = htons(port);
  servaddr.sin_addr.s_addr = htonl(INADDR_ANY);

  if(bind(conn_fd, (struct sockaddr*) &servaddr, sizeof(servaddr)) == -1)
  {
    error("Unale to bind socket", 1);
  }
}

// Receive::~Receive()
// {
//   close(conn_fd);
// }

void Receive::receiveMessage()
{
  cout << "Waiting for data..." << endl;
  fflush(stdout);
  if((recvlen = recvfrom(conn_fd, &message, sizeof(Mat), 0, (struct sockaddr*) &cliaddr, &clilen)) == -1)
  {
    error("Unable to receive", 1);
  }

  cout << message << endl;
}
