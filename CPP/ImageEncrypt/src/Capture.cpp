/*******************************************************************************
* Desc: Captures frames from camera and stores them in the Frames vector
*******************************************************************************/

#include <vector>
#include <string>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
#include "Capture.h"
#include "Transmit.h"
using namespace std;
using namespace cv;

void Capture::captureVideo(string filename)
{
  VideoCapture cap;
  int i = 0;
  Mat tempFrame = Mat::zeros(720, 1280, CV_8UC3);
  Transmit *transmitter = new Transmit;

  if(!tempFrame.isContinuous())
  {
    tempFrame =tempFrame.clone();
  }

  if(!cap.open(filename))
  {
    perror("Unable to open video file");
    exit(1);
  }

  cout << "Start reading from file" << endl;

  while(cap.read(tempFrame))
  {
    if( (i % 8) == 0)
    {
      cout << "Frame #" << i << endl;
      transmitter->sendFrame(tempFrame);
    }
    i++;

  }

  cout << endl << endl;

  // cout << sizeof(frames[0]) << endl;

  return;
}

Mat Capture::getFrames(int i)
{
  Mat frame = frames[i];

  return frame;
}
