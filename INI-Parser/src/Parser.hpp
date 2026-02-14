#pragma once
#include "Exception.hpp"

template <class Type>
class INIParser{
private:
    std::ifstream dataFile;
public:
    INIParser(const std::string &fileName){
        dataFile.open(fileName.c_str());
        if(!dataFile.is_open()){
            throw Exception("Error: File not found!");
        }
    };
    Type GetValue(const std::string &string){
        bool label;
        Type value;
        std::string sectionName = string.substr(0, string.find("."));
        std::string valueName = string.substr(string.find(".") + 1, string.size() - sectionName.size());
        std::string temporary;
        while(std::getline(dataFile, temporary)){
            if(temporary.find(sectionName) != std::string::npos){
                std::getline(dataFile, temporary);
                while(temporary.find("Section") == std::string::npos){
                    if(temporary[0] == ';'){
                        std::getline(dataFile, temporary);
                        continue;
                    }
                    if(temporary.find(valueName) != std::string::npos){
                        value = temporary.substr(temporary.find("=") + 1, temporary.size() - temporary.find("="));
                        label = true;
                    }
                    if(dataFile.eof()){
                        break;
                    }
                    std::getline(dataFile, temporary);
                }
            }
        }
        if(!dataFile.eof()){
            throw Exception("Error: File reading problems!");
        }
       if(!label){
            throw Exception("Error: Variable not found!");
        }
        return value;
    }
};

template <>
class INIParser<int>{
private:
    std::ifstream dataFile;
public:
    INIParser(const std::string &fileName){
        dataFile.open(fileName.c_str());
        if(!dataFile.is_open()){
            throw Exception("Error: File not found!");
        }
    };
    int GetValue(const std::string &string){
        bool label;
        std::string value;
        std::string sectionName = string.substr(0, string.find("."));
        std::string valueName = string.substr(string.find(".") + 1, string.size() - sectionName.size());
        std::string temporary;
        while(std::getline(dataFile, temporary)){
            if(temporary.find(sectionName) != std::string::npos){
                std::getline(dataFile, temporary);
                while(temporary.find("Section") == std::string::npos){
                    if(temporary[0] == ';'){
                        std::getline(dataFile, temporary);
                        continue;
                    }
                    if(temporary.find(valueName) != std::string::npos){
                        value = temporary.substr(temporary.find("=") + 1, temporary.size() - temporary.find("="));
                        label = true;
                    }
                    if(dataFile.eof()){
                        break;
                    }
                    std::getline(dataFile, temporary);
                }
            }
        }
        if(!dataFile.eof()){
            throw Exception("Error: File reading problems!");
        }
       if(!label){
            throw Exception("Error: Variable not found!");
        }
        value = value.substr(0, value.find(" "));
        return std::stoi(value);
    }
};