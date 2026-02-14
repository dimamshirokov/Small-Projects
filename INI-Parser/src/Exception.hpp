#pragma once
#include <iostream>
#include <string>
#include <fstream>

class Exception{
private:
    std::string reason;
public:
    Exception(const std::string &string);
    std::string What() const;
};