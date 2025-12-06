# QuarkPy Development Guide

## Usage

1. Create environment.

   QuarkPy service uses [UV](https://docs.astral.sh/uv/) to manage dependencies.
   First, you need to add the uv package manager, if you don't have it already.

   ```bash
   pip install uv
   # Or on macOS
   brew install uv
   ```

2. Start backend

   ```bash

   # Create a virtual environment
   python3 -m venv .venv

   # Activate the virtual environment
   .venv\Scripts\activate

   # Install dependencies
   uv sync

   # Run the backend server
   uv run -m quark
   ```