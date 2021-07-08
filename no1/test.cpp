#include <iostream>


using namespace std;

void funkcja(const string& msg) {

    cout << msg << endl;
}

int main() {

    void (* wskaznik)(const string& message) ;


    wskaznik = funkcja;
    string msg = "Dane z websocketa";
    wskaznik(msg);

}