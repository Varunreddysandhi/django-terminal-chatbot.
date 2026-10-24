"""Django command to train the chatbot."""

from django.core.management.base import BaseCommand

from chat.bot import create_bot, train_bot


class Command(BaseCommand):
    help = "Train the chatbot with sample conversations."

    def handle(self, *args, **options):
        train_bot(create_bot())
        self.stdout.write(
            self.style.SUCCESS("Training complete.")
        )