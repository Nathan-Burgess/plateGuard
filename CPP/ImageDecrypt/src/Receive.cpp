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
#include "Receive.h"
#include "error.h"
using namespace std;

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

  if(bind(conn_fd, (struct sockaddr*) &servaddr, sizeof(servaddr)) == -1)
  {
    error("Unale to bind socket", 1);
  }
}

Receive::~Receive()
{
  close(conn_fd);
}

void Receive::receiveMessage()
{
  cout << "Waiting for data..." << endl;
  fflush(stdout);
  if((recvlen = recvfrom(conn_fd, message, sizeof(message), 0, (struct sockaddr*) &cliaddr, &clilen)) == -1)
  {
    error("Unable to receive", 1);
  }

  cout << message << endl;
}
