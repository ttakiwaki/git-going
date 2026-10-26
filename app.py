import os


def load_env():
    """Simple helper to read a local .env file without external libraries."""
    if not os.path.exists(".env"):
        print("⚠️  No .env file found! Copy .env.example to .env first.")
        print("Try running 'cp .env.example .env' in your terminal.")
        return
    with open(".env") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key] = value.strip('"').strip("'")


def main():
    load_env()
    name = os.environ.get("NAME", "Unknown")
    secret = os.environ.get("SECRET_API_KEY", None)

    if secret:
        print(f"👋 Welcome to the Fall Hacks Git & GitHub Workshop, {name}!")
        print(f"🔒 Secret loaded locally (First 4 chars: {secret[:4]}****)")


if __name__ == "__main__":
    main()
