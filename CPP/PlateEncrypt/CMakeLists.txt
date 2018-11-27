cmake_minimum_required(VERSION 2.8.9)
project(PlateEncrypt)

set ( GLOB PROJECT_LINK_LIBS *.so )
link_directories( /usr/local/lib )

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local/include )
file(GLOB SOURCES "src/*.cpp" )

add_executable(PlateEncrypt ${SOURCES})
target_link_libraries(PlateEncrypt ${PROJECT_LINK_LIBS}
