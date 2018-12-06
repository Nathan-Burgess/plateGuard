/*******************************************************************************
* Capture.h - written by Michael Nutt, Nathan Burgess
*              source files available at https://github.com/taxisquad/plateGuard
* Desc: Captures frames from camera and stores them in the Frames vector
*******************************************************************************/

#ifndef CAPTURE_H_
#define CAPTURE_H_

#include <vector>
#include <string>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <bits/stdc++.h>
using namespace std;
using namespace cv;

class Capture{
  vector<Mat> frames;
public:
  void captureVideo(string);
  Mat getFrames(int);
  int getFramesSize(){return frames.size();}
};

#endif
