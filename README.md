# Tiny SDG Testing
The vast majority of flows currently present in Red Hat SDG Hub's default installation recommend that any model used have a size of at least 20B. I have 16GiB of RAM total and an RTX 2060. There is absolutely no way that gpt-oss-120b is going to run on any computer I can access. Nor is any equivalent LLM.

There is, however, nothing that says that a smaller LLM (SLM?) can't be used in place of these workloads. Even though there is also nothing that says that a smaller LLM can or should be used in this way. Thus, this proof of concept.

This project aims to recreate the example projects found in the SDG Hub repository, but with more consumer-oriented hardware in mind. First, it implements the tutorial script with the model replaced with ministral-3:3b, which is not recommended or even experimental.

## REQUIREMENTS
1. A computer with a GPU capable of compute workloads. Preferably with >=4GiB of VRAM, but 
2. An Ollama setup with ministral-3 or equivalent.
3. Python 3.10 or higher.
4. An understanding that this is absolutely not what the hardware that would need this setup should be doing.

## SETUP
The first thing to do is set up a simple environment. Use `venv` to generate a Python virtual environment for the dependencies.

    python -m venv .venv
    source .venv/bin/activate

I recommend installing `uv` as instructed [here](https://docs.astral.sh/uv/getting-started/installation/). This is because the packages required here (`sdg_hub` and `datasets`) pull in quite a few dependencies and using `uv` greatly speeds up installation.

Both of these are technically optional, but highly recommended. With older environments, `pyenv` and `virtualenv` may be used instead. If you are not using `uv`, use `pip` instead of `uv pip` where needed.

The second thing to do is install the dependencies listed in `pyproject.toml` if your preferred project manager is unable to do so.

    uv pip install datasets sdg_hub

## AI DISCLOSURE
Very little code was written for this using AI tools. However, Copilot was used to generate the project structure. This gave me a usable project file aside from the fact that it wrote the definitions twice. I also used it for some autocomplete.