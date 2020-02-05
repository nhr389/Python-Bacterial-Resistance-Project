import random  # used to randomize new bacteria resistances


class Bacteria:  # a class used to define bacteria

    def __init__(self, resistance=3, birth_counter=3, health=10, life_span=15):  # the attributes of Bacteria
        self.resistance = resistance + random.randrange(-1, 2)  # the normal resistance with a +1, 0 or -1 modifier
        if self.resistance <= 0:  # if the resistance isn't between 1-10 it is fixed
            self.resistance = 1
        if self.resistance >= 11:
            self.resistance = 10
        self.birth_counter = birth_counter
        self.health = health
        self.life_span = life_span

    def __str__(self):  # a stat print out for bacteria
        stats = 'H({}) R({}) LS({}) BC({})'.format(self.health, self.resistance, self.life_span, self.birth_counter)
        return stats

    def is_alive(self):  # checks to see if a bacteria is still living and returns true or false depending on that
        if self.health <= 0 or self.life_span <= 0:
            return False
        else:
            return True

    def tick(self):  # simulates a time cycle, lowering life and the birth counter
        self.life_span -= 1
        self.birth_counter -= 1

    def dose(self, dosage):  # strength of the antibiotics used
        damage = dosage * (1/self.resistance)  # formula to count health loss
        self.health -= damage

    def reproduce(self):  # simulates bacteria ready to reproduce
        if self.health <= 0 or self.life_span <= 0:  # bacteria cannot reproduce if they are dead
            x = False
        else:
            x = True
        if x is True and self.birth_counter <= 0:  # if their birth counter is 0, they are ready
            new_bac = Bacteria(self.resistance)
            self.birth_counter = 3  # the counter is reset
            bac_names.append(new_bac)  # a new bacteria is born and added to our bacteria list


class Host:  # class used to define our bacteria host

    count = 1  # count used to see how many days they've been carrying

    def __init__(self, num_bacteria):  # the lone attribute, is the number of bacteria
        self.num_bacteria = num_bacteria

    def __str__(self):  # a print out of bacteria information
        avg_health = average_h()
        avg_res = average_r()
        stats = 'Count : {}\n' \
                'Average Health : {}\n' \
                'Average Resistance : {}'.format(self.num_bacteria, avg_health, avg_res)
        Host.count = 1
        return stats

    def tick(self, with_dose):  # this is where the magic happens, runs bacteria ticks for thousands of lil guys
        if Host.count == 1:  # if it is the first one, a list for the bacteria is created
            make_list(self.num_bacteria)
        for y in range(0, len(bac_names)):  # goes through all of the bacteria in the list
            try:  # tries the function, if it fails we know we need to create a new bacteria
                if with_dose == 1 and Host.count > 30:  # if the dose is 1, it will dose every day after 30
                    bac_names[y].dose(25)
                elif with_dose == 2 and Host.count > 30:  # if the dose is 2, it will dose every other day after 30
                    if (Host.count % 2) == 0:
                        bac_names[y].dose(25)
                x = bac_names[y].is_alive()  # checks to see if a bacteria is even still alive
                if x is True:  # if it is, it ticks
                    bac_names[y].tick()
                    bac_names[y].reproduce()
                else:  # if not it is changed to a zero for the sake of not messing with the loops range
                    bac_names[y] = 0
            except:  # this is the failed test, it creates a new bacteria and runs the ticks
                (bac_names[y]) = Bacteria()
                (bac_names[y]).tick()
                (bac_names[y]).reproduce()
        while 0 in bac_names:  # all of the bacterias changed to 0 are removed from the list
            bac_names.remove(0)
        Host.count += 1  # the count is updated
        self.num_bacteria = len(bac_names)  # the number of bacteria is also updated


def make_list(length):  # used to make a list of bacteria for a certain length
    global bac_names  # global variable used to store all bacteria
    bac_names = []
    for i in range(1, length + 1):
        i = Bacteria
        bac_names.append(i)


def average_h():  # calculates the average health of the bacteria at the end, if 0 nan is used instead

    avg_health = 0
    if len(bac_names) == 0:
        avg_health = 'nan'
    else:
        for i in bac_names:
            avg_health += i.health
        avg_health /= len(bac_names)

    return avg_health


def average_r():  # calculates the average resistance of the bacteria at the end, if 0 nan is used instead

    avg_res = 0
    if len(bac_names) == 0:
        avg_res = 'nan'
    else:
        for i in bac_names:
            avg_res += i.resistance
        avg_res /= len(bac_names)

    return avg_res


# some tests of the classes with three different settings
print('No dosage')  # the three tests, no antibiotics
h1 = Host(1)
for i in range(0, 45):
    h1.tick(0)
print(h1, '\n')

print('Full dosage')  # antibiotics daily after 30 days
h2 = Host(1)
for i in range(0, 45):
    h2.tick(1)
print(h2, '\n')

print('Half dosage')  # antibiotics every other day after 30
h3 = Host(1)
for i in range(0, 45):
    h3.tick(2)
print(h3, '\n')






