cmake_minimum_required(VERSION 3.10)

project(threadedQueue)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(threadedQueue main.cpp PrintFunctions.cpp SafeQueue.hpp ThreadPool.hpp)