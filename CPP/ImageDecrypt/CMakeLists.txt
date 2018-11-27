cmake_minimum_required(VERSION 2.8.9)
project(ImageDecrypt)

set ( GLOB PROJECT_LINK_LIBS *.so )
link_directories( /usr/local/lib )

include_directories( ../sharedHeaders )
include_directories( headers )
include_directories( /usr/local/include )
file(GLOB SOURCES "src/*.cpp" )

add_executable(ImageDecrypt ${SOURCES})
target_link_libraries(ImageDecrypt ${PROJECT_LINK_LIBS})
