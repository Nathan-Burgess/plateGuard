cmake_minimum_required(VERSION 2.8.9)
project(ImageEncrypt)

set ( GLOB PROJECT_LINK_LIBS *.so )
link_directories( /usr/local/lib )

find_package(OpenCV)

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local/include )
file(GLOB SOURCES "src/*.cpp" )

add_executable(ImageEncrypt ${SOURCES})
target_link_libraries(ImageEncrypt ${OpenCV_LIBS})
