cmake_minimum_required(VERSION 2.8.9)
project(PlateEncrypt)

set ( GLOB PROJECT_LINK_LIBS *.so )
link_directories( /usr/local/lib )
link_directories( /usr/lib )

find_package(OpenCV)

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local/include )
include_directories( /usr/include )
include_directories(/usr/lib)
file(GLOB SOURCES "src/*.cpp" )

add_executable(PlateEncrypt ${SOURCES})
target_link_libraries(PlateEncrypt ${OpenCV_LIBS} ${PROJECT_LINK_LIBS})
