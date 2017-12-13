"""Santa tracker class, code warmup."""


class LittleBoyOrGirlOfTheWorld():
    """As described. A little boy or girl of the world."""

    def __init__(self, name, location, wishlist):
        """Initialization of boyes and grillz."""
        self.name = name
        self.nice = True
        self.visited = False
        self.presents_received = []
        self.wishlist = wishlist
        self.coal = 0
        self.location = location

    def attack_with_doggos(self):
        """Uh oh..."""
        print('Ho ho---hooooshit, down boy!')
        print('What a bad child you are! Time for the naughty list.')
        self.nice = False

    def give_cookies(self):
        """Giving cookies to santa."""
        if self.nice:
            return 'You were nice before, but now you\'re even nice-er!'
        self.nice = True
        return "Well, well. I can\'t resist that! Guess you\'re off the naughty list."

    def add_item_to_wishlist(self, toy):
        """New wish item."""
        self.wishlist.append(toy)

    def declare_allegiance_to_pct_sign_boiz(self):
        """Percent sign boizzzzz."""
        self.nice = True
        print('ayeeeee')


class Santa():
    """Ho ho ho!"""

    def __init__(self):
        """Initialization of Santa."""
        self.sack_of_gifts = []
        self.visited_loc = []
        self.list = []

    def check_list(self, name):
        """He's checking his list, twice even."""
        for child in self.list:
            if child.name == name:
                return self.check_twice(name)
        child.coal += 1
        return "Oh no, you've been bad! Coal for you."

    def check_twice(self, name):
        """Checking twice!"""
        for child in self.list:
            if child.name == name:
                self.give_gifts(child)

    def give_gifts(self, child):
        """Give gift to child if they are good."""
        gifts_given = 0
        for wish in child.wishlist:
            if gifts_given > 2:
                return "That's enough gifts for now!"
            if wish in self.sack_of_gifts:
                child.presents_received.append(wish)
                self.sack_of_gifts.remove(wish)
                gifts_given += 1
                return "{} has been given to {}".format(wish, child.name)

    def add_child_to_list(self, name, location, wishlist):
        """Add child to visiting list."""
        child = LittleBoyOrGirlOfTheWorld(name, location, wishlist)
        self.list.append(child)
        print('Another on the list!')

    def visit(self, location):
        """Visit a new town."""
        if location in self.visited_loc:
            return "I've already been there tonight! Let's go somewhere else."
        for child in self.list:
            if child.location == location:
                child.give_gifts()
                print('Ho ho ho!')

    def jingle_bells(self):
        """See function name."""
        print("""
            Dashing through the snow
            On a one horse open sleigh
            O'er the fields we go,
            Laughing all the way
            Bells on bob tail ring,
            making spirits bright
            What fun it is to laugh and sing
            A sleighing song tonight

            Oh, jingle bells, jingle bells
            Jingle all the way
            Oh, what fun it is to ride
            In a one horse open sleigh
            Jingle bells, jingle bells
            Jingle all the way
            Oh, what fun it is to ride
            In a one horse open sleigh

            A day or two ago,
            I thought I'd take a ride,
            And soon Miss Fanny Bright
            Was seated by my side;
            The horse was lean and lank
            Misfortune seemed his lot
            We got into a drifted bank,
            And then we got upsot.

            Oh, jingle bells, jingle bells
            Jingle all the way
            Oh, what fun it is to ride
            In a one horse open sleigh
            Jingle bells, jingle bells
            Jingle all the way
            Oh, what fun it is to ride
            In a one horse open sleigh

            Jingle Bells, Jingle Bells,
            Jingle all the way!
            Oh, What fun it is to ride
            In a one horse open sleigh.
            Jingle Bells, Jingle Bells,
            Jingle all the way!
            Oh, What fun it is to ride
            In a one horse open sleigh.

            Now the ground is white
            Go it while you're young
            Take the girls tonight
            And sing this sleighing song
            Just get a bob tailed bay
            two-forty as his speed
            Hitch him to an open sleigh
            And crack! you'll take the lead

            Jingle Bells, Jingle Bells,
            Jingle all the way!
            Oh, What fun it is to ride
            In a one horse open sleigh.
            Jingle Bells, Jingle Bells,
            Jingle all the way!
            Oh, What fun it is to ride
            In a one horse open sleigh.""")


