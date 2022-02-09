#include <iostream>

using namespace std;

int main() {
    int val;
    cin >> val;

    if (90 <= val)
        cout << "A";
    else if (80 <= val)
        cout << "B";
    else if (70 <= val)
        cout << "C";
    else if (60 <= val)
        cout << "D";
    else
        cout << "F";

    return 0;
}