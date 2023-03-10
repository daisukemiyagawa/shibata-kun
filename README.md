# しばたくん

## Introduction
しばたくん is an AI assistant developed by RUTILEA. It is designed to support a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on various topics. As a language model, しばたくん can generate human-like text based on the input it receives and provide coherent, topic-related responses. It can process large amounts of text and use that knowledge to provide accurate and helpful answers to various questions. Additionally, it can generate its own text based on the input it receives, allowing it to participate in discussions and provide explanations and commentary on various topics.

## Usage

To use shibata-kun, the following environment variables need to be set in your setiings.py:
Settings_base.py is a template for settings.py. Copy and use it.

- SLACK_BOT_TOKEN: Token for the Slack Bot.
- SLACK_APP_TOKEN: Token for the Slack app.
- OPENAI_API_TOKEN: Token for OpenAi
- GOOGLE_CSE_ID = ID for Google Custum Search
- GOOGLE_API_KEY = API KEY for Google Custum Search
- SERP_API_KEY = API KEY for serp API


## Installation
Requires Python3.11.0 or higher

1. Clone this repo and run the following commands

```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. cp settings_base.py settings.py

3. Put the API key and other information (e.g., OPEN API KEY).

4. Run the following commands.
```python
python app.py
```

## License

Copyright (c) 2019 [RUTILEA, Inc.][link-rutilea]

This program is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 or later as published by
the Free Software Foundation.

This program can be distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Support

- Report issues on the [GitHub issue tracker][link-github-issues]

<!-- Links -->
[link-github-issues]: https://github.com/RUTILEA/SDTest/issues
[link-rutilea]: https://rutilea.com/
