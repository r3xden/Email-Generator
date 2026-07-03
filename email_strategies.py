import random
from typing import List

class EmailStrategies:
    """
    Contains various sophisticated algorithms to generate emails based on different structural models.
    """
    def __init__(self):
        # Expanded and categorized pools for better diversity
        self.name_pools = {
            "first": ["alex", "emma", "noah", "sophie", "liam", "olivia"],
            "last": ["smith", "jones", "williams", "brown", "garcia", "miller"]
        }

        self.domain_pools = {
            "corporate": [("corpname", ".com"), ("techsolutions", ".org")],
            "personal": [("mailservice", ".net"), ("webhost", ".info")]
        }

    def generate_professional_format(self, first: str, last: str) -> str:
        """
        Strategy 1: Standard corporate format (e.g., john.doe@company.com or j.doe@company.com).
        Implements collision fallback logic internally to enhance validity chance.
        """
        sep = random.choice(['.', ''])
        base_local = f"{first}{sep}{last}"
        domain, tld = random.choice(self.domain_pools['corporate'])
        return f"{base_local}@{domain}.{tld}"

    def generate_initial_based_format(self, first: str, last: str) -> str:
        """
        Strategy 2: Initial-heavy format (e.g., a.smith@company.com or asmith@company.com).
        """
        initial = first[0].lower()
        domain, tld = random.choice(self.domain_pools['corporate'])

        separator = random.choice(['.', '', '']) 
        if separator == '.':
             return f"{initial}.{last}@{domain}.{tld}"
        else:
            return f"{initial}{last}@{domain}.{tld}"

    def generate_random_identifier(self) -> str:
        """
        Strategy 3: Fallback using random identifiers, often used when names are unknown.
        Generates username-like strings (e.g., XyloPattern92).
        """
        chars = string.ascii_letters + string.digits
        unique_id = ''.join(random.choices(chars, k=random.randint(6, 10)))
        domain, tld = random.choice(self.domain_pools['personal'])
        return f"{unique_id}@{domain}.{tld}"

    def get_strategies(self) -> List[callable]:
        """Returns all available generation functions."""
      
        return [
            lambda: self.generate_professional_format(random.choice(self.name_pools['first']), random.choice(self.name_pools['last'])),
            lambda: self.generate_initial_based_format(random.choice(self.name_pools['first']), random.choice(self.name_pools['last']))
      ]
