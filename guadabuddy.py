
# the group should ideally be comprised of 1 business, 2 engineering from dif teams
# at least 1 freshman, and at least 1 sophomore, the last one doesnt matter

import random

class Guadalooper:
    def __init__(self, name):
        self.name = name

class GuadalooperList:
    def __init__(self):
        self.guadalist = []

    def add_guadalooper(self, guadalooper):
        self.guadalist.append(guadalooper)

    def randomize_groups(self):
        groups = []
        previous_groups = []
        guadalist_copy = self.guadalist[:]
        random.shuffle(guadalist_copy) #randomly shuffles the list

        while len(guadalist_copy) >= 3:
            group = []
            for i in range(3):
                guadalooper = guadalist_copy.pop()
                group.append(guadalooper)
            groups.append(group)

            if group in previous_groups:
                groups.pop() #removes it from the list of groups
            else:
                previous_groups.append(group) #else adds it to the list of previously formed groups 

        if len(guadalist_copy) > 0:
            for i, guadalooper in enumerate(guadalist_copy):
                groups[i % len(groups)].add(guadalooper) 

        return groups
        
guadalist = GuadalooperList()

guadalist.add_guadalooper(Guadalooper("Aakash Kurapati"))
guadalist.add_guadalooper(Guadalooper("Aaron Pandian"))
guadalist.add_guadalooper(Guadalooper("Aaryan Anand"))
guadalist.add_guadalooper(Guadalooper("Aditya Matam"))
guadalist.add_guadalooper(Guadalooper("Alexandra Vaughn"))
guadalist.add_guadalooper(Guadalooper("Amelia Modesto"))
guadalist.add_guadalooper(Guadalooper("Amulya Tamma"))
guadalist.add_guadalooper(Guadalooper("Andrew Fan"))
guadalist.add_guadalooper(Guadalooper("Andriy Malyshchak"))
guadalist.add_guadalooper(Guadalooper("Anna Guo"))
guadalist.add_guadalooper(Guadalooper("Archer Tangton"))
guadalist.add_guadalooper(Guadalooper("Arya Anantula"))
guadalist.add_guadalooper(Guadalooper("Athul Tony"))
guadalist.add_guadalooper(Guadalooper("Bonsuck Koo"))
guadalist.add_guadalooper(Guadalooper("Boting Lu"))
guadalist.add_guadalooper(Guadalooper("Dane Akiri"))
guadalist.add_guadalooper(Guadalooper("Daniela Caballero"))
guadalist.add_guadalooper(Guadalooper("Dario Jimenez"))
guadalist.add_guadalooper(Guadalooper("Dillon Ding"))
guadalist.add_guadalooper(Guadalooper("Faaris Kukkadi"))
guadalist.add_guadalooper(Guadalooper("Gautam Rao"))
guadalist.add_guadalooper(Guadalooper("Harshin Sanam"))
guadalist.add_guadalooper(Guadalooper("Hugo Wong"))
guadalist.add_guadalooper(Guadalooper("Ivan Colon Bermudez"))
guadalist.add_guadalooper(Guadalooper("Jack Phillips"))
guadalist.add_guadalooper(Guadalooper("Jack Qiao"))
guadalist.add_guadalooper(Guadalooper("Jacob Boche"))
guadalist.add_guadalooper(Guadalooper("James Liu"))
guadalist.add_guadalooper(Guadalooper("Jason Wang"))
guadalist.add_guadalooper(Guadalooper("Jeremiah Do"))
guadalist.add_guadalooper(Guadalooper("Johem Avila"))
guadalist.add_guadalooper(Guadalooper("Kimberly Wang"))
guadalist.add_guadalooper(Guadalooper("Kireeti Singam Setty"))
guadalist.add_guadalooper(Guadalooper("Kyle Le"))
guadalist.add_guadalooper(Guadalooper("Lipika Chatur"))
guadalist.add_guadalooper(Guadalooper("Luke Pronga"))
guadalist.add_guadalooper(Guadalooper("Luke Venkataramanan"))
guadalist.add_guadalooper(Guadalooper("Mason Wargo"))
guadalist.add_guadalooper(Guadalooper("Mia Villarreal"))
guadalist.add_guadalooper(Guadalooper("Moid Meghani"))
guadalist.add_guadalooper(Guadalooper("Neel Deb Chaudhuri"))
guadalist.add_guadalooper(Guadalooper("Neeraj Anantha"))
guadalist.add_guadalooper(Guadalooper("Neil Ricamata"))
guadalist.add_guadalooper(Guadalooper("Nikhil Bathini"))
guadalist.add_guadalooper(Guadalooper("Nolan Watson"))
guadalist.add_guadalooper(Guadalooper("Pranav Tiwari"))
guadalist.add_guadalooper(Guadalooper("Prithvi Senthilkumar"))
guadalist.add_guadalooper(Guadalooper("Ravi Patel"))
guadalist.add_guadalooper(Guadalooper("Rishi Natarajan"))
guadalist.add_guadalooper(Guadalooper("Ritesh Thakur"))
guadalist.add_guadalooper(Guadalooper("Rohan Jain"))
guadalist.add_guadalooper(Guadalooper("Rudransh Rajaram"))
guadalist.add_guadalooper(Guadalooper("Sahas Veera"))
guadalist.add_guadalooper(Guadalooper("Saheli Ray"))
guadalist.add_guadalooper(Guadalooper("Sam Thawani"))
guadalist.add_guadalooper(Guadalooper("Sanya Sharma"))
guadalist.add_guadalooper(Guadalooper("Sarah Dickerson"))
guadalist.add_guadalooper(Guadalooper("Saujash Barman"))
guadalist.add_guadalooper(Guadalooper("Scott Crowe"))
guadalist.add_guadalooper(Guadalooper("Sidharth Shyamkumar"))
guadalist.add_guadalooper(Guadalooper("Siyuan (Tim) Chen"))
guadalist.add_guadalooper(Guadalooper("Sona George"))
guadalist.add_guadalooper(Guadalooper("Sophia Harder"))
guadalist.add_guadalooper(Guadalooper("Soumil Voma"))
guadalist.add_guadalooper(Guadalooper("Sourish Wawdhane"))
guadalist.add_guadalooper(Guadalooper("Sumedha Gonur"))
guadalist.add_guadalooper(Guadalooper("Trevor Liu"))
guadalist.add_guadalooper(Guadalooper("TY Brinker"))
guadalist.add_guadalooper(Guadalooper("Vaughn Davis"))
guadalist.add_guadalooper(Guadalooper("Vipashchit Nanda"))
guadalist.add_guadalooper(Guadalooper("Zoya Farooqui"))
guadalist.add_guadalooper(Guadalooper("Cindey Xiao"))
guadalist.add_guadalooper(Guadalooper("Samuel Arias"))
guadalist.add_guadalooper(Guadalooper("Srivarshini Senthilkumar"))
guadalist.add_guadalooper(Guadalooper("Ethan Lee"))
guadalist.add_guadalooper(Guadalooper("Falak Shah"))
guadalist.add_guadalooper(Guadalooper("Edward Chen"))
guadalist.add_guadalooper(Guadalooper("Netra Bhargava"))
guadalist.add_guadalooper(Guadalooper("Seoyoung Kong"))
guadalist.add_guadalooper(Guadalooper("Nicholas Tran"))
guadalist.add_guadalooper(Guadalooper("Maxim Gao"))
guadalist.add_guadalooper(Guadalooper("Akshara Viruthagiri"))
guadalist.add_guadalooper(Guadalooper("Stephanie Goff"))
guadalist.add_guadalooper(Guadalooper("Aparna Majety"))
guadalist.add_guadalooper(Guadalooper("Shreya Hegde"))
guadalist.add_guadalooper(Guadalooper("Saket Mukthapuram"))
guadalist.add_guadalooper(Guadalooper("Ryan Zheng"))
guadalist.add_guadalooper(Guadalooper("Jessica Rivera"))
guadalist.add_guadalooper(Guadalooper("Maanasa Chandra"))
guadalist.add_guadalooper(Guadalooper("Ethan Chandra"))
guadalist.add_guadalooper(Guadalooper("Jason Marek"))
guadalist.add_guadalooper(Guadalooper("Sophie Czelusta"))
guadalist.add_guadalooper(Guadalooper("Christos Joseph"))
guadalist.add_guadalooper(Guadalooper("David velasquez"))
guadalist.add_guadalooper(Guadalooper("Omar Elsayed"))
guadalist.add_guadalooper(Guadalooper("Kathryn Labbe"))
guadalist.add_guadalooper(Guadalooper("Luis Castañeda"))
guadalist.add_guadalooper(Guadalooper("Ethan Benson"))
guadalist.add_guadalooper(Guadalooper("Devin Chaky"))
guadalist.add_guadalooper(Guadalooper("Allison Nguyen"))
guadalist.add_guadalooper(Guadalooper("Sarrah Ghadiali"))
guadalist.add_guadalooper(Guadalooper("Abdullah Alwakeel"))
guadalist.add_guadalooper(Guadalooper("Vanshik Aluri"))
guadalist.add_guadalooper(Guadalooper("Nafee Karim"))
guadalist.add_guadalooper(Guadalooper("Ibrahim Eren Bisen"))
guadalist.add_guadalooper(Guadalooper("David Pate"))
guadalist.add_guadalooper(Guadalooper("Amar Saini"))
guadalist.add_guadalooper(Guadalooper("Ashmit Bhatnagar"))
guadalist.add_guadalooper(Guadalooper("Michael Pasala"))
guadalist.add_guadalooper(Guadalooper("Mihir Saripalli"))
guadalist.add_guadalooper(Guadalooper("Pranav Tenneti"))
guadalist.add_guadalooper(Guadalooper("Sathvik Boreda"))
guadalist.add_guadalooper(Guadalooper("Anisya Nair"))
guadalist.add_guadalooper(Guadalooper("Riya Patel"))
guadalist.add_guadalooper(Guadalooper("Ishita Singh"))
guadalist.add_guadalooper(Guadalooper("Victoria Gong"))
guadalist.add_guadalooper(Guadalooper("Mila Nenadic"))
guadalist.add_guadalooper(Guadalooper("Daniel Wang"))
guadalist.add_guadalooper(Guadalooper("Nicholas Verzic"))
guadalist.add_guadalooper(Guadalooper("Sunshine Leeuwon"))
guadalist.add_guadalooper(Guadalooper("Julie Hernandez"))
guadalist.add_guadalooper(Guadalooper("Juan Salinas"))
guadalist.add_guadalooper(Guadalooper("Daniel Gildin"))
guadalist.add_guadalooper(Guadalooper("Luigi Medrano"))
guadalist.add_guadalooper(Guadalooper("Alexander Poll"))
guadalist.add_guadalooper(Guadalooper("Valentina ponce"))

groups = guadalist.randomize_groups()
print("Set 1:")
for i, group in enumerate(groups):
    print(f"Group {i+1}:")
    for guadalooper in group:
        print(f"  {guadalooper.name}")

groups = guadalist.randomize_groups()
print("Set 2:")
for i, group in enumerate(groups):
    print(f"Group {i+1}:")
    for guadalooper in group:
        print(f"  {guadalooper.name}")

groups = guadalist.randomize_groups()
print("Set 3:")
for i, group in enumerate(groups):
    print(f"Group {i+1}:")
    for guadalooper in group:
        print(f"  {guadalooper.name}")