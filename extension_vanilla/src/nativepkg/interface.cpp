//#include "interface.hpp"

extern "C" int add(int x, int y);
extern "C" int subtract(int x, int y);

int add(int x, int y)
{
    return x + y;
}

int subtract(int x, int y)
{
    return x - y;
}
