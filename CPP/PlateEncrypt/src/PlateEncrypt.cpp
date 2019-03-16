#include <iostream>
#include <alpr.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <vector>
#include <algorithm>


#include "Frame.h"

using namespace cv;
using namespace std;
using namespace alpr;




int main()
{
    //Making Frame Object
    Frame f;

    //Setting up video link and openALPR
    Alpr openalpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data");
    openalpr.setTopN(20);
    openalpr.setDefaultRegion("tx");
    f.setLink("../../data/test_video_short.mp4");

    // Variable to hold frame recieved
    Mat tempframe;

    //setting up video window and grabbing frame from FRAME class
    namedWindow("w",1);
    for(int i = 0; i < 200; i++){
        tempframe = f.grabFrame();
        if(tempframe.empty())
          break;
        imshow("w",tempframe);
        waitKey(20);
     }
    waitKey(0);

    //Making Vectors for Uchar for imencode, and char for alpr
    vector<uchar> v3;
    vector<char> v4 ;

    //encoding mat frame to the uchar vector
    imencode(".png",tempframe,v3);

    //copying uchar vector to char vector
    copy(v3.begin(),v3.end(),back_inserter(v4));

    //calling alpr for frame
    AlprResults results = openalpr.recognize((v4));

    //printing out results of alpr call
    for (int i = 0; i < results.plates.size(); i++)
    {
        AlprPlateResult plate = results.plates[i];
        cout << "plate" << i << ": " << plate.topNPlates.size() << " results" << std::endl;

        for (int k = 0; k < plate.topNPlates.size(); k++)
        {
           AlprPlate candidate = plate.topNPlates[k];
            cout << "    - " << candidate.characters << "\t confidence: " << candidate.overall_confidence;
            cout << "\t pattern_match: " << candidate.matches_template << std::endl;
        }

    }


    cout <<"HALO";

return 0;
}


















//ORGINAL CODE
/*
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

*/