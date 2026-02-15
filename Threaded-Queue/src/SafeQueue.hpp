#pragma once
#include <atomic>
#include <condition_variable>
#include <functional>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

template <class Function>
class SafeQueue{
public:
    std::queue<Function> tasks;
    std::mutex mutex;
    std::condition_variable conditionVariable;

    void Push(const Function& function){
        std::lock_guard<std::mutex> lockGuard(mutex);
        tasks.push(function);
        conditionVariable.notify_one();
    }

    void Pop(){
        std::unique_lock<std::mutex> uniqueLock(mutex);
        conditionVariable.wait(uniqueLock, [this]{ return !tasks.empty();});
        tasks.pop();
        uniqueLock.unlock();
    }
    
    void WaitAndPop(Function& out){
        std::unique_lock<std::mutex> uniqueLock(mutex);
        conditionVariable.wait(uniqueLock, [this]{ return !tasks.empty();});
        out = tasks.front();
        tasks.pop();
    }
};