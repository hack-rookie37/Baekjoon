/**
 * @file 17256.달달함이 넘쳐흘러.cpp
 * @author @devappmin
 * @brief 달달함이 넘쳐흘러(브론즈5)
 * @version 0.1
 * @date 2022-01-14
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

class Cake {
   public:
    int x;
    int y;
    int z;
};

int main() {
    Cake a, b, c;

    cin >> a.x >> a.y >> a.z;
    cin >> c.x >> c.y >> c.z;

    cout << c.x - a.z << " " << c.y / a.y << " " << c.z - a.x;

    return 0;
}