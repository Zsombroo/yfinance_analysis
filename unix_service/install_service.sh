#!/usr/bin/bash
cp unix_service/yfinance.service /etc/systemd/system/yfinance.service
systemctl daemon-reload
systemctl enable yfinance.service
systemctl start yfinance.service