import os


def load_env():
    """Simple helper to read a local .env file without external libraries."""
    if not os.path.exists(".env"):
        print("⚠️  No .env file found! Copy .env.example to .env first.")
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

    print(f"👋 Welcome to Git Going, {name}!")
    if secret:
        print(f"🔒 Secret loaded locally (First 4 chars: {secret[:4]}****)")
    else:
        print("❌ No SECRET_API_KEY loaded.")


if __name__ == "__main__":
    main()
