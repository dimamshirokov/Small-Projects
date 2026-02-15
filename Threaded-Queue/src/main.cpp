#include "ThreadPool.hpp"
#include "PrintFunctions.hpp"

int main(int argc, char* argv[]){
    using namespace std::chrono_literals;
    ThreadPool<std::function<void()>> threadPool;
    while(true){
        threadPool.Submit(PrintNameFirst);
        threadPool.Submit(PrintNameSecond);
        std::this_thread::sleep_for(1s);
    }
    return EXIT_SUCCESS;
}