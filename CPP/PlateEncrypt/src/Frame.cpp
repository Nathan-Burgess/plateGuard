#include <iostream>
#include <string>
#include <alpr.h>
#include <opencv2/opencv.hpp>
#include "Frame.h"

using namespace cv;
using namespace std;


bool Frame::setLink(string filename)
{

  if(!cap.open(filename))
  {
    return false;
  }
  else
    return true;

}
Mat Frame::grabFrame(){
    cap >> frame;
    return frame;

}


/*

int main(){
  VideoCapture cap;
  Mat tempFrame = Mat::zeros(720, 1280, CV_8UC3);
  Mat frame;

  if(!cap.open("../../data/117.mp4"))
  {
    perror("Unable to open video file");
    exit(1);
  }
namedWindow("w",1);
  for(;;){
    cap >> frame;
    if(frame.empty())
      break;
    imshow("w",frame);
    waitKey(20);
  }
  waitKey(0);
  cout << "HALO1" << endl;

}
*/
