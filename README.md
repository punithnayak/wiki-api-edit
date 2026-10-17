# Edit a wiki page with the API

One script, `edit.py`: log in with a bot password, append a line to your sandbox on Meta-Wiki, and log out.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/punithnayak/wiki-api-edit&cloudshell_open_in_editor=edit.py&show=ide%2Cterminal)

## Steps

1. Make a bot password at [Special:BotPasswords](https://meta.wikimedia.org/wiki/Special:BotPasswords) (tick **Edit existing pages**). You get a name like `YourName@mybot` and a password.
2. In `edit.py`, change `EXAMPLE` (twice) to your username, and `'lgname'` to your bot name `YourName@mybot`.
3. In the terminal:
   ```sh
   cd ~/cloudshell_open/wiki-api-edit
   export WIKI_BOT_PASSWORD='the-password-you-got'
   python3 edit.py
   ```
4. Open `https://meta.wikimedia.org/wiki/User:YourName/sandbox` and see your edit.

The password stays in the terminal (`export`), never in the file, so it never goes into Git.
