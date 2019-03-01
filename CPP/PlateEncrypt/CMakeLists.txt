cmake_minimum_required(VERSION 3.1)
project(PlateEncrypt)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
#[[
set ( GLOB PROJECT_LINK_LIBS *.so )
link_directories( /usr/local/lib )
link_directories( /usr/lib )
link_directories( /usr/include )

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local/include )
include_directories( /usr/include )
include_directories(/usr/lib)
file(GLOB SOURCES "src/*.cpp" )
SET(OPENALPR_LIB /usr/lib/libopenalpr.so)
SET(OPENCV_DIR /usr/local/include/opencv4)
]]
find_package(OpenCV)
#find_package(OpenCV PATHS /usr/local/include/opencv4)
include_directories( ${OpenCV_INCLUDE_DIRS} )
set ( GLOB PROJECT_LINK_LIBS *.so )

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local )
#include_directories( /usr/include )
#include_directories(/usr/lib)

file(GLOB SOURCES "src/*.cpp" )
#SET(OPENCV_DIR /usr/local/lib/*.so)
SET(OPENALPR_LIB /usr/lib/libopenalpr.so)

add_executable(PlateEncrypt ${SOURCES})
#target_link_libraries(PlateEncrypt ${OpenCV_LIBS} ${PROJECT_LINK_LIBS} ${OPENALPR_LIB})

target_link_libraries(PlateEncrypt  ${OPENALPR_LIB} ${OpenCV_LIBS} ${PROJECT_LINK_LIBS} )
