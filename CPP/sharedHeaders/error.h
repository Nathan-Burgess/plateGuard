//
// Created by Michael Nutt(michaelnutt2@my.unt.edu)
// 11/17/2017(updated 11/16/2018)
//

#include <stdio.h>
#include <stdlib.h>

#ifndef ERROR_H_
#define ERROR_H_

void error(const char * message, int num)
{
    perror(message);
    exit(num);
}


#endif //HW6_ERROR_H
