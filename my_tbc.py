import random

class Fighter:
    def __init__(self, name="Unknown", health=10, accuracy=50, max_hit=5, shield=0):
        self.name = name
        self.health = health
        self.accuracy = accuracy
        self.max_hit = max_hit
        self.shield = shield

    def display_stats(self):
        """Prints the fighter's stats."""
        print(f"\n{self.name.upper()} STATS")
        print(f"Health: {self.health}")
        print(f"Accuracy: {self.accuracy}%")
        print(f"Max Damage: {self.max_hit}")
        print(f"Shield: {self.shield}")

    def attack(self, opponent):
        """Handles the attack sequence."""
        print(f"\n{self.name} attacks {opponent.name}!")
        if random.randint(1, 100) <= self.accuracy:
            damage = random.randint(1, self.max_hit)
            net_damage = max(0, damage - opponent.shield)
            opponent.health -= net_damage
            print(f"Hit! {opponent.name} takes {net_damage} damage. ({damage} - {opponent.shield} shield)")
        else:
            print(f"{self.name} missed!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

def battle(player1, player2):
    """Simulates a turn-based battle between two fighters."""
    print("\n--- BATTLE STARTS ---")
    while player1.health > 0 and player2.health > 0:
        player1.attack(player2)
        if player2.health <= 0:
            print(f"{player1.name} wins!")
            break
        player2.attack(player1)
        if player1.health <= 0:
            print(f"{player2.name} wins!")
            break

    print("\n--- BATTLE ENDS ---")
