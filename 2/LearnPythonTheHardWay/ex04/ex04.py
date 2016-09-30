#paseengers!/usr/bin/env python
cars             = 100
space_in_a_car   = 4.0
drivers          = 30
passengers       = 90
cars_not_driven            = cars - drivers
cars_driven                = drivers
carpool_capacity           = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only",""
print "There will be",cars_not_driven, ""
print "We can transport", carpool_capacity, " people today."
print "We have", passengers, "to carpool today."
print "We ened ot put about", average_passengers_per_car, "in each car"
