import subprocess

def check_tool(tool):
    try:
        result = subprocess.run([tool, "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    with open("tools.txt", "r") as f:
        tools = [line.strip() for line in f.readlines()]

    for tool in tools:
        tool = tool.strip()
        try:
            result = subprocess.run([tool, "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                output = result.stdout.strip() or result.stderr.strip()
                version = output.split()[1]
                print(f"✅ {tool} is available: {version}")
            else:
                print(f"❌ {tool} not found")
        except FileNotFoundError:
            print(f"{tool} not found")