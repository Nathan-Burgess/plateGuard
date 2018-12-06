// g++ test1.cpp -o test -lopencv_core -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -L ../lib

#include <opencv2>
// #include <opencv2/videoio.hpp>
// #include <opencv2/highgui.hpp>
#include <bits/stdc++.h>
#include <iostream>
#include <stdio.h>
using namespace cv;
using namespace std;
int main(int, char**)
{
    Mat frame;
    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;
    // open the default camera using default API
    // cap.open(0);
    // OR advance usage: select any API backend
    int deviceID = 0;             // 0 = open default camera
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    // open selected camera using selected API
    cap.open(deviceID + apiID);
    cap.set(3,1280);
    cap.set(4,720);

    system("v4l2-ctl -d 0 -c auto_exposure=1 -c exposure_time_absolute=200");
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
        << "Press any key to terminate" << endl;

    // wait for a new frame from camera and store it into 'frame'
    cap.read(frame);
    // check if we succeeded
    if (frame.empty()) {
        cerr << "ERROR! blank frame grabbed\n";
    }
    // show live and wait for a key with timeout long enough to show images
    imwrite("test.png", frame);
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
