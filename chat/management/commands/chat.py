"""Django command for an interactive terminal conversation."""

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import OperationalError

from chat.bot import create_bot


class Command(BaseCommand):
    help = "Chat with StudyBot."

    def handle(self, *args, **options):
        try:
            bot = create_bot()

            if bot.storage.count() == 0:
                raise CommandError(
                    "Run python manage.py train_bot first."
                )

            self.stdout.write(
                "StudyBot | Type quit or exit to leave."
            )

            while True:
                try:
                    message = input("user: ").strip()
                except (KeyboardInterrupt, EOFError):
                    self.stdout.write("\nGoodbye!")
                    break

                if message.casefold() in {"quit", "exit"}:
                    self.stdout.write("bot: Goodbye!")
                    break

                # Ignore blank messages.
                if not message:
                    continue

                if len(message) > 500:
                    self.stdout.write(
                        "bot: Please use 500 characters or fewer."
                    )
                    continue

                response = bot.get_response(message)
                self.stdout.write(f"bot: {response}")

        except OperationalError as exc:
            raise CommandError(
                "Run python manage.py migrate first."
            ) from exc