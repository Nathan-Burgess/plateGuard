cmake_minimum_required(VERSION 2.8.9)
project(PlateEncrypt)

set ( GLOB PROJECT_LINK_LIBS *.so )



include_directories( /home/nathan/Desktop/opencv-opencv-e7c915a )

SET(OPENALPR_LIB /usr/lib/libopenalpr.so)
include_directories( headers )
include_directories( /usr/local/include )
include_directories( /usr/include )
file(GLOB SOURCES "src/*.cpp" )



add_executable(PlateEncrypt ${SOURCES})
target_link_libraries(PlateEncrypt ${OPENALPR_LIB} ${PROJECT_LINK_LIBS})
