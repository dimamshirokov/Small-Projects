#include "Exception.hpp"
#include "Parser.hpp"

int main(int argc, char* argv[]){
    try{
        INIParser<std::string> parser("data.txt");
        std::string value = parser.GetValue("Section1.var2");
        std::cout << value << std::endl;
        INIParser<int> intParser("data.txt");
        int intValue = intParser.GetValue("Section1.var1");
        std::cout << intValue << std::endl;
    }catch(Exception &ex){
        std::cout << ex.What() << std::endl;
    }catch(...){
        std::cout << "Error: Unknown Error!" << std::endl;
    }
    return EXIT_SUCCESS;
}