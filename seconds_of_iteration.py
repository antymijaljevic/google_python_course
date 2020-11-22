#!/home/amijaljevic/anaconda3/bin/python3

print("ITERATION TIME CALCULATOR\n")

numOfElements = float(input("Number of elements to iterate through loop? > "));
loopNum = float(input("How many loops you have? > "));

milisec = 1000;
minAndHour = 60;
numOfElements = numOfElements ** loopNum;

resultInMili = numOfElements * milisec;
resultInSec =  numOfElements / milisec;
resultInMin = resultInSec / minAndHour;
resultInHours = resultInMin / minAndHour;

print("\nIn miliseconds ==> " + str(int(resultInMili)));
print("In seconds ==> " + str(int(resultInSec)));
print("In minutes ==> " + str(int(resultInMin)));
print("In hours ==> " + str(round(resultInHours, 2)));
