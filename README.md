# YFinance Analysis

The commands are written to be run from the yfinance_analysis folder

### First steps

1. Change the '{username}' to your actual username in the following files:
    
    1.1 db/db_definition.py

    1.2 db/db_interaction.py
    
    1.3 db/db.conf
    
    1.4 unix_service/yfinance_service.conf
    
    1.5 unix_service/yfinance.service
    
    1.6 yfinance_service.py
    



2. Run to following command to create the database

```
python db/db_definition.py
```

### Automatic data fetcher service

This project contains a systemd service that downloads the latest available data on yahoo finance after booting. I wrote the service this way because I run it on my laptop that I use every day so it fetches the latest data whenever I start working.

#### Run the following commands to installation the service on Fedora:

```
sudo cp unix_service/yfinance.service /etc/systemd/system/yfinance.service
systemctl enable yfinance.service
systemctl start yfinance.service
```

#### Run the following commands to remove the service on Fedora:

```
systemctl disable yfinance.service
sudo rm /etc/systemd/system/yfinance.service
```