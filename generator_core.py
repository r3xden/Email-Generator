import random
from typing import List
from email_strategies import EmailStrategies 

class AdvancedEmailGenerator:
    """
    Orchestrates the use of multiple specialized strategies to ensure a high diversity 
    and realistic pool of generated emails.
    """
    def __init__(self):
        self.strategies = EmailStrategies()
        self._strategy_generators = self.strategies.get_strategies()

    def generate_batch(self, count: int) -> List[str]:
        """
        Attempts to generate 'count' emails by cycling through all available strategies 
        and collecting unique results until the target is met or attempts are exhausted.
        """
        print("[CORE LOGIC]: Starting multi-strategy generation process...")

        generated_emails = set()
        attempts = 0
        max_attempts = count * 10 # Increased attempts for higher coverage

        while len(generated_emails) < count and attempts < max_attempts:
            strategy_func = random.choice(self._strategy_generators)

            try:
                new_email = strategy_func()
                if new_email:
                    generated_emails.add(new_email)
            except Exception as e:
                print(f"Warning: Strategy failed during generation attempt {attempts}: {e}")

            attempts += 1

        final_list = list(generated_emails)
        if len(final_list) < count:
             print(f"\n[WARNING]: Could only generate {len(final_list)} unique emails after reaching max attempts.")

        return final_list
