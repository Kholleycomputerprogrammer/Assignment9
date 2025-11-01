class Person:
    
    def __init__(self, name):
        self.name = name
        self.friends = []  # adjacency list for this person

    def add_friend(self, friend):
        # Avoid duplicate friendships
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person '{name}' already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people ('{person1_name}', '{person2_name}') don't exist!")
            return
        
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add each other as friends (bidirectional)
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}")
            
# Test the Social Network
if __name__ == "__main__":
    network = SocialNetwork()

    #Adding
    network.add_person("Alex")
    network.add_person("Jordan") 
    print(network.people) 
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    #Creating friends
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny") 
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()

# Test your code here
