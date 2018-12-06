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

  capturer.captureVideo("../data/test.mp4");

  return 0;
}
