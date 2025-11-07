import random
import re

class Chatbot:
    def __init__(self):
        self.name = ""
        # Common words for exit and negative responses
        self.negative_responses = ("no", "not", "never", "nah", "nope")
        self.exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

        self.responses = {
            'greeting': [
                "Hello there! I’m your Career Counselor 🤖.",
                "Hi! I’m CareerBot, your guide to finding the right career path!",
                "Hey! Nice to meet you — I’m your friendly career counselor!"
            ],
            'ask_about_interest': [
                "Tell me about your favorite subject or hobby!",
                "What subjects do you enjoy studying?",
                "What do you like doing the most — working with people, technology, or creativity?"
            ],
            'math': [
                "Math lovers often excel as Data Scientists, Engineers, or Statisticians.",
                "If you enjoy math, careers like Financial Analyst, Engineer, or Actuary might suit you."
            ],
            'biology': [
                "You could explore careers in Medicine, Biotechnology, or Nutrition.",
                "Biology enthusiasts can become Doctors, Biotechnologists, or Environmental Scientists."
            ],
            'computer': [
                "That’s awesome! You might enjoy careers like Software Developer, Data Analyst, or AI Engineer.",
                "If you love computers, you could become a Programmer, Game Developer, or Cybersecurity Expert."
            ],
            'art': [
                "Creative minds thrive in Design, Animation, or Architecture!",
                "If you love art, you could explore Graphic Design, Fashion, or Interior Design."
            ],
            'business': [
                "Business-minded people often succeed as Entrepreneurs, Marketers, or Business Analysts.",
                "You might enjoy careers in Management, Finance, or Marketing."
            ],
            'psychology': [
                "You could be a great Psychologist, Counselor, or HR Specialist.",
                "Psychology lovers often become Therapists, Teachers, or Social Workers."
            ],
            'law': [
                "You might enjoy being a Lawyer, Legal Advisor, or Judge.",
                "If you like law, careers in Legal Consultancy or Civil Services could be ideal."
            ],
            'teacher': [
                "Teaching is a noble path! You could become a Professor, Trainer, or Academic Researcher.",
                "If you love education, consider becoming a Teacher or Instructional Designer."
            ],
            'science': [
                "Science lovers can become Researchers, Engineers, or Lab Technicians.",
                "You could explore careers in Physics, Chemistry, or Astronomy!"
            ],
            'thanks': [
                "You’re very welcome!",
                "Happy to help! 😊",
                "Glad I could assist!"
            ],
            'goodbye': [
                "Goodbye! Keep believing in yourself — your future is bright! 🌟",
                "See you later! Remember, every expert was once a beginner. ✨",
                "Bye! Keep chasing your dreams!"
            ],
            'default': [
                "That’s interesting! Could you tell me what subjects you like?",
                "I’m not sure I understand. Do you prefer science, business, or arts?",
                "Hmm… Could you tell me your favorite subject or hobby?"
            ]
        }

    def greet(self):
        self.name = input("🤖 Hello! I'm your Career Counselor. What’s your name?\n").strip()
        will_help = input(f"🤖 Hi {self.name or 'there'}, would you like some help exploring careers today?\n").strip().lower()

        if any(re.search(r'\b' + re.escape(word) + r'\b', will_help) for word in self.negative_responses):
            print("🤖 No problem! Whenever you’re ready, I’ll be here to guide you. Goodbye! 👋")
            return

        print(f"🤖 {random.choice(self.responses['greeting'])}")
        print(f"🤖 {random.choice(self.responses['ask_about_interest'])}")
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if re.search(r'\b' + re.escape(command) + r'\b', reply):
                print(f"🤖 {random.choice(self.responses['goodbye'])}")
                return True
        return False

    def chat(self):
        reply = input("\nYou: ").strip().lower()
        while not reply:
            reply = input("(I didn't catch that.) Tell me something about your interests:\n").strip().lower()

        while not self.make_exit(reply):
            response = self.match_intent(reply)
            print(f"🤖 {response}")
            reply = input("\nAnything else you'd like to ask about careers?\n").strip().lower()
            while not reply:
                reply = input("(I didn't catch that.) Anything else you'd like to ask?\n").strip().lower()

    def match_intent(self, reply):
        # Match user input using regex for different subjects
        if re.search(r'\b(math|algebra|geometry|calculus|statistics)\b', reply):
            return random.choice(self.responses['math'])
        elif re.search(r'\b(biology|bio|medical|medicine)\b', reply):
            return random.choice(self.responses['biology'])
        elif re.search(r'\b(computer|coding|programming|software|it|technology)\b', reply):
            return random.choice(self.responses['computer'])
        elif re.search(r'\b(art|design|drawing|painting|creative)\b', reply):
            return random.choice(self.responses['art'])
        elif re.search(r'\b(business|finance|management|economics|marketing)\b', reply):
            return random.choice(self.responses['business'])
        elif re.search(r'\b(psychology|mind|behavior|counseling)\b', reply):
            return random.choice(self.responses['psychology'])
        elif re.search(r'\b(law|legal|justice|lawyer)\b', reply):
            return random.choice(self.responses['law'])
        elif re.search(r'\b(teacher|education|professor|teaching)\b', reply):
            return random.choice(self.responses['teacher'])
        elif re.search(r'\b(science|physics|chemistry|research|scientist)\b', reply):
            return random.choice(self.responses['science'])
        elif re.search(r'\b(thanks|thank you|thank)\b', reply):
            return random.choice(self.responses['thanks'])
        else:
            return random.choice(self.responses['default'])


if __name__ == "__main__":
    bot = Chatbot()
    bot.greet()
