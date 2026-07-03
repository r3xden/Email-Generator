import sys
from colorama import Fore, Style
from generator_core import AdvancedEmailGenerator

EMAIL_COUNT = 100

def display_header(platform: str) -> None:
    """Displays the stylized header based on the detected platform."""
    if "termux" in platform.lower() or 'android' in platform.lower():
        print("\n" + "="*60)
        print(f"{Fore.CYAN}📡 Running on Mobile Environment (Termux/Android)!{Style.RESET_ALL}")
        print("="*60 + "\n")
    elif "win" in platform.lower() or "linux" in platform.lower():
        print("\n" + "="*60)
        print(f"{Fore.GREEN}🖥️ Running on PC (CMD Prompt / Terminal)!{Style.RESET_ALL}")
        print("="*60 + "\n")
    else:
        print("\n" + "="*60)
        print(f"{Fore.YELLOW}❓ Running in unknown environment: {platform}{Style.RESET_ALL}")
        print("="*60 + "\n")

def generate_and_display(count: int) -> None:
    """Orchestrates the generation and prints results with visual feedback."""
    generator = AdvancedEmailGenerator()

    try:
        emails = generator.generate_batch(count)
    except Exception as e:
        print(f"{Fore.RED}Fatal Error in core execution: {e}{Style.RESET_ALL}")
        return
      
    print("\n" + "="*80)
    print(f"{Fore.MAGENTA}✨ DISPLAYING GENERATED BATCH OF {len(emails)} EMAILS ✨{Style.RESET_ALL}")
    print("="*80)

    for i, email in enumerate(emails):
        progress_bar = f"{i+1}/{count}"
        print(f"[{Fore.BLUE}{progress_bar:<5}]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}{email}")

    print("\n" + "="*80)
    print(f"{Fore.CYAN}✅ Generation Complete! Successfully produced {len(emails)} unique identities.{Style.RESET_ALL}")
    print("="*80)


def run_tool():
    """Main execution flow."""
    system = sys.platform
    display_header(system)
    generate_and_display(EMAIL_COUNT)


if __name__ == "__main__":
    run_tool()
