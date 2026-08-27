name=("input enter your name") 
maths=float(input("Enter Maths marks")
python=float(input("Enter Python marks")
average=(maths+python)/2
print("n/student:",name)
print("Average:",average)
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")
