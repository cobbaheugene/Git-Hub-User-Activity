# Git-Hub-User-Activity

## Description
This is a command-line tool that fetches and displays the recent activity of a GitHub user directly in your terminal. 
It uses the GitHub API to retrieve and display events like commits, issues, and stars based on the provided username.

## Features
- Fetches recent activity for any GitHub user.
- Displays events like pushes, issues, and stars in the terminal.
- Handles errors gracefully (e.g., invalid usernames, API failures).
- No external libraries used, ensuring a lightweight and efficient tool.

## Usage
Clone the repository:

```bash
git clone https://github.com/cobbaheugene/Git-Hub-User-Activity.git
cd Git-Hub-User-Activity-cli
```

Run the CLI tool:

```bash
python Git-Hub-User-Activity.py <username>
```

Replace `<username>` with the GitHub username you want to fetch activity for.

## Example Output
```bash
- Pushed 2 commits to cobbaheugene/Git-Hub-User-Activity
- Opened a new issue in cobbaheugene/Git-Hub-User-Activity
- Starred cobbaheugene/Git-Hub-User-Activity
```

## Requirements
- Python 3.x
- Access to the internet for API calls

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to Dan for his insightful live sessions, which greatly contributed to the development of this project. His guidance on using the GitHub API and working through the data in the terminal was invaluable. Special thanks also to the roadmap.sh community support.