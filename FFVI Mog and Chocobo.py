#Anna Zheng Pd7
#Main Program
#Final Fantasy VI Mog and Chocobo
#Work Time: 2 Days
import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.hideturtle()
turtle.bgcolor('lime')
from myFunctionFile import*
from FFVIMogandChocoboFunctionFile import*
#Row -15
for times in range(3):
    jump(bob,-36+times*6,-96)
    BlackPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-96)
    BlackPixel(bob)
#Row -14
jump(bob,-42,-90)
BlackPixel(bob)
jump(bob,-36,-90)
GoldPixel(bob)
jump(bob,-30,-90)
LightBrownPixel(bob)
jump(bob,-24,-90)
BlackPixel(bob)
jump(bob,42,-90)
BlackPixel(bob)
jump(bob,48,-90)
LightBrownPixel(bob)
jump(bob,54,-90)
BlackPixel(bob)
#Row -13
jump(bob,-42,-84)
BlackPixel(bob)
jump(bob,-36,-84)
BrownPixel(bob)
jump(bob,-30,-84)
LightBrownPixel(bob)
jump(bob,-24,-84)
BlackPixel(bob)
jump(bob,42,-84)
BlackPixel(bob)
jump(bob,48,-84)
BrownPixel(bob)
jump(bob,54,-84)
BlackPixel(bob)
#Row -12
jump(bob,-42,-78)
BlackPixel(bob)
jump(bob,-36,-78)
BrownPixel(bob)
for times in range(2):
    jump(bob,-30+times*6,-78)
    BlackPixel(bob)
for times in range(2):
    jump(bob,36+times*6,-78)
    BlackPixel(bob)
for times in range(2):
    jump(bob,48+times*6,-78)
    BrownPixel(bob)
jump(bob,60,-78)
BlackPixel(bob)
#Row -11
jump(bob,-48,-72)
BlackPixel(bob)
for times in range(2):
    jump(bob,-42+times*6,-72)
    BrownPixel(bob)
jump(bob,-30,-72)
BlackPixel(bob)
for times in range(2):
    jump(bob,24+times*6,-72)
    BlackPixel(bob)
for times in range(4):
    jump(bob,36+times*6,-72)
    BrownPixel(bob)
for times in range(2):
    jump(bob,60+times*6,-72)
    BlackPixel(bob)
#Row -10
jump(bob,-48,-66)
BlackPixel(bob)
for times in range(2):
    jump(bob,-42+times*6,-66)
    BrownPixel(bob)
jump(bob,-30,-66)
BlackPixel(bob)
for times in range(3):
    jump(bob,6+times*6,-66)
    BlackPixel(bob)
for times in range(2):
    jump(bob,24+times*6,-66)
    BrownPixel(bob)
jump(bob,36,-66)
LightBrownPixel(bob)
jump(bob,42,-66)
BrownPixel(bob)
jump(bob,48,-66)
BlackPixel(bob)
for times in range(3):
    jump(bob,54+times*6,-66)
    BrownPixel(bob)
jump(bob,72,-66)
BlackPixel(bob)
#Row -9
jump(bob,-54,-60)
BlackPixel(bob)
jump(bob,-48,-60)
BrownPixel(bob)
jump(bob,-42,-60)
BlackPixel(bob)
for times in range(2):
    jump(bob,-36+times*6,-60)
    BrownPixel(bob)
jump(bob,-24,-60)
BlackPixel(bob)
jump(bob,6,-60)
BlackPixel(bob)
for times in range(3):
    jump(bob,12+times*6,-60)
    BrownPixel(bob)
jump(bob,30,-60)
LightBrownPixel(bob)
for times in range(3):
    jump(bob,36+times*6,-60)
    BlackPixel(bob)
jump(bob,54,-60)
BrownPixel(bob)
jump(bob,60,-60)
GoldPixel(bob)
jump(bob,66,-60)
BlackPixel(bob)
jump(bob,72,-60)
GoldPixel(bob)
jump(bob,78,-60)
BlackPixel(bob)
#Row -8
for times in range(4):
    jump(bob,-54+times*6,-54)
    BlackPixel(bob)
jump(bob,-30,-54)
BrownPixel(bob)
for times in range(11):
    jump(bob,-24+times*6,-54)
    BlackPixel(bob)
for times in range(2):
    jump(bob,54+times*6,-54)
    BlackPixel(bob)
jump(bob,72,-54)
BlackPixel(bob)
#Row -7
jump(bob,-36,-48)
BlackPixel(bob)
for times in range(3):
    jump(bob,-30+times*6,-48)
    BrownPixel(bob)
for times in range(2):
    jump(bob,-12+times*6,-48)
    LightBrownPixel(bob)
jump(bob,0,-48)
BlackPixel(bob)
for times in range(2):
    jump(bob,6+times*6,-48)
    LightBrownPixel(bob)
jump(bob,18,-48)
GoldPixel(bob)
jump(bob,24,-48)
LightBrownPixel(bob)
jump(bob,30,-48)
BrownPixel(bob)
jump(bob,36,-48)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-48)
    BlackPixel(bob)
#Row -6
for times in range(2):
    jump(bob,-36+times*6,-42)
    BlackPixel(bob)
jump(bob,-24,-42)
LightBrownPixel(bob)
jump(bob,-18,-42)
BrownPixel(bob)
for times in range(2):
    jump(bob,-12+times*6,-42)
    BlackPixel(bob)
for times in range(3):
    jump(bob,0+times*6,-42)
    LightBrownPixel(bob)
for times in range(2):
    jump(bob,18+times*6,-42)
    GoldPixel(bob)
jump(bob,30,-42)
YellowPixel(bob)
for times in range(2):
    jump(bob,36+times*6,-42)
    GoldPixel(bob)
jump(bob,48,-42)
OrangePixel(bob)
jump(bob,54,-42)
BlackPixel(bob)
#Row -5
for times in range(2):
    jump(bob,-24+times*6,-36)
    BlackPixel(bob)
jump(bob,-12,-36)
LightBrownPixel(bob)
for times in range(4):
    jump(bob,-6+times*6,-36)
    GoldPixel(bob)
for times in range(2):
    jump(bob,18+times*6,-36)
    LightBrownPixel(bob)
for times in range(3):
    jump(bob,30+times*6,-36)
    YellowPixel(bob)
jump(bob,48,-36)
OrangePixel(bob)
jump(bob,54,-36)
GoldPixel(bob)
jump(bob,60,-36)
BlackPixel(bob)
#Row -4
jump(bob,-24,-30)
BlackPixel(bob)
jump(bob,-18,-30)
BrownPixel(bob)
for times in range(3):
    jump(bob,-12+times*6,-30)
    GoldPixel(bob)
for times in range(3):
    jump(bob,6+times*6,-30)
    WhitePixel(bob)
for times in range(2):
    jump(bob,24+times*6,-30)
    GoldPixel(bob)
for times in range(2):
    jump(bob,36+times*6,-30)
    YellowPixel(bob)
jump(bob,48,-30)
WhitePixel(bob)
jump(bob,54,-30)
YellowPixel(bob)
jump(bob,60,-30)
BlackPixel(bob)
#Row -3
jump(bob,-24,-24)
BrownPixel(bob)
jump(bob,-18,-24)
GoldPixel(bob)
for times in range(3):
    jump(bob,-12+times*6,-24)
    WhitePixel(bob)
jump(bob,6,-24)
GoldPixel(bob)
for times in range(3):
    jump(bob,12+times*6,-24)
    WhitePixel(bob)
jump(bob,30,-24)
LightBrownPixel(bob)
jump(bob,36,-24)
YellowPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-24)
    WhitePixel(bob)
jump(bob,54,-24)
OrangePixel(bob)
jump(bob,60,-24)
BrownPixel(bob)
jump(bob,66,-24)
BlackPixel(bob)
#Row -2
jump(bob,-30,-18)
BlackPixel(bob)
jump(bob,-24,-18)
BrownPixel(bob)
for times in range(2):
    jump(bob,-18+times*6,-18)
    GoldPixel(bob)
for times in range(3):
    jump(bob,-6+times*6,-18)
    YellowPixel(bob)
for times in range(3):
    jump(bob,12+times*6,-18)
    WhitePixel(bob)
jump(bob,30,-18)
GoldPixel(bob)
jump(bob,36,-18)
YellowPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-18)
    WhitePixel(bob)
jump(bob,54,-18)
YellowPixel(bob)
jump(bob,60,-18)
GoldPixel(bob)
jump(bob,66,-18)
BlackPixel(bob)
#Row -1
for times in range(2):
    jump(bob,-42+times*6,-12)
    BlackPixel(bob)
jump(bob,-30,-12)
BrownPixel(bob)
jump(bob,-24,-12)
GoldPixel(bob)
jump(bob,-18,-12)
YellowPixel(bob)
for times in range(3):
    jump(bob,-12+times*6,-12)
    WhitePixel(bob)
for times in range(2):
    jump(bob,6+times*6,-12)
    YellowPixel(bob)
for times in range(2):
    jump(bob,18+times*6,-12)
    WhitePixel(bob)
jump(bob,30,-12)
GoldPixel(bob)
jump(bob,36,-12)
YellowPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-12)
    WhitePixel(bob)
jump(bob,54,-12)
YellowPixel(bob)
jump(bob,60,-12)
GoldPixel(bob)
jump(bob,66,-12)
BlackPixel(bob)
#Row 0
jump(bob,-48,-6)
BlackPixel(bob)
for times in range(3):
    jump(bob,-42+times*6,-6)
    LightBrownPixel(bob)
for times in range(2):
    jump(bob,-24+times*6,-6)
    OrangePixel(bob)
jump(bob,-12,-6)
YellowPixel(bob)
for times in range(3):
    jump(bob,-6+times*6,-6)
    WhitePixel(bob)
jump(bob,12,-6)
YellowPixel(bob)
for times in range(2):
    jump(bob,18+times*6,-6)
    WhitePixel(bob)
jump(bob,30,-6)
GoldPixel(bob)
jump(bob,36,-6)
YellowPixel(bob)
for times in range(2):
    jump(bob,42+times*6,-6)
    WhitePixel(bob)
jump(bob,54,-6)
YellowPixel(bob)
jump(bob,60,-6)
LightBrownPixel(bob)
jump(bob,66,-6)
BlackPixel(bob)
#Row 1
jump(bob,0,0)
BlackPixel(bob)
jump(bob,6,0)
BlackPixel(bob)
jump(bob,-6,0)
WhitePixel(bob)
jump(bob,-12,0)
WhitePixel(bob)
jump(bob,-18,0)
YellowPixel(bob)
for times in range(4):
    jump(bob,-24-times*6,0)
    GoldPixel(bob)
jump(bob,-48,0)
LightBrownPixel(bob)
jump(bob,-54,0)
BlackPixel(bob)
for times in range(8):
    jump(bob,12+times*6,0)
    YellowPixel(bob)
jump(bob,60,0)
BlackPixel(bob)
jump(bob,96,0)
BlackPixel(bob)
#Row 2
jump(bob,6,6)
WhitePixel(bob)
jump(bob,0,6)
LightBluePixel(bob)
for times in range(3):
    jump(bob,-6-times*6,6)
    BlackPixel(bob)
for times in range(4):
    jump(bob,-24-times*6,6)
    GoldPixel(bob)
for times in range(2):
    jump(bob,-48-times*6,6)
    YellowPixel(bob)
jump(bob,-60,6)
LightBrownPixel(bob)
jump(bob,-66,6)
BlackPixel(bob)
jump(bob,12,6)
BlackPixel(bob)
for times in range(3):
    jump(bob,18+times*6,6)
    YellowPixel(bob)
jump(bob,36,6)
GoldPixel(bob)
for times in range(3):
    jump(bob,42+times*6,6)
    YellowPixel(bob)
jump(bob,60,6)
BlackPixel(bob)
for times in range(2):
    jump(bob,84+times*6,6)
    BlackPixel(bob)
jump(bob,96,6)
OrangePixel(bob)
jump(bob,102,6)
BlackPixel(bob)
#Row 3
for times in range(3):
    jump(bob,12-times*6,12)
    WhitePixel(bob)
for times in range(2):
    jump(bob,-6-times*6,12)
    LightBluePixel(bob)
jump(bob,-18,12)
LightGrayPixel(bob)
jump(bob,-24,12)
BlackPixel(bob)
jump(bob,-30,12)
GoldPixel(bob)
for times in range(2):
    jump(bob,-36-times*6,12)
    WhitePixel(bob)
for times in range(3):
    jump(bob,-48-times*6,12)
    GoldPixel(bob)
jump(bob,-66,12)
BlackPixel(bob)
jump(bob,18,12)
BlackPixel(bob)
jump(bob,24,12)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,30+times*6,12)
    GoldPixel(bob)
for times in range(2):
    jump(bob,42+times*6,12)
    YellowPixel(bob)
jump(bob,54,12)
GoldPixel(bob)
jump(bob,60,12)
LightBrownPixel(bob)
for times in range(3):
    jump(bob,66+times*6,12)
    BlackPixel(bob)
for times in range(3):
    jump(bob,84+times*6,12)
    OrangePixel(bob)
jump(bob,102,12)
LightBrownPixel(bob)
jump(bob,108,12)
BlackPixel(bob)
#Row 4
jump(bob,12,18)
WhitePixel(bob)
jump(bob,6,18)
LightBluePixel(bob)
jump(bob,0,18)
LightGrayPixel(bob)
for times in range(2):
    jump(bob,-6-times*6,18)
    WhitePixel(bob)
jump(bob,-18,18)
LightBluePixel(bob)
jump(bob,-24,18)
LightGrayPixel(bob)
jump(bob,-30,18)
BlackPixel(bob)
jump(bob,-36,18)
GoldPixel(bob)
for times in range(2):
    jump(bob,-42-times*6,18)
    WhitePixel(bob)
for times in range(3):
    jump(bob,-54-times*6,18)
    GoldPixel(bob)
jump(bob,-72,18)
BlackPixel(bob)
for times in range(4):
    jump(bob,18+times*6,18)
    BlackPixel(bob)
jump(bob,42,18)
GoldPixel(bob)
for times in range(3):
    jump(bob,48+times*6,18)
    BrownPixel(bob)
jump(bob,66,18)
LightBrownPixel(bob)
for times in range(3):
    jump(bob,72+times*6,18)
    OrangePixel(bob)
for times in range(2):
    jump(bob,90+times*6,18)
    GoldPixel(bob)
jump(bob,102,18)
LightBrownPixel(bob)
jump(bob,108,18)
BlackPixel(bob)
#Row 5
jump(bob,30,24)
BlackPixel(bob)
jump(bob,42,24)
BlackPixel(bob)
for times in range(2):
    jump(bob,48+times*6,24)
    GoldPixel(bob)
for times in range(2):
    jump(bob,60+times*6,24)
    LightBrownPixel(bob)
for times in range(4):
    jump(bob,72+times*6,24)
    GoldPixel(bob)
jump(bob,96,24)
YellowPixel(bob)
jump(bob,102,24)
OrangePixel(bob)
jump(bob,108,24)
BlackPixel(bob)
jump(bob,24,24)
LightGrayPixel(bob)
jump(bob,18,24)
LightGrayPixel(bob)
for times in range(3):
    jump(bob,12-times*6,24)
    BlackPixel(bob)
for times in range(2):
    jump(bob,-6-times*6,24)
    WhitePixel(bob)
jump(bob,-18,24)
LightBluePixel(bob)
jump(bob,-24,24)
LightGrayPixel(bob)
jump(bob,-30,24)
BlackPixel(bob)
jump(bob,-36,24)
GoldPixel(bob)
jump(bob,-42,24)
BlackPixel(bob)
for times in range(2):
    jump(bob,-48-times*6,24)
    WhitePixel(bob)
jump(bob,-60,24)
GoldPixel(bob)
jump(bob,-66,24)
LightBrownPixel(bob)
jump(bob,-72,24)
BlackPixel(bob)
#Row 6
jump(bob,24,30)
LightBluePixel(bob)
for times in range(6):
    jump(bob,18-times*6,30)
    WhitePixel(bob)
jump(bob,-18,30)
LightBluePixel(bob)
jump(bob,-24,30)
LightGrayPixel(bob)
for times in range(2):
    jump(bob,-30-times*6,30)
    BlackPixel(bob)
jump(bob,-42,30)
PinkPixel(bob)
jump(bob,-48,30)
BlackPixel(bob)
jump(bob,-54,30)
YellowPixel(bob)
jump(bob,-60,30)
GoldPixel(bob)
jump(bob,-66,30)
BlackPixel(bob)
for times in range(2):
    jump(bob,30+times*6,30)
    BlackPixel(bob)
jump(bob,42,30)
GoldPixel(bob)
for times in range(3):
    jump(bob,48+times*6,30)
    YellowPixel(bob)
jump(bob,66,30)
GoldPixel(bob)
jump(bob,72,30)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,78+times*6,30)
    GoldPixel(bob)
for times in range(2):
    jump(bob,90+times*6,30)
    YellowPixel(bob)
jump(bob,102,30)
OrangePixel(bob)
jump(bob,108,30)
BlackPixel(bob)
#Row 7
jump(bob,18,36)
LightGrayPixel(bob)
jump(bob,12,36)
LightBluePixel(bob)
for times in range(3):
    jump(bob,6-times*6,36)
    WhitePixel(bob)
for times in range(2):
    jump(bob,-12-times*6,36)
    LightBluePixel(bob)
jump(bob,-24,36)
BlackPixel(bob)
jump(bob,-30,36)
PinkPixel(bob)
jump(bob,-36,36)
BlackPixel(bob)
jump(bob,-42,36)
PinkPixel(bob)
jump(bob,-48,36)
BlackPixel(bob)
jump(bob,-54,36)
OrangePixel(bob)
jump(bob,-60,36)
YellowPixel(bob)
jump(bob,-66,36)
BlackPixel(bob)
for times in range(3):
    jump(bob,24+times*6,36)
    BlackPixel(bob)
for times in range(2):
    jump(bob,42+times*6,36)
    GoldPixel(bob)
for times in range(2):
    jump(bob,54+times*6,36)
    YellowPixel(bob)
jump(bob,66,36)
GoldPixel(bob)
jump(bob,72,36)
BluePixel(bob)
jump(bob,78,36)
WhitePixel(bob)
jump(bob,84,36)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,90+times*6,36)
    GoldPixel(bob)
jump(bob,102,36)
LightBrownPixel(bob)
jump(bob,108,36)
BlackPixel(bob)
#Row 8
jump(bob,30,42)
LightBluePixel(bob)
jump(bob,24,42)
WhitePixel(bob)
for times in range(2):
    jump(bob,18-times*6,42)
    LightBluePixel(bob)
for times in range(3):
    jump(bob,6-times*6,42)
    WhitePixel(bob)
jump(bob,-12,42)
LightBluePixel(bob)
jump(bob,-18,42)
LightGrayPixel(bob)
for times in range(2):
    jump(bob,-24-times*6,42)
    PinkPixel(bob)
jump(bob,-36,42)
LightPinkPixel(bob)
jump(bob,-42,42)
PinkPixel(bob)
jump(bob,-48,42)
BlackPixel(bob)
jump(bob,-54,42)
GoldPixel(bob)
jump(bob,-60,42)
YellowPixel(bob)
jump(bob,-66,42)
BlackPixel(bob)
jump(bob,36,42)
BlackPixel(bob)
for times in range(4):
    jump(bob,42+times*6,42)
    YellowPixel(bob)
jump(bob,66,42)
WhitePixel(bob)
for times in range(2):
    jump(bob,72+times*6,42)
    BluePixel(bob)
jump(bob,84,42)
YellowPixel(bob)
for times in range(2):
    jump(bob,90+times*6,42)
    OrangePixel(bob)
jump(bob,102,42)
LightBrownPixel(bob)
jump(bob,108,42)
BlackPixel(bob)
#Row 9
jump(bob,36,48)
PinkPixel(bob)
for times in range(7):
    jump(bob,30-times*6,48)
    WhitePixel(bob)
jump(bob,-12,48)
LightBluePixel(bob)
jump(bob,-18,48)
LightGrayPixel(bob)
jump(bob,-24,48)
PinkPixel(bob)
for times in range(2):
    jump(bob,-30-times*6,48)
    LightPinkPixel(bob)
jump(bob,-42,48)
PinkPixel(bob)
for times in range(2):
    jump(bob,-48-times*6,48)
    BlackPixel(bob)
jump(bob,-60,48)
LightBrownPixel(bob)
jump(bob,-66,48)
BlackPixel(bob)
jump(bob,42,48)
BlackPixel(bob)
for times in range(2):
    jump(bob,48+times*6,48)
    YellowPixel(bob)
jump(bob,60,48)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,66+times*6,48)
    WhitePixel(bob)
jump(bob,78,48)
LightBrownPixel(bob)
for times in range(2):
    jump(bob,84+times*6,48)
    YellowPixel(bob)
jump(bob,96,48)
GoldPixel(bob)
jump(bob,102,48)
BlackPixel(bob)
#Row 9
jump(bob,36,54)
PinkPixel(bob)
jump(bob,30,54)
WhitePixel(bob)
jump(bob,24,54)
BluePixel(bob)
jump(bob,18,54)
WhitePixel(bob)
jump(bob,12,54)
LightPinkPixel(bob)
for times in range(4):
    jump(bob,6-times*6,54)
    WhitePixel(bob)
jump(bob,-18,54)
LightGrayPixel(bob)
jump(bob,-24,54)
BlackPixel(bob)
jump(bob,-30,54)
PinkPixel(bob)
jump(bob,-36,54)
LightPinkPixel(bob)
jump(bob,-42,54)
PinkPixel(bob)
jump(bob,-48,54)
BlackPixel(bob)
jump(bob,-54,54)
GoldPixel(bob)
jump(bob,-60,54)
BlackPixel(bob)
jump(bob,42,54)
BlackPixel(bob)
for times in range(3):
    jump(bob,48+times*6,54)
    YellowPixel(bob)
for times in range(2):
    jump(bob,66+times*6,54)
    LightBrownPixel(bob)
for times in range(3):
    jump(bob,78+times*6,54)
    YellowPixel(bob)
jump(bob,96,54)
GoldPixel(bob)
jump(bob,102,54)
BlackPixel(bob)
#Row 10
jump(bob,30,60)
WhitePixel(bob)
for times in range(2):
    jump(bob,24-times*6,60)
    BluePixel(bob)
for times in range(5):
    jump(bob,12-times*6,60)
    WhitePixel(bob)
jump(bob,-18,60)
LightBluePixel(bob)
for times in range(2):
    jump(bob,-24-times*6,60)
    BlackPixel(bob)
jump(bob,-36,60)
PinkPixel(bob)
jump(bob,-42,60)
BlackPixel(bob)
for times in range(2):
    jump(bob,-48-times*6,60)
    YellowPixel(bob)
jump(bob,-60,60)
BlackPixel(bob)
jump(bob,36,60)
BlackPixel(bob)
jump(bob,42,60)
LightBrownPixel(bob)
for times in range(3):
    jump(bob,48+times*6,60)
    YellowPixel(bob)
for times in range(3):
    jump(bob,66+times*6,60)
    WhitePixel(bob)
for times in range(2):
    jump(bob,84+times*6,60)
    YellowPixel(bob)
jump(bob,96,60)
LightBrownPixel(bob)
jump(bob,102,60)
BlackPixel(bob)
#Row 11
for times in range(2):
    jump(bob,30-times*6,66)
    WhitePixel(bob)
for times in range(3):
    jump(bob,18-times*6,66)
    BluePixel(bob)
for times in range(4):
    jump(bob,0-times*6,66)
    WhitePixel(bob)
jump(bob,-24,66)
BlackPixel(bob)
for times in range(4):
    jump(bob,-36-times*6,66)
    BlackPixel(bob)
jump(bob,36,66)
BlackPixel(bob)
for times in range(2):
    jump(bob,42+times*6,66)
    YellowPixel(bob)
for times in range(4):
    jump(bob,54+times*6,66)
    WhitePixel(bob)
for times in range(2):
    jump(bob,78+times*6,66)
    YellowPixel(bob)
jump(bob,90,66)
GoldPixel(bob)
jump(bob,96,66)
BlackPixel(bob)
#Row 12
for times in range(9):
    jump(bob,30-times*6,72)
    WhitePixel(bob)
jump(bob,-24,72)
BlackPixel(bob)
jump(bob,36,72)
BlackPixel(bob)
for times in range(6):
    jump(bob,42+times*6,72)
    YellowPixel(bob)
for times in range(2):
    jump(bob,78+times*6,72)
    GoldPixel(bob)
jump(bob,90,72)
BlackPixel(bob)
#Row 13
for times in range(8):
    jump(bob,30-times*6,78)
    WhitePixel(bob)
jump(bob,-18,79)
LightBluePixel(bob)
jump(bob,-24,78)
BlackPixel(bob)
jump(bob,36,78)
BlackPixel(bob)
for times in range(2):
    jump(bob,42+times*6,78)
    YellowPixel(bob)
jump(bob,54,78)
GoldPixel(bob)
jump(bob,60,78)
YellowPixel(bob)
for times in range(2):
    jump(bob,66+times*6,78)
    GoldPixel(bob)
jump(bob,78,78)
LightBrownPixel(bob)
jump(bob,84,78)
BlackPixel(bob)
#Row 14
jump(bob,30,84)
LightGrayPixel(bob)
for times in range(3):
    jump(bob,24-times*6,84)
    WhitePixel(bob)
jump(bob,6,84)
PinkPixel(bob)
for times in range(3):
    jump(bob,0-times*6,84)
    WhitePixel(bob)
jump(bob,-18,84)
LightGrayPixel(bob)
jump(bob,-24,84)
BlackPixel(bob)
for times in range(3):
    jump(bob,36+times*6,84)
    BlackPixel(bob)
jump(bob,54,84)
YellowPixel(bob)
jump(bob,60,84)
GoldPixel(bob)
jump(bob,66,84)
BrownPixel(bob)
jump(bob,72,84)
BlackPixel(bob)
#Row 15
jump(bob,24,90)
LightBluePixel(bob)
for times in range(2):
    jump(bob,18-times*6,90)
    WhitePixel(bob)
jump(bob,6,90)
PinkPixel(bob)
jump(bob,0,90)
WhitePixel(bob)
jump(bob,-6,90)
LightBluePixel(bob)
jump(bob,-12,90)
LightGrayPixel(bob)
jump(bob,-18,90)
BlackPixel(bob)
jump(bob,30,90)
BlackPixel(bob)
#Row 16
jump(bob,6,96)
PinkPixel(bob)
jump(bob,0,96)
WhitePixel(bob)
jump(bob,-6,96)
LightBluePixel(bob)
jump(bob,-12,96)
BlackPixel(bob)
for times in range(3):
    jump(bob,24-times*6,96)
    BlackPixel(bob)
#Row 17
jump(bob,18,102)
LightBluePixel(bob)
for times in range(2):
    jump(bob,12-times*6,102)
    BlackPixel(bob)
jump(bob,0,102)
WhitePixel(bob)
jump(bob,-6,102)
BlackPixel(bob)
jump(bob,24,102)
BlackPixel(bob)
#Row 18
for times in range(2):
    jump(bob,24-times*6,108)
    BlackPixel(bob)
for times in range(3):
    jump(bob,0-times*6,108)
    BlackPixel(bob)
#Row 19
jump(bob,-6,114)
BlackPixel(bob)
jump(bob,-12,114)
LightPinkPixel(bob)
jump(bob,-18,114)
BlackPixel(bob)
#Row 20
jump(bob,-12,120)
BlackPixel(bob)