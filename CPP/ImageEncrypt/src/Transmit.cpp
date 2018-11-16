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
#include "Transmit.h"
#include "error.h"
using namespace std;

Transmit::Transmit()
{
  // Server port number
  port = 1234;
  // Set up socket
  conn_fd = socket(AF_INET, SOCK_DGRAM, 0);

  // Check if connection socket was successful
  if(conn_fd < 0)
  {
    error("Error opening socket", 1);
  }

  // Get address from hostname
  server = gethostbyname("localhost");

  if(server == NULL)
  {
    error("Error: No such host", 0);
  }

  // Set up server connection
  servaddr.sin_family = AF_INET;
  servaddr.sin_port = htons(port);
}

Transmit::~Transmit()
{
  close(conn_fd);
}

void Transmit::send()
{
  if(sendto(conn_fd, "Test Message", 12, 0, (struct sockaddr *) &servaddr, serv_len) == -1)
  {
    error("Error: Unable to send", 1);
  }
}
