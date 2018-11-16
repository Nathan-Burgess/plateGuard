/*******************************************************************************
* Receive.h - Written by Michael Nutt, Nathan Burgess
              source files available at https://github.com/taxisquad/plateGuard
* Desc: Set up UDP server
*******************************************************************************/

#ifndef RECEIVE_H_
#define RECEIVE_H_

#include <cstdlib>
#include <arpa/inet.h>
#include <sys/socket.h>

class Receive
{
private:
  struct sockaddr_in servaddr;
  struct sockaddr_in cliaddr;
  int conn_fd;
  int port;
  int recvlen;
  socklen_t clilen;
  char *message;
public:
  Receive();
  ~Receive();
  void receiveMessage();
};

#endif
