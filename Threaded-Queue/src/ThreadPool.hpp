#pragma once
#include "SafeQueue.hpp"

template <class Function>
class ThreadPool{
public:
    std::vector<std::thread> threads;
    SafeQueue<Function> works;
    std::atomic<bool> done;

    ThreadPool() : done(false){
        size_t numberOfThreads{std::thread::hardware_concurrency()};
        threads.resize(numberOfThreads);
        for(size_t index = 0; index < numberOfThreads; ++index){
            threads[index] = std::thread([this]{
                while(!done){
                    Function task{};
                    works.WaitAndPop(task);
                    task();
                }
            });
        }
    }

    void Work(){
        Function task;
        works.WaitAndPop(task);
        task();
    }

    void Submit(Function function){
        works.Push(function);
    }
    
    ~ThreadPool(){
        done = true;
        for(size_t index = 0; index < threads.size(); ++index){
            threads[index].join();
        }
    }
};