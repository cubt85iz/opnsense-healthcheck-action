# opnsense-healthcheck-action

Integrates with `System > Settings > Cron` to periodically send pings to the specified healthcheck URL.

## Installation

Open an SSH session for opnsense and clone the repo.

```sh
git clone https://github.com/cubt85iz/opnsense-healthcheck-action.git
```

Execute `su` and switch to shell for root user. Navigate to the directory and install the script.

```sh
make install
```

Restart configd to refresh available actions in Web UI

```sh
service configd restart
```

## Removal

Open an SSH session for opnsense and navigate to the repo. Execute the following command to uninstall the script.

```sh
make clean
```

## Usage

Navigate to `System > Settings > Cron` and create a new cron job specifying `Ping a healthcheck url` for the command and `<url>` as a parameter.
