#include <iostream>

#include <alpr.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
//#include <opencv2>
//#include <opencv2/videoio.hpp>
//#include "Frame.h"

using namespace cv;
using namespace std;
using namespace alpr;

int main()
{
  //Frame f;
 Alpr openalpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data");


  //f.setLink("../../data/117.mp4");

/*
*/
/*
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
*/

    openalpr.setTopN(20);


    openalpr.setDefaultRegion("tx");

    if (openalpr.isLoaded() == false)
    {
        std::cerr << "Error loading OpenALPR" << std::endl;
        return 1;
    }

// Recognize an image file. Alternatively, you could provide the image bytes in-memory.
    alpr::AlprResults results = openalpr.recognize("../../data/twoplates.png");


    for (int i = 0; i < results.plates.size(); i++)
    {
        alpr::AlprPlateResult plate = results.plates[i];
        std::cout << "plate" << i << ": " << plate.topNPlates.size() << " results" << std::endl;

        for (int k = 0; k < plate.topNPlates.size(); k++)
        {
            alpr::AlprPlate candidate = plate.topNPlates[k];
            std::cout << "    - " << candidate.characters << "\t confidence: " << candidate.overall_confidence;
            std::cout << "\t pattern_match: " << candidate.matches_template << std::endl;
        }
    }



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
