def greet(name, last_seen):
    print(name + "! By The Light!")
    print("We hadn't seen you since " + last_seen + ", we thought we'd lost you.")


greet("Anduin", "Sylvanas' betrayal")
greet("Sylvanas", "the fall of Azeroth")

# time to learn about function return. Let's say we want to cube something (raise it to the power of 3). i.e. 2
print(pow(2, 3))
print("function time")


def cube(num):
    print(pow(num, 3))


print(cube(2))
# we can see that the print keyword doesn't work as intended. Instead, we can use the keyword return. Note that the
# return keyword signals the end of the def function. Nothing written after it will be included in the def function.


print("correct function time")


def cube(num):
    return pow(num, 3)


print(cube(2))

"""
Μπορώ να προσθέσω προαιρετική μεταβλητή σε συνάρτηση με το να την θέσω = 0. Στο κάτω παράδειγμα μπορώ όταν καλέσω τη
συνάρτηση να δώσω μια μόνο τιμή και η συνάρτηση θα αντιμετωπίσει τη μεταβλητή y ως ίση με το μηδέν. Μπορώ να δώσω και
δύο τιμές, στην οποία περίπτωση θα θέσει τη μεταβλητή y ίση με τη δεύτερη τιμή που έδωσα. Να σημειωθεί ότι adder(3, 10)
και adder(y=10, x=3) είναι το ίδιο.
"""


def adder(x, y=0):
    result = x + y
    return result


"""
By default μια μεταβλητή που ορίστηκε εντός μιας συνάρτησης θα υπάρχει μόνο εντός αυτής της συνάρτησης. Αν θέλω να
υπάρχει γενικά στο αρχείο και όχι μόνο εντός της συνάρτησης, μπορώ να της προσδώσω την ιδιότητα global, ως εξής:

def f():
    global a
    a = 5
    return a
    
Σ'αυτήν την περίπτωση αφού τρέξει η συνάρτηση, θα υπάρχει στο αρχείο η μεταβλητή a με την τιμή 5.
"""

"""
Unpacking arguments. Specifically in this case, unpacking argument lists for functions. Let's say we have the following
"health_calculator" function that takes three arguments.
"""


def health_calculator(age, apples_per_week, cigs_per_week):
    health_value = 100 - age + apples_per_week * 3.5 - cigs_per_week * 2
    return health_value


"""
Now let's say we have the following data that we want to provide the function with, as arguments. The second method
is significantly easier, especially so with more arguments.
"""

buckys_data = [27, 20, 0]
print(health_calculator(buckys_data[0], buckys_data[1], buckys_data[2]))
print(health_calculator(*buckys_data))
