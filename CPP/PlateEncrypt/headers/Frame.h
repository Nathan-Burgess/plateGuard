
#ifndef FRAME_H_
#define FRAME_H_

#include <vector>
#include <string>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

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
