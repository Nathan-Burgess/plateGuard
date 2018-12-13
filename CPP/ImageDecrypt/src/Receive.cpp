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
  port = 6666;
  // Set up socket
  conn_fd = socket(AF_INET, SOCK_STREAM, 0);

  if(conn_fd < 0)
  {
    error("Error opening sockets", 1);
  }

  memset((char*) &servaddr, 0, sizeof(servaddr));

  servaddr.sin_family = AF_INET;
  servaddr.sin_addr.s_addr = INADDR_ANY;
  servaddr.sin_port = htons(port);

  if(bind(conn_fd, (struct sockaddr*) &servaddr, sizeof(servaddr)) < 0)
  {
    error("Unale to bind socket", 1);
  }

  cout << "conn_fd1: " << conn_fd << endl;

}

Receive::~Receive()
{
  close(conn_fd);
}

void Receive::receiveMessage()
{
  Mat frame = Mat::zeros(720,1280, CV_8UC3);
  int frameSize = frame.total() * frame.elemSize();
  vector<Mat> frames;
  uchar *ptr = frame.data;
  int key;
  int i = 0;
  int bytes = 0;

  if(!frame.isContinuous())
  {
    frame = frame.clone();
  }

  listen(conn_fd, 1);
  if((listen_fd = accept(conn_fd, (struct sockaddr*)&cliaddr, (socklen_t *)&clilen)) < 0)
  {
    error("Accept failed", 1);
  }
  while(1)
  {
    if((bytes = recv(listen_fd, ptr, frameSize, MSG_WAITALL)) == -1)
    {
      cerr << "Receive failed, received bytes: " << bytes << endl;
      break;
    }
    imshow("Frame", frame);
    waitKey(8);
  }

}
