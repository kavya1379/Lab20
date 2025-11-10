import sys
if len(sys.argv) == 3:
  script_name=sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("User provided input values:")
else:
script_name=sys.argv[0]
name="kavya"
rollno="122"
print("No input given_using defalut values:")

print("Scipt Name:"script_name)
print("Student Name:"name)
print("Roll Number:"rollno)
