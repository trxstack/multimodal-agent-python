import logging

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)
from livekit.plugins import openai

load_dotenv(dotenv_path=".env.local")
logger = logging.getLogger("multimodal-agent-python")


class Assistant(Agent):
    def __init__(self) -> None:
        logger.info("starting multimodal agent")

        # create a chat context with chat history, these will be synchronized with the server
        # upon session establishment
        chat_ctx = llm.ChatContext()
        chat_ctx.add_message(
            content="Context about the user: you are talking to a software engineer who's building voice AI applications."
            "Greet the user with a friendly greeting and ask how you can help them today.",
            role="assistant",
        )

        super().__init__(
            instructions="You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation. "
            "You were created as a demo to showcase the capabilities of LiveKit's agents framework.",
            llm=openai.realtime.RealtimeModel(),
            chat_ctx=chat_ctx,
        )

    async def on_enter(self):
        # to enable the agent to speak first
        self.session.generate_reply()


async def entrypoint(ctx: JobContext):
    session = AgentSession()
    await session.start(
        room=ctx.room,
        agent=Assistant(),
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
        ),
    )
