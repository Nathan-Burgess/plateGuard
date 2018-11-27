// g++ test.cpp -o test -lopencv_core -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -L ../lib

#include <raspicam/raspicam_cv.h>
#include <iostream>
#include <unistd.h>
using namespace std;

int main(int, char**)
{
  raspicam::RaspiCam_Cv cam;
  cv::Mat frame;

  cam.set(CV_CAP_PROP_FORMAT,CV_8UC1);
  cout << "Open camera" << endl;
  if(!cam.open())
  {
    cerr << "Error opening camera\n";
    return -1;
  }

  cout << "Starting capture" << endl;

  cam.grab();
  cam.retrieve(frame);
  cv::imwrite("test.png",frame);
  cout << "Image saved\n";

}
