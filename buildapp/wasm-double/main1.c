#include<string>
#include<emscripten/emscripten.h>

int main() {
    return 10;
}

extern "C"{
    int EMSCRIPTEN_KEEPALIVE addOne(){
        return 1;
    }
}
    