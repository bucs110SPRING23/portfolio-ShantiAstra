#Part A
import random
weeks = 16
print("Number of weeks is", weeks, "which is a", type(weeks), "variable")
classes = 5
print("Number of classes is", classes, "which is a", type(classes), "variable")
tuition = 6000
print("Tuition is", tuition, "which is a", type(tuition), "variable")
classes_per_week = 3
print("There are", classes_per_week, "classes in a week. Classes per week is a", type(classes_per_week), "variable")
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, "this is a", type(cost_per_week), "variable")
cost_per_class = cost_per_week/classes_per_week
print("You are being charged", cost_per_class, "for every class you take. Cost per class is a", type(cost_per_class), "variable")
#Part B
box_of_things = ["Happy Birthday", 17, "An orange cat", 192.73, -5000]
predict_the_future = ["death and dispair", "sucess in your love life", "be brave and take chances", "watch your step", "an unexpected reunion approaches"]
pick_something = random.choice(box_of_things)
your_future = random.choice(predict_the_future)
print("You picked", pick_something, "from the mysterious box")
print("I see something in your future...", your_future)