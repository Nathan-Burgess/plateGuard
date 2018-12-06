/*******************************************************************************
* Desc: Program to read from camera and then encrypt video using stream cipher,
*       transmits to server using UDP
*******************************************************************************/

#include <iostream>
#include "Transmit.h"
#include "Capture.h"
using namespace std;

int main()
{
  Capture capturer;
  Transmit *transmitter = new Transmit;

  capturer.captureVideo("../data/test.mp4");
  transmitter->send(capturer.getFrames());

  return 0;
}
