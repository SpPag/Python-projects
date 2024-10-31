is_male = False

if is_male:
    print("Hello brother")
else:
    print("Hello sister")

likes_males = False

if is_male and likes_males:
    print("You are a gay dude")
elif is_male and not likes_males:
    print("You are a straight dude")
elif not is_male and likes_males:
    print("You are a straight gal")
elif not is_male and not likes_males:
    print("You are a gay gal")
