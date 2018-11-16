/*******************************************************************************
* Desc: Program to read from camera and then encrypt video using stream cipher,
*       transmits to server using UDP
*******************************************************************************/

#include <iostream>
#include "Transmit.h"
using namespace std;

int main()
{
  Transmit *transmitter = new Transmit;
  transmitter->send();

  return 0;
}
