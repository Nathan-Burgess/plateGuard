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
using namespace std;
using namespace cv;

void Capture::captureVideo(string filename)
{
  VideoCapture cap;
  Mat tempFrame;

  if(!cap.open(filename))
  {
    perror("Unable to open video file");
    exit(1);
  }

  cout << "Start reading from file" << endl;

  while(cap.read(tempFrame))
  {
    frames.push_back(tempFrame);
  }

  cout << frames[0] << endl;

  return;
}

Mat Capture::getFrames()
{
  return frames[0];
}
