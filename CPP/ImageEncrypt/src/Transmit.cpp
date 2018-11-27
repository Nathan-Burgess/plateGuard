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
#include "Transmit.h"
#include "error.h"
using namespace std;

Transmit::Transmit()
{
  // Server port number
  port = 1234;
  // Set up socket
  conn_fd = socket(AF_INET, SOCK_DGRAM, 0);

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
  close(conn_fd);
}

void Transmit::send()
{
  char msg[] = "Test Message";
  cout << "Sending message...\n";
  cout << serv_len << endl;

  if(sendto(conn_fd, msg, strlen(msg), 0, (struct sockaddr *) &servaddr, serv_len) == -1)
  {
    error("Error: Unable to send", 1);
  }
}
