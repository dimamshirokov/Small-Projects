#include "Exception.hpp"

Exception::Exception(const std::string &string){
    reason = string;
};

std::string Exception::What() const{
    return reason;
};