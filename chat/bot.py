"""Create the chatbot and train it with sample conversations."""

from chatterbot import ChatBot
from chatterbot.tagging import LowercaseTagger
from chatterbot.trainers import ListTrainer
from django.conf import settings


CONVERSATIONS = [
    [
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
    ],
    [
        "You're welcome.",
        "Do you like hats?",
    ],
    [
        "Hello",
        "Hello! How can I help you today?",
    ],
    [
        "What is Django?",
        "Django is a Python web framework.",
    ],
    [
        "Thank you",
        "You are welcome!",
    ],
]


def create_bot():
    """Build the bot without downloading a language model."""
    return ChatBot(
        **settings.CHATTERBOT,
        tagger=LowercaseTagger(),
    )


def train_bot(bot):
    """Train the bot using the conversation pairs."""
    trainer = ListTrainer(bot, show_training_progress=False)

    for conversation in CONVERSATIONS:
        trainer.train(conversation)