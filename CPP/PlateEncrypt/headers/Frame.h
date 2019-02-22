
#ifndef FRAME_H_
#define FRAME_H_

#include <vector>
#include <string>
#include "opencv2/opencv.hpp"
#include <bits/stdc++.h>
using namespace std;
using namespace cv;

class Frame{
  //vector<Mat> frames;
  Mat frame;
  VideoCapture cap;
public:
  Mat grabFrame();
  bool setLink(string);

};

#endif
