#include <iostream>
#include <alpr.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include "Frame.h"

using namespace cv;
using namespace std;
using namespace alpr;

int main()
{
  Frame f;
  //Alpr openalpr("us", "/etc/openalpr/openalpr.conf");


  f.setLink("../../data/117.mp4");

/*
*/
//  Mat tempframe = Mat::zeros(720, 1280, CV_8UC3);
  Mat tempframe;
  namedWindow("w",1);
    for(;;){
      tempframe = f.grabFrame();
      if(tempframe.empty())
        break;
        imshow("w",tempframe);
        waitKey(20);
      }
    waitKey(0);
    cout << "HALO1" << endl;
    return 0;


}
