/*******************************************************************************
* Transmit.h - written by Michael Nutt, Nathan Burgess
*              source files available at https://github.com/taxisquad/plateGuard
* Desc: Establish connection to server and transmit packets using UDP
*******************************************************************************/

#ifndef TRANSMIT_H_
#define TRANSMIT_H_

#include <cstdlib>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
using namespace cv;

class Transmit
{
private:
  struct sockaddr_in servaddr;  // Server address structure
  struct sockaddr_in cliaddr;   // Client address structure
  int conn_fd;                  // Connection file descriptor
  int port;                     // Transmit port number
  int serv_len;                 // Length of server address
  int cli_len;                  // Length of client address
  int recv_len;                 // Length of received message
  struct hostent *server;       // Server address
public:
  Transmit();
  ~Transmit();
  void sendFrame(Mat);
};

#endif
