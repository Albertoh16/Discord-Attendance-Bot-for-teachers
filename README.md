# Discord Attendance Bot for Teachers

A Discord bot designed to automate attendance tracking for educators conducting classes on Discord. The bot eliminates the manual process of tracking student attendance by automatically checking voice channel participation and generating attendance reports.

## Features

### Automated Attendance (`-auto`)
- Scans all voice channels in the Discord server
- Automatically marks students present if they're in a voice channel
- Marks students absent if they're not in any voice channel
- Generates a timestamped text file with attendance records
- Sends the attendance report directly to the instructor via DM
- Organizes records by date and server name

### Manual Attendance (`-manual`) [In Development]
- Allows attendance tracking via message reactions
- Students respond to a bot message within a time window
- Marks students present/absent based on their response
- Useful for text-based classes or when voice channels aren't used

## Installation

### Prerequisites
- Python 3.10.x
- Discord Bot Token
- Poetry (for dependency management)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Discord-Attendance-Bot-for-teachers.git
cd Discord-Attendance-Bot-for-teachers
```

2. Install dependencies using Poetry:
```bash
poetry install
```

Or using pip:
```bash
pip install discord.py gspread numpy flask urllib3
```

3. Set up environment variables:
   - Create a Discord bot at the [Discord Developer Portal](https://discord.com/developers/applications)
   - Copy your bot token
   - Set the `token` environment variable:
     ```bash
     export token="YOUR_DISCORD_BOT_TOKEN"
     ```

4. Run the bot:
```bash
poetry run python main.py
```

## Usage

### Adding the Bot to Your Server

Use this invitation link to add the bot to your Discord server:
```
https://discord.com/api/oauth2/authorize?client_id=1075198552638242876&permissions=274877908992&scope=bot
```

### Commands

#### `-auto`
Takes automatic attendance based on voice channel presence.

**Usage:**
```
-auto
```

**Example:**
1. Students join the class voice channel
2. Teacher runs `-auto` command
3. Bot generates attendance report
4. Teacher receives a DM with a text file containing attendance data

**Output Format:**
```
[Student Name]: PRESENT
[Student Name]: ABSENT
...
```
File name format: `[Server Name] attendance: MM-DD-YYYY.txt`

#### `-manual [reaction]` [In Development]
Takes attendance based on student reactions to a message.

**Note:** This feature is currently under development.

## Technical Details

### Dependencies
- **discord.py**: Discord API wrapper for bot functionality
- **gspread**: Google Sheets integration (prepared for future features)
- **Flask**: Web framework (for future web dashboard)
- **numpy**: Numerical computing (for data processing)
- **urllib3**: HTTP client

### File Structure
```
Discord-Attendance-Bot-for-teachers/
├── main.py              # Main bot code
├── pyproject.toml       # Poetry dependencies
├── poetry.lock          # Locked dependency versions
├── README.md            # This file
├── replit.nix          # Replit configuration
└── venv/               # Virtual environment
```

### Permissions Required
The bot requires the following Discord permissions:
- Read Messages/View Channels
- Send Messages
- Read Message History
- Connect (to view voice channels)
- View Guild Members

## How It Works

1. **Bot Initialization**: The bot connects to Discord with all intents enabled, including member intents to access user information.

2. **Attendance Collection**: When `-auto` is triggered:
   - Bot iterates through all members in the Discord server
   - Checks if each member is connected to a voice channel
   - Creates a sorted list of members with their attendance status

3. **Report Generation**:
   - Creates a text file with the current date and server name
   - Writes attendance data in alphabetical order
   - Sends the file to the command author via DM
   - Deletes the local file after sending

## Future Enhancements

- Complete manual attendance feature with reaction-based tracking
- Google Sheets integration for centralized attendance records
- Web dashboard for viewing attendance history
- Automatic scheduled attendance checks
- Export to CSV/Excel formats
- Attendance statistics and analytics

## Use Case

This bot was developed to assist professors conducting classes on Discord. It streamlines the attendance process by:
- Eliminating manual roll calls
- Reducing administrative overhead
- Providing timestamped records for accountability
- Creating portable attendance reports

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is available for educational use.

## Support

For issues or questions, please open an issue on the GitHub repository.

---

**Note**: Make sure to keep your Discord bot token secure and never commit it to version control. Use environment variables or secure secret management.
